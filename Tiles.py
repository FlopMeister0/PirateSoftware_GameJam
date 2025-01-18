import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self,image,x,y,spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        # Manually load in the self.image (self.image = pygame.image.Load(image))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
        
    """helper"""
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
class TileMap():
    def __init__(self,filename,spritesheet):
        self.tile_size = 16 # 16 pixels
        self.start_x, self.start_y = 0,0 # where the player will spawn on the tilemap
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles_background(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0,0,0)) # makes it transparent, draws it all once instead of doing it multiple times to make it less intensive
    
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0,0))
    
    def load_map(self):
        for tile in self.tiles:
            Tile.draw(self.map_surface)
        
        
    """helper"""
    def read_csv(self,filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data,delimiter=',')
            for row in data: # reading each row
                map.append(list(row)) # stores each value of the row into a list.
        return map
    
    def load_tiles_background(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x,y = 0,0
        for row in map: # outer loop to iterate through each row
            x = 0
            for tile in row: # look at at row for the specific tile key
                if tile == '0':
                    tiles.append(Tile('tile_0000.png'), x * self.tile_size, y * self.tile_size, self.spritesheet)
                elif tile == '1':
                    tiles.append(Tile('tile_0001.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('tile_0002.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '18':
                    tiles.append(Tile('tile_0018.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '19':
                    tiles.append(Tile('tile_0019.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '20':
                    tiles.append(Tile('tile_0020.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '36':
                    tiles.append(Tile('tile_0036.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '37':
                    tiles.append(Tile('tile_0037.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '38':
                    tiles.append(Tile('tile_0038.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '54':
                    tiles.append(Tile('tile_0054.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '55':
                    tiles.append(Tile('tile_0055.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '56':
                    tiles.append(Tile('tile_0056.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '72':
                    tiles.append(Tile('tile_0072.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '91':
                    tiles.append(Tile('tile_0091.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '92':
                    tiles.append(Tile('tile_0092.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '93':
                    tiles.append(Tile('tile_0093.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                # move to the next tile in current row.
                x += 1
            # move to the next row
            y += 1
    
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
    