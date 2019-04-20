a = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
print(a)
c = {
    "TOSHIBA" : 10
}
a.update(c)
print(a)
b = sum(a.values())
print("tổng số máy tính có trong kho là ", b)