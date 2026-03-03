t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    balance = 0
    legal = [False] * n

    for i in range(n):
        if a[i] == "1":
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            legal[i] = True

    flip = 0
    flag = True

    for i in range(n-1, -1, -1):

        current = a[i]

        if flip % 2 == 1:
            if current == "0":
                current = "1"
            else:
                current = "0"

        if current != b[i]:
            if not legal[i]:  
                flag = False
                break
            flip += 1         

    if flag:
        print("YES")
    else:
        print("NO")