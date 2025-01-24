import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from sys import exit

class StartButton(pygame.sprite.Sprite):
    def __init__(self,pos, action):
        super().__init__()
        self.normal_start = pygame.image.load('graphics/Buttons/Start/Start1.png').convert_alpha()
        self.pressed_start = pygame.image.load('graphics/Buttons/Start/Start4.png').convert_alpha()
        self.image = self.normal_start # default
        self.rect = self.image.get_rect(topleft=pos)
        self.action = action # Action trigger
    
    def update(self):    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            self.image = self.pressed_start
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.image = self.normal_start 
            if self.rect.collidepoint(pygame.mouse.get_pos()):
              self.action()
              global shot_by
              shot_by = None
    
    def reset(self):
        """back to normal state"""
        self.image = self.normal_start

    def draw(self, screen):
        """Draw the button on the screen"""
        screen.blit(self.image,self.rect)
    
    def start_game():
        global game_active, victory, counter
        game_active = True
        victory = None
        counter = 80
        pygame.time.set_timer(timer,1000)
        background.reset_game()

class Text():
    def Background():
        menu = pygame.image.load("graphics/Menu/Menu.png")
        screen.blit(menu, (0,140))
    
    def title():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_title = Font_countdown.render('TanksALOT', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5)
            screen.blit(scaled_by, (430 + dx, 150 + dy))
            
        title_text = Font_countdown.render('TanksALOT', True, ("Green"))
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(430,150))
        
    def Win():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_title = Font_countdown.render('TanksALOT for playing!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5)
            screen.blit(scaled_by, (160 + dx, 200 + dy))
            
        title_text = Font_countdown.render('TanksALOT for playing!', True, ("Green"))
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(160,200))
        
        additional_text1 = Font_countdown.render('Credits are on the Itch.io page & ReadMe!', True, ("Lime"))
        screen.blit(additional_text1,(50,350))
        
    def Lose():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_title = Font_countdown.render('Not destructive enough!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5)
            screen.blit(scaled_by, (140 + dx, 200 + dy))
            
        title_text = Font_countdown.render('Not destructive enough!', True, ("Green"))
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(140,200))
        
        additional_text1 = Font_countdown.render('"Speed Is key!"', True, ("Lime"))
        screen.blit(additional_text1,(405,350))
    
    def Shotyourself():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_title = Font_countdown.render('You Shot Yourself!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5)
            screen.blit(scaled_by, (250 + dx, 200 + dy))
            
        title_text = Font_countdown.render('You Shot Yourself!', True, ("Green"))
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(250,200))
        
        additional_text1 = Font_countdown.render('"Better luck next time"', True, ("Lime"))
        screen.blit(additional_text1,(300,350))
    
    def instructions():
        instruction_text1 = Font_countdown.render('WASD to Move, Right-Click to Shoot', True, ("Lime"))
        screen.blit(instruction_text1,(130,250))
        instruction_text2 = Font_countdown.render('and R to restart', True, ("Lime"))
        screen.blit(instruction_text2,(370,300))
        game_text1 = Font_countdown.render('Destroy all objects in the stage', True, ("Lime"))
        screen.blit(game_text1,(160,375))
        game_text2 = Font_countdown.render('without running out of time to win!', True, ("Lime"))
        screen.blit(game_text2,(120,425))
        
    def countdown():
        # outline
        outline_color = "black"
        # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_text = Font_countdown.render(f'{counter}', True, outline_color)
            screen.blit(outline_text, (10 + dx, 0 + dy))
        
        # countdown
        Countdown_text = Font_countdown.render(f'{counter}', True, ("turquoise"))
        screen.blit(Countdown_text,(10,0))
        
    def remaining(count):
        # outline
        outline_color = "black"
        # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]:
            outline_text = Font_countdown.render(f'Left: {count}', True, outline_color)
            screen.blit(outline_text, (10 + dx, 650 + dy))
        
        # remaining
        remaining_text = Font_countdown.render(f'Left: {count}', True, ("turquoise"))
        screen.blit(remaining_text,(10,650))
    
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
        self.tiles.empty()
        self.objects.empty()
        
        for layer in self.tmx_data.layers:
            if hasattr(layer,"data"): # nsure this is a tile layer. Since ile layers have "data"
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos = pos, surf = surf, groups = self.tiles)
        
        for obj in self.tmx_data.objects:
            pos = (obj.x, obj.y) # grabbing the position of the object
            obj_type = obj.name if hasattr(obj,"name") else "Unknown" # if defined assign the object
            Gameobject(pos=pos, surf=obj.image, groups=self.objects, obj_type=obj_type)
        
    def draw(self, window):
        self.tiles.draw(window)
        self.objects.draw(window)
    
    def reset_game():
        global player, player_group, Background
        player = Player()
        player_group = pygame.sprite.GroupSingle(player)
        
        tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
        Background = background(tmx_data)
        Background.loading()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed, image):
        super().__init__()
        # Bullet
        self.image = pygame.image.load(image).convert_alpha()
        # Position
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = pygame.math.Vector2(direction) # direction to move in (1 for right, -1 for left)
        self.speed = speed

    def collision(self, background_obj, bullet_group):
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False)
        if collided_obj:
                for obj in collided_obj:
                    if obj.type != "Water":
                     background_obj.remove(obj)
                     hit_sound = pygame.mixer.Sound("audio/sound_effects/Hit.wav")
                     hit_sound.set_volume(0.04)
                     hit_sound.play()
                     self.kill()
                    elif self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
                     self.kill() # kills if it leaves the screen
            
    def update(self, background_obj):
        # move the bullet in a direction
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        self.collision(background_obj, bullet_group)

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
        self.direction = "right"
        self.shooting_cooldown = 300
        self.last_shot = pygame.time.get_ticks()
    
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
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_shot >= self.shooting_cooldown:
            bullet_offset = 20
            if self.direction == "up":
                bullet = Bullet(self.rect.centerx, self.rect.top - bullet_offset, direction=(0,-1), speed=4, image='graphics/Tiles/tile_0191-up.png')
            elif self.direction == "down":
                bullet = Bullet(self.rect.centerx, self.rect.bottom + bullet_offset, direction=(0,1), speed=4, image='graphics/Tiles/tile_0191-down.png')
            elif self.direction == "left":
                bullet = Bullet(self.rect.left - bullet_offset, self.rect.centery, direction=(-1,0), speed=4, image='graphics/Tiles/tile_0191-left.png')
            elif self.direction == "right":
                bullet = Bullet(self.rect.right + bullet_offset , self.rect.centery, direction=(1,0), speed=4, image='graphics/Tiles/tile_0191-right.png')
            bullet_group.add(bullet)
            self.last_shot = current_time # update to the current time.
            
    def collision(self, background_obj):
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False)
        if collided_obj:
                for obj in collided_obj:
                    if obj.type != "Water":
                     background_obj.remove(obj)
                     hit_sound = pygame.mixer.Sound("audio/sound_effects/Powerup.wav")
                     hit_sound.set_volume(0.025)
                     hit_sound.play()
                     self.speed += 0.02 # increase speed of tank
                    elif obj.type == "Water":
                        self.rect.topleft = self.previous_pos
                        self.movement.x = 0
                        self.movement.y = 0
        
        hit_by_bullet = pygame.sprite.spritecollide(self, bullet_group, True) # kills player when set to true
        if hit_by_bullet:
            hit_sound = pygame.mixer.Sound('audio/sound_effects/shotYourself.wav')
            hit_sound.set_volume(0.075)
            hit_sound.play()
            global game_active, victory, shot_by
            victory = False
            shot_by = True
            game_active = False
                
        if self.rect.x < 0 or self.rect.x > 1270 or self.rect.y < 0 or self.rect.y > 685:
            self.rect.topleft = self.previous_pos
            self.movement.x = 0
            self.movement.y = 0
                        
    def update(self, background_obj, bullet_group):
        self.previous_pos = self.rect.topleft
        
        self.player_input()
        # apply the movement vector to the player's postion
        self.rect.x += self.movement.x
        self.rect.y += self.movement.y
        # Update the collision with the object background
        self.collision(background_obj)
        # Update the bullets
        for bullet in bullet_group:
         bullet.update(background_obj)

            
