# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 30, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: rjw
"""

import math

def check_input(side_a, side_b, side_c):
    """
    Verifies that input is valid and meets the appropriate criteria
    """

    try:
        side_a = float(side_a)
        side_b = float(side_b)
        side_c = float(side_c)

    except ValueError:
        # verify that all 3 inputs are integers
        # Python's "isinstance(object,type) returns True if the object is of the specified type
        float_double_a = isinstance(side_a, (float, int))
        float_double_b = isinstance(side_b, (float, int))
        float_double_c = isinstance(side_c, (float, int))
        if not(float_double_a and float_double_b and float_double_c):
            print('Please enter real numbers only')
            return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        print('The values specified are too large')
        return 'InvalidInput'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        print('The values specified are too small or negative')
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not side_a triangle
    a_largest = (side_a >= (side_b + side_c))
    b_largest = (side_b >= (side_a + side_c))
    c_largest = (side_c >= (side_a + side_b))
    if a_largest or b_largest or c_largest:
        print('The sides entered do not form a valid triangle')
        return 'InvalidInput'

    return 'Valid'

def classify_triangle(side_a, side_b, side_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # now we know that we have side_a valid triangle
    if side_a == side_b and side_b == side_c:
        print('Equilateral Triangle')
        return 'Equilateral'

    in_range_c = math.isclose(((side_a ** 2) + (side_b ** 2)), (side_c ** 2), abs_tol=.01)
    in_range_b = math.isclose(((side_a ** 2) + (side_c ** 2)), (side_b ** 2), abs_tol=.01)
    in_range_a = math.isclose(((side_c ** 2) + (side_b ** 2)), (side_a ** 2), abs_tol=.01)
    if in_range_c or in_range_b or in_range_a:
        if (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
            print('Right Scalene Triangle')
            return 'Right Scalene'
        elif(side_a == side_b or side_b == side_c or side_c == side_a):
            print('Right Isosceles Triangle')
            return 'Right Isosceles'
        return 'Right'

    if(side_a == side_b or side_b == side_c or side_c == side_a):
        print('Isosceles Triangle')
        return 'Isosceles'

    #Deprecated
    #if (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
    return 'Scalene'

def get_input():
    """
    Gets input from the user
    """

    sides = input("Enter three sides of a triangle between 1 and 199. Seperate entries by spaces:")
    return sides

if __name__ == '__main__':
    SIDES = get_input().split(' ')
    SIDE_A = SIDES[0]
    SIDE_B = SIDES[1]
    SIDE_C = SIDES[2]
    if check_input(SIDE_A, SIDE_B, SIDE_C) != 'InvalidInput':
        classify_triangle(float(SIDE_A), float(SIDE_B), float(SIDE_C))
