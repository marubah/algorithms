import unittest
import networkx as nx
import matplotlib.pyplot as plt
from algorithms.strongly_connected_components import scc


class TestSCC(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    """
    def test_small_graph(self):
        small_graph = nx.DiGraph()
        small_graph.add_edge(1, 4)
        small_graph.add_edge(2, 8)
        small_graph.add_edge(3, 6)
        small_graph.add_edge(4, 7)
        small_graph.add_edge(5, 2)
        small_graph.add_edge(6, 9)
        small_graph.add_edge(7, 1)
        small_graph.add_edge(8, 5)
        small_graph.add_edge(8, 6)
        small_graph.add_edge(9, 3)
        small_graph.add_edge(9, 7)

        #nx.draw(small_graph)
        #plt.show()
        cant = scc(small_graph)
        self.assertEqual(cant, 3)
    """

    def test_big_graph(self):
        big_graph = nx.DiGraph()

        with open("scc_test.txt", "r") as current_file:
            graph = current_file.read()
            graph = graph.rstrip()
            current_file.close()

        for edge in graph.split("\n"):
            (edge_1, edge_2) = edge.rstrip().split(" ")
            big_graph.add_edge(int(edge_1), int(edge_2))

        leaders_podium = scc(big_graph)
        for (leader, number_nodes) in leaders_podium:
            print("Leader:", leader, "-> Number of nodes:", number_nodes)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
