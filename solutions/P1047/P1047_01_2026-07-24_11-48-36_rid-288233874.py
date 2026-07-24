l,m = map(int,input().split())
areas = []
for i in range(m):
    u,v = map(int,input().split())
    areas.append([u,v])
areas.sort()
result = []
current = areas[0]
for j in range(1,m):
    new = areas[j]
    if new[0] <= current[1]:
        current[0] = min(current[0],new[0])
        current[1] = max(current[1],new[1])
    else:
        result.append(current)
        current = new
result.append(current)
remove = 0
for i in range(len(result)):
    remove = remove + result[i][1] - result[i][0] + 1
print(l + 1 - remove)
