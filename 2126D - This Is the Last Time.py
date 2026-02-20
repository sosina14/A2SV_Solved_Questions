t = int(input())
for _ in range(t):
    n , k  = map(int, input().split()) 
    mat = []
    for _ in range(n):
        l, r, x = map(int, input().split())
        mat.append((l, r, x))

    mat.sort(key=lambda x: x[0])
    for i in range(n):
        if mat[i][0] <= k and k <= mat[i][1]:
            k = max(mat[i][2] ,k)

    print(k)
