from typing import List


def plusOne(digits):
    length = len(digits) - 1
    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if length < 0:
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits


if __name__ == '__main__':
    print(plusOne([1, 9, 9]))
