"""Pong, classic arcade game.

Exercises
 
공을 두개로 늘림. 

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.
"""

from random import choice, random
from turtle import *

from freegames import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])
def value2():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
ball2 = vector(0, 0)
aim = vector(value(), value()) #방향
aim2 = vector(value2(), value2()) #방향
state = {1: 0, 2: 0} #1,과2의 위치는 0에서 시작한다.


def move(player, change): #플레이어의 위치 이동
    """Move player position by change."""
    state[player] += change


def rectangle(x, y, width, height): #직사각형 그리기
    """Draw rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def draw(): #게임 전체 그리기 , 탁구공 움직이기
    """Draw game and move pong ball."""
    clear()
    rectangle(-200, state[1], 10, 50) #1 플레이어의 탁구채 그리기
    rectangle(190, state[2], 10, 50) #2 플레이어의 탁구채 그리기

    ball.move(aim) #공의 방향, 움직임 
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10) #공
    update()

    ball2.move(aim2) #공의 방향, 움직임 
    x2 = ball2.x
    y2 = ball2.y

    up()
    goto(x2, y2)
    dot(10) #공
    update()

    if y < -200 or y > 200: #y좌표가 200이상이거나 -200 이하일때
        aim.y = -aim.y #공이 반대 방향으로 튕김

    if x < -185: #공이 -185보다 작은 위치 값에 들어가 바에 닿았을 때 
        low = state[1]
        high = state[1] + 50

        if low <= y <= high: #y값이 바에 닿았다면
            aim.x = -aim.x #방향을 거꾸로 튕겨 나아간다.
        else:
            return

    if x > 185: #공이 185보다 높은 값에 들어가게 되었을 때
        low = state[2]
        high = state[2] + 50

        if low <= y <= high: #y값이 바에 닿았다면
            aim.x = -aim.x #방향을 거꾸로 튕겨 나아간다.
        else:
            return



    if y2 < -200 or y2 > 200: #y좌표가 200이상이거나 -200 이하일때
        aim2.y = -aim2.y #공이 반대 방향으로 튕김

    if x2 < -185: #공이 -185보다 작은 위치 값에 들어가 바에 닿았을 때 
        low = state[1]
        high = state[1] + 50

        if low <= y2 <= high: #y값이 바에 닿았다면
            aim2.x = -aim2.x #방향을 거꾸로 튕겨 나아간다.
        else:
            return

    if x2 > 185: #공이 185보다 높은 값에 들어가게 되었을 때
        low = state[2]
        high = state[2] + 50
 
        if low <= y2 <= high: #y값이 바에 닿았다면
            aim2.x = -aim2.x #방향을 거꾸로 튕겨 나아간다.
        else:
            return        

    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w') # 1플레이어 의 움직임을 20만큼 이동시킨다.
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i') # 2플레이어 의 움직임을 20만큼 이동시킨다.
onkey(lambda: move(2, -20), 'k')
draw()
done()
