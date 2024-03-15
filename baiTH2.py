def graph_to_adj_matrix(graph, num_vertices):
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)] #- Dòng code này là khởi tạo ra ma trận kề ban đầu với tất cả các phần tử đầu bằng 0 
                                                                      #- ma trận kề này có kích thước là num_vertices x num_vertices (đỉnh x )
                                                                      #- List Comprehension được sử dụng 

    for i in range(num_vertices):    
        if i in graph:
            for j in graph[i]:
                adj_matrix[i][j] = 1

    return adj_matrix

# Số lượng đỉnh của đồ thị
num_vertices = 10

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
adj_matrix = graph_to_adj_matrix(graph, num_vertices)

# In ma trận kề
for row in adj_matrix:
    print(row)