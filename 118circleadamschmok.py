import turtle as trtl # Imports Turtle Module
import random # Imports random Module
tboy = trtl.Turtle()
tboy.hideturtle()
tboy.speed(0)

# Creates variables
color_list = ["red", "green", "blue", "black"] # Creates list of colors
count = 1
small_count = 2

# Draws 4 shapes of different size and color
while count < 5:

    # Sets color for current iteration
    color = color_list.pop(random.randint(0, (4-count))) # Picks a color from color_list and remooves that color from the list
    tboy.color(color)
    tboy.penup()

    if count < 3: # Makes multi-point star
        tboy.goto(0,-350/count)
        tboy.pendown()
        tboy.circle(350/count, 36000, 153)
    else: # reduces number of points due to small size
        tboy.goto(0,-350/(count*small_count))
        tboy.pendown()
        tboy.circle(350/(count*small_count), 3600, (15*count))
        small_count += 1
    count += 1

# Creates 3D effect on center hexagon
tboy.goto(0,0) 
tboy.dot(25)
tboy.right(-30)
tboy.forward(30)
tboy.goto(0,0)
tboy.right(-120)
tboy.forward(30)

# Keeps screen active after code is complete
wn = trtl.Screen() 
wn.mainloop()