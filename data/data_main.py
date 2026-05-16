import sqlite3

# recuperé le nom des tableau
with sqlite3.connect('data\INRA_2018.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    print(tables)


def obtenir_donnees_aliment(nom_aliment, type_aliment):
    """
    Récupère les données soit dans la table 'fourrages', soit 'concentres'.
    type_aliment doit être 'fourrages' ou 'concentres'
    """
    # Sécurité : On vérifie que la table demandée est valide 
    # (car on ne peut pas utiliser le '?' de SQL pour un nom de table)
    if type_aliment not in tables:
        raise ValueError("Type d'aliment invalide")

    conn = sqlite3.connect("data/INRA_2018.db")
    cursor = conn.cursor()
    
    # Construction sécurisée de la requête
    requete = f"SELECT ufl, pdi, ms FROM {type_aliment} WHERE Code_INRA = ?"
    cursor.execute(requete, (nom_aliment,))
    resultat = cursor.fetchone()
    conn.close()
    
    if resultat:
        return resultat
    return None

if __name__ == "__main__":
    
    alim1 = obtenir_donnees_aliment("FV0020","fourrages")
    alim2 = obtenir_donnees_aliment("FE1250","fourrages")
    alim3 = obtenir_donnees_aliment("CN0190","concentres")
    print(alim1 , alim2 , alim3)