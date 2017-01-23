import turtle

def draw_flower(some_turtle):
    for i in range(1,4):
        some_turtle.forward(150)
        some_turtle.left(120)

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(8)

    for i in range(1,37):
        draw_flower(brad)
        brad.left(10)

    for i in range(1,37):
        draw_square(brad)
        brad.left(10)

    for i in range(1,37):
        brad.circle(50)
        brad.left(10)

    brad.right(90)
    brad.forward(250)
    
    window.exitonclick()
    
draw_art()
