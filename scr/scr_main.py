import sqlite3
import math as mh

### Calcule de des besoin: 
##  race
##  Productivité lait(l/VL/an)  
##  Stade de lactation
##  nombre

### Donnée
body_condition = 2.5
live_weight = 650
lactation_week = 22
gestation_week = 10
turnover= 0.3
nb_darry_cow = 100 

milk_production =5500
lactation_day_year = 305
tp = 32
tb = 38
# calculde la production lait potentiel
potential_milk_prod = 30.3 #data base

# calucle incice CI
ci_lactation = 0.65 + (1 - 0.65) * (1 - mh.exp(-0.25 * lactation_week))
ci_gestation = 0.8 + 0.2*(1 - mh.exp(-0.25*(40-gestation_week)))


# calcule de la capacité d'ingestion
intake_capacity =   ((14.25 +
                    (0.015 * (live_weight - 600)) +
                    (0.11 * potential_milk_prod) + 
                    ((2.5 - body_condition))) 
                    * ci_lactation * ci_gestation )



if __name__ == "__main__":
    print(intake_capacity)