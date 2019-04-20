a = [45, 67, 56, 78]
a = sorted(a, reverse=True)
for i in range(len(a)):
    print(i + 1, ", ", a[i])
b = 1
while True:
    x = int(input("Enter your new score ? "))
    a.append(x)
    a = sorted(a, reverse=True)
    for i in range(5):
        print(i + 1, ", ", a[i])
    b += 1
    if b > 2:
        break