import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        scale_factor = 2
        
        # player position
        self.image = pygame.transform.scale_by(pygame.image.load('graphics/Tiles/tile_0134.png').convert_alpha(), scale_factor)
        self.x = 150
        self.y = 400
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        """Movement"""
        if keys[pygame.K_w]:
            self.rect.y -= 2
        elif keys[pygame.K_s]:
            self.rect.y += 2
        elif keys[pygame.K_a]:
            self.rect.x -= 2
        elif keys[pygame.K_d]:
            self.rect.x += 2
            
    def collision():
        object_layer = tmx_data.get_layer_by_name('Objects')
    
    def update(self):
        self.player_input()
        
    
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        
class background(pygame.sprite.Sprite):
    def __init__(self, tmx_data):
        super().__init__()
        """Loading Level"""
        self.tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
        self.Background = pygame.sprite.Group()
        
    def loading(self):
        
        for layer in self.tmx_data.layers:
            if hasattr(layer,"data"): # nsure this is a tile layer. Since ile layers have "data"
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos = pos, surf = surf, groups = self.Background)
                    #scaled_surf = pygame.transform.scale_by(surf, scale_factor)
    
    def draw(self, window):
        self.Background.draw(window)

            
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
game_active = False
running = True

tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
Background = background(tmx_data)
Background.loading()

# player character:
# spritesheet = spritesheet.parse_sprite()
# player_Rect = player_img.get_rect()

"""Player Character"""
player = pygame.sprite.GroupSingle()
player.add(Player())

    
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
        player.draw(screen)
        player.update()
    else:
        screen.fill("Green")

    
    pygame.display.flip()
    clock.tick(60)