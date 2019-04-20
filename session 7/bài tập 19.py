items = ["cầu lông", "LOL"]
print(items)
items.append("BTS")
items.append("Death note")
items.append("Netflis")
print(items)
a = [elem.upper() for elem in items ]
print(a)
x = len(items)
for i,item in enumerate(a):
    print(i + 1, ".", item)