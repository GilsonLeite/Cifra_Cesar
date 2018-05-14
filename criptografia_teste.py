from unittest import TestCase, main
import string


class Testes(TestCase):
    def test_alphabet(self):
        ALPHABET = string.ascii_uppercase
        self.assertEqual(len(ALPHABET), 26)

    def test_deslocamanto_direita(self):
        ALPHABET = string.ascii_uppercase
        aux = ALPHABET[(0 + (1 * 2)) % len(ALPHABET)]
        self.assertEqual(aux, 'C')

    def test_deslocamanto_esquerda(self):
        ALPHABET = string.ascii_uppercase
        aux = ALPHABET[(0 + (-1 * 2)) % len(ALPHABET)]
        self.assertEqual(aux, 'Y')

    def test_vetor_circular(self):
        ALPHABET = string.ascii_uppercase
        aux = ALPHABET[(25 + (1 * 2)) % len(ALPHABET)]
        self.assertEqual(aux, 'B')


if __name__ == '__main__':
    main()
