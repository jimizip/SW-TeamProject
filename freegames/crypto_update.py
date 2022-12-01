"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.

Adapted from code in https://inventwithpython.com/chapter14.html
"""

def encrypt(message, key): # 암호 -> 문자
    result = ''

    for letter in message:
        if letter.isalpha():

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            result += letter

        else:
            result += letter

    return result

def decrypt(message, key):
    return encrypt(message, -key)

def decode(message):
    """Decode message without key."""
    pass  # TODO

def get_key():
    try:
        text = input('Enter a key (1 - 25): ')
        key = int(text)
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0

def encodeUTF8(string): # 문자 -> 암호
    Istr = string.encode('UTF8')
    Istr = str(Istr)
    return Istr.replace('b', '', 1).replace('\\x', '').replace('\'', '')

print('Do you wish to encrypt, decrypt, or decode a message?')
choice = input()

if choice == 'encrypt':
    print("Which do you want ASCII or UTF8?")
    detail = input()

    if detail == 'ASCII' :
        phrase = input('Message: ')
        code = get_key()
        print('Encrypted message:', encrypt(phrase, code))

    elif detail == 'UTF8' :
        phrase = input('Korean: ')
        code = encodeUTF8
        print('Encrypted message:', encodeUTF8(phrase))

elif choice == 'decrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Decrypted message:', decrypt(phrase, code))

elif choice == 'decode':
    phrase = input('Message: ')
    print('Decoding message:')
    decode(phrase)
else:
    print('Error: Unrecognized Command')
