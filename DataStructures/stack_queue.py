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

