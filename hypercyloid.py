# hypocycloid.py
from graphics import *
from math import *

def setup_and_initialize():
    """The "setup_and_initialize" function does just that: sets up the graphics window, asks the user for some values to begin the program with, and returns those values to the main program. There is not yet any error checking: the Outer Radius must be less than 400, the Inner Radius must be less than the Outer Radius."""
    window = GraphWin("Spirograph-TM!", 800, 800)
    window.setCoords(-400.0,-400.0,400.0,400.0)
    window.setBackground("black")
    title = Text(Point(0,100),"Hypocycloid!")
    title.setSize(24)
    title.setFill("white")
    title.draw(window)
    tag = Text(Point(0,50),"This program draws Spirograph-style pictures!")
    tag.setFill("white")
    tag.draw(window)
    prompt_a = Text(Point(-100,0),"Outer radius a?")
    prompt_a.setFill("white")
    prompt_b = Text(Point(-100,-25),"Inner radius b?")
    prompt_b.setFill("white")
    prompt_theta_interval = Text(Point(-100,-50),"Theta interval?")
    prompt_theta_interval.setFill("white")
    input_a = Entry(Point(0,0),5)
    input_b = Entry(Point(0,-25),5)
    input_theta_interval = Entry(Point(0,-50),5)
    prompt_a.draw(window);prompt_b.draw(window);prompt_theta_interval.draw(window)
    input_a.draw(window);input_b.draw(window);input_theta_interval.draw(window)
    prompt = Text(Point(0,-100),"Click this window once your values have been entered.")
    prompt.setFill("white")
    prompt.draw(window)
    click = window.getMouse()     # This mouse click allows the user to enter the values
    a = eval(input_a.getText())   # Make sure to convert the Text values to numbers using eval
    b = eval(input_b.getText())
    theta_interval = eval(input_theta_interval.getText())
    
    # Because we're going to be drawing in this Graphics window, we have to now erase
    # everything that we've drawn in it to this point:
    title.undraw();tag.undraw();prompt_a.undraw();prompt_b.undraw();prompt_theta_interval.undraw()
    input_a.undraw();input_b.undraw();input_theta_interval.undraw();prompt.undraw()
    return window, a, b, theta_interval     # Return these values for use in the drawing function
    
def draw_hypocycloid(window, a, b, theta_interval):
    """This function takes the parameters necessary to draw the epicycloid and draws them in the window."""

    def get_line_color(n):
        """ This internal function is used to get different colors for the lines drawn."""
        k = 700                 # This constant determines how quickly the color changes
        if (n / k == 0):        # n / k is an integer division that returns the whole number
            return "red"        # value of that division. Thus, every "k" lines that are drawn,
        elif (n / k == 1):      # the color switches a little.
            return "orange"
        elif (n / k == 2):
            return "yellow"
        elif (n / k == 3):
            return "green"
        elif (n / k == 4):
            return "cyan"
        elif (n / k == 5):
            return "blue"
        elif (n / k == 6):
            return "purple"
        elif (n / k == 7):
            return "magenta"
        elif (n / k == 8):
            return "white"
        else:
            return "blue"
    
    theta = 0                   # Start at theta = 0
    count = 0                   # This counter is used to determine when we should change color
    x = (a-b) * cos(radians(theta)) + b * cos(((a-b) * radians(theta)) / b)
    y = (a-b) * sin(radians(theta)) - b * sin(((a-b) * radians(theta)) / b)
    x_start = x; y_start = y    # x_start and y_start are used to determine when we've returned
                                # to the start (and thus can stop drawing)
    x_new = -2; y_new = -2      # These are nonsense values until we actually calculate in loop
    while ((x_new != x_start) or (y_new != y_start)):   # While we haven't returned to the start...
        theta += theta_interval 
        count += 1
        x_new = (a-b) * cos(radians(theta)) + b * cos(((a-b) * radians(theta)) / b)
        y_new = (a-b) * sin(radians(theta)) - b * sin(((a-b) * radians(theta)) / b)
        the_line = Line(Point(x_new,y_new),Point(x,y))
        line_color = get_line_color(count)    # Set the line color according to the function
        the_line.setFill(line_color)
        the_line.draw(window)                 # Draw the line!
        x = x_new; y = y_new                  # Transfer new numbers to old variables so
                                              # we can draw the next line
        # print x_new, y_new        # This just monitors the coordinates in the Terminal window
                                    # It's cool to watch them scroll by while the Spirograph
                                    # is drawing, but it does slow the program down!
    Text(Point(0,-380),"Click on the window to close it.").draw(window)  # When done, let them
                                                                         # know how to finish
    click = window.getMouse()       # Pause once we're done so the user can admire the drawing
def main():
    window, a, b, theta = setup_and_initialize()
    draw_hypocycloid(window, a, b, theta)
    
if __name__ == "__main__":
    main()