a = {
    "nhân vật em thích": "không có",
    "ca sĩ em thích": "không có nốt",
    "bộ phim em thích": "avenger",
}
print(a)
while True:
    x = input("mục bạn muốn thay đổi là ? ")
    if x in ["nhân vật em thích", "ca sĩ em thích", "bộ phim em thích"]:
        y = input("như thế nào ? ")
        a[x] = y
        break
print(a)