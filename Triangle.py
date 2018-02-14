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

def classifyTriangle(a,b,c):
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

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        print('The values specified are too large')
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        print('The values specified are too small or negative')
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,(float, int)) and isinstance(b,(float, int)) and isinstance(c,(float, int))):
        print('Please enter real numbers only')
        return 'InvalidInput';

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        print('The sides entered do not form a valid triangle')
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        print('Equilateral Triangle')
        return 'Equilateral'

    if (math.isclose(((a ** 2) + (b ** 2)), (c ** 2), abs_tol = .01) or math.isclose(((a ** 2) + (c ** 2)), (b ** 2), abs_tol = .01) or math.isclose(((c ** 2) + (b ** 2)), (a ** 2), abs_tol = .01)):
        if (a != b) and  (b != c) and (a != c):
            print('Right Scalene Triangle')
            return 'Right Scalene'
        elif(a == b or b == c or c == a):
            print('Right Isosceles Triangle')
            return 'Right Isosceles'
        else:
            return 'Right'

    if (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    if(a == b or b == c or c == a):
        print('Isosceles Triangle')
        return 'Isosceles'

def getInput():
    sides = input("Please enter the three sides of a triangle no less than 1 and no greater than 199. Seperate entries by spaces:")
    return sides

if __name__ == '__main__':
    sides = getInput().split(' ')
    a = float(sides[0])
    b = float(sides[1])
    c = float(sides[2])
    classifyTriangle(a,b,c)
