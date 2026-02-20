t = int(input())
for _ in range(t):
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = []
    count = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            result.append([3,i+1])
            count += 1

    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1] , a[j]
                result.append([1,j+1])
                count += 1

    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1] , b[j]
                result.append([2,j+1])
                count += 1


    print(count)
    for i , j in result:
        print(i,j)
    
    
