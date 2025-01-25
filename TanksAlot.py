import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from sys import exit

"""Buttons"""
class EasyButton(pygame.sprite.Sprite):
    def __init__(self,pos, action):
        super().__init__()
        self.normal_easy = pygame.image.load('data/graphics/Buttons/Easy/Easy1.png').convert_alpha()
        self.pressed_easy = pygame.image.load('data/graphics/Buttons/Easy/Easy4.png').convert_alpha()
        self.image = self.normal_easy # default button position
        self.rect = self.image.get_rect(topleft=pos) # default button position
        self.action = action # Action trigger
    
    """Constantly updated"""
    def update(self):   
        if self.rect.collidepoint(pygame.mouse.get_pos()): 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Only when the player clicks and that button is a left click then the image will change to pressed  
                self.image = self.pressed_easy
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # As the player lifts from the click the game will reset and start.
                self.image = self.normal_easy
                self.action() # Calls the start_game action.
                global shot_by, difficulty
                shot_by = None
                difficulty = "Easy"
            else:
                self.image = self.normal_easy # the button will be lifted up whenever the button is not in use.

    def draw(self, screen):
        """Draw the button on the screen"""
        screen.blit(self.image,self.rect)
    
    # the button will start the game with a different counter depending on the button level.
    def start_game():
        global game_active, victory, counter
        game_active = True
        victory = None
        counter = 90 # Easy difficulty
        pygame.time.set_timer(timer,1000)
        background.reset_game()

class NormalButton(pygame.sprite.Sprite): # Normal button has the same setup as the easy button but will change the immage and how much time you are given when the game will start
    def __init__(self,pos, action):
        super().__init__()
        self.normal_medium = pygame.image.load('data/graphics/Buttons/Medium/Medium1.png').convert_alpha()
        self.pressed_medium = pygame.image.load('data/graphics/Buttons/Medium/Medium4.png').convert_alpha()
        self.image = self.normal_medium # default button position
        self.rect = self.image.get_rect(topleft=pos) # default button position
        self.action = action # Action trigger
    
    """Constantly updated"""
    def update(self):    
        if self.rect.collidepoint(pygame.mouse.get_pos()): 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Only when the player clicks and that button is a left click then the image will change to pressed  
                self.image = self.pressed_medium
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # As the player lifts from the click the game will reset and start.
                self.image = self.normal_medium
                self.action() # Calls the start_game action.
                global shot_by, difficulty
                shot_by = None
                difficulty = "Medium"
            else:
                self.image = self.normal_medium # the button will be lifted up whenever the button is not in use.

    def draw(self, screen):
        """Draw the button on the screen"""
        screen.blit(self.image,self.rect)
    
    # the button will start the game with a different counter depending on the button level.
    def start_game():
        global game_active, victory, counter
        game_active = True
        victory = None
        counter = 75 # Normal difficulty time
        pygame.time.set_timer(timer,1000)
        background.reset_game()
class HardButton(pygame.sprite.Sprite): # Hard button has the same setup as the easy or normal button but will change the immage and how the time given when the game will start
    def __init__(self,pos, action):
        super().__init__()
        self.normal_hard = pygame.image.load('data/graphics/Buttons/Hard/Hard1.png').convert_alpha()
        self.pressed_hard = pygame.image.load('data/graphics/Buttons/Hard/Hard4.png').convert_alpha()
        self.image = self.normal_hard # default button position
        self.rect = self.image.get_rect(topleft=pos) # default button position
        self.action = action # Action trigger
    
    """Constantly updated"""
    def update(self):    
        if self.rect.collidepoint(pygame.mouse.get_pos()): 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Only when the player clicks and that button is a left click then the image will change to pressed  
                self.image = self.pressed_hard
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # As the player lifts from the click the game will reset and start.
                self.image = self.normal_hard
                self.action() # Calls the start_game action.
                global shot_by, difficulty
                shot_by = None
                difficulty = "Hard"
            else:
                self.image = self.normal_hard # the button will be lifted up whenever the button is not in use.

    def draw(self, screen):
        """Draw the button on the screen"""
        screen.blit(self.image,self.rect)
    
    # the button will start the game with a different counter depending on the button level.
    def start_game():
        global game_active, victory, counter
        game_active = True
        victory = None
        counter = 65 # Normal difficulty time
        pygame.time.set_timer(timer,1000)
        background.reset_game()

