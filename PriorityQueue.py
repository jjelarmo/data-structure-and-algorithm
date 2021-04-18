class Item(object):

    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __lt__(self, other):
        return self.key < other.key

    def is_empty(self):
        return len(self)==0

#create PositionalList using Array implementation with same methods from PositionalList using DoubleLinkedList implementation
class PositionalList(object):

    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self)==0

    def first(self):
        return self.data[0]

    def after(self, node):
        next_node=self.data.index(node)+1
        return self.data[next_node]

    def last(self):
        return self.data[-1]

    def add_first(self, node):
        self.data.insert(0, node)

    def add_last(self, node):
        self.data.insert(-1, node)

    def add_after(self, node, current_node):
        next_ptr = self.data.index(current_node)
        self.data.insert(next_ptr, node)

    def add_before(self, node, current_node):
        prev_ptr = self.data.index(current_node)
        self.data.insert(prev_ptr, node)
        
    def __iter__(self):
        for i in self.data:
            yield i

class UnsortedPriorityQueue(object):

    def __init__(self):
        self.data=PositionalList()

    def __len__(self):
        return len(self.data)

    def add(self,k,v):
        new_node = Item(k,v)
        self.data.add_first(new_node)

    def find_min(self):
        min_value = self.data.first()
        for i in self.data:
            if i.key < min_value.key:
                min_value =i
        return min_value.value

class SortedPriorityQueue(object):

    def __init__(self):
        self.data=PositionalList()

    def __len__(self):
        return len(self.data)

    def add(self,k,v):
        new_node=Item(k,v)

        if len(self.data)==0:
            self.data.add_first(new_node)
        else:
            for i in self.data:
              if new_node < i:
                  self.data.add_before(new_node, i)
                  break

    def find_min(self):
        return self.data.first().value
            
class HeapPriorityQueue(object):

    def parent(self,j):
        return (j-1)//2

    def left(self,j):
        return 2*j+1

    def right(self,j):
        return 2*j+2

    def has_left(self,j):
        return self.left(j) < len(self.data)

    def has_right(self,j):
        return self.right(j) < len(self.data)

    def swap(self,i,j):
        self.data[i] , self.data[j] = self.data[j], self.data[i]

    def upheap(self,j):
        parent = self.parent(j)
        if (j>0) and (j <= (len(self.data)-1)):
            if self.data[j] < self.data[parent]:
                self.swap(j, parent)
            self.upheap(parent)
        
    def downheap(self,j):
        if self.has_left(j):
            left=self.left(j)
            small_child=left

            if self.has_right(j):
                right=self.right(j)
                if self.data[right] < self.data[small_child]:
                    small_child=right
                    
            if self.data[small_child] < self.data[j]:
                self.swap(small_child, j)
                return self.downheap(small_child)

    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def add(self, k, value):
        new_node = Item(k, value)
        self.data.append(new_node)
        self.upheap(len(self.data)-1)

    def remove_min(self):
        self.swap(0, len(self.data)-1)
        min_node = self.data.pop()
        self.downheap(0)
        return (min_node.key, min_node.value)

    def __iter__(self):
        for i in self.data:
            yield (i.key, i.value)

class Queue(object):

    def __init__(self):
        self.data=[]

    def push(self,d):
        self.data.append(d)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for i in self.data:
            yield i.value



if __name__ == '__main__':

    L=HeapPriorityQueue()
    
    L.add(3, 'o')
    L.add(5, 'c')
    L.add(2, 'e')
    L.add(7, 't')
    L.add(4, 'w')
    L.add(6, 'a')
    L.add(1, 'm')
    
    #for i in L:
    #    print(i)

    #L.remove_min()
    
    Q=Queue()
    while len(L) is not 0:
        d=L.remove_min()
        new_node=Item(d[0],d[1])
        Q.push(new_node)
        
    for i in Q:
        print(i)
        








    
