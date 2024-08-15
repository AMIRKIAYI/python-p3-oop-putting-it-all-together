#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size
        self.condition = "New"

    def repair(self):
        self.condition = "Repaired"
        print("The shoe has been repaired.")