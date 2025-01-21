import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
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
            Tile(pos=pos, surf=obj.image, groups=self.objects) # ensure each object has a name
        
    def draw(self, window):
        self.tiles.draw(window)
        self.objects.draw(window)
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.scale_factor = 1.5
        
        # player position
        self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134-right.png').convert_alpha(), self.scale_factor)
        self.x = 150
        self.y = 400
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        """Movement"""
        if keys[pygame.K_w]:
            self.rect.y -= 2
            self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134-up.png').convert_alpha(), self.scale_factor)
        elif keys[pygame.K_s]:
            self.rect.y += 2
            self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134-down.png').convert_alpha(), self.scale_factor)
        elif keys[pygame.K_a]:
            self.rect.x -= 2
            self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134-left.png').convert_alpha(), self.scale_factor)
        elif keys[pygame.K_d]:
            self.rect.x += 2
            self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134-right.png').convert_alpha(), self.scale_factor)
        
    def collision(self, background_obj):
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False)
        if collided_obj:
            print("Colliison")
            for obj in collided_obj:
                print(f"Collided with tile at {obj.rect.topleft}")
    
    def update(self, background_obj):
        self.player_input()
        self.collision(background_obj)

            
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

    
"""Game Loop"""
while True:
    # For when the person closes the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
                
            
    if game_active == True:
        Background.draw(screen)
        player_group.draw(screen)
        player_group.update(Background.objects)
    else:
        screen.fill("Green")

    
    pygame.display.flip()
    clock.tick(60)