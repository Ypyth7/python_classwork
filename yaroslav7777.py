from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import pyautogui
win = Tk()
text = """
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
"""
def io():
    win.destroy()
def click():
    wos = Tk()
    progress = ttk.Progressbar(wos,max=100)
    progress.pack()
    progress.start(100)
    file = open("labirint.py","w")
    file.write(text)
    wos.mainloop()
    if progress == 100:
def hello():
    showinfo("info","hello User!")
op = ["install","unistall","install new version"]
ddd = ttk.Combobox(values=op)
ddd.pack(padx=100,pady=100)
re = ttk.Button(text="ok",command=click)
re.pack()
menu = Menu(tearoff=0)
form = Menu(tearoff=0)
fop = Menu(tearoff=0)
fop.add_command(label="hello",command=hello)
fop.add_cascade(label="function",menu=form)
form.add_command(label="exit",command=io)
menu.add_cascade(label="command",menu=fop)
win.config(menu=menu)
win.mainloop()