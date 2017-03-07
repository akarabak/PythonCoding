from collections import defaultdict

graph = {'a': ['e'], 'c': ['b'], 'b': ['a'], 'd': ['a','e'], 'e': []}
graph2 = {'a': ['b'], 'b': ['c'], 'c': ['a']}


def dfs(node, graph, visited, order, path):
    for v in graph[node]:
        if v in path:
            ret = list(path)
            ret.append(v)
            return ret
        path.add(v)
        if v not in visited:
            visited.add(v)
            ret = dfs(v, graph, visited, order, path)
            if len(ret) != 0:
                return ret
        path.remove(v)
    order.append(node)
    return []


def topological_sort(graph):
    visited = set()
    order = []
    for node in graph:
        if node not in visited:
            visited.add(node)
            path = set(node)
            cycle = dfs(node, graph, visited, order, path)
            if len(cycle) != 0:
                print('cycle', cycle)
                return
    print(list(reversed(order)))


def topological_sort2(graph):
    # stores incoming edges for each vertex
    count = defaultdict(int)
    for v in graph:
        if v not in count:
            count[v] = 0
        for e in graph[v]:
            count[e] += 1

    # stores vertices with no incoming edges
    ready = [v for v in count if count[v] == 0]

    output = []
    while len(ready) != 0:
        value = ready.pop()
        output.append(value)
        for e in graph[value]:
            count[e] -= 1
            if count[e] == 0:
                ready.append(e)
    print(output)



if __name__ == '__main__':
    topological_sort(graph)
    topological_sort(graph2)
    topological_sort2(graph)