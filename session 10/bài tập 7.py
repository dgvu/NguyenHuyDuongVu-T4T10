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
for i in a:
    print(i, " : ", a[i])