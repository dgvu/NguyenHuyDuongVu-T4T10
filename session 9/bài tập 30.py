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
a["bộ phim"].pop(6)
for i in range(len(a["bộ phim"])):
    print("- ", a["bộ phim"][i])