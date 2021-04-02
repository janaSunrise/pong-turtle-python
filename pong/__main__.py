import turtle
from functools import partial

from .utils import paddle_up, paddle_down

# Initialize the scores
score_a = 0
score_b = 0

# Windows
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
win.listen()

win.onkeypress(partial(paddle_up, paddle_a), "w")
win.onkeypress(partial(paddle_down, paddle_a), "s")

win.onkeypress(partial(paddle_up, paddle_b), "Up")
win.onkeypress(partial(paddle_down, paddle_b), "Down")

# -- Main loop --
if __name__ == '__main__':
    while True:
        win.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1

            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1

            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
