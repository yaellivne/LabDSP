def twos_comp(val):
    if val != (-2**15):
        return 2 ** 15 - val
    return ~val + 1


def compute_hex(fraction_input):
    if fraction_input > 1 or fraction_input < -1:
        return "input is not a fraction!"
    q15_input = int(fraction_input * (2 ** 15))
    if q15_input < 0:
        return hex(twos_comp(q15_input))
    return hex(q15_input)


if __name__ == '__main__':
    user_input = 0.25
    print(compute_hex(user_input))
