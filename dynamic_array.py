# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Nick Morris
import numpy as np
import random
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.next_index = 0
        self.data = np.ndarray(self.capacity, 'O')

    def is_full(self):
        if self.next_index < self.capacity:
            return self.next_index == self.capacity
        elif self.next_index >= self.capacity:
            return self.next_index >= self.capacity

    def is_empty(self):
        return self.next_index == 0

    def __len__(self):
        return self.next_index

    def append(self, ele):
        if self.next_index == self.capacity:
            self.capacity *= 2
            self.data = np.ndarray(self.capacity, 'O')
        self.data[self.next_index] = ele
        self.next_index += 1

    def delete(self, ele):
        if ele == 0 and self.next_index == 0:
            raise IndexError()
        elif ele == 0:
            self.data = np.delete(self.data, [ele])
            self.next_index -= 1
        elif ele > 0 or ele >= self.next_index:
            self.data = np.delete(self.data, [ele])
            self.next_index -= 1
        elif ele < 0:
            raise IndexError()

    def pop(self):
        if self.next_index -1 < 0:
            raise IndexError()
        lastEle = self.data[self.next_index-1]
        self.data = np.delete(self.data, [self.next_index-1])
        self.next_index -= 1
        return lastEle

    def clear(self):
        for ele in self.data:
            self.data[self.next_index] = 0
        self.next_index = 0

    def insert(self, idx, ele):
        if idx == 0:
            self.data = np.insert(self.data, idx, ele)
            self.next_index += 1 
        if idx < 0 or idx > self.next_index:
            raise IndexError()
        elif idx > 0 and idx <= self.next_index:
            self.data = np.insert(self.data, idx, ele)
            self.next_index += 1
            
    def __getitem__(self, ele):
        if ele < 0 or ele >= self.next_index:
            raise IndexError()
        return self.data[ele]

    def max(self):
        max_ele = self.data[0]
        for idx in self.data:
            if self.data[idx] > max_ele:
                max_ele = self.data[idx] 
            return max_ele
