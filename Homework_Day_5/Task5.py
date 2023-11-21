a = set(int(i) for i in input().split())
b = list(a)
if 11 not in a: a.add(11)
print(a)
respair = []
sorted(a)
for i in b:
    if(b.count(11 - i) != 0):
        respair.append((i, 11 - i))
respair = set(respair)
respair = tuple(respair)
print(11*len(respair) / 2)