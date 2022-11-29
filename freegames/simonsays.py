"""Simon Says

Exercises

1. Speed up tile flash rate.
2. Add more tiles.
"""

from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector

pattern = [] #패턴 리스트
guesses = [] #정답 리스트
tiles = {  #타일
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}


def grid():  #타일을 그리는 함수
    """Draw grid of tiles."""
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()


def flash(tile):  #플래쉬 부분
    """Flash tile in grid."""
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow) #빛내고
    update()
    sleep(0.5)  #0.5초간 정지 후 다음 시행
    square(tile.x, tile.y, 200, dark) #어두워짐
    update()
    sleep(0.5)


def grow():  #패턴과 플래쉬 타일 확장하는 함수
    """Grow pattern and flash tiles."""
    tile = choice(list(tiles))  #choice 함수로 핸덤 선택 -> 타일
    pattern.append(tile) #랜덤으로 생성한 타일변수 패턴에 추가

    for tile in pattern: #패턴이 타일에 있다면 플래쉬 실행
        flash(tile)

    print('Pattern length:', len(pattern)) #플래쉬가 끝난 후에 패턴 수 길이 출력
    guesses.clear()  #정답 칸을 비워줌


def tap(x, y):
    """Respond to screen tap."""
    onscreenclick(None) #마우스 이벤트 함수 : 특정지정 클릭시 좌표를 기억하고 이벤트를 발생
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]: #틀렸을 시에
        exit()  #나가짐.

    guesses.append(tile) #정답 리스트에 타일을 저장
    flash(tile) #해당 타일 플래쉬

    if len(guesses) == len(pattern):  #정답과 패턴 리스트의 길이가 같다면
        grow()  #타일을 확장

    onscreenclick(tap)


def start(x, y): #게임을 시작하는 부분
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()  #타일을 그려주고
onscreenclick(start)  #클릭시에 스타트
done()
