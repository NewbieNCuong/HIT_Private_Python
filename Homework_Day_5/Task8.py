championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Trydamere"]
dataLOL = [
    {"price": 6300, "Util": "Tran troi"},
    {"price": 4800, "Util": "No long cuoc"},
    {"price": 4800, "Util": "Dau an tu than"},
    {"price": 450, "Util": "Chien binh son cuoc"},
    {"price": 450, "Util": "Cong ly Demacia"},
    {"price": 1350, "Util": "Tu choi tu than"},       
]   
d = {}
for i in range(0, len(championLOL)):
    d[championLOL[i]] = dataLOL[i]
print(d)
s = input("Nhap champion s = ")
if(d.get(s) != None):
    print("price")
else: print("No price")