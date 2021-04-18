class Node(object):

    def __init__(self, element, prev_node, next_node):
        self.element = element
        self.prev_node = prev_node
        self.next_node = next_node

class DoubleLinkedList(object):

    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node (None, None, None)
        self.header.next_node = self.trailer
        self.trailer.prev_node = self.header
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def insert_between(self, e, predecessor, successor):
        new_node = Node(e, predecessor, successor)
        predecessor.next_node = new_node
        successor.prev_node = new_node
        self.size +=1
        return new_node

    def delete_node(self, del_node):
        predecessor = del_node.prev_node
        successor = del_node.next_node
        predecessor.next_node = successor
        successor.prev_node = predecessor
        self.size -=1
        element = del_node.element
        del_node.prev_node = del_node.next_node = del_node.element = None
        return element
    
    
class LinkedDeque(DoubleLinkedList):

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        else:
            return self.header.next_node.element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        else:
            return self.trailer.prev_node.element

    def insert_start(self,e):
        self.insert_between(e, self.header, self.header.next_node)

    def insert_last(self, e):
        self.insert_between(e, self.trailer.prev_node, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        else:
            return self.delete_node(self.header.next_node)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        else:
            return self.delete_node(self.trailer.prev_node)

        
class PositionalList(DoubleLinkedList):

    class Position(object):

        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not (self == other)

        def __str__(self):
            return str(self.container)
    
    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next_node is None:
            raise ValueError('p is no longer valid')
        return p.node

    def make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self.make_position(self.header.next_node)

    def last(self):
        return self.make_position(self.trailer.prev_node)

    def before(self, p):
        node = self.validate(p)
        return self.make_position(node.prev_node)

    def after(self, p):
        node = self.validate(p)
        return self.make_position(node.next_node)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def insert_between(self, e, predecessor, successor):
        node = super().insert_between(e, predecessor, successor)
        return self.make_position(node)
    

    def add_first(self, e):
        return self.insert_between(e, self.header, self.header.next_node)

    def add_last(self, e):
        return self.insert_between(e, self.trailer.prev_node, self.trailer)

    def add_before(self,p,e):
        original = self.validate(p)
        return self.insert_between(e, original.prev_node, original)

    def add_after(self,p,e):
        original = self.validate(p)
        return self.insert_between(e, original, original.next_node)

    def delete(self, p):
        original = self.validate(p)
        return self.delete_node(original)

    def replace(self,p,e):
        original= self.validate(p)
        store_prev_element = original.element
        original.element = e
        return store_prev_element

if __name__ == '__main__':
    L=PositionalList()
    n=L.add_last(8)
    L.add_first(9)
    for i in L:
        print(i)
        









    
    
