import random


class Graph(object):
    """
        A class to fill a graph and do its operations

    """

    def __init__(self, connections = None, directed = False):
        self._graph = dict()
        self._directed = directed
        if connections is not None:
            self.add_connections(connections)
        else:
            return

    def add_connections(self, connections):
        """ Add connections to graph """
        node = connections[0]
        self._graph[node] = connections[1:]

    def min_cut(self):
        aux_list = list()

        while len(self._graph) > 2:
            """Choose random edge"""
            node_kept = random.sample(self._graph.keys(), 1)
            node_kept = node_kept[0]
            node_removed = random.sample(self._graph[node_kept], 1)
            node_removed = node_removed[0]

            """remove node_removed from node_kept"""
            aux_list.clear()
            for element in self._graph[node_kept]:
                if element != node_removed:
                    index = self._graph[node_kept].index(element)
                    aux_list.append(self._graph[node_kept][index])
            self._graph[node_kept].clear()
            self._graph[node_kept] = list(aux_list)

            """copy all elements from node_remove to node_kept and erase it"""
            for element in self._graph[node_removed]:
                if element != node_kept:
                    self._graph[node_kept].append(element)
            self._graph.pop(node_removed)

            """replace every node_removed for node_kept in all the graph"""
            for node in self._graph.keys():
                if node != node_kept:
                    for element in self._graph[node]:
                        if element == node_removed:
                            index = self._graph[node].index(element)
                            self._graph[node].remove(node_removed)
                            self._graph[node].insert(index, node_kept)

        return len(self._graph[node_kept])