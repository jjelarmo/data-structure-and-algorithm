class Vertex(object):

    def __init__(self, node):
        self.node = node
        self.neighbor = {}
        self.status = "unvisited"
        self.step = 0
        
    def __str__(self):
        return str(self.node) + ":" + self.status

    def add_neighbor(self, new_node, weight=0):
        if isinstance(new_node, Vertex) and new_node.node not in self.neighbor.keys():
            self.neighbor[new_node] = weight
            return True
        else:
            return False

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
    
class Edge(object):
    
    def __init__(self, vertex1, vertex2, weight=0):
        self.points={vertex1, vertex2}
        self.weight = weight
        vertex1.add_neighbor(vertex2, weight)
        vertex2.add_neighbor(vertex1, weight)

    def __lt__(self, others):
        return self.weight < others.weight

    def __contains__(self, vertex):
        return vertex in self.points

    def __eq__(self, others):
        if self.points == others.points and self.weight == others.weight:
            return True
        else:
            return False

    def __str__(self):
        vertex1, vertex2 = list(self.points)
        return str(vertex1)+ ":" + str(vertex2) + ":" + str(self.weight)
    
class MinHeap(object):

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

    def add(self, edge):
        self.data.append(edge)
        self.upheap(len(self.data)-1)

    def remove_min(self):
        self.swap(0, len(self.data)-1)
        min_node = self.data.pop()
        self.downheap(0)
        return min_node
        
class Graph(object):

    def __init__(self):
        self.vertices = []
        self.edges = []

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, class_obj):
        if isinstance(class_obj, Vertex):
            if class_obj in self.vertices:
                return True
            else:
                return False
        if isinstance(class_obj, Edge):
            if class_obj in self.edges:
                return True
            else:
                return False

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices.append(vertex)
            return True
        else:
            return False
        
    def add_edge(self, edge):
        if isinstance(edge, Edge):
            self.edges.append(edge)
            vertex1, vertex2 = list(edge.points)
            if vertex1 in self.vertices:
                pass
            else:
                self.vertices.append(vertex1)
            if vertex2 in self.vertices:
                pass
            else:
                self.vertices.append(vertex2)
            
    def draw_edge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.vertices and vertex2 in self.vertices and isinstance(vertex1, Vertex) and isinstance(vertex2, Vertex):
            vertex1.add_neighbor(vertex2, weight)
            vertex2.add_neighbor(vertex1, weight)
            self.edges.append(Edge(vertex1,vertex2, weight))
            return True
        else:
            return False

    def djikstra(self, source):
        prev_step={}
        q=Queue()
        self.clear_status()
        if source in self:
            source.status = "found"
            q.enqueue(source)
            prev_step[source]=(None,0)
        while not q.is_empty():
            current_node = q.dequeue()
            if current_node.status == "found":
                for next_node in current_node.neighbor.keys():
                    if next_node.status == "unvisited":
                        next_node.status = "found"
                        q.enqueue(next_node)
                        next_node.step = current_node.step + current_node.neighbor[next_node]
                        
                    if next_node in prev_step.keys():
                        if next_node.step < prev_step[next_node][1]:
                            prev_step[next_node] = (current_node, next_node.step)
                    else:
                        prev_step[next_node]=(current_node, next_node.step)
                        
            current_node.status="visited"

        for keys in prev_step.keys():
            print(str(keys)+ " : " + str(prev_step[keys][0]) + " " +str(prev_step[keys][1]) )
        return
    
    def bfsearch(self, start_node):    
        q = Queue()
        if start_node in self:
            start_node.status = "found"
            q.enqueue(start_node)
        while not q.is_empty():
            current_node = q.dequeue()
            if current_node.status == "found":
                for next_node in current_node.neighbor.keys():
                    if next_node.status == "unvisited":
                        next_node.status = "found"
                        q.enqueue(next_node)
            current_node.status = "visited"
            print(current_node)
        return

    def clear_status(self):
        for i in self.vertices:
            i.status = "unvisited"
            i.step = 0
            
    def dfsearch(self, start_node):
        start_node.status = "found"
        for next_node in start_node.neighbor.keys():
            if next_node.status == "unvisited":
                self.dfsearch(next_node)
        start_node.status = "visited"
        print(start_node)
        return

def prim_mst(input_graph):
    mst = Graph()
    
    #find minimum edge as starting point
    heap_edge = MinHeap()
    for edge in input_graph.edges:
        heap_edge.add(edge)
    start_edge = heap_edge.remove_min()
    mst.add_edge(start_edge)
    del heap_edge

    while set(mst.vertices) != set(input_graph.vertices):
        outgoing_vertices = [vertex for vertex in input_graph.vertices if vertex not in mst.vertices]
        remaining_edges = [edge for edge in input_graph.edges if edge not in mst.edges]
        heap_edge = MinHeap()
        for edge in remaining_edges:
            heap_edge.add(edge)
        new_edge = heap_edge.remove_min()
        vertex1, vertex2= list(new_edge.points)
        #check that at least one from vertex1, vertex2 in outgoing_vertices
        #keep searching if both vertex1, vertex2 not in outgoing_vertices
        '''if vertex1 in outgoing_vertices or vertex2 in outgoing_vertices:
            mst.add_edge(new_edge)
        else:
            while vertex1 not in outgoing_vertices and vertex2 not in outgoing_vertices:
                new_edge = heap_edge.remove_min()
                vertex1, vertex2 = list(new_edge.points)
            mst.add_edge(new_edge)
        '''
        while vertex1 not in outgoing_vertices and vertex2 not in outgoing_vertices:
            new_edge = heap_edge.remove_min()
            vertex1, vertex2 = list(new_edge.points)
        mst.add_edge(new_edge)
        del heap_edge
    return mst
#Notes 3/2
#Prim Minimum spanning tree algorithm
#1. Vertex class - no concern
#2. Queue class - no concern
#3. Edge class - does not mutate existing Vertex objects
#4. MinHeap class - ability to store Edge objects; property dependent on Edge object weights
#5. Graph class
#   - added edges list; must contain same elements with vertices list
#   - added add_edge function; does not mutate Vertex objects
#6. Function Prim_mst
#   - find minimum edge as the starting edge in mst; use heap structure
#   - compare set vertices
#   - create outgoing_vertices using list comprehension
#   - create remaining_edges using list comprehension

if __name__ == "__main__":
    a=Vertex('A')
    b=Vertex('B')
    c=Vertex('C')
    d=Vertex('D')
    g=Graph()
    g.add_vertex(a)
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.draw_edge(a,b,2)
    g.draw_edge(a,c,4)
    g.draw_edge(a,d,1)
    g.draw_edge(b,c,5)
    g.draw_edge(c,d,3)
    #test case 1: shortest path using Djikstra
    g.djikstra(a)

    #testcase 2: minimum spanning tree using Prim MST
    h=prim_mst(g)
    print(h.edges[0])
    print(h.edges[1])
    print(h.edges[2])
    
        
    
