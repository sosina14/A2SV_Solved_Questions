s = input()
n = len(s)

stack = []
d = [-1] * n
c = [-1] * n

max_len = 0
count = 0

for j in range(n):

    if s[j] == "(":
        stack.append(j)

    else: 

        if not stack:
            d[j] = -1
            c[j] = -1

        else:
            i = stack.pop()
            d[j] = i
            c[j] = i

            if i > 0 and s[i-1] == ")" and c[i-1] != -1:
                c[j] = c[i-1]

            length = j - c[j] + 1

            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

if max_len == 0:
    print(0, 1)
else:
    print(max_len, count)