"""All text that will be displayed on screen."""
class Text():
    def Background():
        menu = pygame.image.load("data/graphics/Menu/Menu.png")
        screen.blit(menu, (0,140))
    
    def title():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_title = MainFont.render('TanksALOT', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5) # Scale the text by 1.5x
            screen.blit(scaled_by, (430 + dx, 150 + dy)) # Will blit the outline of the main text.
            
        title_text = MainFont.render('TanksALOT', True, ("Green")) # Main text that will be outlined with Anti-aliasing.
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(430,150))

    def WinHard():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_title = MainFont.render('TanksALOT for playing!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5) # Scale the text by 1.5x
            screen.blit(scaled_by, (160 + dx, 200 + dy)) # Will blit the outline of the main text.
            
        title_text = MainFont.render('TanksALOT for playing!', True, ("Green")) # Main text that will be outlined with Anti-aliasing.
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(160,200))
        
        additional_text1 = MainFont.render("You beat my best time! Fair Play...", True, ("Lime")) # The additional text that will be blitted underneath the title.
        screen.blit(additional_text1,(150,350))
        
    def Win():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_title = MainFont.render('TanksALOT for playing!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5) # Scale the text by 1.5x
            screen.blit(scaled_by, (160 + dx, 200 + dy)) # Will blit the outline of the main text.
            
        title_text = MainFont.render('TanksALOT for playing!', True, ("Green")) # Main text that will be outlined with Anti-aliasing.
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(160,200))
        
        additional_text1 = MainFont.render('Credits are on the Itch.io page & ReadMe!', True, ("Lime")) # The additional text that will be blitted underneath the title.
        screen.blit(additional_text1,(50,350))
        
    def Lose():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_title = MainFont.render('Not destructive enough!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5) # Scale the text by 1.5x
            screen.blit(scaled_by, (140 + dx, 200 + dy)) # Will blit the outline of the main text.
            
        title_text = MainFont.render('Not destructive enough!', True, ("Green")) # Main text that will be outlined with Anti-aliasing.
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(140,200))
        
        additional_text1 = MainFont.render('"Speed Is key!"', True, ("Lime")) # The additional text that will be blitted underneath the title.
        screen.blit(additional_text1,(405,350))
    
    def Shotyourself():
        outline_color = "Black"
        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_title = MainFont.render('You Shot Yourself!', True, outline_color)
            scaled_by = pygame.transform.scale_by(outline_title, 1.5) # Scale the text by 1.5x
            screen.blit(scaled_by, (250 + dx, 200 + dy)) # Will blit the outline of the main text.
            
        title_text = MainFont.render('You Shot Yourself!', True, ("Green")) # Main text that will be outlined with Anti-aliasing.
        scaled_title = pygame.transform.scale_by(title_text, 1.5)
        screen.blit(scaled_title,(250,200)) 
        
        additional_text1 = MainFont.render('"Better luck next time"', True, ("Lime"))
        screen.blit(additional_text1,(300,350))
    
    def instructions(): # The additional text that will be blitted underneath the title.
        instruction_text1 = MainFont.render('WASD to Move, Right-Click to Shoot', True, ("Lime")) 
        screen.blit(instruction_text1,(130,250))
        instruction_text2 = MainFont.render('and R to restart', True, ("Lime"))
        screen.blit(instruction_text2,(370,300))
        game_text1 = MainFont.render('Destroy all objects in the stage', True, ("Lime"))
        screen.blit(game_text1,(160,375))
        game_text2 = MainFont.render('without running out of time to win!', True, ("Lime"))
        screen.blit(game_text2,(120,425))
        
    def countdown():
        outline_color = "black"

        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_text = MainFont.render(f'{counter}', True, outline_color)
            screen.blit(outline_text, (10 + dx, 0 + dy))
        
        # countdown that will be outlined with Anti-aliasing
        Countdown_text = MainFont.render(f'{counter}', True, ("turquoise"))
        screen.blit(Countdown_text,(10,0))
        
    def remaining(count):
        outline_color = "black"

        for dx,dy in [(-3,0), (3,0), (0,-3), (-3,-3), (3,-3), (-3,3), (3,3)]: # dx and dy are to offset the outline from the text, such as (-2,0) shifts 2 pixels to the left. whilst (-2,-2) handle diagonal
            outline_text = MainFont.render(f'Left: {count}', True, outline_color)
            screen.blit(outline_text, (10 + dx, 650 + dy))
        
        # remaining that will be outlined with Anti-aliasing
        remaining_text = MainFont.render(f'Left: {count}', True, ("turquoise"))
        screen.blit(remaining_text,(10,650))

