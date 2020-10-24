def compute_hex(fraction_input):
    if fraction_input > 1 or fraction_input < -1:
        return "input is not a fraction!"
    q15_input = int(fraction_input * (2 ** 15))
    return hex(q15_input & (2**16 - 1))


if __name__ == '__main__':
    user_input = -0.75
    print(compute_hex(user_input))
