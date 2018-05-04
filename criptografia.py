import sys
import string
ALFABETO = string.ascii_uppercase


def criptografia(message, direcao, rot):
    result = ''
    for i in message:
        if i in ALFABETO:
            i_index = ALFABETO.index(i)
            result += ALFABETO[(i_index + (direcao * rot)) % len(ALFABETO)]
        else:
            result += i
    return result


def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].upper()
    rot = int(sys.argv[3])

    if command == 'encrypt':
        print criptografia(message, 1, rot)
    elif command == 'decrypt':
        print criptografia(message, -1, rot)
    else:
        print 'Command not found'


if __name__ == '__main__':
    main()
