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
LW_calf = 35

milk_production =5500
lactation_day_year = 305
milk_production_day = milk_production/ lactation_day_year
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



#### besoin PDI (A APPROFONDIR)
eff_proteique = 1 ### a précisé

unproductive_pdi_need = (0.312 * live_weight) + ((0.2*live_weight**0.6)/eff_proteique)  ## + besPDI_PEF = MSI × [5 × (0,57 + 0,0074 × MOND)]/EffPDI
productive_pdi_need = (tp * milk_production_day)/eff_proteique
if gestation_week != 0:
    gestation_pdi_need = (0.0448 * LW_calf * mh.exp(0.111 * gestation_week))/EffPDI 
else gestation_pdi_need = 0

pdi_need = unproductive_pdi_need + productive_pdi_need + gestation_pdi_need 


#### besoin UFL
activity_index = 1.1
maintenance_ufl_need = 0.0536 * (live_weight**0.75) * activity_index
production_ufl_need = milk_production_day *(0.42 + (0.0053 * (tb - 40)) +(0.0032 * (tp - 31))) 
if gestation_week != 0:
    gestation_ufl_need = 0.000695 * LW_calf * mh.exp(0.116 * gestation_week)
else gestation_ufl_need = 0

ufl_need = maintenance_ufl_need + production_ufl_need + gestation_ufl_need



if __name__ == "__main__":
    print(ufl_need, maintenance_ufl_need,growth_ufl_need,production_ufl_need)
