"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.
"""
#요거

from turtle import *

state = {'turn': 0}
fidgetNum = 3
fidgetColor = [0, 0, 0, 0, 0, 0, 0]


def spinner():
    """Draw fidget spinner."""
    clear()  # turtle을 초기화
    global fidgetNum
    moveAngle = 360 / fidgetNum
    angle = state['turn'] / 10  # turn의 값을 10으로 나눈 수만큼 angle에 할당

    right(angle)  # angle의 각도 만큼 이동
    forward(100)  # 100px 만큼 이동시켜 피젯의 뼈대를 선을 그리고
    dot(120, fidgetColor[0])  # 거북이의 좌표에 빨간색 120크기의 점을 만든 후
    back(100)  # back으로 다시 뒤로 옮깁니다.
    # 이런방식으로 파란색, 초록생의 원을 만들고 turtle 스크린을 update를 사용해 갱신합니다.
    for i in range(1, fidgetNum): # 입력받은 피젯만큼을 그린다
        right(moveAngle)
        forward(100)
        dot(120, fidgetColor[i])
        back(100)

    # right(moveAngle)
    # forward(100)
    # dot(120, 'blue')
    # back(100)

    right(moveAngle)
    update()


def animate():  # 피젯스피너를 돌리는 함수
    """Animate fidget spinner."""
    if state['turn'] > 0:  # turn의 값이 0보다 크면 1을 감소시키고
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)  # spinner를 호출 한 뒤 20밀리초마다 animate를 실행합니다.


def flick():
    """Flick fidget spinner."""
    state['turn'] += 10  # 변수 state의 turn을 10 증가시킵니다.


fidgetNum = int(input("3 ~ 6 사이의 개수를 입력하세요: "))  # 개수를 입력받는다
for i in range(fidgetNum):  # 각 피젯의 색깔을 입력받는다
    color = input("색깔 입력하세요: ")
    fidgetColor[i] = color

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()

# 피젯의 형태가 정해져 있고 ui가 단조롭습니다.
#  피젯을 다른 모양으로도 만들어서
# 사용자가 선택하여 게임을 더욱 다채롭게 개선할 예정입니다.

# 피젯을 기존에는 3개 디폴트로 설정되어 있었는데
# 사용자에게 2~6 사이의 피젯을 입력받고
# 그에따른 피젯의 색깔을 설정 가능하게 변환하였습니다
