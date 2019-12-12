import math
from argparse import ArgumentError


class Flag3:
    def __init__(self, number: int) -> None:
        self._number = self.even_number(number)
        self.inner_circle_symbol = 'o'
        self.outer_circle_symbol = '*'
        self.borders_symbol = '#'
        self.free_space_symbol = ' '
        self.inner_circle_radius = (self._number - 2) // 2
        self.outer_circle_radius = self.inner_circle_radius + 1
        self.circle_center_x = 1 + self._number + self.outer_circle_radius - 0.5
        self.circle_center_y = 1 + (self._number // 2) + self.outer_circle_radius - 0.5
        self.flag_width = 3 * self._number + 2
        self.flag_height = 2 * self._number + 2
        self.outer_radius_correction_coefficient = 0.18

    def even_number(self, number):
        if number and type(number) != str and number > 0 and not number % 2:
            return number
        else:
            raise ArgumentError(None, "The input Number must be positive integer even number!")

    def circle_formula(self, x: int, y: int) -> str:
        """ x**2 + y**2 = r**2 """
        radius = math.sqrt((x - self.circle_center_x) ** 2 + (y - self.circle_center_y) ** 2)

        if radius <= self.inner_circle_radius:
            return self.inner_circle_symbol

        elif self.inner_circle_radius < radius <= self.outer_circle_radius:

            if abs(self.outer_circle_radius - radius) <= self.outer_radius_correction_coefficient:
                return self.free_space_symbol
            else:
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
                    output_str += self.circle_formula(x, y)

            output_str += '\n'

        return output_str

    def print_flag(self):
        print(self.create_flag())


if __name__ == "__main__":
    flag = Flag3(6)
    flag.print_flag()
