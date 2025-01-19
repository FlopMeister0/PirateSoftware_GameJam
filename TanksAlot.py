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
    
    def update(self):
        self.player_input()
        
class background(pygame.sprite.Sprite):
    def __init__(self):
        scale_factor = 2

    def blit_all_tiles(window, tmxdata):
        scale_factor = 2
        for layer in tmxdata:
            for x, y, surf in layer.tiles():
                # tiles[0] = x grid location
                # tiles[1] = y grid location
                # tile[2] = image data for blitting
                #scaled_surf = pygame.transform.scale_by(surf, scale_factor)
                x_pixel = x * 16
                y_pixel = y * 16
                window.blit(surf, (x_pixel, y_pixel))  
            
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
game_active = False
running = True

# player character:
# spritesheet = spritesheet.parse_sprite()
# player_Rect = player_img.get_rect()

"""Loading Level"""
tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
# player_rect.x, player_rect.y = map.start_x, map.start_y

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
        background.blit_all_tiles(screen, tmx_data)
        player.draw(screen)
        player.update()
    else:
        screen.fill("Green")

    
    pygame.display.flip()
    clock.tick(60)