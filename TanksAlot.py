import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        
class Gameobject(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups,obj_type):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.type = obj_type
        
class background(pygame.sprite.Sprite):
    def __init__(self, tmx_data):
        super().__init__()
        """Loading Level"""
        self.tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
        self.tiles = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        
    def loading(self):
        for layer in self.tmx_data.layers:
            if hasattr(layer,"data"): # nsure this is a tile layer. Since ile layers have "data"
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos = pos, surf = surf, groups = self.tiles)
        
        for obj in self.tmx_data.objects:
            pos = (obj.x, obj.y) # grabbing the position of the object
            obj_type = obj.name if hasattr(obj,"name") else "Unknown" # if defined assign the object
            Gameobject(pos=pos, surf=obj.image, groups=self.objects, obj_type = obj_type) # ensure each object has a name
        
    def draw(self, window):
        self.tiles.draw(window)
        self.objects.draw(window)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed, image):
        super().__init__()
        # Bullet
        self.image = pygame.image.load(image).convert_alpha()
        # Position
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = pygame.math.Vector2(direction) # direction to move in (1 for right, -1 for left)
        self.speed = speed
    
    def update(self):
        # move the bullet in a direction
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.rect.x < 0 or self.rect.x > 1280:
            self.kill() # kills if it leaves the screen

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # player position
        self.image = pygame.image.load('graphics/Tiles/tile_0134-right.png').convert_alpha()
        self.x = 150
        self.y = 400
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.previous_pos = self.rect.topleft
        self.speed = 2
        self.movement = pygame.math.Vector2(0,0) # initilize movement
        self.bullets = pygame.sprite.Group() # Group of bullets
        self.direction = "right"
    
    def player_input(self):
        #reset movement vector
        self.movement.x = 0
        self.movement.y = 0
        
        keys = pygame.key.get_pressed()
        
        """Movement"""
        if keys[pygame.K_w]:
            self.movement.y = -self.speed
            self.image = pygame.image.load('graphics/Tiles/tile_0134-up.png').convert_alpha()
            self.direction = "up"
        elif keys[pygame.K_s]:
            self.movement.y = self.speed
            self.image = pygame.image.load('graphics/Tiles/tile_0134-down.png').convert_alpha()
            self.direction = "down"
        elif keys[pygame.K_a]:
            self.movement.x = -self.speed
            self.image = pygame.image.load('graphics/Tiles/tile_0134-left.png').convert_alpha()
            self.direction = "left"
        elif keys[pygame.K_d]:
            self.movement.x = self.speed
            self.image = pygame.image.load('graphics/Tiles/tile_0134-right.png').convert_alpha()
            self.direction = "right"
        
    def shooting(self):
        if self.direction == "up":
            bullet = Bullet(self.rect.centerx, self.rect.top, direction=(0,-1), speed=4, image='graphics/Tiles/tile_0191-up.png')
        elif self.direction == "down":
            bullet = Bullet(self.rect.centerx, self.rect.bottom, direction=(0,1), speed=4, image='graphics/Tiles/tile_0191-down.png')
        elif self.direction == "left":
            bullet = Bullet(self.rect.left, self.rect.centery, direction=(-1,0), speed=4, image='graphics/Tiles/tile_0191-left.png')
        elif self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, direction=(1,0), speed=4, image='graphics/Tiles/tile_0191-right.png')
        self.bullets.add(bullet)
            
    def collision(self, background_obj):
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False)
        if collided_obj:
                for obj in collided_obj:
                    if obj.type != "Water":
                     background_obj.remove(obj)
                     self.speed += 0.1 # increase speed of tank
                    elif obj.type == "Water":
                        self.rect.topleft = self.previous_pos
                        self.movement.x = 0
                        self.movement.y = 0
                
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.rect.topleft = self.previous_pos
            self.movement.x = 0
            self.movement.y = 0
                        
    def update(self, background_obj):
        self.previous_pos = self.rect.topleft
        
        self.player_input()
        # apply the movement vector to the player's postion
        self.rect.x += self.movement.x
        self.rect.y += self.movement.y
        # Update the collision with the object background
        self.collision(background_obj)
        # Update the bullets
        self.bullets.update()

            
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
game_active = False
running = True

tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
Background = background(tmx_data)
Background.loading()

"""Player Character"""
player = Player()
player_group = pygame.sprite.GroupSingle(player)

"""Countdown"""
font = pygame.font.SysFont(None, 100)
counter = 10
text = font.render(str(counter), True, (0, 128, 0))

timer = pygame.USEREVENT+1
pygame.time.set_timer(timer, 1000) # in milliseconds
    
"""Game Loop"""
while True:
    # For when the person closes the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
            elif event.key == pygame.K_SPACE:
                player.shooting()
        
        elif event.type == timer:
            if game_active == True:
                counter -= 1
                text = font.render(str(counter), True, (0, 128, 0))
                print(counter)
                if counter == 0:
                    pygame.time.set_timer(timer, 0)
                    game_active = False
            
                
    if game_active == True: 
        Background.draw(screen)
        player_group.draw(screen)
        player_group.update(Background.objects)
        player.bullets.draw(screen)
        player.bullets.update()
    else:
        screen.fill("Green")

    
    pygame.display.flip()
    clock.tick(60)