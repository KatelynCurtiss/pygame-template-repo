import pygame
import sys
import config


pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.TITLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config.HOT_PINK) 


def init_game():
    pygame.init()
    screen = pygame.display.set_mode(( config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  
    pygame.display.set_caption("Draw Lines Without Using a Function")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                return False  
    return True  

def main():
    screen = init_game()
    clock = pygame.clock.Clock() # Initialize the clock object
    
    start_pos1 = [150, 150]
    end_pos1 = [350, 500]
    line_color1 = config.GREEN
    line_thickness1 = 10  

   
    start_pos2 = [400, 350]
    end_pos2 = [225, 425]
    line_color2 = config.BLUE
    line_thickness2 = 6 

    start_pos3 = [100, 400]
    end_pos3 = [250, 50]
    line_color3 = config.PURPLE
    line_thickness3 = 25  

    start_pos4 = [400, 400]
    end_pos4 = [120, 500]
    line_color4 = config.PINK
    line_thickness4 = 8 

    
    start_pos5 = [100, 500]
    end_pos5 = [120, 50]
    line_color5 = config.RED
    line_thickness5 = 7 


   
    running = True
    while running:
        running = handle_events()   
        screen.fill(config.HOT_PINK)  

       
        pygame.draw.line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        pygame.draw.line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        pygame.draw.line(screen, line_color3, start_pos3, end_pos3, line_thickness3)
        pygame.draw.line(screen, line_color4, start_pos4, end_pos4, line_thickness4)
        pygame.draw.line(screen, line_color5, start_pos5, end_pos5, line_thickness5)

        pygame.display.flip()  

        clock.tick(config.FPS)

    pygame.quit() 
    sys.exit()  
if __name__ == "__main__":
    main()  

    thickness = 15
    for x_offset in range(0, 300, 50):
        pygame.draw.line(screen, config.HOT_PINK, [75 + x_offset, 300], [440 + x_offset, 525], thickness)
        x_offset = x_offset + 20
    
pygame.display.flip()

pygame.quit()
sys.exit()

def draw_rectangle(screen, rect, color, thickness):

    pygame.draw.rect(screen, color, rect, thickness)


my_rect1 = [100, 100, 200, 150]
thickness1 = 8 

draw_rectangle(screen, my_rect1, config.GREEN, thickness1)


def draw_circle(screen, center, radius, color, thickness):
    
    pygame.draw.circle(screen, color, center, radius, thickness)

circle_center = (300, 200)  
circle_radius = 50           
circle_color = config.GREEN   
circle_thickness = 0         

draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

def draw_line(surface, color, start_pos, end_pos, thickness):
    

    pygame.draw.line(surface, color, start_pos, end_pos, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()  

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  

        
        draw_line(screen, config.BLUE, [100, 100], [700, 500], 5)  

       
        draw_line(screen, config.RED, [75, 250], [500, 300], 2)  

        pygame.display.flip()

        clock.tick(config.FPS) 

    pygame.quit()
    sys.exit()


