"""Finds the closer node from the start node"""
def find_closer_node(distances):
    closer_distance = float("inf")
    closer_node = None

    for node in distances:
        distance = distances[node]
        if distance < closer_distance and node not in processed:
            closer_distance = distance
            closer_node = node
    return closer_node

processed = []

def dijkstra(graph):
    node = find_closer_node(distances)
    while node is not None:
        distance = distances[node]
        neighbor = graph[node]
        for n in neighbor.keys():
            new_distance = distance + neighbor[n]
            if distances[n] > new_distance:
                distances[n] = new_distance
                parents[n] = node
        processed.append(node)
        node = find_closer_node(distances)
    return parents

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

infinity = float("inf")
distances = {}
distances["a"] = 6
distances["b"] = 2
distances["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

print(dijkstra(graph))