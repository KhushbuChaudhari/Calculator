from tkinter import *
import math as m

root = Tk()
root.title("Scientific Calculator")

# Entry field
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="white", bg="black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

# Button click function
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)

# Scientific functions
def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    try:
        if text == 'deg':
            result = str(m.degrees(float(no)))
        elif text == 'sin':
            result = str(m.sin(m.radians(float(no))))
        elif text == 'cos':
            result = str(m.cos(m.radians(float(no))))
        elif text == 'tan':
            result = str(m.tan(m.radians(float(no))))
        elif text == 'lg':
            result = str(m.log10(float(no)))
        elif text == 'sqrt':
            result = str(m.sqrt(float(no)))
        elif text == 'x!':
            result = str(m.factorial(int(no)))
        elif text == '1/x':
            result = str(1 / float(no))
        elif text == 'pi':
            result = str(float(no) * m.pi if no else m.pi)
        elif text == 'e':
            result = str(m.e ** float(no) if no else m.e)
    except Exception as err:
        result = "Error"
    e.delete(0, END)
    e.insert(0, result)

# Clear function
def clear():
    e.delete(0, END)

# Backspace function
def bksps():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

# Evaluate function for basic calculations
def evaluate():
    try:
        ans = e.get()
        ans = eval(ans)
        e.delete(0, END)
        e.insert(0, ans)
    except Exception as err:
        e.delete(0, END)
        e.insert(0, "Error")

# Scientific and numeric button definitions
lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED,bg="black", fg="white")
lg.bind("<Button-1>", sc)
ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED,bg="black", fg="white")
ln.bind("<Button-1>", sc)
par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("("))
par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click(")"))
dot = Button(root, text=".", padx=30, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("."))

exp = Button(root, text="^", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("^"))

degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, bg="black", fg="white")
degb.bind("<Button-1>", sc)
sinb = Button(root, text="sin", padx=24, pady=10, relief=RAISED, bg="black", fg="white")
sinb.bind("<Button-1>", sc)
cosb = Button(root, text="cos", padx=23, pady=10, relief=RAISED, bg="black", fg="white")
cosb.bind("<Button-1>", sc)
tanb = Button(root, text="tan", padx=23, pady=10, relief=RAISED, bg="black", fg="white")
tanb.bind("<Button-1>", sc)

sqrtm = Button(root, text="sqrt", padx=23, pady=10, relief=RAISED, bg="black", fg="white")
sqrtm.bind("<Button-1>", sc)
ac = Button(root, text="AC", padx=25, pady=10, relief=RAISED, command=clear, bg="red", fg="white")
bksp = Button(root, text="Bksp", padx=19, pady=10, relief=RAISED, command=bksps, bg="orange", fg="white")
mod = Button(root, text="mod", padx=19, pady=10, relief=RAISED, command=lambda: click("%"),bg="black", fg="white")
div = Button(root, text="/", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("/"))

fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="black", fg="white")
fact.bind("<Button-1>", sc)
seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, command=lambda: click("7"))
eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, command=lambda: click("8"))
nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, command=lambda: click("9"))
mult = Button(root, text="*", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("*"))

frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="black", fg="white")
frac.bind("<Button-1>", sc)
four = Button(root, text="4", padx=30, pady=10, relief=RAISED, command=lambda: click("4"))
five = Button(root, text="5", padx=29, pady=10, relief=RAISED, command=lambda: click("5"))
six = Button(root, text="6", padx=29, pady=10, relief=RAISED, command=lambda: click("6"))
minus = Button(root, text="-", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("-"))

pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="black", fg="white")
pib.bind("<Button-1>", sc)
one = Button(root, text="1", padx=30, pady=10, relief=RAISED, command=lambda: click("1"))
two = Button(root, text="2", padx=29, pady=10, relief=RAISED, command=lambda: click("2"))
three = Button(root, text="3", padx=29, pady=10, relief=RAISED, command=lambda: click("3"))
plus = Button(root, text="+", padx=29, pady=10, relief=RAISED,bg="#EBB8DD",fg="black", command=lambda: click("+"))

e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="black", fg="white")
e_b.bind("<Button-1>", sc)
zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, command=lambda: click("0"))
equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, command=evaluate, bg="green", fg="white")

# Place buttons on grid
lg.grid(row=1, column=0)
ln.grid(row=1, column=1)
par1st.grid(row=1, column=2)
par2nd.grid(row=1, column=3)
dot.grid(row=1, column=4)

exp.grid(row=2, column=4)
degb.grid(row=2, column=0)
sinb.grid(row=2, column=1)
cosb.grid(row=2, column=2)
tanb.grid(row=2, column=3)

sqrtm.grid(row=3, column=0)
ac.grid(row=3, column=1)
bksp.grid(row=3, column=2)
mod.grid(row=3, column=3)
div.grid(row=3, column=4)

fact.grid(row=4, column=0)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
mult.grid(row=4, column=4)

frac.grid(row=5, column=0)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
minus.grid(row=5, column=4)

pib.grid(row=6, column=0)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
plus.grid(row=6, column=4)

e_b.grid(row=7, column=0)
zero.grid(row=7, column=1)
equal.grid(row=7, column=2,columnspan=2,sticky="we")
root.mainloop()