# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Nick Morris
import numpy as np
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.n = 0
        self.data = np.ndarray(self.capacity, 'O')

    def is_empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def append(self, num):
        self.data[self.n] = num
        self.n += 1

    def __getitem__(self, number):
        return self.data[number]