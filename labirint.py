NO_X = 1
NO_Y = 0
NO2_X = 1
NO2_Y = 1
#-------------
S_X = 2
S_Y = 0
S2_X = 2
S2_Y = 1
#-------------
B_X = 4
B_Y = 0

x = 0
y = 0

Null = "undef"
def print_all(val):
    for stroka in val:
        for kletka in stroka:
            print(kletka,end="")
        print()


pole = [["s","|","?","*","!"],
        ["*","|","?","*","-"],
        ["*","*","/","*","*"],
        ["*","*","*","*","*"],
        ["*","*","*","*","f"]]
c = None
skin = input("skin: ")
while c != "exit":
    c = input("command: ")
    if c == "left":
        pole[y][x] = "."
        x=x-1
        pole[y][x] = skin
        print_all(pole)
    if c == "right":
        pole[y][x] = "."
        x=x+1
        pole[y][x] = skin
        print_all(pole)
    if c == "up":
        pole[y][x] = "."
        y = y - 1
        pole[y][x] = skin 
        print_all(pole)
    if c == "down":
        pole[y][x] = "."
        y = y + 1
        pole[y][x] = skin
        print_all(pole)