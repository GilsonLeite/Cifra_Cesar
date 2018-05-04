import sys
import string
ALPHABET = string.ascii_uppercase


def criptografia(message, direcao, rot):
    result = ''
    for i in message:
        if i in ALPHABET:
            i_index = ALPHABET.index(i)
            result += ALPHABET[(i_index + (direcao * rot)) % len(ALPHABET)]
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
