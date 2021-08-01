
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



