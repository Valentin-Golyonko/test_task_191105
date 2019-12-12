import math


class Flag3:
    def __init__(self, number: int) -> None:
        self._number = number
        self.inner_circle_symbol = 'o'
        self.outer_circle_symbol = '*'
        self.borders_symbol = '#'
        self.free_space_symbol = ' '
        self.inner_circle_radius = (number - 2) // 2
        self.outer_circle_radius = self.inner_circle_radius + 1
        self.circle_center_x = 1 + number + self.outer_circle_radius
        self.circle_center_y = 1 + (number // 2) + self.outer_circle_radius
        self.flag_width = 3 * number + 2
        self.flag_height = 2 * number + 2

    def create_empty_flag(self, number):
        pass

    def circle_formula(self, x: int, y: int) -> str:
        """ x**2 + y**2 = r**2 """
        r = math.sqrt((x - self.circle_center_x) ** 2 + (y - self.circle_center_y) ** 2)
        print("r: %s" % r)
        if r <= self.inner_circle_radius:
            return self.inner_circle_symbol
        elif self.inner_circle_radius < r <= self.outer_circle_radius:
            return self.outer_circle_symbol
        else:
            return self.free_space_symbol

    def create_flag(self) -> str:
        output_str = ''
        for y in range(self.flag_height):
            for x in range(self.flag_width):
                if (x == 0) or (x == self.flag_width - 1) or (y == 0) or (y == self.flag_height - 1):
                    output_str += self.borders_symbol
                else:
                    cf = self.circle_formula(x, y)
                    print("cf: %s" % cf)
                    output_str += cf
            output_str += '\n'

        return output_str

    def print_flag(self):
        print(self.create_flag())


if __name__ == "__main__":
    flag = Flag3(2)
    flag.print_flag()
