topic = [int(i) for i in input().split()]
topic = sorted(topic)
res = []
tmp = [topic[0]]
for i in range(1, len(topic)):
    if topic[i] == tmp[0]:
        tmp.append(topic[i])
    else:
        res.append(tmp)
        tmp = [topic[i]]
print(res)
    