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
for i in range(len(a["bộ phim"])):
    print("- ", a["bộ phim"][i])