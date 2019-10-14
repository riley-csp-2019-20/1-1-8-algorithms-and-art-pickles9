import turtle as trtl # Imports turtle
tboy = trtl.Turtle() # Makes turtle
tboy.hideturtle()
tboy.speed(0)

window_color = "#ffffff" # Makes variables for color palette
window_border = "#cfe1f4"
edge_color = "#66707c"
outer_edge = "#4a525b"
circle_color = "#d54747"

tboy.pencolor(outer_edge)
tboy.fillcolor(window_border)

tboy.penup()
tboy.goto(-137, 69)
tboy.pendown()

count = 0
tboy.begin_fill()
while count < 4: # Draws back box
    if count%2 == 0:
        tboy.forward(274)
    else:
        tboy.forward(137)
    tboy.circle(-5, 90)
    count += 1
tboy.end_fill()

tboy.penup()
tboy.goto(-130, 42) # Moves to draw smaller box
tboy.pendown()

small_count = 0
tboy.pencolor(edge_color)
tboy.fillcolor(window_color)

tboy.begin_fill()
while small_count < 4:
    if small_count%2 == 0:
        tboy.forward(261)
    else:
        tboy.forward(104)
    tboy.right(90)
    small_count += 1
tboy.end_fill()

tboy.penup()
tboy.goto(-129, -20) # Moves to draw smaller box
tboy.pendown()
tboy.color("#dfdfdf", "#f0f0f0")
smaller_count = 0
tboy.begin_fill()
while smaller_count < 4:
    if smaller_count%2 == 0:
        tboy.forward(259)
    else:
        tboy.forward(41)
    tboy.right(90)
    smaller_count += 1
tboy.end_fill()

tboy.pencolor(edge_color)
tboy.fillcolor(window_color)

tboy.penup()
tboy.goto(-130, 47) # Moves to draw Internet Explorer text
tboy.pendown()

tboy.write("Internet Explorer", False, align="left" ,font=("Courier New", 10, "normal"))

tboy.penup()
tboy.goto(-69, 15) # Moves to draw Unknown Error text
tboy.pendown()

tboy.write("Unknown error", False, align="left" ,font=("Courier New", 10, "normal"))

tboy.penup()
tboy.goto(-98, 31) # Moves to draw circle
tboy.pendown()

tboy.circle(-15)

tboy.color(circle_color)
tboy.penup()
tboy.goto(-98, 28) # Moves to draw circle
tboy.pendown()
tboy.begin_fill()
tboy.circle(-12)
tboy.end_fill()

tboy.penup()
tboy.goto(-100, 16) # Moves to draw x
tboy.pendown()
tboy.color(window_color)
tboy.seth(135)
xcount = 0
tboy.begin_fill()
while xcount < 4:
    tboy.forward(5)
    tboy.right(90)
    tboy.forward(3)
    tboy.right(90)
    tboy.forward(5)
    tboy.left(90)
    xcount += 1
tboy.end_fill()

wn = trtl.Screen()
wn.mainloop()
