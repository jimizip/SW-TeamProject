import math
from turtle import *
from freegames import vector

# start에서 end까지 선을 그린다
def line(start, end):
    "Draw line from start to end."
    up() # 거북이가 이동시에 그림을 그리지 않는다
    goto(start.x, start.y) # 거북이를 start.x, start.y로 이동
    down() # 거북이가 이동시에 그림을 그린다
    goto(end.x, end.y) # 거북이를 end.x, end.y로 이동

# start에서 end크기의 단색 사각형을 그린다
def square(start, end):
    "Draw square from start to end."
    up() # 거북이가 이동시에 그림을 그리지 않는다
    goto(start.x, start.y) # 거북이를 start.x, start.y로 이동
    down() # 거북이가 이동시에 그림을 그린다
    begin_fill() # 거북이가 그릴 도형을 채운다

    for count in range(4): # 4번
        forward(end.x - start.x) # 거북이를 end.x-start.x 만큼 이동
        left(90) # 거북이를 왼쪽으로 90도 회전

    end_fill() # 거북이가 그릴 도형을 채우지 않는다

#### 개선 사항 : 원 그리기
def circle(start, end):
    "Draw circle from start to end."
    up()
    begin_fill()

    for i in range(361):
        t = i * (math.pi / 180)
        x = (end.x - start.x)/2 * math.sin(t + start.x) + start.x + (end.x - start.x)/2
        y = (end.y - start.y)/2 * math.cos(t + start.x) + start.y + (end.y - start.y)/2
        goto(x, y)
        down()
        
    end_fill()
    up()
####

#### 개선 사항 : 사각형 그리기
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2) :
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()
    up()
####

#### 개선 사항 : 삼각형 그리기
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x + (end.x-start.x)/2, start.y)
    down()
    begin_fill()
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x + (end.x-start.x)/2, start.y)
    end_fill()
    up()
####

# 시작점을 저장하거나 그림을 그리게 한다
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start'] # start에 state['start']의 값을 저장

    if start is None: # start가 None이면
        state['start'] = vector(x, y) # state['start']에 x, y를 좌표로 갖는 벡터 객체 생성
    else: # start가 None이 아니면
        shape = state['shape'] # shape에 state['shape']의 값을 저장
        end = vector(x, y) # end에 x, y를 좌표로 갖는 벡터 객체 생성
        shape(start, end) # start에서 end까지 그림을 그린다
        state['start'] = None # shape['start']의 값에 None을 저장
    update()

# state[key]에 value를 저장
def store(key, value):
    "Store value in state at key."
    state[key] = value # start[key]에 value를 저장

def setScreen(screen):
    Turtle._screen = screen

def setPen(pen):
    Turtle._pen = pen

def setTurtle(t):
    Turtle = t


def main():
    tracer(False)
    hideturtle()
    onscreenclick(tap) # 클릭했을시 그림을 그리도록 설정
    listen() # 키 입력모드를 실행시킨다
    onkey(undo, 'u') # u를 눌렀을때 undo()를 호출한다
    onkey(lambda: color('black'), 'K') # K를 눌렀을때 색을 검정으로 바꾼다
    onkey(lambda: color('white'), 'W') # W를 눌렀을때 색을 하양으로 바꾼다
    onkey(lambda: color('green'), 'G') # G를 눌렀을때 색을 초록으로 바꾼다
    onkey(lambda: color('blue'), 'B') # B를 눌렀을때 색을 파랑으로 바꾼다
    onkey(lambda: color('red'), 'R') # R를 눌렀을때 색을 빨강으로 바꾼다
    onkey(lambda: store('shape', line), 'l') # l을 눌렀을때 store('shape', line)을 호출한다
    onkey(lambda: store('shape', square), 's') # s을 눌렀을때 store('shape', square)을 호출한다
    onkey(lambda: store('shape', circle), 'c') # c을 눌렀을때 store('shape', circle)을 호출한다
    onkey(lambda: store('shape', rectangle), 'r') # r을 눌렀을때 store('shape', rectangle)을 호출한다
    onkey(lambda: store('shape', triangle), 't') # t을 눌렀을때 store('shape', triangle)을 호출한다


state = {'start': None, 'shape': line} # 시작 벡터와 모양을 갖고 있는 변수
if __name__ == "__main__":
    setup(420,420,300,0)
    main()
    done()