class MyLinkedList(object):

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node(None)
        self.tail = self.head
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        
        if index >= self.length:
            return -1
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = self.Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.length==0:
            self.tail = new_node
        self.length +=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = self.Node(val)
        self.tail = new_node
        if self.length==0:
            self.head.next = new_node
        self.length +=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = self.Node(val)
        if index < self.length:
            current_node = self.head.next
            for i in range(self.length - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length +=1
        if index == self.length:
            self.addAtTail(self, val)
            self.length +=1
        if index > self.length:
            return 
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        delete_node = current_node.next
        current_node.next = current_node.next.next
        delete_node.val = None
        delete_node.next = None
        self.length -= 1
