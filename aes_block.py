from aes_utils import *


def cipher(block, words, round):
    state = block
    state = add_round_key(state, words[0:4])

    for i in range(1, round):
        state = substitute_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, words[i * 4:(i + 1) * 4])

    state = substitute_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, words[round * 4:(round + 1) * 4])

    return state


def inverse_cipher(block, words, round):
    state = block

    state = add_round_key(state, words[round * 4:(round + 1) * 4])

    for i in range(9, 0, -1):
        state = inverse_shift_rows(state)
        state = inverse_substitute_bytes(state)
        state = add_round_key(state, words[i * 4:(i+1) * 4])
        state = inverse_mix_columns(state)

    state = inverse_shift_rows(state)
    state = inverse_substitute_bytes(state)
    state = add_round_key(state, words[0:4])

    return state
