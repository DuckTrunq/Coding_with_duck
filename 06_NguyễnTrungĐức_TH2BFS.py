from collections import deque

#Bieu dien do thi
graph = {
    1: [2, 3],
    2: [1, 4, 3, 5],
    3: [1, 2, 5, 9],
    4: [2, 5, 7, 6],
    5: [3, 2, 4, 6],
    6: [4, 5, 7, 8],
    7: [4, 6, 8, 9],
    8: [6, 7, 9, 10],
    9: [3, 7, 8, 10],
    10: [8, 9]
}

num_vertices = 10
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

for vertex in graph:
    for neighbor in graph[vertex]:
        adjacency_matrix[vertex - 1][neighbor - 1] = 1

for row in adjacency_matrix:
    print(row)
print()

#Thuật toán BFS
def bfs(adj_matrix, start, end):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor, connected in enumerate(adj_matrix[current - 1]):
            if connected and not visited[neighbor]:
                queue.append((neighbor + 1, path + [neighbor + 1]))
                visited[neighbor] = True
#Thuật toán DFS
def dfs(adj_matrix, start, end):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    all_paths = []
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()

        if current == end:
            all_paths.append(path)
        else:
            for neighbor, connected in enumerate(adj_matrix[current - 1]):
                if connected and not visited[neighbor]:
                    stack.append((neighbor + 1, path + [neighbor + 1]))
                    visited[neighbor] = True

    return all_paths
#Đặt điểm bắt đầu và kết thúc
start_vertex = 1
end_vertex = 10
# Duyệt BFS từ đỉnh 1 đến 10
result_bfs = bfs(adjacency_matrix, start_vertex, end_vertex)
if result_bfs:
    print(f"Đường đi từ {start_vertex} đến {end_vertex} bằng BFS:")
    print(" -> ".join(map(str, result_bfs)))
else:
    print(f"Không có đường đi từ {start_vertex} đến {end_vertex}.")
# Duyệt DFS từ đỉnh 1 đến 10
result_dfs = dfs(adjacency_matrix, start_vertex, end_vertex)
if result_dfs:
    print(f"đường đi từ {start_vertex} đến {end_vertex} bằng DFS:")
    for path in result_dfs:
        print(" -> ".join(map(str, path)))
else:
    print(f"Không có đường đi từ {start_vertex} đến {end_vertex}.")