a = [
    {
        "question" : {
            "ques": "how many legs an octopus has:",
            "1" : "1 leg",
            "2" : "2 leg",
            "3" : "4 leg",
            "4" : "8 leg",
        },
        "answer" : 4,
    },
    {
        "question" : {
            "ques": "how many legs an octopus has:",
            "1" : "None",
            "2" : "4 legs",
            "3" : "8 legs",
            "4" : "12 legs",
        },
        "answer" : 2
    }
]
score = 0
z = {
    "question" : {
        "ques" : input("câu hỏi ?? "),
        "1" : input("câu trả lời thứ nhất ? "),
        "2" : input("câu trả lời thứ 2 ? "),
        "3" : input("câu trả lời thứ 3 ? "),
        "4" : input("câu trả lời thứ 4 ? "),
    },
    "answer" : input("đáp án đúng là ? ")
}
a.append(z)
for i in a:
    print(i["question"]["ques"])
    for x in i["question"]:
        print(x, ".", i["question"][x])
    answer = int(input("Press Your Answer: "))
    if (i["answer"] == answer):
        print("HURA!!!!")
        score += 1
    else:
        print("faux")
        print("answer true is ", i["answer"])
        break
print("Ban duoc: ",score)
print("tỉ số người làm đúng là ", score/len(a)*100,"%")
