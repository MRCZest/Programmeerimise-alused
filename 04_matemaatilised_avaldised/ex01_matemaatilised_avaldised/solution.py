"""Math exercises."""

import math

def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    addition_result = num_a + num_b
    difference = num_a - num_b
    return addition_result, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    integer_division = num_a // num_b
    return integer_division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiplication = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiplication, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = 3.14 * radius ** 2
    return circle_area


def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return round(hypotenuse)


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    cathetus = math.sqrt(c ** 2 - a ** 2)
    return round(cathetus)

if __name__ == '__main__':
    addition_result, difference = sum_and_difference(5, 6)
    assert addition_result == 11
    assert difference == -1

    float_division_result = float_division(10, 10)
    assert isinstance(float_division_result, float)
    assert 0.99 < float_division_result < 1.01
    float_division_result = float_division(10, 2)
    assert 4.99 < float_division_result < 5.01

    integer_division_result = integer_division(10, 10)
    assert isinstance(integer_division_result, int)
    assert integer_division_result == 1
    integer_division_result = integer_division(10,2)
    assert integer_division_result == 5

    multiplication, power, remainder = powerful_operations(3, 4)
    assert multiplication == 12
    assert power == 81
    assert remainder == 3

    average_result = find_average(10, 5)
    assert average_result == 7.5

    circle_area_result = area_of_a_circle(10)
    assert circle_area_result == 314

    triangle_area_result = area_of_an_equilateral_triangle(8)
    assert triangle_area_result == 28

    discriminant_result = calculate_discriminant(8, 20, 12)
    assert discriminant_result == 16

    hypotenuse_result = calculate_hypotenuse_length(10, 8)
    assert hypotenuse_result == 13

    cathetus_result = calculate_cathetus_length(10, 16)
    assert cathetus_result == 12
