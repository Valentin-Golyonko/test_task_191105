import numpy as np


def inner_circle(r: int):
    d = 2 * r + 1
    rx, ry = d / 2, d / 2
    x, y = np.indices((d, d))

    arr_0 = np.abs(np.hypot(rx - x, ry - y) - r)
    print('x =', len(arr_0[0]), ', y =', len(arr_0))

    for row in arr_0:
        str_0 = ''
        for i in row:
            str_0 += '%0.3f ' % i
        print(str_0)

    # print((arr_0 < 0.5).astype(int))
    arr = (arr_0 < 0.64).astype(int)

    arr_2 = ''
    start_inner_circle = False
    for row in arr:
        arr_2 = ''
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
                elif arr_2[-3:] == ' **' or arr_2[-1:] == 'o' or arr_2[:2] == '**':
                    arr_2 += 'o'
                else:
                    arr_2 += ' '
        print(arr_2)


def borders(n: int):
    right_border = 3 * n + 2
    bottom_border = 2 * n + 2
    print('x =', right_border, ', y =', bottom_border)

    flag_border = [
        ['#' if x == 0 or x == right_border - 1 or y == 0 or y == bottom_border - 1 else ' ' for x in
         range(right_border)]
        for y in range(bottom_border)]

    for row in flag_border:
        print(''.join(row))


if __name__ == "__main__":
    N = 12
    inner_circle(N)
    borders(N)

    s = '   **'
    print(s[-3:])
