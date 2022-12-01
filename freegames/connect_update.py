import turtle
import os 
 
# 게임판 [0]*8 배열
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
 
# 말 상태를 배열로 player를 yellow로 시작
def state(board, row, col, piece):
    board[col][row] = piece
 
# 승자를 판별하기 위해 모든 가능성에서 위치를 확인
def winEx(board, piece):

    for c in range(3): # 마지막 3열에서 4열을 얻지 못하는 경우
        for r in range(5):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
 
    # 수직선 
    for c in range(6): 
        for r in range(2): # 마지막 3행에서 4열을 얻은 경우
            if board[r][c] == piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
 
    # 기울기가 양인 대각선 (오른쪽 위로 향하는 선)
    for c in range(3): # 대각선 일부에서는 4행만 가능
        for r in range(2):
            if board[r][c] == piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
 
    # 기울기가 음인 경우 (오른쪽 아래로 향하는 선)
    for c in range(6): 
        for r in range(3, 5): # 이런 경우 대각선 일부에서는 4행만 가능
            if board[r][c] == piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
 
             
win = turtle.Screen()
win.title('connect_update')
win.setup(500, 600)
win.bgcolor('light blue') # 배경색
win.tracer(False)
win.listen() #방향키로 움직임 (left, right, space)
 
piece_list = [] # 게임판 안에 들어온 말들을 저장


class gameTile(turtle.Turtle): 
    def __init__(self):
        super().__init__(shape='square') # 초기화
        self.shapesize(5, 5) # 열과 행 
        self.up() 
        self.color('light blue')

class Piece(turtle.Turtle):
    def __init__(self, color, state):
        super().__init__(shape='circle')
        self.shapesize(4.5, 4.5)
        self.up()
        self.c = color # 색깔 저장 변수
        self.color(self.c)
        self.state = state
         
 
    def move_right(self):
        # 말의 위치가 게임 판 안에 있는 경우에만 이동
        if self.xcor()<200 and self.state == 'move':
            self.goto(self.xcor()+100, self.ycor())
 
 
    def move_left(self):
        if self.xcor()>-200 and self.state =='move':
            self.goto(self.xcor()-100, self.ycor())
 
 
    def drop(self):
        global game_over
        global message
        global board
        global piece_list # 말이 게임판 안에 들어오고 나서의 좌표 저장
         
        # 말을 게임판에 들여놓은 뒤 새로운 말 생성
        dropped_piece = turtle.Turtle()
        dropped_piece.shape('circle')
        dropped_piece.shapesize(4.5, 4.5)
        dropped_piece.color(self.c)
        dropped_piece.up()
 
        # 마지막 요소까지 놓은 위치 확인
        for i in y_list[::-1]:
            #print(i)
             
            if (self.xcor(),i) not in piece_list:
                ypos = i
                break
            else:
                # 열이 가득찬 경우
                if (self.xcor(), 150) in piece_list:
                    ypos = 1000  # 화면을 숨긴다.
                    
        os.system('afplay drop.wav&')              
        dropped_piece.goto(self.xcor(), ypos)
        xcor = dropped_piece.xcor()
        ycor = dropped_piece.ycor()
         
        # 게임판 안에 놓인 경우에만 배열에 추가
        if ycor != 1000:
            piece_list.append((xcor,ycor))
                         
        # 플레이어의 색을 마음대로 변경 가능
        if self.c == 'yellow':
            piece = 1
 
            self.c = 'red'
            self.color(self.c)
        else:
            self.c = 'yellow'
            self.color(self.c)
            piece = 2
 
        # 말을 놓는다
        state(board, x_list.index(xcor), y_list.index(ycor), piece)
 
        # 승리한 경우 메시지를 출력
        if winEx(board,1):
            win.update()
            game_over = True
            message = 'Winner: Yellow'
        if winEx(board,2):
            win.update()
            game_over = True
            message = 'Winner: Red'
 
 
x_list = [-200, -100, -0, 100, 200]
y_list = [150, 50, -50, -150, -250]
 
# 게임판을 셋팅한다
for i in x_list:
    for j in y_list:
        tile = gameTile()
        tile.goto(i,j)
 
        piece = Piece('white', 'still')
        piece.goto(i,j)
 
# 왼쪽 키, 오른쪽 키로만 움직일 수 있도록 말 생성
piece1 = Piece('yellow', 'move')
piece1.goto(0, 250)
 
win.onkey(piece1.move_right, 'Right')
win.onkey(piece1.move_left, 'Left')
win.onkey(piece1.drop, 'Return') # 엔터 키로 놓기
 
game_over = False
message = ''
 
# 메인 게임 루프
while not game_over:
    if len(piece_list) >= 25:
        game_over = True
    win.update()
 
 
# 게임이 끝난 경우 승자 메시지 출력
print("GAME OVER")
pen = turtle.Turtle()
pen.up()
pen.hideturtle() # 거북이 숨기기
if message == 'Winner: Red':
    pen.color('red')
else:
    pen.color('yellow')
  
pen.goto(0, 220)
pen.write(f'GAME OVER, {message}', align='center', font=('Courier', 20, 'bold'))
