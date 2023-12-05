from tkinter import *
import sqlite3

#création fenêtre 
root = Tk()
root.title('Formulaire')
root.geometry("450x450")

#gestion BD
conn = sqlite3.connect('formulaire.db')
c = conn.cursor()
# c.execute('''CREATE TABLE user (
#           matricule text,
#           prenom text,
#           nom text,
#           email text,
#           tel integer
# )''')

def submit():
    conn = sqlite3.connect('formulaire.db')
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (:matricule, :prenom, :nom, :email, :tel)",
    {
        'matricule':e_matricule.get(),
        'prenom':e_prenom.get(),
        'nom':e_nom.get(),
        'email':e_email.get(),
        'tel':e_tel.get()              
    }
    )
    conn.commit()
    conn.close()

    #Effacer les entrées
    e_matricule.delete(0, END)
    e_prenom.event_delete(0, END)
    e_nom.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)

def afficher():
    conn = sqlite3.connect('formulaire.db')
    c = conn.cursor()

    c.execute("SELECT *, oid from user ")
    records = c.fetchall()

    p_records = ""

    for record in records:
        p_records += str(record) + "\n"
    
    query_label = Label(root, text=p_records)
    query_label.grid(row=7, column=0, columnspan=2)

    conn.commit()
    conn.close()

    
#Création des labels et entrées
matricule = Label(root, text="Matricule :")
prenom = Label(root, text="Prénom :")
nom = Label(root, text="nom :")
email = Label(root, text="email :")
tel = Label(root, text="tel :")

e_matricule = Entry(root, width=35)
e_prenom = Entry(root, width=35)
e_nom = Entry(root, width=35)
e_email = Entry(root, width=35)
e_tel = Entry(root, width=35)

matricule.grid(row=0, column=0, padx=15, pady=20)
e_matricule.grid(row=0, column=1, padx=15)

prenom.grid(row=1, column=0, padx=15)
e_prenom.grid(row=1, column=1, padx=15)

nom.grid(row=2, column=0, padx=15, pady=20)
e_nom.grid(row=2, column=1, padx=15)

email.grid(row=3, column=0, padx=15)
e_email.grid(row=3, column=1, padx=15)

tel.grid(row=4, column=0, padx=15, pady=20)
e_tel.grid(row=4, column=1,padx=15)

#Bouton SAVE
save = Button(root, text="Enregistrer", width=30, command=submit)
save.grid(row=5, column=1, columnspan=2)

show_records = Button(root, text="Voir les enregistrements", width=30)
show_records.grid(row=6, column=1, columnspan=2, pady=15)

conn.commit()
conn.close()

root.mainloop()

