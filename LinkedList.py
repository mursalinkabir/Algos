#node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Linked List class        
class LinkedList:
    #Function to initialize the linked list obj
    def __init__(self):
        self.head = None

# This function is in LinkedList class
# Function to insert a new node at the beginning    
    def push(self,new_data):
         # 1 & 2: Allocate the Node &
        #        Put in the data   
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node
        

# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */
    def insertAfter(self,prev_node,new_data):
        
        #check if the prev node exists
        if prev_node is None:
            print ("The given previous node must inLinkedList.")
            return
        # Put in the data   
        new_node = Node(new_data)      
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
        
    # This function is defined in Linked List class
    # Appends a new node at the end.  This method is
    # defined inside LinkedList class shown above */
    def append(self, new_data):
        
        # Put in the data   
        new_node = Node(new_data)    
        # 4. If the Linked List is empty, then make the
        #    new node as head        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        # 5. Else traverse till the last node
        while(last.next):
            last = last.next
        # 6. Change the next of last node    
        last.next = new_node
        
            # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            
# Code execution starts here            
if __name__ == '__main__':
    
    lnklist = LinkedList()
    
    # Insert 6.  So linked list becomes 6->None    
    lnklist.append(6)
    
    lnklist.push(7);
    lnklist.push(1);
    
    lnklist.append(4)
    
    lnklist.insertAfter(lnklist.head.next,8)
    

    print('Created linked list is:')
    lnklist.printList()
 
    
        
        
