score = 0
a = [
    {"Skill 1" :{
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3,
    }},
    {"Skill 2" :{
        "Name" : "Quick attack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate": 0.5,
    }},
    {"Skill 3" :{
        "Name" : "Strong Kick",
        "Minimum level" : 3,
        "Damage" : 7,
        "Hit rate" : 0.2,
    }}
]
from random import randint
b = randint(1, 3)
from random import randint
d = randint(1, 10)/10
print("Hit rate là ", d)
print("Bạn combat ở level", b)
for i in range(len(a)):
    print(i + 1, ". ", *a[i],": ", *a[i].values())
x = int(input("bạn muốn chọn skill mấy ? "))
if x in [1, 2, 3]:
    if x <= b:
        print("Skill của bạn có thể sử dụng")
        for c in a[x - 1]:
            if d <= a[x - 1][c]["Hit rate"]:
                print("Damage của bạn là", a[x - 1][c]["Damage"])
            else:
                print("Rất tiếc shill không trúng mục tiêu")
    else:
        print("Skill của bạn không thể sử dụng")
else:
    print("ngu")