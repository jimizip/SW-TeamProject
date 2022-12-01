"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import * #turtle 모듈

from freegames import line #freegame의 line모듈

#tic tac toe 그리드 함수
def grid(): 
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67) #가로줄 2개와 세로줄 2개 생성

#x직선을 그리는 함수
def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y) #선 2개를 이용하여 X모양을 그리는 함수

#o직선을 그리는 함수
def drawo(x, y):
    """Draw O player."""
    up() #위로 올린다
    goto(x + 67, y + 5) #x좌표를 67만큼 이동, y좌표를 5만큼 이동한다
    down() #아래로 내린다
    circle(62) #반지름이 62인 원을 그린다

#값을 사각형 크기 133의 그리드로 반올림하는 함수
def floor(value): 
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200 
#파라메터로 받은 value값을 계산해서 반환해준다

state = {'player': 0} #player를 0상태로 만든다
players = [drawx, drawo] # 플레이어를 위치시킨다

#정사각형에 X 또는 O를 그리는 함수
def tap(x, y): 
    """Draw X or O in tapped square."""
    x = floor(x) #x값을 floor함수에 넣는다
    y = floor(y) #y값을 floor함수에 넣는다
    player = state['player'] #player에 state값 0을 저장
    draw = players[player] #draw에 players = [drawx,drawy]를 저장한다.
    draw(x, y) #x와 y를 그린다
    update() #업데이트를 한다
    state['player'] = not player #player의 상태는 player가 아니다


setup(420, 420, 370, 0)
hideturtle() #거북이를 화면에서 숨긴다
tracer(False) #전체 자취를 보이지 않게 한다
grid() #그리드 함수 호출
update() #업데이트를 한다
onscreenclick(tap) #tap함수에서 화면 내 특정지점을 클릭하면 좌표를 기억하고 실행한다(마우스 이벤트 함수)
done() #게임을 종료한다
