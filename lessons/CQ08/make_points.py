"""Checking methods from file Point."""
__author__ = "730395850"

from lessons.CQ08.point import Point


test_1: Point = Point(2.5, 4.5)

print(test_1.x)
print(test_1.scale(2)) 
test_1.scale_by(4)
print(test_1.scale(3))  
