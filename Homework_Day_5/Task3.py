s = (str)(input())
a = [i for i in map(str, s.split())]
b = set(a)
restmp = []
maxtmp = 0
for tmp in b:
    restmp.append((tmp, a.count(tmp)))
    maxtmp = max(a.count(tmp), maxtmp)
res = []
for i in restmp:
    if(i[1] == maxtmp):
        res.append(i)
print(tuple(res))