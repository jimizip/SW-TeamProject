"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()    #처음에는 up으로 그리지 않고
    goto(start.x, start.y)  #파라미터로 받은 start로 이동
    down()  #down으로 펜으로 내려서 
    goto(end.x, end.y)  #start부터 end까지 직선을 그립니다. 


def square(start, end):
    """Draw square from start to end."""
    up()    #up으로 펜을 들어
    goto(start.x, start.y)  #start 지점까지 turtle을 이동시키고
    down()  #펜을 내린후에
    begin_fill()

    for count in range(4): # 4번 이동하여 정사각형의 각 변을 그립니다.
        forward(end.x - start.x)    #end.x에서 start.x를 뺀값만큼 앞으로
        left(90)   #  90만큼 왼쪽으로 이동

    end_fill()


def circle(start, end): # 파라미터로 받은 start와 end를 기준으로 원을 그립니다.
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):  # 파라미터로 받은 start와 end를 기준으로 직사각형을 그립니다.
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):   # 파라미터로 받은 start와 end를 기준으로 삼각형을 그립니다.
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']  # state의 start값을 tap함수에서 정의한 start에 넣습니다.

    if start is None:   #  만약 start가 비어있으면
        state['start'] = vector(x, y)  #  state 딕셔너리의 start에 x,y를 좌표로 가지는 vector를 넣고
    else:   # 만약 start가 채워져있으면 
        shape = state['shape']  # state 딕셔너리의 shape 밸류값을 shape 변수에 넣고
        end = vector(x, y)  # end에는 x,y를 가지는 벡터를 넣습니다.
        shape(start, end)   # shape에 start와 end값을 넣고 
        state['start'] = None  #  start를 비웁니다.


def store(key, value): #  받은 킷값과 value 값을 state에 key값과 value값으로 추가합니다.
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')  # 각각 K,W,G,B,R이 눌리면 해당되는 색으로 바꿉니다.
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')    # 각각 l,s,c,r,t가 눌리면 도형이 바뀝니다.
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

# 현재 구현하지 않고 pass로 둔 기능이 많습니다. pass로 되어 있는 부분을 구현하여 
# 사각형, 타원 등을 그릴수 잇게 추가할 예정입니다.
