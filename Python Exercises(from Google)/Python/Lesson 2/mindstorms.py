#mindstorms.py

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    
    henry = turtle.Turtle()
    # you can customize your turtle
    # but I'm not going to do that
    henry.shape("arrow")
    henry.color("black")
    henry.speed(10)
    for j in range(1,37):
        for i in range(1,5):
            henry.forward(100)
            henry.right(90)
        henry.right(10)
        
    window.exitonclick()



draw_square()

# a for loop
# for i in range(1,5):
