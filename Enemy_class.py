
import pygame


class Enemy:
    def __init__(self, image_source, size_of_image, position_x, position_y, rect_width, rect_heigh, health):
        self.image_source = image_source
        self.size_of_image = size_of_image
        self.position_x = position_x
        self.position_y = position_y
        self.rect_width = rect_width - 10
        self.rect_heigth = rect_heigh -10
        self.surface_to_be_rendered = None
        self.flame = None
        self.startign_position = 0
        self.hero = None
        self.health = health
        self.object = None
        


    
    def load_enemy(self, surface_to_be_rendered):
        image = pygame.image.load(self.image_source)
        image1 = pygame.transform.flip(image, True, False)
        image2 = pygame.transform.scale(image1, self.size_of_image)
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_heigth)
        self.surface_to_be_rendered = surface_to_be_rendered

        #all this does is that it loads the image

        return self.surface_to_be_rendered.blit(image2, image_rect)

        
    
    def rect(self):
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
    
    def enemy_got_hit_flame(self, flame):
        self.flame = flame

        if self.rect().colliderect(flame.rect()):
            return True
        else:
            return False
    
    def move_towards(self, hero):
        self.hero = hero
        
        if hero.position_x > self.position_x:
            self.position_x += 5
        
        elif hero.position_x < self.position_x:
            self.position_x -= 5

    def keep_in_platform(self):
        self.position_x -= 10

    
    def in_contact_with(self, object):
        self.object = object

        if self.rect().colliderect(object.rect()):
            return True
        else:
            return False
            


    # def is_in_contact_with(self, character):
    #     self.character = character

    #     if self.platform_rect().colliderect(character.enemy_rect()):
    #         return True
        
    #     else: 
    #         return False

        
    

    

    

    
        

        
        
    
#if self.position_x < -window_width then self.position_x = window_width * 2