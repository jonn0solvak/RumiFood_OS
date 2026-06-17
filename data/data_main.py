import sqlite3
from class_aliment import *



def obtenir_donnees_aliment(nom_aliment, type_aliment):

    #On récupère le nom des table de la DB
    with sqlite3.connect("data/Data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in cursor.fetchall()]
        print(tables)

    #on selectionne que class utilisé
    if type_aliment == "fourrages":
        class_cible = fourrage_bl
        element_class = [champ.name for champ in fields(fourrage_bl)]
        list_colonnes_sql = ", ".join(element_class)
    else:
        class_cible = concentre_bl
        element_class = [champ.name for champ in fields(concentre_bl)]
        list_colonnes_sql = ", ".join(element_class)
    

    """
    Récupèration des données dans table.
    type_aliment doit être 'fourrages' ou 'concentres'
    """
    # On vérifie que la table demandée est valide 
    if type_aliment not in tables:
        raise ValueError("Type d'aliment invalide")

    #Connection et récuperation des infromation dans la DB
    conn = sqlite3.connect("data/Data.db")
    cursor = conn.cursor()
    
    # Construction sécurisée de la requête
    requete = f"SELECT {list_colonnes_sql}   FROM {type_aliment} WHERE ID_code = ?"
    cursor.execute(requete, (nom_aliment,))
    resultat = cursor.fetchone()
    conn.close()
    
    if resultat:
        return class_cible(*resultat)
    return None

# def liste_stock(nom_aliment, type_aliment): 

# PLUTOT DEF ALIMENT : EXTRERE LES ELEMENT UTILISER EN CALULE RATION + QUANTITE STOQUER

#Connection et récuperation des infromation dans la DB
conn = sqlite3.connect("data/Data.db")
cursor = conn.cursor()
    
# Construction sécurisée de la requête 
requete = f"SELECT ID_code, Quantite FROM Stock"
cursor.execute(requete)
resultat = cursor.fetchall()
conn.close()
print(resultat)

if __name__ == "__main__":
    
    alim1 = obtenir_donnees_aliment("FV0020","fourrages")
    alim2 = obtenir_donnees_aliment("FE1250","fourrages")
    alim3 = obtenir_donnees_aliment("CN0190","concentres")

    
    print(alim1.pdi,alim1.ee, alim2.pdi)


