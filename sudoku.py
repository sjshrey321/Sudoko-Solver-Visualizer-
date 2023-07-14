from tkinter import *
from solver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("470x340")
root['bg']="#222222"

label= Label(root,text="Fill in the numbers and click solve",fg="white",bg="#111111",font=(10,16),relief=SUNKEN,padx=20).grid(row=0,column=1,columnspan=10)

notLabel = Label(root,text="" ,fg = "red")
notLabel.grid(row=20,column=1,columnspan=10,padx=5,pady=5)

solvedLabel = Label(root,text="" ,fg = "green")
solvedLabel.grid(row=20,column=1,columnspan=10,padx=5,pady=5)

cells = {}

def ValiNumber(blok):
    out = (blok.isdigit() or blok =="") and len(blok)<2
    return out

reg = root.register(ValiNumber)

def Grid3x3(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width=5,bg=bgcolor,justify="center",fg="white")
            # e = Entry(root,width=5,bg=bgcolor,justify="center",validate="key",validatecommand=(reg,"%blok"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=2,pady=2,ipadx=3,ipady=3)
            cells[(row+i+1,column+j+1)] = e

def Grid9x9():
    color = "#333333"
    for rown in range (1,10,3):
        for coln in range(0,9,3):
            Grid3x3(rown,coln,color)
            if color == "#333333":
                color = "#505050"
            else :
                color = "#333333"


def clearValues():
    notLabel.configure(text="")
    solvedLabel.configure(text="")

    for row in range (2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

def getValues():
    board = []
    notLabel.configure(text="")
    solvedLabel.configure(text="")

    for row in range (2,11):
        rows=[]
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val =="":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    updateValues(board)

button = Button(root,command=getValues,text = "Let's GO",width = 12,fg="white",bg="#222222",font=(10,12))
button.grid(row=25,column=1,columnspan=3,pady=10,padx=20)

button = Button(root,command=clearValues,text = "Clear",width = 12,fg="white",bg="#222222",font=(10,12))
button.grid(row=25,column=7,columnspan=5,pady=10,padx=10)

def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        solvedLabel.configure(text="Sudoku Solved!",fg="white")
    else :
        notLabel.configure(text="No Solution exists",fg="white")

Grid9x9()
root.mainloop()



