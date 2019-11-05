from argparse import ArgumentError


def flag(_n: str) -> str:
    try:
        n = int(_n)
        if n > 0 and not n % 2:  # even numbers
            out_str = ''

            right_border = 3 * n + 2
            bottom_border = 2 * n + 2
            h = n // 2  # free space height
            sq_x_o = range(n + 1, n * 2 + 1)  # outer square
            sq_y_o = range(h + 1, bottom_border - h - 1)  # outer square
            # print(sq_x, sq_y)

            """ l1 - l4: outer circle borders """
            # l1 = (x, y)
            # l2 = (x + n, y)
            # l3 = (n * 2 + 1 - x, y)
            # l4 = (n * 3 + 1 - x, y)

            for y in range(bottom_border):
                for x in range(right_border):
                    if (x == 0) or (x == right_border - 1) or (y == 0) or (y == bottom_border - 1):
                        """ rectangle borders """
                        out_str += '#'
                    elif (x in sq_x_o) and (y in sq_y_o):
                        """ outer square """
                        if x == y or x == y + n or x == (-y + 2 * n + 1) or x == (-y + 3 * n + 1):
                            """ outer circle border """
                            out_str += '*'
                        elif y < x < (-y + 3 * n + 1) and y + n > x > (-y + 2 * n + 1):
                            """ inner circle """
                            out_str += 'o'
                        else:
                            out_str += ' '
                    else:
                        """ free space """
                        out_str += ' '
                out_str += '\n'

            return out_str
        else:
            # raise ValueError("Number must be even!")
            raise ArgumentError(None, "")
    except Exception as ex:
        raise ArgumentError(None, "The input N shall be an integer even number!")


if __name__ == "__main__":
    string = input("Enter positive integer even number: ")
    print(flag(string))
