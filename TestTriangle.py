# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from prettytable import PrettyTable

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

table = PrettyTable()
table.field_names = ['Test ID', 'Input', 'Expected Results', 'Actual Result', 'Pass or Fail']

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    global table

    def testRightTriangleA(self):

        id = 'testRightTriangleA'
        a, b, c = 3, 4, 5
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'Right'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)


    def testRightTriangleB(self): 

        id = 'testRightTriangleB'
        a, b, c = 5, 3, 4
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'Right'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)


    def testEquilateralTriangles(self):

        id = 'testEquilateralTriangles'
        a, b, c = 1, 1, 1
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'Equilateral'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)

    def testScaleneTriangles(self):

        id = 'testScaleneTriangles'
        a, b, c = 2, 3, 4
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'Scalene'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        print("\n")
        print(table)
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)

    def testIsocelesTriangles(self):

        id = 'testIsocelesTriangles'
        a, b, c = 5, 5, 6
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'Isoceles'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)

    def testInvalidInput1(self):

        id = 'testInvalidInput1'
        a, b, c = -3, -4, -5
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'InvalidInput'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)
    
    def testInvalidInput2(self):

        id = 'testInvalidInput2'
        a, b, c = 1000, 1000, 1000
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'InvalidInput'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)

    def testNotATriangle(self):

        id = 'testNotATriangle'
        a, b, c = 1, 1, 100
        Input = ', '.join(map(str, [a, b, c]))
        expected = 'NotATriangle'
        actual = classifyTriangle(a, b, c)
        p_f = ('Pass' if expected == actual else 'Fail')

        table.add_row([id, Input, expected, actual, p_f])
        self.assertEqual(classifyTriangle(a, b, c),expected, Input+' should be '+expected)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()