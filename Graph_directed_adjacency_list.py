class Edge(object):
    
    def __init__(self, start_vertex, end_vertex, weight=0):
        self.points=(start_vertex, end_vertex)
        self.weight = weight
        start_vertex.add_neighbor(end_vertex, weight)

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
        return str(self.points[0])+ ":" + str(self.points[1]) + ":" + str(self.weight)

class Vertex(object):

    def __init__(self, node):
        self.node = node
        self.neighbor = {}
        self.status = "unvisited"
        self.predecessor = None
        self.step = 0
        
    def __str__(self):
        return str(self.node) + ":" + str(self.predecessor) +":" + str(self.step)

    def add_neighbor(self, new_node, weight=0):
        if isinstance(new_node, Vertex) and new_node.node not in self.neighbor.keys():
            self.neighbor[new_node] = weight
            return True
        else:
            return False

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
            
    def draw_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex in self.vertices and end_vertex in self.vertices and isinstance(start_vertex, Vertex) and isinstance(end_vertex, Vertex):
            start_vertex.add_neighbor(end_vertex, weight)
            self.edges.append(Edge(start_vertex,end_vertex, weight))
            return True
        else:
            return False


    def clear_status(self):
        for i in self.vertices:
            i.step = 999
            i.predecessor = None

    def bellman_ford(self, source):

        self.clear_status()
        for node in source.neighbor.keys():
            node.predecessor = source
            node.step = source.neighbor[node]

        found_vertices=[]
        for i in range(len(self)):
            for node in self.vertices:
                if node.predecessor is not None and node.step != 999 and node not in found_vertices:
                    found_vertices.append(node)
            
            for start_node in found_vertices:
                #end_node = start_node.neighbor.keys()
                for end_node in start_node.neighbor.keys():
                    current_step = start_node.step + start_node.neighbor[end_node]
                    if current_step < end_node.step:
                        end_node.step = current_step
                        end_node.predecessor = start_node


if __name__ == "__main__":
    a=Vertex('A')
    b=Vertex('B')
    c=Vertex('C')
    d=Vertex('D')
    s=Vertex('S')
    g=Graph()
    g.add_vertex(a)
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.add_vertex(s)
    g.draw_edge(s,a)
    g.draw_edge(a,b,2)
    g.draw_edge(a,c,1)
    g.draw_edge(a,d,5)
    g.draw_edge(b,c,4)
    g.draw_edge(c,d,2)
    g.bellman_ford(s)
