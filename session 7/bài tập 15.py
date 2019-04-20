items = ["cầu lông", "LOL", "BTS", "toán"]
print(items)
items.remove("LOL")
print(items)
i = int(input("vị trí bạn muốn xóa ?"))
items.pop(int(i))
print(items)