"""Used for tilemapping of each tile sprite."""
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        
"""Used identifying each object in the object class in Tiled to load them in."""
class Gameobject(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups,obj_type):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.type = obj_type

"""To load the background"""
class background(pygame.sprite.Sprite):
    def __init__(self, tmx_data):
        super().__init__()
        """Loading Level"""
        self.tmx_data = load_pygame('data/graphics/Tiled/Gamejam.tmx')
        self.tiles = pygame.sprite.Group() # Put each tile into a group
        self.objects = pygame.sprite.Group() # Put each object into a group

    def loading(self):
        self.tiles.empty() 
        self.objects.empty() # Reset the map so that the player starts in a freshly new map.
        
        for layer in self.tmx_data.layers:
            if hasattr(layer,"data"): # ensures this is a tile layer. Since tile layers have "data"
                for x, y, surf in layer.tiles(): # places each tile from their positon in the tiled map editor.
                    pos = (x * 16, y * 16)
                    Tile(pos = pos, surf = surf, groups = self.tiles) # loads that specific tile at that given positon.
        
        for obj in self.tmx_data.objects: # loads each object from the object class.
            pos = (obj.x, obj.y) # grabbing the position of the object
            obj_type = obj.name if hasattr(obj,"name") else "Unknown" # if defined assign the object, otherwise if the object is not named then "unknown"
            Gameobject(pos=pos, surf=obj.image, groups=self.objects, obj_type=obj_type) # loads that object into the map.
        
    def draw(self, window):
        self.tiles.draw(window)
        self.objects.draw(window) # drawing onto the map.
    
    # Resetting the game assets and player position.
    def reset_game():
        global player, player_group, Background
        player = Player()
        player_group = pygame.sprite.GroupSingle(player)
        
        tmx_data = load_pygame('data/graphics/Tiled/Gamejam.tmx')
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
        self.speed = speed # speed of bullet

    # when the bullet will collide with an object.
    def collision(self, background_obj, bullet_group):
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False) # For future, set this to true so that both the object and the bullet are killed (set to true)
        if collided_obj:
                for obj in collided_obj: 
                    if obj.type != "Water": # if the object is not water
                     background_obj.remove(obj) # remove the object
                     hit_sound = pygame.mixer.Sound("data/audio/sound_effects/Hit.wav") 
                     hit_sound.set_volume(0.04)
                     hit_sound.play() # play the hit sound.
                     player.speed += 0.02 # increase the speed
                     self.kill() # kills the bullet
                    elif self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
                     self.kill() # kills if it leaves the screen
            
    def update(self, background_obj):
        # move the bullet in a direction with the speed, and check if the bullet collision.
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        self.collision(background_obj, bullet_group)

