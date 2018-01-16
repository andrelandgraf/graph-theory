import itertools


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    # TODO 3 description
    def is_coherent(self):
        # graphs with no vertices / only one are always coherent
        if len(self.vertices) <= 1:
            return True
        # graphs with no edges but vertices can never be coherent
        if len(self.edges) == 0:
            return False

        # get next v from V, check for all possible ways in dive in recursively
        # important: visited is used by reference so that every recrusive helper can add information
        def is_coherent_helper(i):
            # TODO 1 index function throws exception if element not in list, should we throw exception if i < 0?
            # get next v and mark index of v as visited
            v = self.vertices[i]
            visited[i] = True
            # Base Case: if all vertices have been visited, we can return true
            if all(v is True for v in visited):
                return True
            # loop through all edges and find those who have v as one side
            for e in self.edges:
                # check if v is on one end of this edge and check if the other end has not been visited yet
                # we do not want to revisit the same nodes again, this includes ignoring slings like (a,a,)
                if v == e[0] and not visited[self.vertices.index(e[1])]:
                    # next call using the neighbour node
                    if is_coherent_helper(self.vertices.index(e[1])):
                        return True
                # else if check if v is the other end
                elif v == e[1] and not visited[self.vertices.index(e[1])]:
                    # next call using the neighbour node
                    if is_coherent_helper(self.vertices.index(e[0])):
                        return True
            # if no edges neighbour returned true -> the graph is not coherent
            return False
        # init visited array and start recrusive helper with index = 0
        visited = list(itertools.repeat(False, len(self.vertices)))
        return is_coherent_helper(0)

    # simple graphs do not have slings
    def is_simple(self):
        if any(e[0] == e[1] for e in self.edges):
            return False
        return True

    # TODO 2 def is_tree(self):
    # TODO 3 description
    # TODO ERR I am mixing non directional and directional logic rn... :/ what do I want?
    def has_circle(self):
        # graphs with no/one/two vertices cannot contain circle
        if len(self.vertices) <= 2:
            return False
        # graphs with no/one/two edges but vertices can never contain circle
        if len(self.edges) <= 2:
            return False

        def has_circle_helper(i):
            # TODO 1 index function throws exception if element not in list, should we throw exception if i < 0?
            # get next w and mark index of w as visited
            w = self.vertices[i]
            visited[i] = True
            # loop through all edges and find those who have w as one side
            for e in self.edges:
                # TODO 9 visited muss wohl doch wie bei coherent eingesetzt werden,
                # TODO 9 basisfall nur wenn ich wieder bei v bin...
                # Base Case: if we find v as a neighbour of w, we might have found a circle
                #            slings (w,w,) with w = v do not count as circles
                if (w == e[0] and v == e[1]) or (v == e[0] and w == e[1]) and not (w == v):
                    count = 0
                    for boolean in visited:
                        if boolean:
                            count += count
                    # if at least 3 nodes have been visited, we have found a circle
                    if count >= 3:
                        return True
                # check if w is on one end of this edge and check if the other end has not been visited yet
                # we do not want to revisit the same nodes again, this includes ignoring slings like (a,a,0)
                if w == e[0] and not visited[self.vertices.index(e[1])]:
                    # next call using the neighbour node
                    if has_circle_helper(self.vertices.index(e[1])):
                        return True
                # else if check if w is the other end
                elif w == e[1] and not visited[self.vertices.index(e[0])]:
                    # next call using the neighbour node
                    if has_circle_helper(self.vertices.index(e[0])):
                        return True
            # if no edges neighbour returned true -> the graph is not coherent
            return False

        # iterate through all vertices
        for v in self.vertices:
            # init visited array and start recrusive helper
            # important: reset list visited in every iteration
            visited = list(itertools.repeat(False, len(self.vertices)))
            if has_circle_helper(self.vertices.index(v)):
                return True
        return False


g = Graph(["a", "b", "c", "d", "e", "f"],[("a", "b", 0), ("a", "c", 0), ("b", "d", 0),
                                          ("b", "e", 0), ("e", "f", 0), ("f", "a", 0)])
print("is coherent: {}".format(g.is_coherent()))
print("is simple: {}".format(g.is_simple()))
print("has circle: {}".format(g.has_circle()))