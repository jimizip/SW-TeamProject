"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import * #turtle 모듈

from freegames import line #freegame의 line모듈

#변수 선언
p = None
spot = None
count = None
state = None
players = None

#초기화 함수
def initialize():
    global p, spot, count, state, players
    p = [[1,2,3], [4,5,6], [7,8,9]]
    spot = [] #아무 칸도 안눌린 상태
    count = 0
    state = {'player': 0} #현재 상태는 0이다
    players = [drawx, drawo] #플레이 순서는 X가 먼저, O가 그 다음이다

#tic tac toe 그리드 함수
def grid(): 
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67) #가로줄 2개와 세로줄 2개 생성

#x직선을 그리는 함수
def drawx(x, y):
    "Draw X player."
    color("red")
    global spot #전역변수 선언
    global count
    global p
    count = 0
    for i in spot:
        if i == (x,y):
            count += 1

    if count == 0:
        line(x, y, x + 133, y + 133)
        line(x, y + 133, x + 133, y) #매개변수로 전달받은 위치에 X를 그린다.
        spot += [(x,y)]

        if x == -200.0 :
            if y == 66.0 :
                p[0][0] = "x"
            elif y == -67.0 :
                p[1][0] = "x"
            else : p[2][0] = "x"
        elif x == -67.0 :
            if y == 66.0 :
                p[0][1] = "x"
            elif y == -67.0 :
                p[1][1] = "x"
            else : p[2][1] = "x"
        else :
            if y == 66.0 :
                p[0][2]= 'x'
            elif y == -67.0 :
                p[1][2] = 'x'
            else : p[2][2] = 'x'
    print_win()

#o직선을 그리는 함수
def drawo(x, y):
    "Draw O player."
    up()
    goto(x + 67, y + 5)
    down()
    color("blue")
    global spot #전역변수 선언
    global count
    global p
    count = 0
    for i in spot:
        if i == (x,y):
            count += 1

    if count == 0:
        circle(62) #매개변수로 전달받은 위치에 O를 그린다.
        spot +=[(x, y)]
        if x == -200.0 :
            if y == 66.0 :
                p[0][0] = 'o'
            elif y == -67.0 :
                p[1][0] = 'o'
            else : p[2][0] = 'o'
        elif x == -67.0 :
            if y == 66.0 :
                p[0][1] = 'o'
            elif y == -67.0 :
                p[1][1] = 'o'
            else : p[2][1] = 'o'
        else :
            if y == 66.0 :
                p[0][2]= 'o'
            elif y == -67.0 :
                p[1][2] = 'o'
            else : p[2][2] = 'o'
    print_win()

#값을 사각형 크기 133의 그리드로 반올림하는 함수
def floor(value): 
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200 
#파라메터로 받은 value값을 계산해서 반환해준다

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

def print_win():
    global p
    if str(p[0][0]) == str(p[1][1]) == str(p[2][2]) or str(p[2][0]) == str(p[1][1]) == str(p[0][2]):
        goto(0,0)
        if (p[0][0] == 'x')or(str(p[2][0]) == 'x') :
            color("red")
            write('player1 Win', move = False, align='center', font=('Courier', 30, 'normal'))
        else :
            color("blue")
            write('player2 Win', move = False, align='center', font=('Courier', 30, 'normal'))
    for i in range(3):
        if str(p[0][i]) == str(p[1][i]) == str(p[2][i]):
            goto(0,0)
            if str(p[0][i]) == str(p[1][i]) == str(p[2][i]) == 'x' :
                color("red")
                write('player1 Win', move = False, align='center', font=('Courier', 30, 'normal'))
            else :
                color("blue")
                write('player2 Win', move = False, align='center', font=('Courier', 30, 'normal'))
        if str(p[i][0]) == str(p[i][1]) == str(p[i][2]):
            goto(0,0)
            if str(p[i][0]) == str(p[i][1]) == str(p[i][2]) == 'x' :
                color("red")
                write('player1 Win', move = False, align='center', font=('Courier', 30, 'normal'))
            else :
                color("blue")
                write('player2 Win', move = False, align='center', font=('Courier', 30, 'normal'))

def setScreen(screen):
    Turtle._screen = screen

def setPen(pen):
    Turtle._pen = pen

def setTurtle(t):
    Turtle = t

def main():
    initialize()
    hideturtle() #거북이를 화면에서 숨긴다
    tracer(False) #전체 자취를 보이지 않게 한다
    grid() #그리드 함수 호출
    update() #업데이트를 한다
    onscreenclick(tap) #tap함수에서 화면 내 특정지점을 클릭하면 좌표를 기억하고 실행한다(마우스 이벤트 함수)

if __name__ == "__main__":
    setup(420, 420, 370, 0)
    main()
    done() #게임을 종료한다


#문제점 : 게임 자체는 문제가 없지만 게임이 단조로워 약간 지루하게 느껴질 수도 있습니다.
#시간제한이나 난이도 조절기능을 통해 조금 더 재미있게 개선할 예정입니다.