"""Player Tank"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # player position
        self.image = pygame.image.load('data/graphics/Tiles/tile_0134-right.png').convert_alpha()
        self.x = 150
        self.y = 400
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.previous_pos = self.rect.topleft # Checks the player previous position.
        self.speed = 2 # the starting speed of the tank.
        self.movement = pygame.math.Vector2(0,0) # initilize movement
        self.direction = "right" # the starting direction for bullet direciton.
        self.shooting_cooldown = 300 
        self.last_shot = pygame.time.get_ticks() # 300 millisecond cool down and then update last shot.
    
    def player_input(self):
        #reset movement vector
        self.movement.x = 0
        self.movement.y = 0
        
        keys = pygame.key.get_pressed() # initilize key presses.
        
        """Movement"""
        if keys[pygame.K_w]:
            self.movement.y = -self.speed # sprite moves up the screen. (decrease the y direction)
            self.image = pygame.image.load('data/graphics/Tiles/tile_0134-up.png').convert_alpha() # sprite is changed to be up
            self.direction = "up" # used for bullet direction.
        elif keys[pygame.K_s]:
            self.movement.y = self.speed # sprite moves down the screen. (increase the y direction)
            self.image = pygame.image.load('data/graphics/Tiles/tile_0134-down.png').convert_alpha() # sprite is changed to be down
            self.direction = "down" # used for bullet direction.
        elif keys[pygame.K_a]:
            self.movement.x = -self.speed # sprite moves left on the screen. (minus the x direction)
            self.image = pygame.image.load('data/graphics/Tiles/tile_0134-left.png').convert_alpha() # sprite is changed to be left
            self.direction = "left" # used for bullet direction.
        elif keys[pygame.K_d]:
            self.movement.x = self.speed # sprite moves right on the screen. (increase the x direction)
            self.image = pygame.image.load('data/graphics/Tiles/tile_0134-right.png').convert_alpha() # sprite is changed to be right
            self.direction = "right" # used for bullet direction.
    
    """Bullet direction and sprite"""
    def shooting(self):
        current_time = pygame.time.get_ticks() # the cooldown is initilized
        
        if current_time - self.last_shot >= self.shooting_cooldown: # if the current time has passed the time since last shot to now shoot.
            bullet_offset = 20 # used for spawning the bullet out of the way
            if self.direction == "up": # 
                bullet = Bullet(self.rect.centerx, self.rect.top - bullet_offset, direction=(0,-1), speed=4, image='data/graphics/Tiles/tile_0191-up.png') # will spawn the bullet with the given direction of the tank, on the tank with the offset to not kill the player.
            elif self.direction == "down":
                bullet = Bullet(self.rect.centerx, self.rect.bottom + bullet_offset, direction=(0,1), speed=4, image='data/graphics/Tiles/tile_0191-down.png') # will spawn the bullet with the given direction of the tank, on the tank with the offset to not kill the player.
            elif self.direction == "left":
                bullet = Bullet(self.rect.left - bullet_offset, self.rect.centery, direction=(-1,0), speed=4, image='data/graphics/Tiles/tile_0191-left.png') # will spawn the bullet with the given direction of the tank, on the tank with the offset to not kill the player.
            elif self.direction == "right":
                bullet = Bullet(self.rect.right + bullet_offset , self.rect.centery, direction=(1,0), speed=4, image='data/graphics/Tiles/tile_0191-right.png') # will spawn the bullet with the given direction of the tank, on the tank with the offset to not kill the player.
            bullet_group.add(bullet) # adds the bullet to the current bullets on the screen group.
            self.last_shot = current_time # update to the current time.
            
    def collision(self, background_obj): # Collison with the object and player
        collided_obj = pygame.sprite.spritecollide(self, background_obj, False) # when the player collides with an object.
        if collided_obj:
                for obj in collided_obj:
                    if obj.type != "Water": # if the object is not water.
                     background_obj.remove(obj) # remove the obj
                     hit_sound = pygame.mixer.Sound("data/audio/sound_effects/Powerup.wav")
                     hit_sound.set_volume(0.025)
                     hit_sound.play() # play the powerup sound
                     self.speed += 0.02 # increase speed of tank
                    elif obj.type == "Water": # when the obj is water
                        self.rect.topleft = self.previous_pos # keep the player in their previous position.
                        self.movement.x = 0
                        self.movement.y = 0 # will stop the movement 
        
        hit_by_bullet = pygame.sprite.spritecollide(self, bullet_group, True) # Will kill the player if hit by the bullet
        if hit_by_bullet: # if the player is hit by themselves, the game will go into game over
            hit_sound = pygame.mixer.Sound('data/audio/sound_effects/shotYourself.wav')
            hit_sound.set_volume(0.075)
            hit_sound.play()
            global game_active, victory, shot_by
            victory = False
            shot_by = True
            game_active = False
                
        # if the player tries to leave the screen then they will be kept in their previous position and stopped in place.
        if self.rect.x < 0 or self.rect.x > 1270 or self.rect.y < 0 or self.rect.y > 685:
            self.rect.topleft = self.previous_pos
            self.movement.x = 0
            self.movement.y = 0
    
    """Constantly updated."""
    def update(self, background_obj, bullet_group):
        self.previous_pos = self.rect.topleft
        
        self.player_input()
        # apply the movement vector to the player's postion
        self.rect.x += self.movement.x
        self.rect.y += self.movement.y
        # Update the collision with the object background
        self.collision(background_obj)
        # Update the bullets on screen.
        for bullet in bullet_group:
         bullet.update(background_obj)

"""Game initilization"""
pygame.init()
screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()
game_active = False
victory = None
shot_by = None
previously_played = None
Playing = "Menu"
difficulty = None

"""Bullets"""
bullet_group = pygame.sprite.Group()

"""Buttons"""
easy_button = EasyButton(pos=(100,550), action=EasyButton.start_game)
medium_button = NormalButton(pos=(450,550), action=NormalButton.start_game)
hard_button = HardButton(pos=(800,550), action= HardButton.start_game)
button_group = pygame.sprite.Group(easy_button, medium_button, hard_button)

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
MainFont = pygame.font.Font("data/graphics/Fonts/VCR_OSD_MONO.ttf", 50)

"""Background"""
tmx_data = load_pygame('data/graphics/Tiled/Gamejam.tmx')
Background = background(tmx_data)
Background.loading()

"""Player Character"""
player = Player()
player_group = pygame.sprite.GroupSingle(player)

timer = pygame.USEREVENT+1
        
"""Game Loop"""
while True:
    for event in pygame.event.get():
        # For when the person closes the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if the player right clicks.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            player.shooting()
        
        # restart button and resetting the game.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = False
                victory = None
                shot_by = None
                bullet_group.empty()
        
        # the countdown timer when the game starts.
        elif event.type == timer:
            if game_active == True:
                counter -= 1 # removes each second.
                if counter == 0: # when the game reaches 0 it goes into game over
                    pygame.time.set_timer(timer, 0)
                    victory = False
                    game_active = False
                if destructable_count == 0: # when the destructible objects have reached zero, player wins.
                    victory = True
                    game_active = False
    
    """Music applied"""
    if Playing != previously_played:
        if not game_active and Playing == "Menu":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('data/audio/music/Menu.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1) # will loop the track.
            Playing = "Menu"
        elif game_active and Playing == "Game":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('data/audio/music/Game.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1) # will loop the track.
            Playing = "Game"
        elif not game_active and Playing == "TimeOut":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('data/audio/music/TimeOut.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1) # will loop the track.
            Playing = "TimeOut"
        elif not game_active and Playing == "Victory":
            pygame.mixer_music.stop()
            pygame.mixer_music.load('data/audio/music/Victory.wav')
            pygame.mixer_music.set_volume(0.25)
            pygame.mixer_music.play(loops= -1) # will loop the track.
            Playing = "Victory"
        else:
            pygame.mixer_music.stop()
            Playing == "None" 
        
        previously_played = Playing # after the track is played, so that it does not repeat.
    
    """Places and draws the game"""
    if game_active: 
        Background.draw(screen)
        player_group.draw(screen)
        player_group.update(Background.objects, bullet_group)
        bullet_group.draw(screen)
        Playing = "Game"
        Text.countdown()
        
        destructable_count = len([obj for obj in Background.objects if obj.type=="Destructable"]) # counts each destructible object left.
        Text.remaining(destructable_count)
    
    else: # when the game is not running. Places the menu
        Background.draw(screen)
        screen.blit(gray_overlay,(0,0))
        button_group.update()
        button_group.draw(screen)
        Playing = "Menu"
        Text.Background()
        Text.instructions()
        Text.title()

        if victory == True: # if the victory is achieved.
            if difficulty == "Hard": # if the difficulty is hard, the text will be placed differently to when the player plays a different difficulty.
                screen.blit(green_overlay,(0,0))
                button_group.draw(screen)
                Playing = "Victory"
                Text.Background()
                Text.WinHard()
            else: # when played on a different difficulty.
                screen.blit(green_overlay,(0,0))
                button_group.draw(screen)
                Playing = "Victory"
                Text.Background()
                Text.Win()

        elif victory == False: # if the player does not achieve victory and fails.
            if shot_by: # if the player shot themself, places a different text compared to if they run out of time.
                screen.blit(red_overlay,(0,0)) 
                button_group.draw(screen)
                Playing = "None"
                Text.Background()
                Text.Shotyourself()
            else: # if the player runs out of time. Game over screen.
                screen.blit(red_overlay,(0,0))
                button_group.draw(screen)
                Playing = "TimeOut"
                Text.Background()
                Text.Lose()
        
        bullet_group.empty() # empty the bullets in the level after game loop.
    
    pygame.display.flip() # updates the display
    clock.tick(60) # max 60 fps