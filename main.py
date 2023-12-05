import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('ma_base_de_donnees.db')
curseur = conn.cursor()

# Exécution d'une commande SQL pour créer une table
curseur.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        age INTEGER
    )
''')

# Insertion de données dans la table utilisateurs
curseur.execute("INSERT INTO utilisateurs (nom, prenom, age) VALUES (?, ?, ?)", ('Doe', 'John', 25))
curseur.execute("INSERT INTO utilisateurs (nom, prenom, age) VALUES (?, ?, ?)", ('Smith', 'Jane', 30))

# Supprimer toutes les données de la table utilisateurs
curseur.execute("DELETE FROM utilisateurs")

# Sélection de toutes les données de la table utilisateurs
curseur.execute("SELECT * FROM utilisateurs")
donnees = curseur.fetchall()

for ligne in donnees:
    print("\t".join(map(str, ligne)))

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()


