matrix = []
for _ in range(5):
    l1 = list(map(int, input().split()))
    matrix.append(l1)

found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            found = True
            break
    if found:
        break
        
print(abs(2-i)+abs(2-j))



