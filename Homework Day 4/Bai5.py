res = []
def detached(a):
    if(type(a) == list):
        for i in a:
            detached(i)
    else:
        res.append(a)

s = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
detached(s)

print(res)