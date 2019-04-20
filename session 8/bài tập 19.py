a = [45, 67, 56, 78]
for i in range(len(a)):
    print(i + 1, ", ", a[i])
x = input("Enter your new score ? ")
a.append(x)
for i in range(len(a)):
    print(i + 1, ", ", a[i])