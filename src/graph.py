import itertools


# a directional graph
# multiple arrows not supported (ignored)
# see: https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms
# and: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Directed_graph
class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    #TODO good practice? Is empty edges list finite or infinite :P?
    @classmethod
    def is_finite(cls):
        return True

    # coherence means there is a connection to every node of the vertices.
    # the direction of this connection does not matter -> see strong coherence
    # TODO name is connected instead?
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

    # a graph is strong coherent if it is coherent
    # and for every (v, w, 0) in graphs edges, there also exists (w,v,0)
    # TODO name it strong_connected instead?
    def is_strong_coherent(self):
        if self.is_coherent() and self.is_symmetrical():
            return True
        return False

    # TODO is complete

    # a circle is a path of at least three nodes that start and end at the same node
    def has_circle(self):
        # graphs with no/one/two vertices cannot contain circle
        if len(self.vertices) <= 2:
            return False
        # graphs with no/one/two edges but vertices can never contain circle
        if len(self.edges) <= 2:
            return False

        # important: visited is used by reference so that every recrusive helper can add information
        def has_circle_helper(i):
            # TODO 1 index function throws exception if element not in list, should we throw exception if i < 0?
            # get next w and mark index of w as visited
            w = self.vertices[i]
            visited[i] = True
            # loop through all edges and find those who have w as one side
            for e in self.edges:
                # Base Case: if we find v as a neighbour of w, we might have found a circle
                #            slings (w,w,) with w = v do not count as circles
                if (w == e[0] and v == e[1]) and not (w == v):
                    # if at least 3 nodes have been visited, we have found a circle
                    # otherwise this is just a bi directional edge like
                    # ("v","w", 0) and ("w", "v", 0) and that does not count as circle.
                    count = 0
                    for boolean in visited:
                        if boolean:
                            count += 1
                    if count >= 3:
                        return True
                # check if w is on one end of this edge and check if the other end has not been visited yet
                # we do not want to revisit the same nodes again, this includes ignoring slings like (a,a,0)
                if w == e[0] and not visited[self.vertices.index(e[1])]:
                    # next call using the neighbour node
                    if has_circle_helper(self.vertices.index(e[1])):
                        return True
                    # important: delete last hop as it was not helpful in building a the circle
                    visited[self.vertices.index(e[1])] = False
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

    # simple graphs do not have slings / loops
    # (loop: arrows that connect vertices to themselves)
    def is_simple(self):
        if any(e[0] == e[1] for e in self.edges):
            return False
        return True

    # TODO verify
    # TODO description
    def is_reflexive(self):
        # iterate through all verticles
        for v in self.vertices:
            # if edges does not contain the the loop for v, return false
            if all(v != e[0] and v != e[0] for e in self.edges):
                return False
        # otherwise all verticles have a loop
        return True

    # directed graphs where all edges are bidirected
    # (bidirected: for every arrow that belongs to the digraph, the corresponding inversed arrow also belongs to it)
    def is_symmetrical(self):
        # iterate through all edges
        # loop works as follows:
        # if it exists e where no i exists that is the the inversed arrow -> not symmetrical
        # equivalent to if exists e where all i are the inversed arrow -> not symmetrical
        for e in self.edges:
            # if edges does not contain the inversed arrow to e, return false
            if all(e[0] != i[1] or e[1] != i[0] for i in self.edges):
                return False
        # otherwise all edges are bidirected
        return True

    # TODO verify
    # directed graphs where no edge is bidirected and where no loops exist
    def is_asymmetrical(self):
        # if not simple -> a loop exists -> not asymmetrical
        if not self.is_simple():
            return False
        # iterate through all edges
        for e in self.edges:
            # if edges does not contain any inversed arrow to e, return false
            if all(e[0] != i[1] and e[1] != i[0] for i in self.edges):
                return False
        # otherwise all edges are bidirected
        return True

    # TODO is_antisymmetrical

    # TODO is_transitive

    # TODO description
    def get_root(self):
        # TODO implementation
        return None

    # TODO verify
    # trees have a root node from where you can reach every other node, but they do not contain circle
    def is_tree(self):
        if self.is_simple() and not self.has_circle() and not self.get_root() is None:
            return True
        return False

    # TODO get Spannbaum