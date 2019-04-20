a = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000
}
x = input("tên hãng máy tính bạn muốn tra là ? ")
if x.upper() in a:
    print(a[x.upper()])
else: 
    print("rất tiếc chúng tôi không có")