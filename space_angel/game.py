import pygame
from game_variables import *
import random

pygame.init()

on_platform = None

last_y_position = [500,500]

can_fall = False

while is_runnign:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_runnign = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_forward = True
                
            elif event.key == pygame.K_LEFT:
                move_back = True
            
            if event.key == pygame.K_SPACE:
                jump = True
            
            if event.key == pygame.K_DOWN:
                shoot = True
                
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_forward = False
                
            elif event.key == pygame.K_LEFT:
                move_back = False
            
            if event.key == pygame.K_SPACE:
                jump = True

    enemy_1.enemy_move_left()
    enemy_2.enemy_move_left()
    enemy_3.enemy_move_left()
    enemy_4.enemy_move_left()
    enemy_5.enemy_move_right()

    floor.hide_and_repeat() 
    floor2.hide_and_repeat()
    floor3.hide_and_repeat()


    if move_forward == True:

        
        if hero.position_x > WINDOW_WIDTH // 3:

            floor.move_floor_forward() 
            floor2.move_floor_forward()
            floor3.move_floor_forward()
            platform_A.lock_to_floor_left()
            platform_B.lock_to_floor_left()
            platform_C.lock_to_floor_left()
            platform_D.lock_to_floor_left()
            platform_E.lock_to_floor_left()
            enemy_5.enemy_move_left()
        
        else:
            
            hero.hero_move_forward()

    if move_back == True:
        hero.hero_move_back()

        
        if hero.position_x < 2:
            hero.position_x = 2


    if not shoot: 
        flame_obj.position_xf = hero.position_x + 70 
        flame_obj.position_yf = hero.position_y + 70 

    if shoot:
        flame_obj.shoot_flame()
        if flame_obj.position_xf > WINDOW_WIDTH:
            shoot = False


################################################################################################################
    

    

    
      
        
        
    if jump:
        hero.jump_up()
        hero.jump_down()
         
        if hero.y_velocity == hero.jump_height:
            jump = False

            # if last_y_position[-1] != hero.position_y:
            #     last_y_position.append(hero.position_y) 
        
    on_platform = any(hero.is_hero_on_a_platform(platform) for platform in all_platforms)

    for platforms in all_platforms:
        if hero.is_hero_on_a_platform(platforms):
            hero.hero_on_platfom(platforms)
        
    
    
    print(on_platform)

    if hero.position_y < hero_properties["hero"]["position_y"] and on_platform == False and jump == False:
        can_fall = True
    

    if can_fall:
        hero.fall()
        if hero.position_y > 500:
            hero.position_y = 500

        if hero.position_y >= hero_properties["hero"]["position_y"]:
            can_fall = False
        
        elif on_platform:
            for plaforms in all_platforms:
                if hero.is_hero_on_a_platform(plaforms):
                    hero.hero_on_platfom(plaforms)
        
        elif jump == True:
            can_fall = False
        

        
        
        
    
        
    

    

    
    # if not jump:
    #     print('whats going on here') 
    #     if last_y_position[-1] > last_y_position[-2]:
    #         hero.position_y = last_y_position[-1]
    #         print(last_y_position[-1], ' CASE 1')
    #     else:
    #         hero.position_y = last_y_position[-2]
    #         print(last_y_position[-2], ' CASE 2')
                    

    # print(last_y_position, ' the array')       
    
    #now this works, now we have to figure out how to remove values

    #if the y position that was inserted into [-1] is larger, than the second to last position [-2], the y is now [-2]
    #if the y position that was inserted into [-1] is smaller, than the second to last postion [-2] the y is now [-1]

          
            
        
    
##############################################################################################################
       
    screen.blit(background, (0,0))
    background_0.load_background(screen)
    floor.load_background(screen)
    floor2.load_background(screen)
    floor3.load_background(screen)
    enemy_1.load_enemy(screen)
    enemy_2.load_enemy(screen)
    enemy_3.load_enemy(screen)
    enemy_4.load_enemy(screen) 
    enemy_5.load_enemy(screen)
    flame_obj.load_flame(screen)
    hero.load_hero(screen) 
    platform_A.load_platform(screen)
    platform_B.load_platform(screen)
    platform_C.load_platform(screen)
    platform_D.load_platform(screen)
    platform_E.load_platform(screen)

    pygame.display.update()

    clock.tick(fps)



pygame.quit()