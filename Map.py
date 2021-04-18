#define Map Abstract Data Type class functionality
#__getitem__ for query; M.get(k, d=None)
#__setitem__ for modify; M.setdefault(k, d=None)
#__delitem__ for deletion
#__len__
#__iter__
#M.pop(k, d=None)

#using try statements

#hash codes are directly computed using python library function
#compression function MAD method ((ai+b)mod p]mode N
#N is the size of the bucket array
#p is a prime number
#a and b are integers within the interval [0, p-1] 

#n/N wherein n is the number of items insinde the bucket array of capacity N
#maintain n/N < 0.5 to create a Hash table with no possible collisions
#collision handling by inserting UnsortedTableMap on affected index

#Sorted Map using hash tables
#Inexact searches using binary search

#unit testing of UnsortedTableMap
#resize method for HashTable 



import random

class MapBase(object):

    class Item(object):

        def __init__(self,k,v):
            self.key=k
            self.value=v

        def __eq__(self,other):
            return self.key == other.key

        def __ne__(self, other):
            return not(self == other)

        def __lt__(self, other):
            return self.key < other.key

        def __str__(self):
            return "("+ str(self.key) + "," + str(self.value) + ")"
        
class UnsortedTableMap(MapBase):   

    def __init__(self):
        self.table=[]

    def __getitem__(self,k):
        for item in self.table:
            if k == item.key:
                return item.value

    def __setitem__(self,k,v):
        for item in self.table:
            if k == item.key:
                item.value=v
                return 
        self.table.append(self.Item(k,v))

    def __delitem__(self,k):

        for j in range(len(self.table)):
            if k == self.table[j].key:
                self.table.pop[j]
                return

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        for item in self.table:
            yield item

#if __name__ == "__main__":
#    M=UnsortedTableMap()
#    M['K']=2
#    M['L']=3
#    for item in M:
#        print (item)

#    store_data= []
#    for item in M:
#        store_data.append(item)

#    for item in store_data:
#      print (item)
    
class HashTable(UnsortedTableMap):

    #((ai+b)mod p]mode N

    def __init__(self, cap=11, p=109345121):

        self.table=cap*[None]
        self.n=0
        self.prime=p
        self.scale= 1+ random.randrange(p-1)
        self.shift=random.randrange(p)

    def hash_function(self,k):
        return (hash(k)*self.scale + self.shift) % self.prime % len(self.table)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        index = self.hash_function(k)
        return self.table[index][k]

    def __setitem__(self,k,v):
        index = self.hash_function(k)
        if self.table[index] is None:
            self.table[index] = UnsortedTableMap()
        old_size = len(self.table[index])
        self.table[index][k] = v
        if len(self.table[index]) > old_size:
            self.n+=1

        if( self.n > (len(self.table) // 2)):
            self.resize( 2*len(self.table))     #how does the location of key-value pair change after resize
                                                #retriving the correct key-value pair after resize
            
    def __delitem__(self,k):
        index = self.hash_function(k)
        del self.table[index][k]
        self.n -=1


    def __iter__(self):
        for index in range(len(self.table)):
            for item in self.table[index]:
                yield item

    def resize(self, c):
       store_data = []
       for item in self.table:
           store_data.append(item)                      #1. items() method is not defined #2. structure and order of key-value pair when converted to list
       self.table=c*[None]
       for item in store_data:
           self[item.key]=item.value                    #__setitem__ method implementation




class SortedMap(MapBase):

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def coarse_find(self,target, low_l, high_l):

        if int(target) >= self.table[int(high_l)].key:
            return high_l + 1
        if int(target) <= self.table[int(low_l).key]:
            return low_l - 1

        mid= (low_l + high_l)//2
        
        if mid >= high_l:
            return mid + 1
        if mid <= low_l:
            return mid - 1

        elif low_l < mid and mid < high_l :
            if target >= self.table[mid].key:
                return self.coarse_find(target, mid+1 , high_l)
            else:
                return self.coarse_find(target, low_l, mid-1)

    def find_index(self,target):
        i = self.coarse_find(target, 0, len(self)-1)
        if target >= self.table[i-2].key:
            return i-2
        if target >= self.table[i-1].key:
            return i-1
        if target >=self.table[i].key:
            return i
        if target >=self.table[i+1].key:
            return i+1
        if target >=self.table[i+2].key:
            return i+2

    def __setitem__(self,k,v):

        #setitem method cases:
        #self.table has no elements
        #new element Item is at the end of the array
        #new element key is existing
        #new element is not existing
        if len(self)==0:
            self.table.append(self.Item(k,v))
        else:
            index = self.find_index(k)
            if index > len(self.table):
                self.table.append(self.Item(k,v))
            elif self.table[index].key == k:
                self.table[index].value = v
            else:
                self.table.insert(index, self.Item(k,v))

    def __getitem__(self,k):

        index= self.find_index(int(k))
        if len(self) != 0 and index < len(self):
            return self.table[index].value


    def __iter__(self):
       for i in self.table:
           yield i

    def find_min(self):
        if len(self) > 0:
            return self.table[0]

    def find_max(self):
        if len(self)>0:
            return self.table[-1]


               
if __name__ == "__main__":
    M=SortedMap()
    M[4]='ek'
    M[5]='ke'
    for i in M:
        print(i)
    
   

        





        


        
