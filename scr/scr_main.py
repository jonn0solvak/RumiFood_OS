import numpy as np
import math as mh
import sqlite3

def obtenir_donnees_aliment(nom_aliment, type_aliment):
    """
    Récupère les données soit dans la table 'fourrages', soit 'concentres'.
    type_aliment doit être 'fourrages' ou 'concentres'
    """
    # Sécurité : On vérifie que la table demandée est valide 
    # (car on ne peut pas utiliser le '?' de SQL pour un nom de table)
    if type_aliment not in ["fourrage", "concentre"]:
        raise ValueError("Type d'aliment invalide")

    conn = sqlite3.connect("data/INRA_2018.db")
    cursor = conn.cursor()
    
    # Construction sécurisée de la requête
    requete = f"SELECT ufl, pdi, ms FROM {type_aliment} WHERE Code_INRA = ?"
    cursor.execute(requete, (nom_aliment,))
    resultat = cursor.fetchone()
    conn.close()
    if resultat:
        return {"ufl": resultat[0], "pdi": resultat[1], "ms": resultat[2]}
    return None

if __name__ == "__main__":
    print (obtenir_donnees_aliment("FV0020","fourrages") )
    print("hello")

