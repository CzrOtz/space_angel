import pygame
# WW == WINDOW_WIDTH, WH == WINDOW_HEIGHT

class Background:
    def __init__(self, image_source, size_of_image, position_x, position_y, rect_width, rect_height, WW, WH):
        self.image_source = image_source
        self.size_of_image = size_of_image
        self.position_x = position_x 
        self.position_y = position_y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.WW = WW
        self.WH = WH
        self.surface_to_be_rendered = None

    
    def load_background(self, surface_to_be_rendered):
        pre_image = pygame.image.load(self.image_source)
        image2 = pygame.transform.scale(pre_image, self.size_of_image)
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        self.surface_to_be_rendered = surface_to_be_rendered 

        return self.surface_to_be_rendered.blit(image2, image_rect)

    def background_rect(self):
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        return image_rect

    def move_floor_forward(self):
        self.position_x -= 10
    
    def move_floor_backward(self):
        self.position_x += 10
        
    def track_floor(self):
        return self.position_x
    
    def move_background_forward(self):
        self.position_x -= 2
    
    def move_background_backwards(self):
        self.position_x += 2
    
    def hide_and_repeat(self):
        if self.position_x == - self.WW:
            self.position_x = self.WW * 2
    



   