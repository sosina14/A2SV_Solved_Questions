from collections import Counter

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()

    fre1 = Counter(s1)
    fre2 = Counter(s2)

    possible = True
    for k, v in fre1.items():
        if v > fre2[k]:
            print("Impossible")
            possible = False
            break

    if not possible:
        continue

    for k in fre1:
        fre2[k] -= fre1[k]

    new = []
    for k, v in fre2.items():
        new.extend([k] * v)

    new.sort()
    new = "".join(new)

    i = 0
    j = 0
    result = ""

    while i < len(s1) and j < len(new):
        if s1[i] < new[j]:
            result += s1[i]
            i += 1
        elif s1[i] > new[j]:
            result += new[j]
            j += 1
        else:
            result += s1[i]
            i += 1

    result += s1[i:]
    result += new[j:]

    print(result)
