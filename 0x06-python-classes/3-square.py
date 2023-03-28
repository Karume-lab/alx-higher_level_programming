#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif 0 > size:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size * self.__size
