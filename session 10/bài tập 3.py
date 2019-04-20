a = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
x = input("hãng máy tính bạn cần là ")
b = x.upper()
if b in a:
    print(a[b])
else:
    print(" không tìm thấy loại máy tính trên")