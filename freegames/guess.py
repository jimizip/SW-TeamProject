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

# print(value)
print("I'm thinking of a number between", start, 'and', end)

guess = None #guess값을 비워둠

while guess != value: #guess값이 value값과 다를때
    text = input('Guess the number: ') #text를 입력받아
    guess = int(text) #guess 변수에 정수로 저장

    if guess < value: #guess 값이 value 보다 작을때
        print('Higher.') #higher 출력
    elif guess > value: #guess 값이 value 보다 클때
        print('Lower.') #lower 출력

print('Congratulations! You guessed the right answer:', value)

#문제를 한번 못맞추면 시간이 오래걸릴 것 같습니다.
#사용자가 조금 더 즐겁게 이 게임을 즐길 수 있도록 숫자의 범위를 늘리거나, 숫자에 대한 추가 힌트를 제공할 예정입니다.
