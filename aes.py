def fill(message, fill_character, block_size):
    return message + fill_character * (block_size - (len(message) % block_size))


def string_to_bytes(string):
    bytes = []
    for character in string:
        bytes.append(ord(character))
    return tuple(bytes)


def split_by_length(string, length):
    return tuple(string[i: i + length] for i in range(0, len(string), length))


def resize(array, width, height):
    new_array = []
    for y in range(height):
        new_row = []
        for x in range(width):
            new_row.append(array[y * width + x])
        new_array.append(tuple(new_row))
    return tuple(new_array)


def bytes_to_string(bytes):
    result = ''
    for row in bytes:
        for byte in row:
            result += chr(byte)
    return result


rounds = {
    16: 10,
    24: 12,
    32: 14
}

import aes_block
import aes_utils


def encrypt(message, key):
    filled_message = fill(message, '\0', 16)
    encoded_message = string_to_bytes(filled_message)
    blocks = split_by_length(encoded_message, 16)
    blocks2d = tuple(resize(block, 4, 4) for block in blocks)

    key_in_bytes = resize(string_to_bytes(key), 4, 4)

    encrypted_blocks = []
    for block in blocks2d:
        encrypted_blocks.append(aes_block.cipher(block, aes_utils.expand_key(key_in_bytes, 44), 10))

    ciphertext = ''
    for encrypted_block in encrypted_blocks:
        ciphertext += bytes_to_string(encrypted_block)

    return ciphertext


def decrypt(message, key):
    encoded_message = string_to_bytes(message)
    blocks = split_by_length(encoded_message, 16)
    blocks2d = tuple(resize(block, 4, 4) for block in blocks)

    key_in_bytes = resize(string_to_bytes(key), 4, 4)

    decrypted_blocks = []
    for block in blocks2d:
        decrypted_blocks.append(aes_block.inverse_cipher(block, aes_utils.expand_key(key_in_bytes, 44), 10))

    plaintext = ''
    for decrypted_block in decrypted_blocks:
        plaintext += bytes_to_string(decrypted_block)

    return plaintext
