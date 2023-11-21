s = input()
d = {}
for i in range(0, len(s)):
    if(d.get(s[i]) != None):
        d[s[i]] = d[s[i]] + 1
    else: d[s[i]] = 1
print(d)