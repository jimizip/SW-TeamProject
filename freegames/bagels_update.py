"""Bagels, a number puzzle game.

Exercises:

1. Can you guess the number?
2. How much harder is 6 digits? Do you need more guesses?
3. What's the maximum number of digits we could support?

Adapted from code in https://inventwithpython.com/chapter11.html
"""

# sample() : 랜덤하게 여러 개의 원소를 선택
# shuffle() : 원소의 순서를 랜덤하게 바꿈
from random import sample, shuffle

# 변수의 초기값 설정
# !!!!!!코드 수정부분 숫자야구 3개로 진행하는것을 4개로 변경
digits = 4          # 유저가 맞추어야 하는 숫자의 크기 (0000 : 네자리 수)
guesses = 10

print('I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  pico         One digit is correct but in the wrong position.')
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number.
# 0~9까지의 숫자중에 digits(3)개를 추출
letters = sample('0123456789', digits)

# letters의 0번째 값이 0이면 역순정렬
if letters[0] == '0':
    letters.reverse()

# letters의 3개의 원소를 문자열로 합쳐주고 number에 저장
number = ''.join(letters)   #['2', '4', '3'] -> '243'

# 맞춰야할 숫자가 완성되었음을 안내하고 
# 유저가 추측할 수 있는 기회가 몇 번 남았는지 안내
print('I have thought up a number.')
print('You have', guesses, 'guesses to get it.')

counter = 1

# 무한루프
while True:
    # 유저가 추측한 숫자를 guess에 저장
    print('Guess #', counter)
    guess = input()

    # 유저가 입력한 숫자가 digits(3)자리수가 아니면 에러 안내 및 재답변 유도
    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.

    clues = []

    # digits(3)만큼 for문 돌면서 유저의 숫자와 number의 값 비교
    for index in range(digits):
        # guess의 index번째 값과 number의 index번째 값이 같으면 clues에 'fermi' 추가
        if guess[index] == number[index]:
            clues.append('fermi')
        # guess의 index번째 값과 number의 index번째 값이 같지않고, 
        # guess의 index번째 값이 number(3자리 숫자)에 포함되면
        # clues에 'pico' 추가
        elif guess[index] in number:
            clues.append('pico')

    # 3번 for문을 돌면서 'fermi' 또는 'pico' clues에 저장해둔 상태(조건성립시)
    # 무작위로 clues의 값들을 섞음 ex. ['fermi', 'pico']
    shuffle(clues)

    # 추측했던 숫자와 number가 같지않고, 숫자들이 number를 이루는 숫자에 포함이 되지 않는다면
    # ex. 추측한 숫자 789, number 243 이면 bagels 출력
    if len(clues) == 0:
        print('bagels')
    # 추측했던 숫자와 number의 비교에서 한번이라도 'fermi' 또는 'pico'이 나온 경우
    # 'fermi' 또는 'pico'를 저장한 clues의 값을 출력
    else:
        print(' '.join(clues))

    # 추측의 과정이 한 번 끝날때 마다 counter +1씩 증가
    counter += 1

    # 만약 추측한 숫자와 number가 동일하다면 성공 후 무한루프 탈출
    if guess == number:
        print('You got it!')
        break

    # 추측의 기회를 모두 써버린 경우 number 값 알려주고 실패안내 후 게임 종료 
    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break