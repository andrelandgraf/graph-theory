import unittest
from graph import Graph


# see https://docs.python.org/3/library/unittest.html
class GraphTestCase(unittest.TestCase):

    @staticmethod
    def get_empty_graph():
        return Graph([], [])

    @staticmethod
    def get_simple_single_node_graph():
        return Graph(["a"], [])

    @staticmethod
    def get_single_node_graph():
        return Graph(["a"], [("a", "a", 0)])

    @staticmethod
    def get_no_edge_graph():
        return Graph(["a", "b", "c"], [])

    @staticmethod
    def get_simple_connected_graph():
        return Graph(["a", "b", "c"], [("a", "b", 0), ("b", "c", 0), ("c", "a", 0)])

    @staticmethod
    def get_simple_circle_graph():
        return Graph(["a", "b", "c", "d", "e", "f"], [("a", "b", 0), ("a", "c", 0), ("b", "d", 0),
                                               ("b", "e", 0), ("e", "f", 0), ("d", "e", 0), ("e", "c", 0)])

    @staticmethod
    def get_weird_tree_graph():
        return Graph(["a", "b", "c", "d", "e", "f"], [("a", "b", 0), ("a", "c", 0), ("b", "d", 0),
                                               ("b", "e", 0), ("e", "f", 0)])

    @staticmethod
    def get_loose_complex_graph():
        return Graph(["a", "b", "c", "d", "e", "f", "g"], [("a", "a", 0), ("b", "a", 0),
                                                           ("f", "a", 0), ("f", "e", 0), ("d", "e", 0),
                                                           ("c", "d", 0), ("c", "b", 0)])


    @staticmethod
    def get_bidirectional_graph():
        return Graph(["a", "b", "c", "d"],
              [("a", "b", 0), ("b", "a", 0), ("a", "c", 0), ("c", "a", 0), ("b", "d", 0), ("d", "b", 0)])

    def test_is_coherent(self):
        self.assertTrue(self.get_empty_graph().is_coherent())
        self.assertTrue(self.get_simple_single_node_graph().is_coherent())
        self.assertTrue(self.get_single_node_graph().is_coherent())
        self.assertFalse(self.get_no_edge_graph().is_coherent())
        self.assertTrue(self.get_simple_connected_graph().is_coherent())
        self.assertTrue(self.get_simple_circle_graph().is_coherent())
        self.assertTrue(self.get_weird_tree_graph().is_coherent())
        self.assertFalse(self.get_loose_complex_graph().is_coherent())
        self.assertTrue(self.get_bidirectional_graph().is_coherent())

    def test_is_strong_coherent(self):
        self.assertTrue(self.get_empty_graph().is_strong_coherent())
        self.assertTrue(self.get_simple_single_node_graph().is_strong_coherent())
        self.assertTrue(self.get_single_node_graph().is_strong_coherent())
        self.assertFalse(self.get_no_edge_graph().is_strong_coherent())
        self.assertFalse(self.get_simple_connected_graph().is_strong_coherent())
        self.assertFalse(self.get_simple_circle_graph().is_strong_coherent())
        self.assertFalse(self.get_weird_tree_graph().is_strong_coherent())
        self.assertFalse(self.get_loose_complex_graph().is_strong_coherent())
        self.assertTrue(self.get_bidirectional_graph().is_strong_coherent())


if __name__ == '__main__':
    unittest.main()
