#!/usr/bin/env python3
""" Module BaseGeometry """
BaseGeometry = __import__('0-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe rectangle"""
    def __init__(self, width, height):
        """Init du rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
