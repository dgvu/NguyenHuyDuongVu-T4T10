a = {
    "raichu": """have a regional variant that is Electric/Psychic. 
It evolves from Pikachu when exposed to a thunder stone. 
All Pikachu in Alola will evole into form regardless of their origin.""",
    "onix": """resemble a giant chain of gray boulders that becom smaller 
towards the tail. It has a rocky spine on its head and a pair of 
black eyes right beneath it. This Pokemon has a magnet in its brain
that serves as an internal compass. its body absorbs many hard 
objects, making its body very solid. As it grows older, it becomes
more rounded and smoother, eventually becoming similar to black diamonds"""
}
while True:
    x = str(input("từ bạn muốn tra ? "))
    b = x.lower()
    if b in a:
        print(a[b])
    elif b == "hết":
        break