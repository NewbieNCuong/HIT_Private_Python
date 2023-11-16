import re
s = input()
pattern = r'-?\d+'
match = re.findall(pattern, s)
print(sum([int(i) if '-' not in i else -int(i[1:]) for i in match]))
