"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?
"""

from turtle import *

from freegames import line

# turns 변수를 선언하여 다음 순서의 말을 저장합니다.
turns = {'red': 'yellow', 'yellow': 'red'}
# state 변수를 선언하여 시작 player를 yellow, 게임 판의 열을 8로 저장합니다.
state = {'player': 'yellow', 'rows': [0] * 8}

# 게임 판을 그리는 함수 grid()
def grid():
    """Draw Connect Four grid."""
    # 배경색을 하늘색으로 지정합니다. 
    bgcolor('light blue')

    # 게임 판의 세로선 그립니다.
    for x in range(-150, 200, 50): 
        line(x, -200, x, 200)

    # 게임 판의 가로선 그리면서 위로 이동(up()), 세로선과 가로선을 그릴 때 해당 좌표로 이동하고  
    # (goto(x,y)), 현재 위치에 반경 40오 하얀색 빈칸을 그려 넣습니다.(dot(40, 'white'))
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')
    # update() 메소드로 dict안의 데이터를 갱신합니다.   
    update()

# 차례에 맞게 말을 판에 그리는 tap 함수()
def tap(x, y):
    """Draw red or yellow circle in tapped row."""
    # 현재 플레이어와 열을 state에서 불러옵니다. 
    player = state['player']
    # 마우스 클릭한 곳의 좌표로 열을 계산하고 말이 들어갈 열을 저장합니다. 
    rows = state['rows']

    # 말을 넣을 가로좌표, 세로좌표를 계산합니다. 
    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    # up() 함수 모듈을 이용하여 위로 이동, goto(x, y) 함수 모듈을 이용하여 앞서 계산한 말을 넣을 
    # 좌표로 이동하고, dot(40, palyer) 함수 모듈을 이용하여 현재 좌표에 반경 40의 원을 그려 넣습니다. 
    # update() 메소드를 이용하여 데이터를 갱신합니다. 
    up()
    goto(x, y)
    dot(40, player)
    update()

    # 말을 넣은 경우 말이 한칸 채워졌으므로 rows[row] 변수로 count + 1을 한다. 
    # 마지막으로 player을 불러옵니다.
    rows[row] = count + 1
    state['player'] = turns[player]

# setup(420, 420, 370, 0) 메소드로 화면크기와 좌표를 지정합니다.
setup(420, 420, 370, 0)
# Hideturtle() 함수 모듈을 이용해 거북이를 숨깁니다.
hideturtle()
# Tracer(False) 함수 모듈을 이용해 거북이가 움직일 때 남는 자취를 감춥니다.
tracer(False)
grid()
# 화면에 클릭한 좌표를 tap 함수에 매개변수로 넘깁니다.
onscreenclick(tap)
done()

# 문제점: 말이 4개 연속될 경우 게임이 끝나지 않는데 
# 4개 연속될 경우 끝나도록 개선해볼 것입니다.
