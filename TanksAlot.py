import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # player position
        self.image = pygame.image.load('graphics/Tiles/tile_0134.png')
        self.rect = self.image.get_rect(midbottom = (150,400))
        self.x = 150
        self.y = 400
        
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        """Movement"""
        if keys[pygame.K_w]:
            self.y -= 1
        elif keys[pygame.K_s]:
            self.y += 1
        elif keys[pygame.K_a]:
            self.x -= 1
        elif keys[pygame.K_d]:
            self.y += 1
    
    def update(self):
        self.player_input()

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
game_active = False
running = True

"""Player Character"""
player = pygame.sprite.GroupSingle()
player.add(Player())
player_x_pos = 500
player_y_pos = 500
player_surf = pygame.image.load('graphics/Tiles/tile_0134.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (player_x_pos, player_y_pos))
    
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
        screen.fill("purple")
        player.draw(player_surf, screen)
        player.update()
    else:
        screen.fill("Green")

    
    pygame.display.flip()
    clock.tick(60)