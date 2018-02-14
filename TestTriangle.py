# -*- coding: utf-8 -*-
"""
Updated Jan 30, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: rjw
"""

import math
import unittest

from Triangle import classifyTriangle getInput

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right Scalene','3,4,5 is a Right Scalene triangle')

    def testRightScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right Scalene','5,3,4 is a Right Scalene triangle')

    def testRightScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(3.0005,4.0005,5.0005), 'Right Scalene')

    def testRightIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(10*(2**.5), 10*(2**.5), 20), 'Right Isosceles')

    def testRightTriangleA(self):
        self.assertNotEqual(classifyTriangle(4, 4, 4), 'Right')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertNotEqual(classifyTriangle(4, 5, 5), 'Equilateral')

    def testValidA(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'NotATriangle')

    def testValidB(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testInputA(self):
        self.assertEqual(classifyTriangle(201, 203, 257), 'InvalidInput')

    def testInputB(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')

    def testInputC(self):
        self.assertEqual(classifyTriangle(-3, -4, -5), 'InvalidInput')

    def testScaleneA(self):
        self.assertEqual(classifyTriangle(2, 4, 5), 'Scalene')

    def testScaleneB(self):
        self.assertNotEqual(classifyTriangle(2, 2, 1), 'Scalene')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isosceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(1, 3, 3), 'Isosceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(4, 2, 4), 'Isosceles')

    def testIsoscelesD(self):
        self.assertNotEqual(classifyTriangle(2,2,2), 'Isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
