import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        scale_factor = 2
        
        # player position
        self.image = pygame.image.load('graphics/Tiles/tile_0134.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale_factor, self.image.get_height() * scale_factor))  # Scaled here
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
            
    def collision(self):
        object_layer = tmx_data.get_layer_by_name('Objects')
    
    def update(self):
        self.player_input()

    
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        scale_factor = 2
        self.image = pygame.transform.scale(surf, (surf.get_width() * scale_factor, surf.get_height() * scale_factor))  # Scaled here
        self.rect = self.image.get_rect(topleft=pos)
        
class Background(pygame.sprite.Sprite):
    def __init__(self, tmx_data):
        super().__init__()
        """Loading Level"""
        self.tmx_data = tmx_data  # Store the tmx_data passed in
        self.Background = pygame.sprite.Group()
        
    def loading(self):
        scale_factor = 2
        for layer in self.tmx_data.layers:
            if hasattr(layer, "data"):  # Ensure this is a tile layer
                for x, y, surf in layer.tiles():
                    # Scale the tile surface to double the size
                    scaled_surf = pygame.transform.scale(surf, (surf.get_width() * scale_factor, surf.get_height() * scale_factor))
                    pos = (x * 16 * scale_factor, y * 16 * scale_factor)  # Adjust position based on scale
                    Tile(pos=pos, surf=scaled_surf, groups=self.Background)
    
    def draw(self, window):
        self.Background.draw(window)

            
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
game_active = False
running = True

# Load the tmx data
tmx_data = load_pygame('graphics/Tiled/Gamejam.tmx')
Background = Background(tmx_data)
Background.loading()

# player character
player = pygame.sprite.GroupSingle()
player.add(Player())

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
                
    if game_active:
        Background.draw(screen)
        player.draw(screen)
        player.update()
    else:
        screen.fill("Green")

    pygame.display.flip()
    clock.tick(60)