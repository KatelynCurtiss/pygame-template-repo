# Write this function above your main( ) function
def draw_rectangle(screen, rect, color, thickness):
    """Draws a rectangle on the Pygame window."""
    pygame.draw.rect(screen, color, rect, thickness)

# Call the rectangle function from your main ( ) function like so:
# In the list my_rect1, 100 and 100 are the x,y coordinates for the top left corner of the rectangle
# Rectangle has a width of 200 pixels
# Height of rectangle is 150 pixels
my_rect1 = [100, 100, 200, 150]
thickness1 = 8 # Line thickness (width) in pixels

draw_rectangle(screen, my_rect1, config.GREEN, thickness1)

# Write this function above your main( ) function
def draw_circle(screen, center, radius, color, thickness):
    """Draws a circle on the Pygame window."""
    pygame.draw.circle(screen, color, center, radius, thickness)

# Define circle arguments for the function call
circle_center = (300, 200)  # Center point of the circle (x, y)
circle_radius = 50           # Radius of the circle
circle_color = config.GREEN   # Color of the circle
circle_thickness = 0         # 0 pixels creates a filled in circle

# Call the function that draws the circle from your main() function
draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

# Write function above your main( ) function
def draw_line(surface, color, start_pos, end_pos, thickness):
    """Draws a line on the screen with the specified color and thickness."""

    pygame.draw.line(surface, color, start_pos, end_pos, thickness)

# Calling the function to draw lines
def main():
    screen = init_game()
    clock = pygame.time.Clock()  # Initialize the clock here

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config

        # Call the function to draw the lines

        # Draw a BLUE line with thickness/width of 5 pixels
        draw_line(screen, config.BLUE, [100, 100], [700, 500], 5)  

        # Draw a RED line with thickness/width of 2 pixels
        draw_line(screen, config.RED, [75, 250], [500, 300], 2)  

        pygame.display.flip()

        clock.tick(config.FPS)  # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()
