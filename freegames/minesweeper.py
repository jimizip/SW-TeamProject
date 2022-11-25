"""Minesweeper

Exercises

1. What does the `seed(0)` function call do?
2. Change the number of bombs on the grid.
3. Change the size of the grid.
"""

from random import randrange, seed
from turtle import *

from freegames import floor, square

seed(0)
bombs = {}  #폭탄의 좌표
shown = {}  #해당되는 좌표가 클릭됬는지 안됬는지를 담는 변수
counts = {} #주변의 폭탄수를 담은 좌표


def initialize():
    """Initialize `bombs`, `counts`, and `shown` grids."""
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombs[x, y] = False
            shown[x, y] = False
            counts[x, y] = -1
            # 이중 반복문을 사용하여 –250 부터 
            # 250까지 50씩 증가시키며 지뢰와 숫자, 개수를 초기화 시킵니다.

    for count in range(8):
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        bombs[x, y] = True
        #  random 모듈의 randrange 함수를 사용하여 –200부터 200까지의 
        #  수중 50의 무작위 배수를 얻어 8개 폭탄의 좌표를 선정합니다.

    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            #  4중 반복문을 사용하여 x,y를 –200부터 200까지의 수중 
            #  50의 배수로 설정
            total = 0
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombs[x + i, y + j]
                    # I,j에는 –50에서 50까지의 수를 넣어 해당되는 좌표의 주변의 폭탄수를 세어서 
                    # counts에 담아줍니다.
            counts[x, y] = total


def stamp(x, y, text):
    """Display `text` at coordinates `x` and `y`."""
    square(x, y, 50, 'white')   #각각의 좌표에 사각형을 그려주고
    color('black')
    write(text, font=('Arial', 50, 'normal'))   #검정색으로 해당되는 text를 arial 폰트로 그려줍니다.


def draw():
    """Draw the initial board grid."""
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            stamp(x, y, '?')
            #-200부터 200까지 각각의 좌표에 ?를 그립니다.


def end():
    """Draw the bombs as X's on the grid."""
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombs[x, y]:
                stamp(x, y, 'X')
                #-200 부터 200까지의 각각의 좌표가 폭탄의 좌표인 경우 X를 그립니다.


def tap(x, y):
    """Respond to screen click at `x` and `y` coordinates."""
    x = floor(x, 50)
    y = floor(y, 50)

    if bombs[x, y]: #좌표를 파라미터로 받으면 주어진 좌표가 폭탄 좌표라면 종료
        end()
        return

    pairs = [(x, y)]    #폭탄의 좌표가 아니라면 pairs에 해당 좌표를 넣고

    while pairs:    #pairs에 좌표가 들어있는 동안 반복문을 작동시킵니다.
        x, y = pairs.pop()  #처음에 pairs에서 좌표를 빼서 x,y에 넣고
        stamp(x, y, counts[x, y])   #해당하는 좌표에 해당되는 숫자를 넣
        shown[x, y] = True  #hown을 true로 바꿔서 이미 선택한 좌표라고 표시해줍니다,

        if counts[x, y] == 0:   #counts가 0이라면 인접한 좌표들중 shown이 true가 아닌 좌표를 pair에 넣습니다.
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    pair = x + i, y + j
                    if not shown[pair]:
                        pairs.append(pair)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
onscreenclick(tap)
done()

#  지뢰 표시 기능이 없고 난이도가 단조롭습니다. 
#  보편적인 지뢰 찾기 게임처럼 깃발을 두어 
#  자신이 생각하기에 지뢰가 있다고 생각되는 곳에 
#  표시할 수 있게 만들과 난이도 설정을 가능하게 하도록 개선할 예정입니다.
