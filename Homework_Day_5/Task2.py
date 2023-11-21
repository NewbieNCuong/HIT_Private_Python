n = int(input())
listn = [int(i) for i in input().split()]
x = int(input())
res, j = [], 0
for i in range(n):
    j = i + 1
    listres = [listn[i]]
    tmp = listn[i]
    while(j <= (n - 1) and tmp < x):
        tmp += listn[j]
        if(tmp > x): break
        listres.append(listn[j])
        j += 1
    res = res if len(res) > len(listres) else listres

print(res)

# Complexity: O(n^2)