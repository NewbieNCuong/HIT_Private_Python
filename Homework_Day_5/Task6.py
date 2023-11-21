dictionary = {
    1 : 1,
    2 : 2.5, 
    3 : 3,
    4 : 4,
    5 : 5.5,
    6 : 6,
    7 : 7,
}

cnt = 0

for index, value in (dictionary).items():
    if(value >= 2.5 and value <= 3.5): cnt += 1

print(cnt)

dictionary.update({1: 3})

keyremove = [i for i in dictionary if i < 2]
for i in keyremove:
    dictionary.pop(i, None)
print(dictionary)