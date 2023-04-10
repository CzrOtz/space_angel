import pygame

class Hero: 
    def __init__(self, hero_image, size_of_hero, position_x, position_y, rect_width, rect_heigh):
        self.hero_image = hero_image
        self.size_of_hero = size_of_hero
        self.position_x = position_x
        self.position_y = position_y
        self.rect_width = rect_width - 20
        self.rect_height = rect_heigh - 20
        self.surface_to_be_rendered = None
        self.y_gravity = 2 
        self.jump_height = 35 
        self.y_velocity = self.jump_height
        self.last_y_position = None
        self.platform = None
        self.fall_velocity = 1
        self.enemy = None
        
    def load_hero(self, surface_to_be_rendered):
        image = pygame.image.load(self.hero_image)
        image2 = pygame.transform.scale(image, self.size_of_hero)
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        self.surface_to_be_rendered = surface_to_be_rendered

        return self.surface_to_be_rendered.blit(image2, image_rect)
    
    def hero_rect(self):
        image_rect = pygame.Rect(self.position_x, self.position_y, self.rect_width, self.rect_height)
        return image_rect
        

    def hero_move_back(self):
        self.position_x -= 10
    
    def hero_move_forward(self):
        self.position_x += 15

    def is_hero_on_a_platform(self, platform):
        self.platform = platform

        if self.hero_rect().colliderect(platform.platform_rect()) and self.position_y + 50 < platform.position_y:
            return True
        else:
            return False

    def hero_on_platfom(self, platform):
        self.platform = platform

        self.position_y = platform.position_y - 175
    
    def hero_platform_dismount(self, last_y_position):
        self.last_y_position = last_y_position


        self.position_y = last_y_position[-1]
        print(self.position_y, ' im the method ')

    def jump_up(self):
        self.position_y -= self.y_velocity
         
    def jump_down(self):
       
        self.y_velocity -= self.y_gravity
       
        if self.y_velocity < -self.jump_height:
            self.y_velocity = self.jump_height
    
    def fall(self):
        self.position_y += self.fall_velocity
        self.fall_velocity += self.y_gravity
    
    def hero_got_hit(self, enemy):
        self.enemy = enemy

        if self.hero_rect().colliderect(enemy.enemy_rect()):
            return True
        else:
            return False
         
    
class Flame(Hero):
    def __init__(self, image, size_of_image, position_xf, position_yf, ):
        
        self.image = image
        self.size_of_image = size_of_image
        self.position_xf = position_xf
        self.position_yf = position_yf
        self.surface_to_be_rendered = None
        self.enemy = None
 
    
    def load_flame(self, surface_to_be_rendered):
        image = pygame.image.load(self.image)
        image2 = pygame.transform.scale(image, self.size_of_image)
        image_rect = pygame.Rect(self.position_xf, self.position_yf, self.size_of_image[0], self.size_of_image[1])
        self.surface_to_be_rendered = surface_to_be_rendered

        return self.surface_to_be_rendered.blit(image2, image_rect)
    
    def flame_rect(self):
        image_rect = pygame.Rect(self.position_xf, self.position_yf, self.size_of_image[0], self.size_of_image[1])
        return image_rect



    def shoot_flame(self):
        self.position_xf += 100

    def flame_enemy_collide(self, enemy):
        self.enemy = enemy

        if self.flame_rect().colliderect(enemy.enemy_rect()):
            return True
        else:
            return False
        
    
    
    





        

    
