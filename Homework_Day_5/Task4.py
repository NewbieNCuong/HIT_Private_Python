a = input().split()
b = tuple(a)
print(b)
countres = 0
for i in b:
    if(i.isdigit() == True): countres += 1

print(countres)