pygame.init()
screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()
game_active = False
running = True
victory = None
shot_by = None
previously_played = None
Playing = "Menu"

"""Bullets"""
bullet_group = pygame.sprite.Group()

"""Buttons"""
start_button = StartButton(pos=(400,550), action=StartButton.start_game)
button_group = pygame.sprite.Group(start_button)

"""Gray Overlay"""
gray_overlay = pygame.Surface((1280, 720))
gray_overlay.set_alpha(128)
gray_overlay.fill((64,64,64))

"""Red Overlay"""
red_overlay = pygame.Surface((1280, 720))
red_overlay.set_alpha(128)
red_overlay.fill((255,0,0))

"""Green Overlay"""
green_overlay = pygame.Surface((1280, 720))
green_overlay.set_alpha(128)
green_overlay.fill((0,255,0))

"""Fonts"""
Font_countdown = pygame.font.Font("graphics/Fonts/VCR_OSD_MONO.ttf", 50)

"""Background"""
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

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            player.shooting()
        
        # restart button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = False
                victory = None
                shot_by = None
                start_button.reset()
                bullet_group.empty()
        
        elif event.type == timer:
            if game_active == True:
                counter -= 1
                if counter == 0:
                    pygame.time.set_timer(timer, 0)
                    victory = False
                    game_active = False
                if destructable_count == 0:
                    victory = True
                    game_active = False
    
    """Music"""
    if Playing != previously_played:
        if not game_active and Playing == "Menu":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('audio/music/Menu.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1)
            Playing = "Menu"
        elif game_active and Playing == "Game":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('audio/music/Game.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1)
            Playing = "Game"
        elif not game_active and Playing == "TimeOut":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('audio/music/TimeOut.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1)
            Playing = "TimeOut"
        elif not game_active and Playing == "Victory":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('audio/music/Victory.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1)
            Playing = "Victory"
        else:
            pygame.mixer_music.stop()
            Playing == "None"
        
        previously_played = Playing
    
    if game_active: 
        Background.draw(screen)
        player_group.draw(screen)
        player_group.update(Background.objects, bullet_group)
        bullet_group.draw(screen)
        Playing = "Game"
        Text.countdown()
        
        destructable_count = len([obj for obj in Background.objects if obj.type=="Destructable"])
        Text.remaining(destructable_count)
        
    else:
        Background.draw(screen)
        screen.blit(gray_overlay,(0,0))
        button_group.update()
        button_group.draw(screen)
        Playing = "Menu"
        Text.Background()
        Text.instructions()
        Text.title()

        if victory == True:
            screen.blit(green_overlay,(0,0))
            button_group.draw(screen)
            Playing = "Victory"
            Text.Background()
            Text.Win()

        elif victory == False: 
            if shot_by:
                screen.blit(red_overlay,(0,0))
                button_group.draw(screen)
                Playing = "None"
                Text.Background()
                Text.Shotyourself()
            else:
                screen.blit(red_overlay,(0,0))
                button_group.draw(screen)
                Playing = "TimeOut"
                Text.Background()
                Text.Lose()
        
        bullet_group.empty()
    
    pygame.display.flip()
    clock.tick(60)