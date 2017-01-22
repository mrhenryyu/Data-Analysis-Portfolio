#draw flower

import turtle

#instead of one single function, we will just start writing the program

def init_turtle():

    window = turtle.Screen()
    window.bgcolor("white")

    henry= turtle.Turtle()
    henry.shape("arrow")
    henry.color("black")
    henry.speed(5)

    window.exitonclick()

init_turtle()

