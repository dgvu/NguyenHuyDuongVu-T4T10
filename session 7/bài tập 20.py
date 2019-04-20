items = ["cầu lông", "LOL"]
print(items)
items.append("BTS")
items.append("Death note")
items.append("netflis")
print(items)
a = [elem.upper() for elem in items ]
print(a)
x = len(items)
b = [k for k in a if 'E' in k]
for i in b:
    print(i)
