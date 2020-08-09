#!/usr/bin/env python3

"""
# @Create    : 2020/8/2   
# @Author  : xuxh
# @Description   :  说明文件功能
# @Modify Time      @Version    @Description
------------      --------    -----------
2020/8/2             1.0         None
"""
from unittest import TestCase
from rectangle import Rectangle
print("I update code")
print(" Smith update code")
print(" kate update code too")



class TestRectangle(TestCase):

    def setUp(self):
        self.rectangle = Rectangle(30, 15)

    def test_area(self):

        area = self.rectangle.area()
        self.assertEqual(area, 450)

    def test_perimeter(self):

        perimeter = self.rectangle.perimeter()
        self.assertEqual(perimeter, 90)

    def test_diff(self):

        diff = self.rectangle.diff()
        self.assertEqual(diff, 15)

    def test_width(self):
        self.assertEqual(self.rectangle.width, 15)

    def test_height(self):
        self.assertEqual(self.rectangle.height, 30)

    def test_resize(self):

        self.assertRaises(ValueError, self.rectangle.resize, 15, 0)

    def test_resize_positive(self):
        self.rectangle.resize(20, 50)
        self.assertEqual(self.rectangle._size[0], 20)

    from unittest import skip
    
    @skip('just for testing')
    def test_skip(self):

        print('skip this case')

    def tearDown(self):
        self.rectangle = None

