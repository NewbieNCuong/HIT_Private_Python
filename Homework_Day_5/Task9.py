import random
n = int(input("Nhap so luong sinh vien: "))
res = {}
a = ["CNTT", "KHMT", "KTPM", "HTTT"]
for i in range(0, n):
    print("Nhap sinh vien thu", i + 1, ":")
    tmp1 = {}
    tmp2 = {}
    ma_sv = input("Ma SV: ")
    tmp1["Username"] = ma_sv
    tmp2["Password"] = random.choice(a) + ma_sv
    Account =  "Account" + str(i + 1)
    tmp1.update(tmp2)
    res[Account] = tmp1
print(res)