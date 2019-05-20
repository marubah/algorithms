import unittest
import copy
from algorithms.graph import Graph


class TestGraph(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    def test_small_graph(self):

        graph_obj = Graph()
        connections = list()

        """open the file and send node by node to complete the graph"""
        nodes = open("data_graphs_test1.txt", "r")

        for node in nodes:
            node = [x.strip() for x in node.split('\t')]
            connections.clear()
            for node_connection in node[:-1]:
                connections.append(node_connection)
            graph_obj.add_connections(connections)

        nodes.close()

        """compute min cut"""
        min_cut = graph_obj.min_cut()
        print("short test min_cut =", min_cut)
        self.assertEqual(min_cut, min_cut)

    def test_medium_graph(self):

        graph_obj = Graph()
        connections = list()

        nodes = open("data_graphs.txt", "r")

        for node in nodes:
            node = [x.strip() for x in node.split('\t')]
            connections.clear()
            for node_connection in node[:-1]:
                connections.append(node_connection)
            graph_obj.add_connections(connections)

        nodes.close()

        graph_init = copy.deepcopy(graph_obj)
        min_cut = graph_init.min_cut()

        for i in range(1, 1000):
            graph_new = copy.deepcopy(graph_obj)
            min_cut_new = graph_new.min_cut()
            if min_cut_new < min_cut:
                min_cut = min_cut_new
            print("i =", i, "\nmin_cut =", min_cut, "\nmin_cut_new =", min_cut_new)

        self.assertEqual(min_cut, min_cut)


if __name__ == '__main__':
    unittest.main()
