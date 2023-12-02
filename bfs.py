def bfs(graph, source):  # takes in adjacency list (dict of vertex:list of adjacent vertices) and source vertex

    # list of visited vertices
    visited = []
    visited.append(source)

    # queue of vertices being visited
    queue = []
    queue.append(source)

    # while the queue is not empty, pop the first item and add any of its adjacent vertices to the queue
    # (given that they haven't already been visited)
    while queue:
        source = queue.pop(0)
        for i in graph[source]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
