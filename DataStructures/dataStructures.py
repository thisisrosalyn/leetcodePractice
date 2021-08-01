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
        
        


###################
# Sinlge Linked List
###################
# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        return
    
    def delete(self, value):
        return
    
    def deleteAt(self, index):
        return
    
    def deleteList(self):
        # initialize the current node
        current = self.head
        while current:
            prev = current.next  # move next node
 
            # delete the current node
            del current.data
 
            # set current equals prev node
            current = prev
 
        # In python garbage collection happens
        # therefore, only
        # self.head = None
        # would also delete the link list
    
    def length(self):
        # Possible recursive way
        # 1) If head is NULL, return 0.
        # 2) Else return 1 + getCount(head->next) 
        temp = self.head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count
    
    def find(self, value):
        return
 
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    llist.head.next = second # Link first node with second
    second.next = third # Link second node with the third node
 
    llist.printList()


###################
# Double Linked List
###################




###################
# Tree, Tries & Graphs
###################






###################
# Stacks
# Last-in First-out
###################

class stack:
    def __init__(self):
        return
    
    def pop(self):
        # Remove the top item from the stack
        return
    
    def push(self, item):
        # Add an item to he top of the stack
        return
    
    def peek(self):
        # Return the top of the stack
        return
    
    def isEmpty(self):
        # Return true if and only if the stack is empty
        return

#####################################################################################################
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop()) 
# will cause an IndexError
# as the stack is now empty
#####################################################################################################

###################
# Queues
# First-in First-out
###################
class queue:
    def __init__(self):
        return
    
    def add(self, item):
        # Add an tiem to the end of the list
        return
    
    def remove(self):
        # Remove the first item in the list
        return
    
    def peek(self):
        # Return the top of the queue
        return
    
    def isEmpty(self):
        # Return true if and only if the queue is empty
        return
#####################################################################################################
# Initializing a queue
queue = []
 
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
 
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)
 
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

#####################################################################################################
from queue import Queue
 
# Initializing a queue
q = Queue(maxsize = 3)
 
# qsize() give the maxsize of the Queue
print(q.qsize())
 
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
 
# Return Boolean for Full Queue
print("\nFull: ", q.full())
 
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
# Return Boolean for Empty Queue
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
 
# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())
#####################################################################################################
import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')


###################
# Heaps
###################



###################
# Hash Tables / Hash Maps
###################


