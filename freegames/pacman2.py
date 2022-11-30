"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
from turtle import *

from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False) 
writer = Turtle(visible=False)
aim = vector(5,0)  #목표 방향 설정 vector(양수/음수,0)-우측/좌측, vector(0,양수/음수)-위/아래
pacman = vector(-40, -80) #플레이어의 시작 위치
ghosts = [   #고스트들의 시작 위치
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]
# fmt: off
tiles = [        #맵의 생김새
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):  #좌표에 따라 배열의 인덱스 값을 반환해주는 함수
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):    #유효성을 판별해주는 함수 
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world(): #맵을 만드는 함수 world 
    bgcolor('black')#배경을 검정.
    path.color('blue')                                                  #

    for index in range(len(tiles)):     #tiles 배열에 들어간 수만큼 반복
        tile = tiles[index]        #  tiles의 값을 tile에 저장 0 or 1

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')     #점수를 얻을 수 있는 팩맨의 먹이에 해당 dot(size,*color)


def move():
    """Move pacman and all ghosts."""
    writer.undo()    #마지막 writer 의 동작실행 취소
    writer.write(state['score'])    #화면에 글자 쓰기'score' 

    clear()       #지나온 잔상을 없애줌

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:      #tiles의 인덱스 값이 1일 경우
        tiles[index] = 2       #tiles의 인덱스 값을 2로 바꿔서 지나온 길로 만듦
        state['score'] += 1     #tiles의 인덱스가 1인 경우에는 score값에 +1을 해줌
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')                                               #플레이어 팩맨의 점의 속성(크기,색상)

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [     #옵션은 오른쪽,왼쪽,위,아래가 있음 !!!!!!!!!!수정 부분!!!!!!!!!!!!!!!!!
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            plan = choice(options) #랜덤으로 옵션중에 하나를 선택.
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')                                                                  #장애물의 속성(크기,색상)

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)                                                  #ontimer(함수,시간) 일정 시간 뒤에 실행


def change(x, y):                                                                       #팩맨의 목표방향 바꾸기
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False) #전체 터틀의 자취를 보지 않게 함. 해당 코드를 없애면 맵 생성 과정을 볼 수 있음.
writer.goto(160, 160) #점수판의 위치
writer.color('white') #점수판의 색깔
writer.write(state['score']) 
listen() #사용자의 입출력을 받는 소켓프로그래밍 listen함수
onkey(lambda: change(5, 0), 'Right')#onkey함수로 아이콘을 이동시킴 onkey(fun,key)
onkey(lambda: change(-5, 0), 'Left')#lamda = 사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()#맵 생성
move() #동작 실행
done()
