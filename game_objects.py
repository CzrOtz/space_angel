
import pygame
from Enemy_class import Enemy
from Background_class import Background
from Hero_class import Hero, Flame
from Platform_class import Platforms
from game_parameters import *

pygame.init()

flame_obj = Flame(
    flame["flame"]["image"], #source
    flame["flame"]["size"], #size
    flame["flame"]["position_x"], #position x
    flame["flame"]["position_y"], #position y
    )
background_0 = Background(
    background_images["background0"]["image"],
    background_images["background0"]["size"],
    background_images["background0"]["position_x"],
    background_images["background0"]["position_y"],
    background_images["background0"]["size"][0],
    background_images["background0"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)
background_1 = Background(
    background_images["background1"]["image"],
    background_images["background1"]["size"],
    background_images["background1"]["position_x"],
    background_images["background1"]["position_y"],
    background_images["background1"]["size"][0],
    background_images["background1"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)
background_2 = Background(
    background_images["background2"]["image"],
    background_images["background2"]["size"],
    background_images["background2"]["position_x"],
    background_images["background2"]["position_y"],
    background_images["background2"]["size"][0],
    background_images["background2"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)
background_3 = Background(
    background_images["background3"]["image"],
    background_images["background3"]["size"],
    background_images["background3"]["position_x"],
    background_images["background3"]["position_y"],
    background_images["background3"]["size"][0],
    background_images["background3"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

floor = Background(
    background_images["floor"]["image"],
    background_images["floor"]["size"],
    background_images["floor"]["position_x"],
    background_images["floor"]["position_y"],
    background_images["floor"]["size"][0],
    background_images["floor"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
    )
floor2 = Background(
    background_images["floor2"]["image"],
    background_images["floor2"]["size"],
    background_images["floor2"]["position_x"],
    background_images["floor2"]["position_y"],
    background_images["floor2"]["size"][0],
    background_images["floor2"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
    )
floor3 = Background(
    background_images["floor3"]["image"],
    background_images["floor3"]["size"],
    background_images["floor3"]["position_x"],
    background_images["floor3"]["position_y"],
    background_images["floor3"]["size"][0],
    background_images["floor3"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
    )

platform_A = Platforms(
    platforms["platform1"]['image'],
    platforms["platform1"]["size"],
    platforms["platform1"]["position_x"],
    platforms["platform1"]['position_y'],
    platforms["platform1"]["size"][0],
    platforms["platform1"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

platform_B = Platforms(
    platforms["platform2"]['image'],
    platforms["platform2"]["size"],
    platforms["platform2"]["position_x"],
    platforms["platform2"]['position_y'],
    platforms["platform2"]["size"][0],
    platforms["platform2"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

platform_C = Platforms(
    platforms["platform3"]['image'],
    platforms["platform3"]["size"],
    platforms["platform3"]["position_x"],
    platforms["platform3"]['position_y'],
    platforms["platform3"]["size"][0],
    platforms["platform3"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

platform_D = Platforms(
    platforms["platform4"]['image'],
    platforms["platform4"]["size"],
    platforms["platform4"]["position_x"],
    platforms["platform4"]['position_y'],
    platforms["platform4"]["size"][0],
    platforms["platform4"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

platform_E = Platforms(
    platforms["platform5"]['image'],
    platforms["platform5"]["size"],
    platforms["platform5"]["position_x"],
    platforms["platform5"]['position_y'],
    platforms["platform5"]["size"][0],
    platforms["platform5"]["size"][1],
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)


enemy_1 = Enemy(
        enemy_properties["enemy0"]["image"],
         enemy_properties["enemy0"]["size"],
          enemy_properties["enemy0"]["position_x"],
           enemy_properties["enemy0"]["position_y"],
            enemy_properties["enemy0"]["size"][0],
             enemy_properties["enemy0"]["size"][1]
             )

enemy_1_2 = Enemy(
        enemy_properties["enemy0"]["image"],
         enemy_properties["enemy0"]["size"],
          platform_A.position_x,
           platform_A.position_y - 70,
            enemy_properties["enemy0"]["size"][0],
             enemy_properties["enemy0"]["size"][1]
             )

enemy_1_3 = Enemy(
        enemy_properties["enemy0"]["image"],
         enemy_properties["enemy0"]["size"],
          platform_B.position_x,
           platform_B.position_y - 70, 
            enemy_properties["enemy0"]["size"][0],
             enemy_properties["enemy0"]["size"][1]
             )

enemy_1_4 = Enemy(
        enemy_properties["enemy0"]["image"],
         enemy_properties["enemy0"]["size"],
          platform_B.position_x + 30,
           platform_B.position_y - 80,
            enemy_properties["enemy0"]["size"][0],
             enemy_properties["enemy0"]["size"][1]
             )



enemy_2 = Enemy(
        enemy_properties["enemy1"]["image"],
         enemy_properties["enemy1"]["size"],
          enemy_properties["enemy1"]["position_x"],
           enemy_properties["enemy1"]["position_y"],
            enemy_properties["enemy1"]["size"][0],
            enemy_properties["enemy1"]["size"][1]
            )

enemy_2_1 = Enemy(
        enemy_properties["enemy1"]["image"],
         enemy_properties["enemy1"]["size"],
          enemy_properties["enemy1"]["position_x"],
           enemy_properties["enemy1"]["position_y"],
            enemy_properties["enemy1"]["size"][0],
            enemy_properties["enemy1"]["size"][1]
            )

enemy_2_2 = Enemy(
        enemy_properties["enemy1"]["image"],
         enemy_properties["enemy1"]["size"],
          platform_C.position_x + 30,
           platform_C.position_y - 150,
            enemy_properties["enemy1"]["size"][0],
            enemy_properties["enemy1"]["size"][1]
            )

enemy_2_3 = Enemy(
        enemy_properties["enemy1"]["image"],
         enemy_properties["enemy1"]["size"],
          enemy_properties["enemy1"]["position_x"],
           enemy_properties["enemy1"]["position_y"],
            enemy_properties["enemy1"]["size"][0],
            enemy_properties["enemy1"]["size"][1]
            )


enemy_3 = Enemy(
        enemy_properties["enemy2"]["image"],
         enemy_properties["enemy2"]["size"],
          enemy_properties["enemy2"]["position_x"],
           enemy_properties["enemy2"]["position_y"],
            enemy_properties["enemy2"]["size"][0],
             enemy_properties["enemy2"]["size"][1]
             )

enemy_4 = Enemy(
        enemy_properties["enemy4"]["image"],
         enemy_properties["enemy4"]["size"],
          enemy_properties["enemy4"]["position_x"],
           enemy_properties["enemy4"]["position_y"],
            enemy_properties["enemy4"]["size"][0],
             enemy_properties["enemy4"]["size"][1]
             )

enemy_5 = Enemy(
        enemy_properties["enemy5"]["image"],
         enemy_properties["enemy5"]["size"],
          enemy_properties["enemy5"]["position_x"],
           enemy_properties["enemy5"]["position_y"],
            enemy_properties["enemy5"]["size"][0],
             enemy_properties["enemy5"]["size"][1]
             )

hero = Hero(
    hero_properties["hero"]["image"],
     hero_properties["hero"]["size"],
      hero_properties["hero"]["position_x"],
       hero_properties["hero"]["position_y"],
        hero_properties["hero"]["size"][0],
         hero_properties["hero"]["size"][1]
    )

all_platforms = [
    platform_A,
    platform_B,
    platform_C,
    platform_D,
    platform_E
    ]


all_enemies = [
    enemy_1,
    enemy_2,
    enemy_3,
    enemy_4,
    enemy_5
]