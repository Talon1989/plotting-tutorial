
class Node:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, src: Node, dest: Node):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph:
    def __init__(self):
        self.edges = {}

    def addNode(self, node: Node):
        if node in self.edges:
            raise ValueError('duplicate')
        else:
            self.edges[node] = []

    def addEdge(self, edge: Edge):
        source = edge.getSource()
        dest = edge.getDestination()
        if not (source in self.edges and dest in self.edges):
            raise ValueError('missing nodes')
        else:
            self.edges[source].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]  # omit final new line


def buildCityGraph(graphType):  # Creation
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver',
                 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


def DFS(gr, start, end, path, shortest):  # Depth First Search algorithm
    path = path + [start]
    if start == end:
        return path
    for n in gr.childrenOf(start):
        if n not in path:
            if shortest is None or len(path) < len(shortest):
                shortest = DFS(gr, n, end, path, shortest)
                # if temp is not None:
                #     temp = shortest
    return shortest


g = buildCityGraph(Digraph)
nn = DFS(g, g.getNode('Boston'), g.getNode('Phoenix'), [], None)
if nn is not None:
    for n in nn:
        print(n)


















graph = buildCityGraph(Digraph)













































