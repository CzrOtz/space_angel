import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space angel')
background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
background.fill((25,255,255))
is_runnign = True

clock = pygame.time.Clock()

fps = 30

can_jump = True

enemies_down = 0

#to modify these, you need to do that in the method
#they can be tracked directly but moddified with the methods

move_forward = False
move_back = False
jump = False
hero_hit = False
shoot = False

enemy_5_switch = False
enemy_1_switch = False
enemy_2_switch = False
enemy_3_switch = False
enemy_4_switch = False

background_images = {
    "floor": {
        "image" : "images/better_floor.png",
        "size": (WINDOW_WIDTH, 200),
        "position_x" : 0,
        "position_y": WINDOW_HEIGHT - 200
        },

    "floor2": {
        "image" : "images/better_floor_2.png",
        "size": (WINDOW_WIDTH, 200),
        "position_x" : WINDOW_WIDTH,
        "position_y": WINDOW_HEIGHT - 200
         },
        
    "floor3": {
        "image": "images/better_floor_3.png",
        "size": (WINDOW_WIDTH, 200),
        "position_x": WINDOW_WIDTH * 2,
        "position_y": WINDOW_HEIGHT - 200 
    },

    "background0": {
        "image":"images/new_background.png",
        "size": (WINDOW_WIDTH, WINDOW_HEIGHT),
        "position_x": 0,
        "position_y": 0
    },

    "background1" : {
    "image":"images/new_1background.png",
    "size": (WINDOW_WIDTH, WINDOW_HEIGHT),
    "position_x": 0,
    "position_y": 0
    },

     "background2" : {
    "image":"images/new_1background_2.png",
    "size": (WINDOW_WIDTH, WINDOW_HEIGHT),
    "position_x": WINDOW_WIDTH,
    "position_y": 0
    },

     "background3" : {
    "image":"images/new_1background_3.png",
    "size": (WINDOW_WIDTH, WINDOW_HEIGHT),
    "position_x": WINDOW_WIDTH * 2,
    "position_y": 0
    }
}

platforms = {
    "platform1" : {
        "image":"images/better-platform.png",
        "size": (250, 75),
        "position_x": WINDOW_WIDTH // 2,
        "position_y": 450,
        
    },
    "platform2" : {
        "image":"images/better-platform.png",
        "size": (350, 75),
        "position_x": WINDOW_WIDTH,
        "position_y": 300,
        
    },
    "platform3" : {
        "image":"images/better-platform.png",
        "size": (250, 75),
        "position_x": WINDOW_WIDTH + 550,
        "position_y": 250,
        
    },
    "platform4" : {
        "image":"images/better-platform.png",
        "size": (250, 75),
        "position_x": WINDOW_WIDTH * 2,
        "position_y": 300,
        
    },
    "platform5" : {
        "image":"images/better-platform.png",
        "size": (250, 75),
        "position_x": WINDOW_WIDTH * 2.5,
        "position_y": 200,
        
    }
}

enemy_properties = {
    "enemy0": {
        "image": "images/enemy0.png",
        "size" : (100, 100),
        "position_x" : WINDOW_WIDTH // 1,
        "position_y" :  WINDOW_HEIGHT - 200,
        "health": 15
    },
    "enemy1": {
        "image": "images/enemy1.png",
        "size" : (200, 200),
        "position_x" : WINDOW_WIDTH + 600,
        "position_y": WINDOW_HEIGHT - 200,
        "rect_width": 100,
        "rect_height": 100,
        "health": 50
    },
    "enemy2": {
        "image": "images/enemy2.png",
        "size": (200, 200),
        "position_x": WINDOW_WIDTH + WINDOW_WIDTH,
        "position_y": WINDOW_HEIGHT - 200,
        "rect_width": 100,
        "rect_height": 100,
        "health": 100 
    },

    "enemy4": {
        "image": "images/angry.png",
        "size": (200, 200),
        "position_x": 500,
        "position_y": WINDOW_HEIGHT - 200,
        "rect_width": 100,
        "rect_height": 100,
        "health": 50 
    },

    "enemy5": {
        "image": "images/new_enemy_5.png",
        "size": (200,200),
        "position_x": 600,
        "position_y": WINDOW_HEIGHT - 200,
        "rect_width": 100,
        "rect_height": 100,
        "health": 1000

    }

    
} 
hero_properties = {

    "hero" : {
        "image" : "images/latest_hero.png",
        "size" : (125, 200),
        "position_x" : WINDOW_WIDTH // 3,
        "position_y" : WINDOW_HEIGHT - 200
    }
    
}
flame = {
    "flame": {
        "image": "images/flame2.png",
        "size": (50, 50),
        "position_x": hero_properties["hero"]["position_x"] + 70,
        "position_y": hero_properties["hero"]["position_y"] + 65
    }
}