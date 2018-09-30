import networkx as nx
import operator

time = 0
leader_node = None
order = list()
forward = False

def scc(graph):
    global time
    global leader_node
    global order
    global forward

    size = graph.number_of_nodes()

    for node in graph.nodes():
        graph.node[node]["explored"] = False
        graph.node[node]["finishing_time"] = 0
        graph.node[node]["leader"] = None

    for i in range(size, 0, -1):
        if graph.node[i]["explored"] is False:
            DFS(graph, i)

    for node in graph.nodes():
        graph.node[node]["explored"] = False

    forward = True
    for node in reversed(order):
        if graph.node[node]["explored"] is False:
            leader_node = node
            DFS(graph, node)

    leaders = dict()
    for node in graph.nodes():
        if graph.node[node]["leader"] in leaders.keys():
            leaders[graph.node[node]["leader"]] += 1
        else:
            leaders[graph.node[node]["leader"]] = 1

    leaders_podium = sorted(leaders.items(), key=operator.itemgetter(1))

    return leaders_podium


def DFS(graph, starting_node):
    global time
    global leader_node
    global order
    global forward

    graph.node[starting_node]["explored"] = True

    if forward is True:
        graph.node[starting_node]["leader"] = leader_node
        for neighbor in graph.neighbors(starting_node):
            if graph.node[neighbor]["explored"] is False:
                DFS(graph, neighbor)
    else:
        for back_neighbor in graph.pred[starting_node]:
            if graph.node[back_neighbor]["explored"] is False:
                DFS(graph, back_neighbor)
        time += 1
        graph.node[starting_node]["finishing_time"] = time
        order.append(starting_node)
