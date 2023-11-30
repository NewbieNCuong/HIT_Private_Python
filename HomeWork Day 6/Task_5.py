def gcd(a, b):
    '''
        This functon compact
    '''
    if(b == 0): return a
    else: return gcd(b, a % b)

n = int(input())
ts, ms = 1, 1
for i in range(n):
    x = [int(i) for i in input().split()]
    ts *= x[0]
    ms *= x[1]

tmp = gcd(ts, ms)
print(int(ts / tmp), int(ms / tmp))
