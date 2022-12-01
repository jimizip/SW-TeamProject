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

ball = vector(-200, -200) #공과 타겟을 움직이는 변수
speed = vector(0, 0) #공의 속도
targets = [] #타겟

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
    """Move ball and targets."""
    if randrange(40) == 0: #만약 randrange함수로 40까지의 정수를 생성했을때 그 수가 0이라면
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


setup(420, 420, 370, 0) #그래픽 창의 크기를 지정한다
hideturtle() #거북이를 보이지 않게 한다
up() #위로이동하는 함수 호출
tracer(False) #전체 자취를 보이지 않게 한다
onscreenclick(tap) #tap함수에서 화면 내 특정지점을 클릭하면 좌표를 기억하고 실행한다(마우스 이벤트 함수)
move() #move함수 실행
done() #게임 종료
