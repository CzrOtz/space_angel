
import pygame


class Enemy:
    def __init__(self, image_source, size_of_image, position_x, position_y, rect_width, rect_heigh):
        self.image_source = image_source
        self.size_of_image = size_of_image
        self.position_x = position_x
        self.position_y = position_y
        self.rect_width = rect_width - 10
        self.rect_heigth = rect_heigh -10
        self.surface_to_be_rendered = None
        


    
    def load_enemy(self, surface_to_be_rendered):
        image = pygame.image.load(self.image_source)
        image1 = pygame.transform.flip(image, True, False)
        image2 = pygame.transform.scale(image1, self.size_of_image)
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_heigth)
        self.surface_to_be_rendered = surface_to_be_rendered

        # temp_surface = pygame.Surface((self.rect_width, self.rect_heigth))
        # temp_surface.fill((255,255,255))
        # temp_surface.blit(image2, (0,0))

    
        return self.surface_to_be_rendered.blit(image2, image_rect)

        
    
    def enemy_rect(self):
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_heigth)
        return image_rect


    def enemy_move_left(self):
        self.position_x -= 15
        
    def enemy_move_right(self):
        self.position_x += 6.2
        
    
    def enemy_move_up(self):
        self.position_y -= 5
        
    
    def  enemy_move_down(self):
        self.position_y += 5
    
    def enemy_got_hit(self):
        self.position_y += 100

        
        
    
#if self.position_x < -window_width then self.position_x = window_width * 2