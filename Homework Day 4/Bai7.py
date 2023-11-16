s = [i for i in input().split()]
n = int(input())
res, tmp = [], []
count = len(s) // n
count1 = 0
for i in range(n):
    for i in range(0, count):
        tmp.append(s[count1])
        count1 += 1
    res.append(tmp)
    tmp = []
print(res)
        