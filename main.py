from aes import *

from aes_block import *


def main():
    message = "Caner"
    key = "1234567890123456"

    ciphertext = encrypt(message, key)
    plaintext = decrypt(ciphertext, key)

    print(message)
    print(ciphertext)
    print(plaintext)


if __name__ == '__main__':
    main()
