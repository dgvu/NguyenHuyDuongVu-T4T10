from random import randint
a = int(input("nhập chiều rộng của căn hầm ? "))
b = int(input("nhập chiều dài của căn hầm ? "))
player = {
    "x": randint(0,a - 1),
    "y": randint(0,b - 1),
    "key": 0
}
while True:
    x = randint(0,a-1)
    y = randint(0, b-1)
    if x != player['x'] and y != player['y']:
        keys = {
        "x": x,
        "y": y
        }
        break
while True:
    x = randint(0,a-1)
    y = randint(0, b-1)
    if (x != player['x'] and y != player['y']) or (x != keys['x'] and y != keys['y']):
        _exit = {
        "x": x,
        "y": y
        }
        break       
_round = True
while _round:
    for y in range (b):
        for x in range (a):
            if x == player["x"] and y == player["y"]:
                if x == a - 1:
                    print('P')
                else:
                    print('P', end ="")
            elif x == _exit["x"] and y == _exit["y"]:
                if x == a - 1:
                    print('E')
                else:
                    print('E', end ="")
            elif x == keys["x"] and y == keys["y"]:
                if x == a - 1:
                    print('K')
                else:
                    print('K', end ="")
            elif x == a - 1:
                print("-")
            else:
                print("-", end="")

    move = input("Bạn muốn nhân vật đi chuyển như thế nào ? ")
    player_0 = {
        "x": player['x'],
        "y": player['y']
    }
    if move in ["a", "w", "s", "d"]:
        if move == "w":
            player_0["y"] -= 1
        elif move == "s":
            player_0["y"] += 1
        elif move == "a":
            player_0["x"] -= 1
        elif move == "d":
            player_0["x"] += 1
    else:
        print("thử lại")

    if player_0['x'] in range(a - 1) and player_0['y'] in range(b - 1):
        player['x'] = player_0['x']
        player['y'] = player_0['y']

    if player['x'] == keys['x'] and player['y'] == keys['y']:
        keys['x'] = -1
        keys['y'] = -1
        player["key"] = 1 

    if player["x"] == _exit["x"] and player["y"] == _exit["y"]:
        if player["key"] == 1:
            print("you win")
            _round = False
        else:
            print("bạn cần chìa khóa để ra ngoài")