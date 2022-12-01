"""Tiles, number swapping game.

Exercises

1. Track a score by the number of tile moves.
2. Permit diagonal squares as neighbors.
3. Respond to arrow keys instead of mouse clicks.
4. Make the grid bigger.

"""

from random import *                 # random 모듈에서 모든 메소드 가져옴.
from turtle import *                 # turtle 모듈에서 모든 메소드 가져옴.
from freegames import floor, vector  # freegames 모듈에서 floor, vector 가져옴.

# 초기값
tiles = None
neighbors = None
buttons = None
interval = None
size = None
fontsize = None

def reset():
    global tiles, neighbors, buttons, interval, size, fontsize
    tiles = {}  # 처음: 빈 딕셔너리. tiles{ mark : spot }로 채울 것이다.
    neighbors = []
    buttons = []
    interval = 0 # 칸 간의 간격
    size = 0     # 1칸의 크기
    fontsize = 0 # 폰트의 크기. 16개일때 60, 25개일 때 48, 100개일 때 25


def load():                             # 타일과 꼭짓점 격자를 세팅한다. 처음엔 1~16순서대로 세팅. 나중엔 숫자들이 섞인다.
    "Load tiles and scramble."
    global interval
    count = 1                           # 처음 꼭지점의 개수는 1
                                        # 4x4격자를 만들기 위해, 16개를 만든다.
    for y in range(-200, 200, interval):     # y좌표 -200~100을 100 간격으로. -200 -100 0 100. 총 4회 반복
        for x in range(-200, 200, interval): # x좌표 -200~100을 100 간격으로. 총 4회 반복
            mark = vector(x, y)         # mark = vector(-200~100,-200), = vector(-200~100,-100).. 16회
            tiles[mark] = count         # 16개 각 점에 1~16라고 번호를 매긴다.
            count += 1

    tiles[mark] = None                  # 마지막 count값이었던 16에 해당하는 점을 None으로 세팅. 빈 점으로 만든다.

    for count in range(1000):           # 17부터 999까지 983회 반복.
        neighbor = choice(neighbors)    # random모듈의 choice. neighbors의 4개 요소 중에 1개 랜덤 선택.
        spot = mark + neighbor          # spot = vector(-200+100,0) or vector(-100+0,100) or ...

        if spot in tiles:               # spot: 바꿔줄 위치의 대상. 빈 번호 <-> spot번호 바꿔준다.
            number = tiles[spot]        # number = tiles[vector(-100,0)].. = 1~15 중 하나. 1회차: number = 15라면,
            tiles[spot] = None          # 15가 있던 자리는 None = 빈 번호로 만들고,
            tiles[mark] = number        # 15를 빈 번호였던 자리에 새로이 부여하며,
            mark = spot                 # mark는 빈 번호가 된 자리를 새로이 가리키게 된다.

def square(mark, number):   # 게임판을 그려주는 기능. = 하얀 사각형, 검정 테두리와 숫자를 그려주는 기능.
    "Draw white square with black outline and number."
    global size, fontsize
    up()                  # 펜을 도화지에서 뗀다. 네모가 이동 시, 자취 선을 그리지 않는다.
    goto(mark.x, mark.y)  # (mark.x, mark.y)좌표로 이동한다.
    down()                # 이동이 끝났으면, 펜을 다시 도화지에 댄다.

    color('black', 'white') # 펜의 색(테두리)은 검정, 채우기 색(내부)은 흰색
    begin_fill()            # begin_fill과 end_fill 사이엔 색을 채울 도형을 그려준다.
    for count in range(4):  # 네모를 그린다.
        forward(size)
        left(90)
    end_fill()              # begin_fill과 end_fill 사이엔 색을 채울 도형을 그려준다.

    if number is None:      # number가 빈 자리라면
        return              # 바로 리턴
    elif number < 10:       # number = 1~9라면
        forward(20)         # 왼쪽에 공백으로 조금 띄어준다.

    write(number, font=('Arial', fontsize, 'normal')) # 숫자를 그려준다. (폰트 종류, 폰트 크기, 폰트 상태:굵게/기울임 등)

