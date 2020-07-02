ls = []
r = 0
n = 5
for i in range(n):
    ls.append([])
    for j in range(n):
        ls[i].append(r)
        r += 1
    if i % 2 != 0:
        ls[i].reverse()

for item in ls:
    print(item)



