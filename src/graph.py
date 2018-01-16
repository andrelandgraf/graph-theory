import itertools


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def is_coherent(self):
        # graph with no vertices / only one are always coherent
        if len(self.vertices) <= 1:
            return True
        # graph with no edges but vertices can never be coherent
        if len(self.edges) == 0:
            return False

        # get next v from V, check for all possible ways in dive in recursively
        # important: visited is used by reference so that every recrusive helper can add information
        def is_coherent_helper(i):
            # TODO index function throws exception if element not in list, should we throw exception if i < 0?
            # get next v and mark index of v as visited
            v = self.vertices[i]
            visited[i] = True;
            #TODO
            print("current v: "+v)
            # if all vertices have been visited, we can return true
            if all(v is True for v in visited):
                return True;
            # loop through all edges and find those who have v as one side
            for e in self.edges:
                # check if v is on one end of this edge and check if the other end has not been visited yet
                # we do not want to revisit the same nodes again, this includes ignoring slings as (a,a,0)
                if v == e[0] and not visited[self.vertices.index(e[1])]:
                    # TODO
                    print("using edge: {}".format(e))
                    # next call using the neighbour node
                    if is_coherent_helper(self.vertices.index(e[1])):
                        return True
                # else if check if v is the other end
                elif v == e[1] and not visited[self.vertices.index(e[1])]:
                    # TODO
                    print("using edge: {}".format(e))
                    # next call using the neighbour node
                    if is_coherent_helper(self.vertices.index(e[0])):
                        return True
            # if no edges neighbour returned true -> the graph is not coherent
            return False;
        # init visited array and start recrusive helper with index = 0
        visited = list(itertools.repeat(False, len(self.vertices)))
        return is_coherent_helper(0)

g = Graph(["a", "b", "c", "d", "e", "f"],[("a", "b", 0), ("a", "c", 0), ("b", "d", 0), ("b", "e", 0), ("e", "f", 0)])
print(g.is_coherent())