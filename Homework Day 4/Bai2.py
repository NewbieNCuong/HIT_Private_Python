n = int(input())
a = [i for i in input().split()]
tmp = ['1', '3', '5', '7', '9']
res = [int(i) for i in a if (len(i) == 1 and (i in tmp)) or (i[len(i) - 1] in tmp)]
res = sorted(res)
print(len(res))
for i in res: print(i, end = " ")