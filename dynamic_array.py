# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Nick Morris
import numpy as np
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.next_index = 0
        self.data = np.ndarray(self.capacity, 'O')

    def is_empty(self):
        return self.next_index == 0

    def __len__(self):
        return self.next_index

    def append(self, ele):
        self.data[self.next_index] = ele
        self.next_index += 1

    def clear(self):
        for ele in self.data:
            self.data[self.next_index] = 0
        self.next_index = 0
            
    def __getitem__(self, ele):
        if ele < 0 or ele >= self.next_index:
            raise IndexError()

        return self.data[ele]
       
    