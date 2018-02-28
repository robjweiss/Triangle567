# -*- coding: utf-8 -*-
"""
Updated Jan 30, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: rjw
"""

import unittest

from triangle import classify_triangle
from triangle import check_input

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class testTriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_right_scalene_triangle_a(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene', '3,4,5 is a Right Scalene triangle')

    def test_right_scalene_triangle_b(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene', '5,3,4 is a Right Scalene triangle')

    def test_right_scalene_triangle_c(self):
        self.assertEqual(classify_triangle(3.0005, 4.0005, 5.0005), 'Right Scalene')

    def test_right_isosceles_triangle_a(self):
        self.assertEqual(classify_triangle(10*(2**.5), 10*(2**.5), 20), 'Right Isosceles')

    def test_right_triangle_a(self):
        self.assertNotEqual(classify_triangle(4, 4, 4), 'Right')

    def test_equilateral_triangles_a(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_equilateral_triangles_b(self):
        self.assertNotEqual(classify_triangle(4, 5, 5), 'Equilateral')

    def test_equilateral_triangles_c(self):
        self.assertNotEqual(classify_triangle(3, 4, 5), 'Equilateral')

    def test_valid_a(self):
        self.assertNotEqual(check_input(3, 4, 5), 'InvalidInput')

    def test_valid_b(self):
        self.assertEqual(check_input(1, 2, 3), 'InvalidInput')

    def test_input_a(self):
        self.assertEqual(check_input(201, 203, 257), 'InvalidInput')

    def test_input_b(self):
        self.assertEqual(check_input(0, 0, 0), 'InvalidInput')

    def test_input_c(self):
        self.assertEqual(check_input(-3, -4, -5), 'InvalidInput')

    def test_input_d(self):
        self.assertEqual(check_input('notnum1', 'string', 'notnum2'), 'InvalidInput')

    def test_scalene_a(self):
        self.assertEqual(classify_triangle(2, 4, 5), 'Scalene')

    def test_scalene_b(self):
        self.assertNotEqual(classify_triangle(2, 2, 1), 'Scalene')

    def test_isosceles_a(self):
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles')

    def test_isosceles_b(self):
        self.assertEqual(classify_triangle(1, 3, 3), 'Isosceles')

    def test_isosceles_c(self):
        self.assertEqual(classify_triangle(4, 2, 4), 'Isosceles')

    def test_isosceles_d(self):
        self.assertNotEqual(classify_triangle(2, 2, 2), 'Isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
