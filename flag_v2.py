from argparse import ArgumentError

import numpy as np

""" Just for fun and real/tru round sun """


def inner_circle(_r: str) -> str:
    try:
        r = int(_r)
        if r > 0:
            d = 2 * r + 1
            rx, ry = d / 2, d / 2
            x, y = np.indices((d + 1, d + 1))

            arr_0 = np.abs(np.hypot(rx - x, ry - y) - r)
            # print('x =', len(arr_0[0]), ', y =', len(arr_0))

            arr = (arr_0 < 0.54).astype(int)

            borders_top(r)

            start_inner_circle = False

            for row in arr:
                arr_2 = '#' + ' ' * r
                for i in row:
                    if i:
                        arr_2 += '*'
                        if not start_inner_circle:
                            start_inner_circle = True
                        else:
                            start_inner_circle = False
                    else:
                        if start_inner_circle:
                            arr_2 += 'o'
                        elif arr_2[:2 * r + 3] == ('#' + ' ' * 2 * r + '**'):  # circle top and bottom points
                            arr_2 += ' '
                        elif arr_2[-3:] == ' **' or arr_2[-1:] == 'o' or arr_2[:2] == '**':
                            arr_2 += 'o'
                        else:
                            arr_2 += ' '
                arr_2 += ' ' * r + '#'
                print(arr_2)

            borders_bottom(r)
        else:
            raise ValueError("Number must be positive integer")
    except Exception as ex:
        raise ArgumentError(None, "The input N shall be an positive integer number!\n%s" % ex)


def borders_top(n: int):
    right_border = 4 * n + 4

    flag_border = [
        ['#' if x == 0 or x == right_border - 1 or y == 0 else ' ' for x in range(right_border)] for y in
        range(n // 2 + 1)]

    for row in flag_border:
        print(''.join(row))


def borders_bottom(n: int):
    right_border = 4 * n + 4
    bottom_border = n // 2 + 1

    flag_border = [
        ['#' if x == 0 or x == right_border - 1 or y == bottom_border - 1 else ' ' for x in range(right_border)] for y
        in range(bottom_border)]

    for row in flag_border:
        print(''.join(row))


if __name__ == "__main__":
    # for j in range(2, 13):
    #     print("N: %s" % j)
    #     inner_circle(j)

    string = input("Enter positive integer even number: ")
    inner_circle(string)
