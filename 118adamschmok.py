import turtle as trtl # Imports turtle
tboy = trtl.Turtle() # Makes turtle
#tboy.hideturtle()

window_color = "#ffffff"
window_border = "#cfe1f4"
edge_color = "#66707c"
outer_edge = "#4a525b"

tboy.pencolor(outer_edge)
tboy.fillcolor(window_border)
count = 0
tboy.penup()
tboy.goto(-137, 68.5)
tboy.pendown()
tboy.begin_fill()
while count < 4:
    if count%2 == 0:
        tboy.forward(274)
    else:
        tboy.forward(137)
    tboy.circle(-5, 90)
    count += 1
tboy.end_fill()
tboy.penup()
tboy.goto(-130, 41.5)
tboy.pendown()
small_count = 0
while small_count < 4:
    if small_count%2 == 0:
        tboy.forward(274)
    else:
        tboy.forward(137)
    tboy.right(90)
    small_count += 1

wn = trtl.Screen()
wn.mainloop()