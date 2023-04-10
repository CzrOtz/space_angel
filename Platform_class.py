import pygame

class Platforms:
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
        self.character = None

    
    def load_platform(self, surface_to_be_rendered):
        pre_image = pygame.image.load(self.image_source)
        image2 = pygame.transform.scale(pre_image, self.size_of_image)
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        self.surface_to_be_rendered = surface_to_be_rendered 
    
        return self.surface_to_be_rendered.blit(image2, image_rect)

    def platform_rect(self):
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        return image_rect


    def lock_to_floor_left(self):
        self.position_x -= 10
    
    def lock_to_floor_right(self):
        self.position_x += 10
    
    def is_in_contact_with_platform(self, character):
        self.character = character

        if self.platform_rect().colliderect(character.enemy_rect()):
            return True
        
        else: 
            return False
        
    def hero_in_contact(self, character):
        self.character = character

        if self.platform_rect().colliderect(character.hero_rect()):
            return True
        
        else:
            return False
        