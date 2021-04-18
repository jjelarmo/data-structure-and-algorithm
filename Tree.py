class Tree(object):

    class Position(object):

        def element(self):
            raise NotImplementedError('must be implemented in subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented in subclass')

        def __ne__(self, other):
            raise NotImplementedError('must be immplemented in subclass')


    def root(self):
        raise NotImplementedError('must be implemented in subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented in subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented in subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented in subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented in subclass')

    def is_root(self, p):
        return self.root()==p

    def is_leaf(self, p):
        return self.num_children(p) ==0

    def is_empty(self):
        return len(self)==0

    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))
        
class BinaryTree_List(Tree):

    def __init__(self):
        self.container = []

    def __len__(self):
        return len(self.container)

    def element(self,p):
        return self.container[p]
    
    def add_root(self,element):
        #check first if root exists
        if len(self)>0:
            raise ValueError('Root element does not exists')
        self.container.append(element)

    def root(self):
        return 0
    
    def left(self,p):
        #check if left_ptr index < len(self)
        #check if self.contiainer[left_ptr] is not None
        left_ptr = (2*p)+1
        if left_ptr < len(self):
            if (self.container[left_ptr] == None):
                raise ValueError('Left element does not exists')
        return left_ptr
        
    def set_left(self, p, e):
        #check if self.container[left_ptr] already exists
        left_ptr = (2*p)+1
        if len(self) <= left_ptr:
            while (left_ptr - len(self))>= 0:
                self.container.append(None)
            self.container[left_ptr]=e
        elif self.container[left_ptr] == None:
            self.container[left_ptr]=e
        else:
            raise ValueError('Left element already exists') 
        return left_ptr

    def right(self,p):
        #check if right exists
        right_ptr = (2*p)+2
        if right_ptr < len(self):
            if self.container[right_ptr] == None:
                raise ValueError('Right element does not exists')
        return right_ptr

    def set_right(self, p, e):
        right_ptr = (2*p)+2
        if len(self) <= right_ptr:
            while (right_ptr - len(self))>=0:
                self.container.append(None)
            self.container[right_ptr]=e
        elif self.container[right_ptr] == None:
            self.container[right_ptr]=e
        else:
            raise ValueError('Right element already exists') 
        return right_ptr

    def parent(self,p):
        #check if p is left or right node
        if p%2 ==0: #right
            return int((p-2)/2)
        if p%2 ==1: #left
            return int((p-1)/2)

    def num_children(self,p):
        num_children=0
        right_ptr=(2*p)+2
        left_ptr=(2*p)+1
        if (right_ptr < len(self)) and (self.container[right_ptr] is not None):
            num_children+=1
        if (left_ptr < len(self)) and (self.container[left_ptr] is not None):
            num_children+=1
        return num_children
        
    def children(self,p):
        children_ptr=[]
        right_ptr = (2*p)+2
        left_ptr=(2*p)+1
        if (left_ptr < len(self)) and (self.container[left_ptr] is not None):
            children_ptr.append(left_ptr)
        if (right_ptr < len(self)) and (self.container[right_ptr] is not None):
            children_ptr.append(right_ptr)
        return children_ptr      

def PreorderTraverse(L,p):

    print(L.element(p))
    for i in L.children(p):
        PreorderTraverse(L,i)
    return 0

def PostorderTraverse(L,p):
    for i in L.children(p):
        PostorderTraverse(L,i)
    print(L.element(p))
    return 0

class Queue(object):

    def __init__(self):
        self.array=[]

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self)==0

    def enqueue(self,i):
        self.array.append(i)

    def dequeue(self):
        return self.array.pop(0)
    
def BreadthFirst(L):

    Q=Queue()
    Q.enqueue(L.root())

    while not(Q.is_empty()):
        p=Q.dequeue()
        print(L.element(p))
        for i in L.children(p):
            Q.enqueue(i)
        
if __name__ == '__main__':
    L=BinaryTree_List()
    L.add_root(10)
    a=L.root()
    b=L.set_left(a,6)
    c=L.set_right(a,4)
    d=L.set_left(b,3)
    e=L.set_left(c,3)
    f=L.set_right(c,1)

    #node a = 10
    #node b = 6
    #node c = 4
    #node d = 3
    #node e = 3
    #node f = 1
    
    PreorderTraverse(L, L.root())
    PostorderTraverse(L, L.root())
    
class BinaryTree(object):

    class Node(object):

        def __init__ (self, left_node, right_node, parent_node, element):
            self.left_node = left_node
            self.right_node = right_node
            self.parent_node = parent_node
            self.element = element

        def get_parent(self):
            if self.parent_node is not None:
                return self.parent_node.element

        def get_left(self):
            return self.left_node.element

        def get_right(self):
            return self.right_node.element

        def get_element(self):
            return self.element

        def set_left(self, new_left):
            self.left_node = new_left

        def set_right(self, new_right):
            self.right_node = new_right    

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root(self):
        next_node = self.root
        return next_node.get_element()
    
    def add_root(self,element):
        self.root = self.Node(0, 0, 0, element)
        self.size = 1

    def left(self, current_node): #for traversal
        next_node = current_node.left_node
        return next_node
    
    def add_left(self, current_node, element):
        if current_node.get_left() is not None: raise ValueError('Left element exists')
        new_node = Node(None, None, current_node, element)
        current_node.set_left(new_node)
        self.size +=1

    def right(self, current_node):
        next_node = current_node.right_node
        return next_node

    def add_right(self, current_node, element):
        if current_node.get_right() is not None: raise ValueError('Right element exisists')
        new_node = Node(None,None, current_node, element)
        current_node.set_right(new_node)
        self.size+=1


    def parent(self, current_node):
        next_node = current_node.parent_node
        return next_node


        
