# Khai báo các biến và gán giá trị cho biến
num_vertices=10 # Số lượng đỉnh của đồ thị
graph={
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
} # Đồ thị được biểu diễn dưới dạng danh sách kề

# hàm chuyển đổi từ đồ thi sang ma trận kề
def translate_to_matrix(graph,num_vertices):
    # Dòng này khởi tạo một ma trận kề ban đầu với các phần tử bằng 0.
    # Với kích thước của ma trận là num_vertices x num_vertices (đỉnh x đỉnh)
    adj_matrix = [ [0]*num_vertices for _ in range(num_vertices) ]

    for i in range(num_vertices):
        if i in graph:
            for j in graph[i]:
                adj_matrix[i][j]=1
    return adj_matrix        
    
# In ra ma trận kề
adj_matrix = translate_to_matrix(graph,num_vertices)

for row in adj_matrix:
    print(row)


