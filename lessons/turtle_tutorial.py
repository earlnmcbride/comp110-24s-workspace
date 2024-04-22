from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255) # color mode to Red-Green-Blue (RGB)

carolina_blue_rgb = (80, 160, 211) # RGB values for Carolina blue

leo.color(carolina_blue_rgb) # fill color and set pen

leo.penup ()
leo.goto(45,60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(100)
    leo.left(120)
    i = i + 1

leo.end_fill()
leo.speed(50)
leo.hideturtle()

done()