"""Mad Libs: Funny Story Creation Game

Exercises:

1. How to replace the story?
2. How load the story and from a file?
3. How to add additional parts of speech?
"""

# The quick brown fox jumps over the lazy dog.
template = 'The |1| |2| |3| |4| over the |5| |6|.'  #문장의 틀을 저장해놓는 스트링
parts = {   #각각의 문장성분을 입력받아서 저장해두는 딕셔너리
    '1': 'adjective',
    '2': 'adjective',
    '3': 'noun',
    '4': 'verb',
    '5': 'adjective',
    '6': 'noun',
}

chunks = [] #templt을 나누어서 저장할 비어있는 튜플

for chunk in template.split('|'):
    # template을 |를 경계로 나누어서 parts에 있으면 즉, 1,2,3,4,5,6중 하나이면 
    # description에 해당되는 숫자의 parts 값을 넘겨줍니다.
    if chunk in parts:
        description = parts[chunk]
        prompt = 'Enter [{}]: '.format(description)
        word = input(prompt)    #그리고 이 description을 prompt에 저장하여 입력할 문장성분을 알려주고
        chunks.append(word) #  word에 입력받아서 chunks에 붙입니다.
    else:
        chunks.append(chunk)  #만약 parts에 없으면 바로 chunks 에 붙입니다.

print('=' * 80) #경계선을 만듬
story = ''.join(chunks) #story에 join을 사용하여 chunk를 스페이스를 넣으며 문장으로 만듭니다.
print(story)    #마지막으로 story를 출력합니다.

# 만들어주는 문장의 형식이 하나밖에 없습니다.
#  랜덤으로 주어진 문장 형식을 선택하여 더욱 
#  다양한 문장을 만들어 사용자가 흥미를 느낄수 있도록 
#  개선할 예정입니다.

