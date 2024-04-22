"""My picture depicts flowers and bees with mountains in the distance, created using the turtle module."""

__author__ = "730395850"

from turtle import Turtle, colormode, done
import random


def main() -> None:
    """The entry point of the scene."""
    colormode(255)
    screen = Turtle()
    screen.speed(0)

    draw_sky(screen, 400, 300)
    draw_grass(screen, 400, 150)
    draw_sun(screen, 30)
    for i in range(3):
        draw_flower(screen, -100 + i * 100, -100, 10)
    draw_fly(screen, 400, 300, 20)
    draw_mountain(screen, 200, 150, 1, -50)
    done()


def draw_sky(a_turtle: Turtle, width: float, height: float) -> None:
    """This function draws a blue sky."""
    a_turtle.penup()
    a_turtle.goto(-width / 2, height / 4)
    a_turtle.setheading(0)
    a_turtle.pendown()
    a_turtle.color("blue")
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(height / 2)
        a_turtle.right(90)
    a_turtle.end_fill()


def draw_grass(a_turtle: Turtle, width: float, height: float) -> None:
    """This function draws green grass."""
    a_turtle.penup()
    a_turtle.goto(-width / 2, -height / 2)
    a_turtle.setheading(0)
    a_turtle.pendown()
    a_turtle.color("green")
    a_turtle.begin_fill()
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height / 2)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.end_fill()


def draw_sun(a_turtle: Turtle, radius: float) -> None:
    """This function draws a sun."""
    a_turtle.penup()
    a_turtle.goto(0, 70)
    a_turtle.pendown()
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def draw_flower(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """This function draws the flower stem and root."""
    # stem
    a_turtle.penup()
    a_turtle.goto(x, y - size * 5)
    a_turtle.pendown()
    a_turtle.setheading(90)
    a_turtle.forward(size * 5)

    # root
    a_turtle.penup()
    a_turtle.goto(x, y - size * 5)
    a_turtle.pendown()
    a_turtle.color("brown")
    a_turtle.setheading(90)
    a_turtle.circle(size, 180)
    
    draw_petals(a_turtle, x, y, size, 6)
    draw_petals(a_turtle, x, y, size / 2, 6)


def draw_petals(a_turtle: Turtle, x: float, y: float, size: float, num_petals: int) -> None:
    """This function draws petals recursively."""
    if num_petals > 0:
        a_turtle.penup()
        a_turtle.goto(x, y)
        a_turtle.pendown()
        a_turtle.color("red")
        a_turtle.circle(size)
        a_turtle.left(60)
        draw_petals(a_turtle, x, y, size, num_petals - 1)  # Call itself recursively


def draw_mountain(a_turtle: Turtle, width: float, height: float, level: int, distance: float) -> None:
    """This function draws mountains."""
    if level > 0:
        a_turtle.penup()
        a_turtle.goto(-width / 2 + distance, -height / 2)
        a_turtle.pendown()
        a_turtle.color("gray")
        a_turtle.begin_fill()
        a_turtle.goto(-width / 4 + distance, 0)
        a_turtle.goto(0 + distance, -height / 2)
        a_turtle.goto(width / 4 + distance, 0)
        a_turtle.goto(width / 2 + distance, -height / 2)
        a_turtle.goto(-width / 2 + distance, -height / 2)
        a_turtle.end_fill()

        # second mountain
        draw_mountain(a_turtle, width * 0.75, height * 0.75, level - 1, distance + width / 2)


def draw_fly(a_turtle: Turtle, width: float, height: float, num_flies: int) -> None:
    """Draw flies randomly in the blue sky."""
    a_turtle.penup()
    a_turtle.color("black")
    for _ in range(num_flies):
        x = random.randint(-round(width / 2), round(width / 2))
        y = random.randint(round(height / 10), round(height / 8))
        a_turtle.goto(x, y)
        a_turtle.dot(3)


if __name__ == "__main__":
    main()