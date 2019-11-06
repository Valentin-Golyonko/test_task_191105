import numpy as np


def inner_circle(r: int):
    d = {2: (2, 0.5), 3: (2, 0.54), 4: (1, 0.54), 5: (2, 0.5), 6: (1, 0.52), 8: (1, 0.64)}  # N(d, 0.x)

    d = 2 * r + 1
    rx, ry = d / 2, d / 2
    x, y = np.indices((d + 1, d + 1))

    arr_0 = np.abs(np.hypot(rx - x, ry - y) - r)
    # print('x =', len(arr_0[0]), ', y =', len(arr_0))

    # for row in arr_0:
    #     str_0 = ''
    #     for i in row:
    #         str_0 += '%0.3f ' % i
    #     print(str_0)

    # print((arr_0 < 0.5).astype(int))
    arr = (arr_0 < 0.54).astype(int)

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
                elif arr_2[:r + 2] == ' ' * r + '**':
                    arr_2 += ' '
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
    for i in range(2, 13):
        print("i: %s" % i)
        inner_circle(i)
    # borders(N)
