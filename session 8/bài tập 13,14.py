a = ["Sơn Tây", "Ba Đình", "Bắc Từ Liêm", "Cầu Giấy", "Đống Đa", "Hai Bà Trưng"]
b = ["150,300", "247,100", "333,300", "266,800", "420,900", "318,000"]
for i in range(len(b)):
    if b[i] == max(b):
        print(a[i])

for i in range(len(b)):
    if b[i] == min(b):
        print(a[i])
