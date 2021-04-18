class Node(object):
    def __init__ (self, current_data, next_node=None):
        self.current_data = current_data
        self.next_node = next_node

    def get_current_data(self):
        return self.current_data

    def get_next_node(self):
        return self.next_node

    def reset_next_node(self, new_node):
        self.next_node= new_node

#i can try read a file then make it as linked list!

class Stack(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def push(self,e):
        previous_head = self.head
        self.head = Node(e, previous_head)
        self.size+=1

    def peek(self):
        return self.head
    
    def pop(self):
        new_head = self.head.next_node
        return_element = self.head
        self.head = new_head
        self.size -=1
        return return_element

    def __str__(self):
        n = self.head
        for i in range(len(self)):
            print(n.current_data)
            if n.next_node is None:
                break
            else:
                n=n.next_node
            

class Queue(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, e):
        if self.size==0:
            self.head = self.tail = Node(e)
        elif self.size==1:
            self.tail = Node(e)
            self.head.reset_next_node(self.tail)
        else:
            new_tail = Node(e)
            self.tail.reset_next_node(new_tail)
            self.tail = new_tail
        self.size +=1

    def dequeue(self):
        e = self.head.get_current_data()
        self.head = self.head.get_next_node()
        self.size-=1
        return e
    
    def check_head(self):
        return self.head.get_current_data()

    def check_tail(self):
        return self.tail.get_current_data()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.current

    def index_item(self, k):
        e=self.head
        if k>len(self):
            raise Exception('Invalid index')
        else:
            if k==0:
                return e.get_current_data()
            else:
                for i in range(k):
                    e=e.get_next_node()
                return e.get_current_data()
        
    def __str__(self):
        e=self.head
        print_q = ''
        for i in range(len(self)):
            print_q += ( str(e.get_current_data()) + ' -> ' )
            if e.get_next_node() is None:
                break
            else:
                e=e.get_next_node()
        print_q += ' None ' 
        return print_q


class Linkedlist(Queue):
    def __getitem__(self,k):
        n=self.head
        for i in range(k):
            n=n.get_next_node()
        return n.get_current_data()

    def __next__(self):
        if self.head is None:
            raise StopIteration()
        else:
            item = self.head.get_current_data()
            self.head = self.hea

class LinkedListIterator(object):
    def __init__(self,head):
        self.current = head

    def
    
if __name__ == '__main__':
    n=Linkedlist()
    n.enqueue(5)
    n.enqueue(6)
    print(n)
    
    n.enqueue(9)
    print(n)
    
    n.dequeue()
    print(n)

    n.enqueue(19)
    print(n)

    n.enqueue(6)
    print(n)

    n.dequeue()
    print(n)

    print(n[0])
    print(n[1])
    print(n[2])






    
    
