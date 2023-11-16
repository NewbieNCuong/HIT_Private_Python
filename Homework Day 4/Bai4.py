n = int(input())
a = [int(i) for i in input().split()]
even, odd = 0, 0
for i in a:
    if i % 2 == 0:
        even += i
    else: odd += i
print("even" if even > odd else "odd")