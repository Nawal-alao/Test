from customtkinter import *

root = CTk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("500x500")
root.title("word counter")
text = CTkTextbox(root, border_color="grey", border_width=1, font=("Avenir", 15))
text.insert(0.0, text="Entrer le text...")
text.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)


def Stockage():
    liste = text.get(0.0, END)
    mot = 0
    for i in liste:
        if i == " " or i == "'":
            mot += 1

    button.configure(text=f"Nombre de mot: {mot+1}", text_color="white")
    button.place(x=360, y=10)


button = CTkButton(root, text="RUN", text_color="red", corner_radius=30,
                   height=10, width=30, fg_color="transparent", command=Stockage
                   )
button.place(x=450, y=10)

root.mainloop()
