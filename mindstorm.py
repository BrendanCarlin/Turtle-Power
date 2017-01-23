import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create turtle class for square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(4)
    draw_square(brad)
    for i in range(1,37):
        brad.right(10)
        draw_square(brad)
    #create turtle class for circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.circle(100)

    window.exitonclick()

draw_art()
