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
d = a[0]
print(d)
d["name"] = "huyen"
d["role"] = "Waitress"
d["hours"] = "14"
d["salary per Hour"] = "1"
print(d)