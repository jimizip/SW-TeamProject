"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange #random의 randrange 모듈
from turtle import * #turtle 모듈

from freegames import vector #freegames의 vector 모듈
from tkinter import *

ball = None
speed = None
targets = None
choice = None
buttons = None

def reset():
    global ball, speed, targets, choice, buttons
    # ball: 빨간 공, target: 파란 구름 타겟
    ball = vector(-200, -200) # 좌표평면 맨 왼쪽밑 구석에서 시작, (0,0)은 중앙,
    speed = vector(0, 0) # 빨간공의 속도를 0으로 초기화.
    targets = [] # 타겟들은 빈 리스트에서 시작, 타겟이 1개씩 추가될 예정.
    choice = 0
    buttons = []

#화면의 탭 응답 함수
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball): #ball의 좌표가 inside 함수내에 있지 않을때
        ball.x = -199 #ball의 x좌표
        ball.y = -199 #ball의 y좌표
        speed.x = (x + 200) / 25 #ball의 x좌표 탭 응답시간
        speed.y = (y + 200) / 25 #ball의 y좌표 탭 응답시간

#화면 내에 xy가 있으면 True를 반환하는 함수
def inside(xy): #화면내에 xy가 있을때
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200
#x와 y가 -200과 200사이의 좌표에 있을때 xy값을 반환

#공과 목표물을 그리는 함수
def draw(): 
    """Draw ball and targets."""
    clear() #화면을 지우고 거북이는 그 자리에 그대로 둔다

    for target in targets: #targets를 target만큼 반복한다
        goto(target.x, target.y) #target의 x와y 좌표를 이동시키고
        dot(20, 'blue') #현재 위치에 지름이 20인 파란색 점을 찍는다

    if inside(ball): #ball이 inside함수 안에 있다면
        goto(ball.x, ball.y) #ball의 x와y 좌표를 이동시키고
        dot(6, 'red') #현재 위치에 지름이 6인 색 빨간색점을 찍는다

    update() #업데이트한다

#공과 목표물을 움직이는 함수
def move(): 
    global choice
    """Move ball and targets."""
    targetNum = randrange(choice)  # 타겟 출현 빈도: (40). (100)이면 적게 나옴. (3)이면 많이 나옴.

    if targetNum == 0: #만약 randrange함수로 40까지의 정수를 생성했을때 그 수가 0이라면
        y = randrange(-150, 150) #randrange함수를 통해 -150~150중 임의의 정수를 생성하여 y값 좌표에 저장
        target = vector(200, y) #위에 생성한 정수를 vector의 y값에 넣어 target에 저장
        targets.append(target) #targets에 입력받은 target을 추가한다

    for target in targets: #dupe를 target만큼 반복할때
        target.x -= 0.5 #target의 좌표는 0.5씩 줄어든다

    if inside(ball): #만약에 ball의 좌표가 inside함수 안에 위치해 있을때
        speed.y -= 0.35
        ball.move(speed) #y의 좌표의 시간은 0.35씩 줄며 이동한다

    dupe = targets.copy() #dupe에 targets의 값을 복사해서 저장한다
    targets.clear() #화면을 지우고 targets는 그 자리에 그대로 둔다

    for target in dupe: #dupe를 target만큼 반복할때
        if abs(target - ball) > 13: #abs(target에서 ball을 뺀 값)가 13보다 크면
            targets.append(target) #targets에 target을 추가한다

    draw() #draw함수를 호출하여 그린다

    for target in targets: #targets를 target만큼 반복할 때 
        if not inside(target): #target의 값이 inside함수 좌표안에 있지 않으면
            return #값을 반환한다

    ontimer(move, 50) #ontimer함수를 통해 0.05초후에 move함수를 실행한다

#버튼 클래스
class Button:
    def __init__(self, startx, starty, sizex, sizey, name, string): #초기화
        self.startx = startx
        self.starty = starty
        self.sizex = sizex
        self.sizey = sizey
        self.name = name
        self.string = string

    def draw(self):
        temp = pencolor()
        up()
        goto(self.startx, self.starty)
        color(self.name)
        down()
        begin_fill()

        for count in range(2) :
            forward(self.sizex)
            left(90)
            forward(self.sizey)
            left(90)

        end_fill()
        up()
        color(temp)
        goto(self.startx+self.sizex/2-2.6*len(self.string), self.starty+self.sizey/2-3.5)
        write(self.string)

    def getString(self):
        return self.string

    def isButton(self, x, y):
        return self.startx <= x and x <= self.startx + self.sizex and self.starty <= y and y <= self.starty+self.sizey

def chkButton(x, y):
    global buttons
    global choice
    for button in buttons :
        if button.isButton(x, y):
            if button.getString() == "easy":
                print("easy")
                choice = 40 #타겟 출현 빈도: (40). (100)이면 적게 나옴. (3)이면 많이 나옴.

            if button.getString() == "normal":
                print("normal")
                choice = 20 #타겟 출현 빈도: (20). easy모드보다 2배 더 많이 나옴.

            if button.getString() == "hard":
                print("hard")
                choice = 10 #타겟 출현 빈도: (10). easy모드보다 4배 더 많이 나옴.

            clear()
            onscreenclick(tap) #화면을 클릭할 때, tap메소드를 실행한다. 클릭한 좌표를 tap함수에 매개변수로 넘긴다.
            move() #48줄의 move()메소드 호출
            update()


def diffInit():
    buttons.append(Button(-155, 0, 50, 30, 'gray', 'easy'))
    buttons.append(Button(-25, 0, 50, 30, 'gray', 'normal'))
    buttons.append(Button(105, 0, 50, 30, 'gray', 'hard'))
    onscreenclick(chkButton)
    for button in buttons:
        button.draw()
    update()
####

def setScreen(screen):
    Turtle._screen = screen

def setPen(pen):
    Turtle._pen = pen

def setTurtle(t):
    Turtle = t

def main():
    hideturtle() #거북이를 숨기고 주석화하면 공에 검은거북이가 붙어서 출현한다
    up() #펜을 도화지에서 떼고 공과 타겟이 이동 시, 자취 선을 그리지 않는다
    tracer(False) #그리기 과정을 생략한다.

    reset()
    diffInit()

if __name__ == "__main__":
    setup(420, 420, 370, 0) #화면의 크기/좌표를 지정한다(가로길이, 세로길이, 시작 x좌표, 시작 y좌표)
    main()
    done() #코드 종료 후 게임창이 바로 닫히지 않게 한다. 주석화하면 게임창이 열리자마자 바로 닫힌다

#문제점 :게임 자체에는 특별한 문제가 없어 보이지만 혼자 게임하는 것에 대해 조금 흥미가 떨어질 수 있을 것 같아 레벨 조절 기능을 넣을 예정입니다
#개선사항 : 난이도에 따라 상중하를 선택하여 게임을 즐길 수 있도록 수정했다
