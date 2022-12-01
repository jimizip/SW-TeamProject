"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

from random import *
from turtle import *

from freegames import vector

bird = vector(0, 0) # 새의 위치 벡터 변수
balls = [] # 날아오는 장애물 배열 변수

# 새의 위치를 위쪽 방향으로 30 옮기는 함수
def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30) # 새의 위치를 30 아래로 이동하는 벡터변수
    bird.move(up) # 새의 위치를 up변수에 저장한 만큼 move()함수를 호출해 이동해줍니다.

# 점이 화면 안에 위치하는 지 여부를 확인하는 함수
def inside(point):
    """Return True if point on screen."""
    # 점이 화면 안에 있을 경우 (-200과 200 사이) True를 반환합니다.
    return -200 < point.x < 200 and -200 < point.y < 200

# 새의 생존여부에 따라 색깔을 변경하는 함수
def draw(alive):
    """Draw screen objects."""
    clear() # clear() 함수를 사용합니다.

    goto(bird.x, bird.y) # 현재 bird의 위치를 goto() 모듈 함수를 사용하여 위치를 이동합니다.

    if alive: # 새가 살아있을 경우 현재 위치에 반경 10의 초록색 원을 그립니다.
        dot(10, 'green')
    else: # 살아 있지 않을 경우 현재 위치에 반경 10의 빨간색 원을 그립니다.
        dot(10, 'red')

    # balls 배열에 있는 원소 차례대로 balls들의 위치로 이동한 후 현재 위치에 반경 20의 검정색 원을  그립니다.
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update() # update() 모듈 함수로 현재 상태를 저장합니다.

# 물체들의 위치를 변경하는 함수
def move():
    """Update object positions."""
    bird.y -= 5 # 새의 y좌표를 5씩 감소합니다.

    for ball in balls: # balls 배열에 있는 원소 차례대로 balls의 x좌표를 3씩 감소합니다.
        ball.x -= 3

    # 장애물의 y좌표를 10 안의 임의의수 중 랜덤으로 설정한 값이 0이면 장애물의 위치를 화면 오른쪽에서 높이를 랜덤으로 지정하고 장애물을 balls 리스트에 추가합니다.
    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    # 장애물이 화면 밖을 벗어나면 balls의 0번째를 pop합니다.
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    # 새가 화면 맨 위와 맨 아래에 닿을 경우 새가 죽어, draw함수에 False 값을 넣습니다.
    if not inside(bird):
        draw(False)
        return
        
    # 그렇지 않을 경우 새가 살아있는 것이므로 draw함수에 True 값을 넣습니다.
    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)

# setup(420, 420, 370, 0)메소드를 사용하여 화면크기와 좌표를 지정합니다.
setup(420, 420, 370, 0)
# Hideturtle() 모듈 함수를 사용하여 거북이를 숨깁니다.
hideturtle()
# up() 함수를 사용합니다.
up()
# Tracer() 모듈 함수를 사용하여 거북이가 움직일 때 남는 자취를 감춥니다.
tracer(False)
onscreenclick(tap)
# move() 함수를 사용해 위치를 옮기고 게임을 종료합니다.
move()
done()

# 문제점: 투사 체의 속도가 느리다고 생각하여 투사 체의 속도를 빠르게 하여 난이도를 높이는 것을 생각하고 있습니다.
