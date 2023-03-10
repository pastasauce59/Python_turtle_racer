from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# turtle1 = Turtle(shape='turtle')
# turtle1.penup()
# turtle1.goto(x=-230, y=0)

yaxis = 0
while yaxis != 6 * 30:
    for color in colors:
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=yaxis)
        yaxis += 30

screen.exitonclick()