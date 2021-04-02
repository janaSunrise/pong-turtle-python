def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)
