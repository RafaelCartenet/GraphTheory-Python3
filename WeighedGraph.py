from collections import deque

def dijkstra(graph, current, target, start="", visited=set(), dist=dict(), paths=dict()):
    if not visited:
        start = current
        dist[current] = 0
    if current == target:
        return dist[target], get_path_dijkstra(paths, start, target, [])
    for next in get_neighbours(graph, current):
        if next not in visited:
            dist_next = dist.get(next, float('inf'))
            candidate_dist = dist[current] + graph[current][next]
            if candidate_dist < dist_next:
                dist[next] = candidate_dist
                paths[next] = current
    visited.add(current)
    nexts = dict((node, dist.get(node, float('inf'))) for node in graph if node not in visited)
    next = min(nexts, key=nexts.get)
    if dist.get(next, float('inf')) == float('inf'):
        return -1
    return dijkstra(graph, next, target, start, visited, dist, paths)


def get_path_dijkstra(paths, start, current, path):
    if current == start:
        return [start] + path
    return get_path_dijkstra(paths, start, paths[current], [current] + path)


def dfs(graph, current, target, visited=set()):
    if current not in visited:
        visited.add(current)
        if current == target:
            return True
        else:
            nexts = get_neighbours(graph, current)
            return True in [dfs(graph, node, target, visited) for node in nexts]
    return False


def bfs(graph, start, target):
    visited = set()
    next = deque(get_neighbours(graph, start))
    visited.add(start)
    while next:
        current = next.popleft()
        if current == target:
            return True
        else:
            visited.add(current)
            [next.append(node) for node in get_neighbours(graph, current) if node not in visited]
    return False


def add_edge(graph, edge, weight):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        node2 = edge.pop()
    else:
        node2 = node1
    graph[node1][node2] = weight


def add_node(graph, node):
    if node not in graph:
        graph[node] = {}


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


def get_neighbours_edges(graph, node):
    edges = dict()
    if node in graph:
        edges = graph[node]
    return edges


def get_edges(graph):
    edges = []
    for node1 in graph:
        for node2 in graph[node1]:
            edges.append([node1, node2, graph[node1][node2]])
    return edges


def edges_to_graph(edges):
    graph = dict()
    for edge in edges:
        weight = edge.pop()
        node1 = edge.pop()
        if node1 not in graph:
            add_node(graph, node1)
        if edge:
            node2 = edge.pop()
            if node2 not in graph:
                add_node(graph, node2)
        else:
            node2 = node1
        graph[node2][node1] = weight
    return graph


def to_string(graph):
    res = "Graph :\n"
    for k in graph:
        res += str(k) + " : " + str(graph[k]) + "\n"
    return res


G = {'a': {'b': 4, 'c': 2},
     'b': {'a': 4, 'c': 1},
     'c': {'a': 2}}

E = [['A', 'B', 3],
     ['A', 'C', 5],
     ['B', 'C', 6],
     ['B', 'D', 7],
     ['C', 'D', 1],
     ['D', 'C', 2],
     ['E', 'F', 3],
     ['F', 'C', 5]]

print(len(G))

add_edge(G, ['c', 'b'], 10)
add_edge(G, ['a', 'a'], 5)

print(get_neighbours(G, 'c'))
add_node(G, 'z')
print(to_string(G))

H = edges_to_graph(E)
print(to_string(H))

print(bfs(H, 'A', 'F'))

print(dijkstra(H, 'A', 'F'))

print(get_edges(H))
