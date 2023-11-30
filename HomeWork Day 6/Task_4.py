import math
import re

def readfile():
    '''
        This function to read file
    '''
    f = open("D:/HIT Private/Python/Pythoncode/Day 6/HomeWork Day 6/input.txt")
    a  = f.read()
    pattern = r'\d+\.\d+|\d+'
    tmp = re.findall(pattern, a)
    res = [float(i) for i in tmp]
    f.close()
    return res

def writefile(res) -> float:
    '''
        This function write in file
    '''
    ans = math.sqrt((res[2] - res[0]) ** 2 + (res[3] - res[1]) ** 2)
    ans_round = round(ans, 2)
    ans1 = "A(" + str(res[0]) + "," + str(res[1]) + ") B(" + str(res[2]) + "," + str(res[3]) + ") AB = " + str(ans_round) 
    with open("output.txt", "w") as f : f.write(ans1)

res = readfile()
writefile(res)