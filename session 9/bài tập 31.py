a = {
    "bộ phim": [
        "ở nhà một mình 3",
        "12/12/1997",
        "Alex D.Link trong vai Alex Pruitt",
        "Olex Krupa, Rya Kihlstedt, Lenny Von Dohlen, Davie Thornton trong vai 4 thằng trộm",
        "và một số diên viên khác"
    ]
}
a["bộ phim"].append("bộ phim được sản xuất tại Mỹ")
a["bộ phim"][4] = "Haviland Morris trong vai mẹ Alex"
a["bộ phim"].append("và một số diễn viên khác")

print(a["bộ phim"][2])
print(a["bộ phim"][3])
print(a["bộ phim"][4])
print(a["bộ phim"][5])
print(a["bộ phim"][6])