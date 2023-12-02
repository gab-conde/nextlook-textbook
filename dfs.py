def dfs(graph, source):  # takes in adjacency list (dict of vertex:list of adjacent vertices) and source vertex

    # list of visited vertices
    visited = []
    visited.append(source)

    # stack of vertices being visited
    stack = []
    stack.append(source)

    # while the stack is not empty, pop the last item and add any of its adjacent vertices to the stack
    # (given that they haven't already been visited)
    while stack:
        source = stack.pop()
        for i in graph[source]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
