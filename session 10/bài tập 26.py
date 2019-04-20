a = [
    {"Skill 1" :{
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3,
    }},
    {"Skill 2":{
        "Name" : "Quick attack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate": 0.5,
    }},
    {"Skill 3" :{
        "Name" : "Strong Kick",
        "Minimum level" : 4,
        "Damage" : 7,
        "Hit rate" : 0.2,
    }}
]
print(a)
for i in range(len(a)):
    print(i + 1, ". ", *a[i],": ", a[i].values())