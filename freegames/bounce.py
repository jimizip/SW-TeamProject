"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""

from random import *
from turtle import *

from freegames import vector

# 실행 시 (-5, -3) 또는 (3, 5) 사이의 값을 무작위로 생성
def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)             # 튕길 시작점을 0,0으로 지정
aim = vector(value(), value())  # (-5, -3) 또는 (3, 5) 사이의 값 중에서 무작위로 정해진 좌표값을 목적지로 지정


def draw():
    """Move ball and draw game."""
    # ball의 좌표를 aim의 좌표로 이동
    ball.move(aim)

    # ball의 좌표값 x, y를 x와 y 변수에 각각 저장
    x = ball.x
    y = ball.y

    # 만약 x의 좌표값이 -200 미만이거나 200 초과이면(실행창 테두리까지 닿은 상태이면) 
    # x 좌표값에 -를 붙여 반대좌표로 표시
    if x < -200 or x > 200:
        aim.x = -aim.x
    # 만약 y의 좌표값이 -200 미만이거나 200 초과이면(실행창 테두리까지 닿은 상태이면) 
    # y 좌표값에 -를 붙여 반대좌표로 표시
    if y < -200 or y > 200:
        aim.y = -aim.y

    clear()
    # x, y 좌표로 이동
    goto(x, y)

    dot(10)

    # draw 함수를 50초 후에 호출
    ontimer(draw, 50)

# 게임의 캔버스, 키 및 속성을 설정
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
done()