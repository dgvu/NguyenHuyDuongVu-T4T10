a = [
    {
        "name": "Huy",
        "role": "Waiter",
        "hours": "12",
        "salary per Hour": "0.8",
    },
    {
        "name": "Tung",
        "role": "Cook",
        "hours": "24",
        "salary per Hour": "1.5",
    },
    {
        "name": "M.Duc",
        "role": "Manager",
        "hours": "20",
        "salary per Hour": "2",
    }
]

b = {
    "name": "Don",
    "role": "Waiter",
    "hours": "12",
    "salary per Hour": "0.9",
}
c = {
    "name": "H.Duc",
    "role": "Waiter",
    "hours": "14",
    "salary per Hour": "0.7",
}

a.append(b)
a.append(c)
e = []
for i in range(len(a)):
    d = a[i]
    f = float(d["hours"]) * float(d["salary per Hour"])
    e.append(f)
    print(d,"lương của nhân viên là", f)
print("tổng số tiền chi nhánh phải trả cho nhân viên là", sum(e))