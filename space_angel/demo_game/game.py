import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Platformer Game")

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 50
player_velocity = 0
player_jump_power = 35
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the platforms
platform_width = 100
platform_height = 20
platform_gap = 200
platform_speed = 3
platform_color = (100, 100, 100)
platform_list = [
    pygame.Rect(0, screen_height - platform_height, screen_width, platform_height),
    pygame.Rect(screen_width // 2 - platform_width // 2, 400, platform_width, platform_height),
    pygame.Rect(screen_width + platform_gap, 300, platform_width, platform_height),
]

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    player_rect.y += player_velocity

    # Apply gravity to the player 
    player_velocity += 1

    # Detect collisions with the platforms
    for platform in platform_list:
        if player_rect.colliderect(platform):
            player_rect.bottom = platform.top
            player_velocity = 0

    # Move the platforms
    for platform in platform_list:
        platform.x -= platform_speed

        # Generate new platforms
        if platform.right < 0:
            platform.left = screen_width + platform_gap

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_rect.bottom == screen_height - platform_height:
        player_velocity = -player_jump_power

    # Draw the game to the screen
    screen.fill((255, 255, 255))
    for platform in platform_list:
        pygame.draw.rect(screen, platform_color, platform)
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    pygame.display.update()

    # Wait for a short time to control the game speed
    pygame.time.wait(10)