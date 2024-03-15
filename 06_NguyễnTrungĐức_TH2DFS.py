"""def dfs(graph, current_vertex, visited):
    visited[current_vertex] = True
    for neighbor in graph[current_vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def translate_to_matrix(graph):
    num_vertices = len(graph)
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        visited = [False] * num_vertices
        dfs(graph, i, visited)
        for j in range(num_vertices):
            if j != i and visited[j]:
                adj_matrix[i][j] = 1

    return adj_matrix

# Đồ thị với 10 đỉnh được biểu diễn dưới dạng danh sách kề
graph = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1, 4, 8],
    3: [1, 4, 5, 6],
    4: [1, 2, 3, 5],
    5: [3, 4, 6, 7],
    6: [3, 5, 7, 8],
    7: [5, 6, 8, 9],
    8: [2, 6, 7, 9],
    9: [7, 8]
}

# Chuyển đồ thị thành ma trận kề
adj_matrix = translate_to_matrix(graph)

# In ma trận kề
for row in adj_matrix:
    print(row)

    """
def dfs(graph, current_vertex, destination, visited, path, shortest_path):
    visited[current_vertex] = True
    path.append(current_vertex)

    if current_vertex == destination:
        shortest_path[:] = path[:]
    else:
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                dfs(graph, neighbor, destination, visited, path, shortest_path)

    path.pop()
    visited[current_vertex] = False

def find_shortest_path(graph, source, destination):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    path = []
    shortest_path = []

    dfs(graph, source, destination, visited, path, shortest_path)
    return shortest_path

# Đồ thị với 10 đỉnh được biểu diễn dưới dạng danh sách kề
graph = {
    1: [2, 3],
    2: [1, 3, 4, 5],
    3: [1, 2, 5, 9],
    4: [2, 5, 6, 7],
    5: [2, 3, 4, 6],
    6: [4, 5, 7, 8],
    7: [4, 6, 8, 9],
    8: [6, 7, 9, 10],
    9: [3, 7, 8, 10],
    10: [8, 9]
}

# Tìm đường đi ngắn nhất từ đỉnh 1 đến đỉnh 10
shortest_path = find_shortest_path(graph, 1, 10)
print("Đường đi ngắn nhất từ đỉnh 1 đến đỉnh 10:", shortest_path)

