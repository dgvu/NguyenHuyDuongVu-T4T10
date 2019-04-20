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
x = input("loại máy tính là ? ")
y = input("số lượng bao nhiêu ? ")
a[x.upper()] = y
print(a)