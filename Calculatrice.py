from customtkinter import *
import tkinter

fenetre = CTk()
fenetre.title("")
number = (1, 2, 3, 4, 5, 6)
fenetre.rowconfigure(number, weight=1)
fenetre.columnconfigure((0, 1, 2, 3), weight=1)
# set_default_color_theme("green")
Buttons = ["AC", "+/-", "%", "/", "7", "8", "9", "*", "4", "5", "6",
           "-", "1", "2", "3", "+", "0", ".", "="]
entrer = CTkEntry(fenetre, placeholder_text="0", justify="right",
                  height=60, border_width=0, font=("Avenir", 25)
                  )
entrer.grid(row=0, column=0, sticky="nsew", columnspan=4)
x, y = 1, 0


def click(event):
    current_text = entrer.get()
    new_text = current_text + event.widget.cget("text")
    entrer.delete(0, tkinter.END)
    entrer.insert(0, new_text)


def evaluer():
    try:
        resultat = eval(entrer.get())
        entrer.delete(0, tkinter.END)
        entrer.insert(0, str(resultat))
    except Exception:
        entrer.delete(0, tkinter.END)
        entrer.insert(0, "Erreur")


def boutton_1():
    operateur = "-"
    current_text = entrer.get()
    new_text = current_text + operateur
    entrer.delete(0, tkinter.END)
    entrer.insert(0, new_text)


def effacer():
    entrer.delete(0, tkinter.END)


for buttons in Buttons:
    button = CTkButton(fenetre, text=buttons, width=60, corner_radius=0,
                       height=50, fg_color="transparent"
                       )
    button.grid(row=x, column=y, sticky="nsew")

    if buttons == "=":
        button.grid_configure(column=3)
        button.configure(command=evaluer, fg_color="purple")

    elif buttons == "AC":

        button.configure(command=effacer)
    elif buttons == "/":
        button.bind("<Button-1>", click)
        button.configure(fg_color="purple")
    elif buttons == "+":
        button.bind("<Button-1>", click)
        button.configure(fg_color="purple")
    elif buttons == "-":
        button.bind("<Button-1>", click)
        button.configure(fg_color="purple")
    elif buttons == "*":
        button.bind("<Button-1>", click)
        button.configure(fg_color="purple")
    elif buttons == "abs":
        button.bind("<Button-1>", click)
        button.configure(fg_color="purple")
    elif buttons == ".":
        button.bind("<Button-1>", click)
        button.grid_configure(column=2)
    elif buttons == "0":
        button.grid_configure(columnspan=2)
        button.bind("<Button-1>", click)
    elif buttons == "+/-":
        button.configure(command= boutton_1)
    else:
        button.bind("<Button-1>", click)
    y += 1
    if y == 4:
        y = 0
        x += 1

fenetre.mainloop()
