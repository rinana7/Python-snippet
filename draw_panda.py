import turtle

pen = turtle.Turtle()
pen.screen.title("turtle demo")
pen.screen.bgcolor("pink")


def circle(col, rad):
    # Set the fill
    pen.fillcolor(col)

    # Start filling the color
    pen.begin_fill()

    # Draw a circle
    pen.circle(rad)

    # Ending the filling of the color
    pen.end_fill()


def move_position(pos_x, pos_y):
    pen.up()
    pen.setpos(pos_x, pos_y)
    pen.down()


def draw_panda():
    # Draw first ear
    move_position(-45, 125)
    circle("black", 20)

    # Draw second ear
    move_position(45, 125)
    circle("black", 20)

    # Draw face
    move_position(0, 35)
    circle("white", 60)

    # Draw first eye
    move_position(-18, 75)
    circle("black", 13)

    # Draw second eye
    move_position(18, 75)
    circle("black", 13)

    # Draw nose
    move_position(0, 55)
    circle("black", 8)

    # Draw mouth
    move_position(0, 55)
    pen.right(90)
    pen.circle(5, 180)

    move_position(0, 55)
    pen.left(360)
    pen.circle(5, -180)
    pen.hideturtle()

    pen.hideturtle()
    pen.screen.mainloop()


if __name__ == "__main__":
    draw_panda()
