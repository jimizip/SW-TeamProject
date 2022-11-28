"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""
#요거

from random import *
from turtle import *

from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)
antSpeed = 6
antColor = 'black'
antShape = '.'
antSize = 10

def wrap(value):        # -200에서 200까지의 값을 래핑해주는 함수
    """Wrap value around -200 and 200."""
    return value  # TODO


def draw():
    """Move ant and draw screen."""
    global antSpeed
    global antColor
    global antShape
    global antSize

    ant.move(aim)    #ant의 좌표에 aim의 좌표를 move를 사용해 넘겨준후
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y) # wrap을 이용해 깊은 복사를 진행합니다.

    move = float(random() - 0.5)
    while( move >= 420): 
        move = random() - 0.5
    aim.move(move)

    move2 = float(random() * 10 - 5)
    while( move >= 420 ): 
        move2 = random() * 10 - 5
    aim.rotate(move2)    #aim을 move와 rotate를 사용해 랜덤하게 좌표를 변환

    clear() #clear로 거북이의 상태를 초기화
    speed(antSpeed)
    goto(ant.x, ant.y)  #goto로 ant의 좌표로 이동
    color(antColor) #점 4개를 만듬
    write(antShape,font=('Arial', antSize, 'normal'))
    ontimer(draw, 100)  #100밀리초에 한번씩 draw를 호출 해줍니다.

def tap(x,y):
    ant.move(aim)    #ant의 좌표에 aim의 좌표를 move를 사용해 넘겨준후
    ant.x = wrap(x)
    ant.y = wrap(y) # wrap을 이용해 깊은 복사를 진행합니다.


antSpeed = int(input("0~10사이의 속도를 입력하세요: "))
antShape = input("개미의 모양을 입력하세요: ")
antColor = input("개미의 색깔을 입력하세요: ")
antSize = input("개미의 크기 입력하세요: ")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
onscreenclick(tap)
done()

# 개미의 움직임을 조작하는 것이 아니라 
# 관찰만 하는것이라 사용자의 흥미를 얻기 힘들것이라 예상되어 개미를 
# 관찰하는 것 말고도 사용자가 개미의 움직임을 조작할 수 있게 하거나 
# 개미의 속도를 조절하는 등의 다양한 게임 진행 방법을 추가하여 
# 사용자의 지속적인 흥미를 유발하도록 개선할 예정입니다.


# 개미의 움직임을 관찰하고 지켜보는데 의의가 있는 게임이라 
# 개미를 움직이게 만들면 게임의 본질을 해친다고 생각하여 
# 개미를 지켜보되 화면을 클릭시 그곳으로 개미가 이동가능하게 만들었고
# 개미의 크기, 색깔, 모양등을 정할 수 있게 다양성을 높였습니다.
