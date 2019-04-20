x = input("từ bạn muốn nhập ?")
a = list(x)
c = [elem.upper() for elem in a]
from random import shuffle
b = c[:] 
shuffle(b) 
for i in range(len(b)):
    print(b[i])
