###################
# Array
###################
import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('Index out of bound')
        return self.A[k]

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n += 1

    def insertAt(self, item, index):
        if index < 0 or index > self.n:
            print('please enter an appropriate index')
            return
        
        if self.n == self.capacity:
            self._resize()
        
        for i in range(self.n - 1, index - 1, -1):
            self.A[i+1] = self.A[i]
        
        self.A[index] = item
        self.n += 1

    def delete(self):
        if self.n == 0:
            print('Array is emtpy')
        
        self.A[self.n-1] = 0
        self.n -= 1
    
    def removeAt(self,index):
        if self.n == 0:
            print('Array is empty')
            
        if index < 0 or index >= self.n:
            return IndexError('Index out of range')
        
        if index == self.n-1:
            self.delete()
            return
        
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        
        self.A[self.n-1] = None
        self.n -= 1
    
    def _resize(self):
        B = self.make_array(2*self.capacity)

        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = 2*self.capacity
    
    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()