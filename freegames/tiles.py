"""Tiles, number swapping game.

Exercises

1. Track a score by the number of tile moves.
2. Permit diagonal squares as neighbors.
3. Respond to arrow keys instead of mouse clicks.
4. Make the grid bigger.
"""

from random import *
from turtle import *

from freegames import floor, vector

tiles = {}  #16개의 타일들을 저장할 딕셔너리
neighbors = [   #이동 할 때의 크기를 저장해 놓은 튜플
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]


def load():
    """Load tiles and scramble."""
    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100): #이중 반복문에서는 –200부터 200까지 100스텝씩 증가시키며 
            mark = vector(x, y)
            tiles[mark] = count
            count += 1
            #총 16개의 좌표에 해당되는 count를 1부터 1씩 올려주며 할당합니다.

    tiles[mark] = None  #tiles의 mart를 none으로 바꾸어 마지막 16번째 칸을 빈칸으로 만듭니다.

    for count in range(1000):   #마지막 반복문은 숫자를 섞기 위한 반복문  count가 1000번이 될 때까지 반복
        neighbor = choice(neighbors)    #nighbor에 상하좌우중 하나를 random 모듈의 choice 함수를 이용하여 하나 저장
        spot = mark + neighbor  #spot에 mark 좌표와 nighbor 좌표를 합친 값을 넣습니다. 

        if spot in tiles:   #이 spot이 빈칸이 아니라 숫자라면 빈칸과 숫자를 바꿉니다.
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot


def square(mark, number):   #mark와 number를 파라미터로 받습니다.
    """Draw white square with black outline and number."""
    up()    #up으로 펜을 올려서 그리지 못하게 하고
    goto(mark.x, mark.y)    # turtle을 mark의 x와 y로 이동한뒤
    down()  #펜을 다시 내립니다. 

    color('black', 'white') #색깔을 외각선은 검정 내부는 흰색으로 설정
    begin_fill()    #begin_fill을 호출하여 모양을 그린다는 것을 알려준후
    for count in range(4):
        forward(99) #앞으로 99 이동하고 
        left(90)    #왼쪽으로 90 4번이동합니다.
    end_fill()  #end_fill로 모양그리기가 끝났음을 알려줍니다.

    if number is None:  #만약 빈칸이면 종료하고
        return
    elif number < 10:   #해당되는 숫자가 10 미만이면 앞으로 20 이동합니다.
        forward(20)

    write(number, font=('Arial', 60, 'normal')) # 해당되는 숫자를 적습니다.


def tap(x, y):
    """Swap tile and empty square."""
    x = floor(x, 100)   #floor를 실행시켜 100을 스텝으로 내림을 진행
    y = floor(y, 100)
    #예를들어 0~100 사이의 수는 0이 되고 –100~0 사이의 수는 –100이 됩니다.
    mark = vector(x, y) #x와 y를 내림하여 변환한 후 mark에 저장합니다. 

    for neighbor in neighbors:  
        spot = mark + neighbor  #반복문에서는 상하좌우 4 방향으로 이동하며

        if spot in tiles and tiles[spot] is None:   # 만약 해당하는 방향이 빈칸이라면 mark에 저장되어 있는 수와 spot을 교환합니다. 
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)


def draw():
    """Draw all tiles."""
    for mark in tiles:  #저장되어 있는 tile들을 순회
        square(mark, tiles[mark])   #square에 저장되어 있는 좌표를 파라미터로 전달해주며 호출하여 각각의 타일을 그려 총 16개의 타일을 그립니다.
    update()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()

# 게임 자체는 문제가 없지만 추가 콘텐츠가 부족합니다. 초기 화면에서 난이도를 선택하여 그에 맞는 난이도 
# 조절기능을 추가하여 사용자의 흥미를 이끌어 낼 수 있도록 개선할 예정입니다.
