def InsertionSort(L):
    #arrange from maximum to minimum
    for index in range(len(L)):
        if index>0:
            cursor=index
            while cursor>=1:
                current_element=L[cursor]
                previous_element=L[cursor-1]
                if current_element > previous_element:
                    L.insert(cursor-1, L.pop(cursor))
                cursor-=1

class Node(object):

    def __init__(self, element, next_node):
        self.element = element
        self.next_node = next_node
        
if __name__ == '__main__':
    L=[None,None]
    L.insert(1,Node(1,L[len(L)-1]))
    L.insert(2,Node(2,L[len(L)-2]))
    for i in L:
        if i is not None:
            print(i.element)
    
