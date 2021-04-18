class LinkedList_array(object):

    class Node(object):

        def __init__(self, element, prev_node, next_node):
            self.element = element
            self.prev_node = prev_node
            self.next_node = next_node
            self.address = 0

        def set_address(self, ptr):
            self.address = ptr

        def get_next_node(self):
            return self.next_node

        def get_prev_node(self):
            return self.prev_node

        def set_next_node(self, next_ptr):
            self.next_node = next_ptr

        def set_prev_node(self, prev_ptr):
            self.prev_node = prev_ptr

    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.array = [self.header, self.trailer]
        self.header.set_address(1)
        self.trailer.set_address(-1)
        self.header.set_next_node(-1)
        self.trailer.set_prev_node(1)
        self.size = 0

    def validate
        
        
