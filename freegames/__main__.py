"""Free Games CLI
"""

import argparse # 인자들을 입력 받아 프로그램이 동작하게 하는 모듈
import os # 운영체제에서 제공되는 기본적인 기능들을 제공하는 모듈

directory = os.path.dirname(os.path.realpath(__file__)) # directory 변수 선언
contents = os.listdir(directory) # contents 변수 선언

# 파일 이름이 게임 파일 이름과 같으면 True를 반환하는 함수 선언
def game_file(name): 
    """Return True if filename represents a game."""
    return (
        name.endswith('.py')
        and not name.startswith('__')
        and name != 'utils.py'
    )


games = sorted(name[:-3] for name in contents if game_file(name)) # games 변수 선언

parser = argparse.ArgumentParser( # parser 변수 선언
    prog='freegames', # 입력 받을 인자의 조건 설정. freegames 폴더 안에 있어야한다는 조건.
    description='Free Python Games', # 'Tree Python Games'라는 표시가 있어야한다는 조건.
    epilog='Copyright 2022 Grant Jenks', # 마지막 부분은 'Copyright 2022 Grant Jenks'로 끝나야한다는 조건.
)
# subparsers 변수 선언. parsers 명령어와 sub-parsers 명령어를 도움말로 안내한다.
subparsers = parser.add_subparsers(dest='command', help='sub-command help') 

# 명령어 py -m freegames list를 입력하면 게임의 목록을 안내한다.
parser_list = subparsers.add_parser('list', help='list games') 

# 명령어 py -m freegames copy 선언
parser_copy = subparsers.add_parser('copy', help='copy game source code')
# 명령어 py -m freegames copy 게임이름 을 입력하면 게임을 복사한다.
parser_copy.add_argument('game', choices=games, help='game name') 
parser_copy.add_argument(
    '--force',
    action='store_true', # 명령어 행에서 game이 발견되면 'store_true'를 표시한다.
    help='overwrite existing file', # 도움말은 존자하는 파일에 대해 덮어쓰기 하는 방법을 안내한다.
)

# 명령어 py -m freegames show 선언.
parser_show = subparsers.add_parser('show', help='show game source code') 
# 명령어 py -m freegames show 게임이름을 입력하면 코드를 보여준다.
parser_show.add_argument('game', choices=games, help='game name') 

args = parser.parse_args() # args 변수 선언

if args.command == 'list': # args 명령어가 py -m freegames list 라면
    for game in games: # games들의 이름을 모두 출력
        print(game)
elif args.command == 'copy': # args 명령어가 py -m freegames copy 라면
    filename = args.game + '.py' # .py를 더해서 저장

    with open(os.path.join(directory, filename)) as reader: # 디렉토리 게임 파일을 연다.
        text = reader.read() # text 변수를 사용해 텍스트들을 읽어와 저장

    cwd = os.getcwd() # cwd 변수를 이용하여 현재 디렉토리의 위치 저장
    path = os.path.join(cwd, filename) # path 변수 선언

    if args.force or not os.path.exists(path): # py -m freegames --force 라면
        with open(path, 'w') as writer: # 쓰기모드로 파일을 열고,
            writer.write(text) # 파일의 내용을 출력.
    else: # 그렇지 않으면,
        print('ERROR: File already exists. Specify --force to overwrite.') # 에러 문구를 출력.
else: # list, copy 명령어가 아닌 다른 명령어라면,
    assert args.command == 'show' # 또한, 그 중 show가 아니라면 예외 처리를 한다. 

    with open(os.path.join(directory, args.game + '.py')) as reader: # py -m freegames show라면 .py를 붙이고
        print(reader.read()) # 파일을 읽기모드로 읽고 출력한다.