def tap(x, y):                     # 타일과 빈 공간을 자리교체한다. (x,y) = 마우스 클릭한 좌표
    "Swap tile and empty square."
    global interval, neighbors
    x = floor(x, interval)              # x,y를 -200,-100,0,100,200처럼 100단위로 잘라서 다시 저장한다.
    y = floor(y, interval)              # x,y가 -200~ -101 = -200, -100~ -1 = -100, 0~99 = 0, 100~199 = 100, 200 = 200
    mark = vector(x, y)            # 마우스 누른 곳의 바닥값이 mark = vector(-100,100)인 경우일 때, (원위치 기준 점14)
                                   # (마우스 누른 곳은 숫자가 존재하는 곳 = 빈 자리가 아님)
    for neighbor in neighbors:     # neighbor = vector(100,0) 인 경우,
        spot = mark + neighbor     # spot = (0,100)                 (원위치 기준 점15, 빈 자리)

        if spot in tiles and tiles[spot] is None:  # tiles[spot]이 빈 자리일 때,
            number = tiles[mark]                   # number = 14
            tiles[spot] = number                   # 14를 빈 자리에 넣어줌.
            square(spot, number)                   # 14를 나타내게 네모와 숫자를 다시 그려줌.
            tiles[mark] = None                     # 14였던 자리는 빈 자리로.
            square(mark, None)                     # 빈 자리이며, 공백칸이 되도록 네모만 다시 그려줌.

def draw():                        # 타일들을 전부 그려준다.
    "Draw all tiles."
    for mark in tiles:             # 타일들에 있는 마크에 대하여,
        square(mark, tiles[mark])  # 46줄의 게임판 그리는 메소드 호출
    update()            # 사용하지 않는 메소드

# 초기화면 난이도 선택 버튼
class Button:
    def __init__(self, startx, starty, sizex, sizey, color, string):
        self.startx = startx
        self.starty = starty
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.string = string

    def draw(self): # 사각형 버튼 그리기
        temp = pencolor()
        up()
        goto(self.startx-24, self.starty-6)
        color(self.color)
        down()
        begin_fill()

        for count in range(2) : # 사각형
            forward(100)
            left(90)
            forward(50)
            left(90)

        end_fill()
        up()
        color(temp)
        goto(self.startx+self.sizex/2-2.6*len(self.string), self.starty+self.sizey/2-3.5)
        write(self.string, font=('Courier', 15, 'bold'))

    def getString(self):
        return self.string

    def isButton(self, x, y):
        return self.startx <= x and x <= self.startx + self.sizex and self.starty <= y and y <= self.starty+self.sizey

def changeButton(x, y):
    global buttons
    global interval, size, fontsize, neighbors
    for button in buttons :
        if button.isButton(x, y):
            if button.getString() == "4x4": # 4x4 단계 버튼
                print("4x4")
                interval = 100
                size = 99
                fontsize = 60


            if button.getString() == "5x5": # 5x5 단계 버튼
                print("5x5")
                interval = 80
                size = 79
                fontsize = 48

            if button.getString() == "10x10": # 10x10 단계 버튼
                print("10x10")
                interval = 40
                size = 39
                fontsize = 25

            neighbors = [  # 처음: (0,0)기준, 십자 모양으로 이웃한 꼭짓점 4개
                vector(interval, 0),
                vector(-interval, 0),
                vector(0, interval),
                vector(0, -interval),
            ]

            clear()
            load()  # load()메소드 호출.
            draw()  # draw()메소드 호출.
            onscreenclick(tap)  # 화면을 마우스 클릭할 때, tap메소드를 실행한다. 클릭한 좌표를 tap함수에 매개변수로 넘긴다.
            update()

def diffInit(): # 버튼 나타내기
    buttons.append(Button(-25, 100, 32, 25, 'lightblue', '4x4'))
    buttons.append(Button(-25, 0, 32, 25, 'lightblue', '5x5'))
    buttons.append(Button(-25, -100, 20, 25, 'lightblue', '10x10'))
    onscreenclick(changeButton)
    for button in buttons:
        button.draw()
    update()

def setScreen(screen):
    Turtle._screen = screen

def setPen(pen):
    Turtle._pen = pen

def setTurtle(t):
    Turtle = t

def main():
    hideturtle()            # 거북이를 숨긴다.
    tracer(False)           # 그림 그리는 자취를 보이게 하지 않고, 완성본을 띄워줌. (True)로 하면 그림 그리는 과정이 진행됨.
    reset()
    diffInit()

if __name__ == "__main__":
    setup(420, 420, 370, 0) # 화면의 크기/좌표를 지정한다. (가로길이, 세로길이, 시작 x좌표, 시작 y좌표)
    main()
    done()