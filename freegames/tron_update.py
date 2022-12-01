"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?
"""

# Turtle 라이브러리를 사용하여 게임 화면을 만들고 
# Freegames 라이브러리를 사용하여 이 프로젝트의 코드에서 나중에 사용되는 벡터 및 
# 사각형과 같은 일부 게임 작업을 처리
from turtle import *

from freegames import square, vector

# 각 플레이어의 좌표, 방향 및 각 플레이어의 body 값을 저장할 변수 생성
p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

# 플레이어의 머리가 게임 화면 안에 있는지 확인
# (리턴값을 받아 확인 후 머리가 더 이상 게임 화면 안에 없으면 게임 종료)
def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200

# 게임 화면과 간단한 그래픽을 그리고 설정
def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    # p1의 머리가 화면 밖으로 나가거나 p1의 머리가 p2 body에 닿으면 p2 승리
    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    # p2의 머리가 화면 밖으로 나가거나 p2의 머리가 p1 body에 닿으면 p1 승리
    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    # 게임을 진행하는 동안 p1, p2의 머리를 각 body 영역에 추가
    p1body.add(p1head)
    p2body.add(p2head)

    # 게임을 진행하는 동안 플레이어를 발전시킴(크기가 점점 커짐)
    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    #!!!!!!! 코드 수정 부분 속도 변경 -> 너무 빨라서 게임 진행이 어려움!!!!!!
    ontimer(draw, 100)

# 게임 화면 설정
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# 각 플레이어가 이동하는 방식을 제어하는 ​​데 사용되는 람다 함수 생성
#!!!!!!! 코드 수정 부분 속도 변경 -> 방향키 추가
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(180), 'w')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(90), 'i')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()