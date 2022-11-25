"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""

from random import *
from turtle import *

from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):        # -200에서 200까지의 값을 래핑해주는 함수
    """Wrap value around -200 and 200."""
    return value  # TODO


def draw():
    """Move ant and draw screen."""
    ant.move(aim)    #ant의 좌표에 aim의 좌표를 move를 사용해 넘겨준후
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y) # wrap을 이용해 깊은 복사를 진행합니다.

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)    #aim을 move와 rotate를 사용해 랜덤하게 좌표를 변환

    clear() #clear로 거북이의 상태를 초기화
    goto(ant.x, ant.y)  #goto로 ant의 좌표로 이동
    dot(4) #점 4개를 만듬

    ontimer(draw, 100)  #100밀리초에 한번씩 draw를 호출 해줍니다.


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
done()

# 개미의 움직임을 조작하는 것이 아니라 
# 관찰만 하는것이라 사용자의 흥미를 얻기 힘들것이라 예상되어 개미를 
# 관찰하는 것 말고도 사용자가 개미의 움직임을 조작할 수 있게 하거나 
# 개미의 속도를 조절하는 등의 다양한 게임 진행 방법을 추가하여 
# 사용자의 지속적인 흥미를 유발하도록 개선할 예정입니다.
