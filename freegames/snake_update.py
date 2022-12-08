"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange #random의 randrange 모듈
from turtle import * #turtle 모듈

from freegames import square, vector #freegames의 square 모듈

#게임 시작시에 food, snake, aim의 위치를 vector를 통하여 지정한다

food = vector(0, 0)
obstacle_1 = vector(25, 15)
obstacle_2 = vector(25, 15)
obstacle_3 = vector(25, 15)
obstacle_4 = vector(25, 15)
obstacle_5 = vector(25, 15)
snake = [vector(10, 0)]
aim = vector(0, -10)
writer = Turtle(visible=False)
state = {'score': 0}
writer.write(state['score'])

#snake의 방향을 바꾸는 함수
def change(x, y): 
    """Change snake direction."""
    aim.x = x #x의 방향을 바꾼다
    aim.y = y #x의 방향을 바꾼다

#헤드가 경계 내에 있으면 True를 반환하는 함수
def inside(head): 
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190 #head의 x와y가 -200과 190 사이에 있을때 값을 반환

#뱀을 한 부분 앞으로 이동
def move(): 
    """Move snake forward one segment."""
    head = snake[-1].copy() #snake가 -1만큼 이동했을때 복사하여 head에 저장
    head.move(aim) #head를 aim만큼 이동

    if not inside(head) or head in snake: #inside나 head에 snake가 없을때
        square(head.x, head.y, 9, 'red') # head의 x,y값을 빨간색으로 바꾼다
        update() #위의 과정을 업데이트한다.
        return #반환

    elif (head == obstacle_1) or (head == obstacle_2) or (head == obstacle_3) or (head == obstacle_4) or (head == obstacle_5):
        square(head.x, head.y, 9, 'red') #snake의 끝에 head를 추가한다.
        update() #업데이트한다
        return # 반환한다

    snake.append(head) #snake의 head에 추가한다

    if head == food: #snake의 head와 food가 같을때
        print('Snake:', len(snake)) #snake의 길이를 출력
        food.x = randrange(-15, 15) * 10 #food의 x를 randrange를 통해 -15부터 15까지 증분하여 10을 곱한다
        food.y = randrange(-15, 15) * 10 ##food의 y를 randrange를 통해 -15부터 15까지 증분하여 10을 곱한다
        obstacle_1.x = randrange(-10, 10) * 10 #장애물 추가
        obstacle_1.y = randrange(-10, 10) * 10
        obstacle_2.x = randrange(-10, 10) * 10
        obstacle_2.y = randrange(-10, 10) * 10
        obstacle_3.x = randrange(-10, 10) * 10
        obstacle_3.y = randrange(-10, 10) * 10
        obstacle_4.x = randrange(-10, 10) * 10
        obstacle_4.y = randrange(-10, 10) * 10
        obstacle_5.x = randrange(-10, 10) * 10
        obstacle_5.y = randrange(-10, 10) * 10
    else:
        snake.pop(0) #snake의 head가 food와 다를때 snake의 첫 번째 데이터를 제거

    clear() #snake의 요소를 제거

    for body in snake: 
        square(body.x, body.y, 9, 'black') #snake가 body만큼 반복된다면 x와y를 검정색으로 바꾼다

    square(food.x, food.y, 9, 'green') #snake가 body만 x와y를 초록색으로 바꾼다

    square(obstacle_1.x, obstacle_1.y, 9, 'gray') #갱신한다
    square(obstacle_2.x, obstacle_2.y, 9, 'gray')
    square(obstacle_3.x, obstacle_3.y, 9, 'gray')
    square(obstacle_4.x, obstacle_4.y, 9, 'gray')
    square(obstacle_5.x, obstacle_5.y, 9, 'gray')
    
    update() #위의 과정을 업데이트 한다
    ontimer(move, 100) #0.1초뒤에 움직인다.


setup(420, 420, 370, 0) #그래픽 창의 크기를 지정한다
hideturtle() #거북이를 보이지 않게 한다
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') #오른쪽으로 (10.0)만큼 이동한다
onkey(lambda: change(-10, 0), 'Left') #왼쪽으로 (-10.0)만큼 이동한다
onkey(lambda: change(0, 10), 'Up') #위쪽으로 (0.10)만큼 이동한다
onkey(lambda: change(0, -10), 'Down') #아래쪽으로 (0.-10)만큼 이동한다
move() #move함수 실행
done() #게임 종료

#문제점 : 게임이 조금 단조롭게 느껴질 수도 있다
#snake의 빠르기를 키우거나 추가기능을 추가해 조금 더 흥미롭게 개선할 예정이다

#개선사항 : 장애물을 넣어서 게임의 난이도를 높여서 더욱 흥미롭게 게임을 개선하였다
