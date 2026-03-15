h , w = map(int, input().split())

matrix = []
for _ in range(h):
    arr = list(input())
    matrix.append(arr)

hor = [[0]*(w+1) for _ in range(h+1)]
ver = [[0]*(w+1) for _ in range(h+1)]

for r in range(1, h+1):
    for c in range(1, w+1):

        hor[r][c] = hor[r-1][c] + hor[r][c-1] - hor[r-1][c-1]
        ver[r][c] = ver[r-1][c] + ver[r][c-1] - ver[r-1][c-1]

        if c < w and matrix[r-1][c-1] == '.' and matrix[r-1][c] == '.':
            hor[r][c] += 1

        if r < h and matrix[r-1][c-1] == '.' and matrix[r][c-1] == '.':
            ver[r][c] += 1


q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    h_ans = hor[r2][c2-1] - hor[r1-1][c2-1] - hor[r2][c1-1] + hor[r1-1][c1-1]
    v_ans = ver[r2-1][c2] - ver[r1-1][c2] - ver[r2-1][c1-1] + ver[r1-1][c1-1]

    print(h_ans + v_ans)