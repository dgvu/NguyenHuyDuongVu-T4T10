a = ["red", "white", "black", "yellow", "blue", "green", "brown","pink", "purple" ]
print("hãy xắp sếp lại các từ cho phù hợp")
print("gợi ý: đây là các màu trong tiếng anh")
import random
d = random.choice(a)
b = list(d)
from random import shuffle
c = b[:] 
shuffle(c) 
print(*c,sep= ",")
e = input("đáp án của bạn là ?")
if e == d:
    print("true")
else:
    print("false")