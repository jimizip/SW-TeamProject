"""Maze, move from one side to another.

Excercises

1. Keep score by counting taps.
2. Make the maze harder.
3. Generate the same maze twice.
"""

from random import random
from turtle import *

from freegames import line


def draw():
    """Draw maze."""
    color('black')  #검정색에 너비는 5로 미로의 선을 설정합니다. 
    width(5)

    for x in range(-200, 200, 40):  #이중 반복문으로 –200,-200부터 200,200까지 y부터 40씩 올려가며 반복문을 진행
        for y in range(-200, 200, 40):
            if random() > 0.5:  #증가시키는 x와 y값을 random 함수가 0.5이상이라면 종점에,
                line(x, y, x + 40, y + 40)
            else:   #0.5 이하라면 시점의 y좌표와 종점의 x 좌표를 40 증가시키면서 선을 그립니다.
                line(x, y + 40, x + 40, y)

    update()


def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:    #만약 x나 y가 198보다 크다면 펜을 들어 그림을 그리지 못하게 하고
        up()
    else:   #아니라면 펜을 내려서 그릴 수 있게 해줍니다.
        down()

    width(2)
    color('red')    #빨간색 너비 2의 선
    goto(x, y)  #주어진 x와 y를 사용하여 turtle을 움직여 선을 그립니다.
    dot(4)  #마지막에 up을 실행한 상황이라면 해당되는 좌표에 점을 찍습니다.


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()


# 출발점이 확실하지 않고 선이 미로를 통과하는 경우가 발생합니다. 
# 게임을 진행하면서 출발점을 정해 두고 표시하여 
# 사용자가 더욱 편하게 게임을 진행할 수 있고 벽을 넘어갈 경우 경고 
# 문구를 띄우거나 조작을 무시하여 게임을 원할히 진행되도록 개선할 예정입니다.
