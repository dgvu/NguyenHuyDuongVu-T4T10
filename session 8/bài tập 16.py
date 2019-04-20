a = ["Sơn Tây", "Ba Đình", "Bắc Từ Liêm", "Cầu Giấy", "Đống Đa", "Hai Bà Trưng"]
b = ["150300", "247100", "333300", "266800", "420900", "318000"]
c = ["117.43", "9.224", "43.33", "12.04", "9.96", "10.09"]
for i in range(len(a)):
    print(a[i],": ", b[i],",      ", c[i])
d = []
for i in range(len(b)):
    e = int(b[i]) / float(c[i])
    d.append(e)
print(*d, sep=", ")
g = sum(d) / len(a)
print(g)