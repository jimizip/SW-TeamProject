"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.
"""

from random import randint #사용모듈 random의 radint

start = 1 #start를 1로 초기화
end = 100 #end를 100으로 초기화
value = randint(start, end) #1부터100까지의 랜덤한 정수를 value에 저장

#print(value) #선택된 랜덤한 정수
print("I'm thinking of a number between", start, 'and', end)

guess = None #guess값을 비워둠
count = 0
number = 5

while number != count and guess != value: #guess값이 value값과 다를때
    text = input('Guess the number: ') #text를 입력받아
    guess = int(text) #guess 변수에 정수로 저장

    if guess < value: #guess 값이 value 보다 작을때
        print('Higher.') #higher 출력
        count += 1
        print("You used", count, "chance")

    elif guess > value: #guess 값이 value 보다 클때
        print('Lower.') #lower 출력
        count += 1
        print("You used", count,"chance")
    
    else :
        print("Congratulations! You guessed the right answer:", value)

if number == count :
    print("Sorry.. You loose")

#문제점 : 문제를 한번 못맞추면 시간이 오래 걸릴 것 같습니다.
#사용자가 조금 더 즐겁게 이 게임을 이용할 수 있도록 시간제한을 추가하거나 숫자에 대한 추가 힌트를 제공할 예정입니다.

#개선사항 : 한번 못맞추면 시간이 오래 걸릴 것 같다는 문제점을 개선하였습니다
#문제를 한번 맞추지 못하면 끊임 없이 도전할 수 있기에 시간이 오래걸리고 게임이 루즈해질 것 같아
#사용자가 조금 더 긴장감 있게 게임을 사용할 수 있도록 도전할 수 있는 기회를 5번으로 제한하고
#몇번째 도전인지 표기하였습니다.
