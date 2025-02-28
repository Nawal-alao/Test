import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror

from customtkinter import *

root = CTk()
# root.config(background="black")
root.geometry("600x500")
root.rowconfigure((0, 1, 2, 3), weight=1)
root.columnconfigure(0, weight=1)

user_information = CTkFrame(root, border_width=2)
user_information.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

parameter = CTkFrame(root, border_width=2)
parameter.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

terms = CTkFrame(root, border_width=2)
terms.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# first frame
user_information.rowconfigure((0, 1, 2, 3), weight=1)
user_information.columnconfigure((0, 1, 2), weight=1)

first_name = CTkLabel(user_information, text="First Name")
last_name = CTkLabel(user_information, text="Last name")
choice_name = ["Mr", "Mme"]
nation = ["Benin", "Togo", "Gabon", "Mozanbique", "Australia", "America"]
title = CTkLabel(user_information, text="Title")

first_name.grid(row=0, column=0, pady=5)
last_name.grid(row=0, column=1)
title.grid(row=0, column=2)

enter_name = CTkEntry(user_information, placeholder_text="ex:John")
enter_last_name = CTkEntry(user_information, placeholder_text="ex:Smith")
choice = CTkComboBox(user_information, values=choice_name)

enter_name.grid(row=1, column=0)
enter_last_name.grid(row=1, column=1)
choice.grid(row=1, column=2)

age = CTkLabel(user_information, text="Age")
nationality = CTkLabel(user_information, text="Nationnality")
age.grid(row=2, column=0)
nationality.grid(row=2, column=1)
# , from_=16, to=100, width=14
l = []
for i in range(0, 25):
    l.append(str(i))
enter_age = CTkComboBox(user_information, values=l)
enter_nationality = CTkComboBox(user_information, values=nation)
enter_age.grid(row=3, column=0, pady=5)
enter_nationality.grid(row=3, column=1, pady=5)

# Second frame
parameter.rowconfigure((0, 1), weight=1)
parameter.columnconfigure((0, 1, 2), weight=1)

register = CTkLabel(parameter, text="Register Status")
courses = CTkLabel(parameter, text="Completed courses")
semester = CTkLabel(parameter, text="Semester")

register.grid(row=0, column=0, sticky="w", padx=35)
courses.grid(row=0, column=1, padx=5)
semester.grid(row=0, column=2, padx=5)

reg = CTkCheckBox(parameter, text="Currently Registered")
# , from_=0, to=7
j = []
for k in range(0, 8):
    j.append(str(k))
cour = CTkComboBox(parameter, values=j)
seme = CTkComboBox(parameter, values=["0", "1", "2"])

reg.grid(row=1, column=0, padx=5, pady=5)
cour.grid(row=1, column=1, padx=5, pady=5)
seme.grid(row=1, column=2, padx=5, pady=5)

# third frame
accepted = CTkCheckBox(terms, text="I accept the terms and contions.")
accepted.grid(row=0, column=0, padx=20, pady=5)
# button
def fontction():
    a = enter_name.get()
    b = enter_last_name.get()
    c = choice.get()
    d = enter_age.get()
    f = enter_nationality.get()
    g = reg.get()
    h = cour.get()
    m = seme.get()
    n = accepted.get()
    liste = [a, b, c, d, f, g, h, m, n]
    for elem in liste:
        if elem == "":
            showerror(message="Un champs vide!!!")
            break
        else:
            print(f"""
        Nom: {a}
        Prenom: {b}
        Genre: {c}
        age: {d}
        Nationalite:{f}
        Nombre de cours:{h}
        semestre : {m}
        ___________________________________________________
        """)

            break


button = CTkButton(root, text="Enter data", height=45, command=fontction)
button.grid(row=3, column=0, sticky="ew", padx=10)

if __name__ == '__main__':
    root.mainloop()
