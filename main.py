# Katelyn Curtiss
# Febraury 11 2025
# Pygame Template 

def init_game():
    pygame.init()
    screen = pygame.display.set.mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT 
          return False
        return True
    
    
    
def main():
    screen = init_game()
    clock = pygame.time.Clock()

    running = True
    while running: 
        running = handle_events()
        screen.fill(config.WHITE)
        pygame.display.flip

        clock.tick()