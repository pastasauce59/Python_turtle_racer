from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle1 = Turtle(shape='turtle')
turtle1.penup()
turtle1.goto(x=-230, y=0)


screen.exitonclick()