import customtkinter as ctk
import qrcode
from PIL import ImageTk, Image
import os


# Fonction pour générer et afficher le code QR
def generate_qr():
    text = text_entry.get()
    if text:
        # Générer le code QR
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        # Sauvegarder l'image temporairement
        img_path = "qr_code.png"
        img.save(img_path)

        # Ouvrir et afficher l'image dans l'interface
        img_show = Image.open(img_path)
        img_show = img_show.resize((250, 250))  # Redimensionner l'image
        img_tk = ImageTk.PhotoImage(img_show)

        qr_label.configure(image=img_tk)
        qr_label.image = img_tk  # Garder une référence à l'image
        status_label.configure(text="Code QR généré avec succès!", fg_color="green")
    else:
        status_label.configure(text="Veuillez entrer un texte.", fg_color="red")


# Configuration de l'interface
ctk.set_appearance_mode("dark")  # Mode sombre
ctk.set_default_color_theme("blue")  # Thème bleu

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Générateur de Code QR")
app.geometry("400x500")

# Élément d'entrée pour le texte
text_label = ctk.CTkLabel(app, text="Entrez le texte ou le lien :", font=("Arial", 14))
text_label.pack(pady=10)

text_entry = ctk.CTkEntry(app, placeholder_text="Texte ou lien", width=300, height=40)
text_entry.pack(pady=10)

# Bouton pour générer le code QR
generate_button = ctk.CTkButton(app, text="Générer Code QR", command=generate_qr)
generate_button.pack(pady=20)

# Label pour afficher le code QR
qr_label = ctk.CTkLabel(app, text="")
qr_label.pack(pady=10)

# Label pour le statut
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Lancer l'application
app.mainloop()

# Supprimez l'image temporaire après la fermeture de l'application (facultatif)
if os.path.exists("qr_code.png"):
    os.remove("qr_code.png")

