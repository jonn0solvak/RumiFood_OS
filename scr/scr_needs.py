import sqlite3
import math as mh
# NB: mh.log = ln

### Calcule de des besoin: 
##  race
##  Productivité lait(l/VL/an)  
##  Stade de lactation
##  nombre

### Donnée
body_condition = 2.5
live_weight = 650 #kg
batch_age = None # months
lactation_week = 22 # months
gestation_week = 10 # months
turnover= 0.3 # Pourcentage
nb_darry_cow = 100 
LW_calf = 35 #kg

dmi = 18 # kg MS/j

milk_production_year =5500 #l/year/Darry Cow
lactation_day_year = 305 
milk_production_day = milk_production_year/ lactation_day_year
tp = 32
tb = 38

# calculde la production lait potentiel
potential_milk_prod = 30.3 #data base


# calucle incice CI
ind_lactation = 0.65 + (1 - 0.65) * (1 - mh.exp(-0.25 * lactation_week))
ind_gestation = 0.8 + 0.2*(1 - mh.exp(-0.25*(40-gestation_week)))
# ind_pdi = 0.91 + (0.115 / (1+ mh.exp(0.13*(90- pdi_total/ufl_total))))
ind_pdi_initial_BL = 0.67

#### calcule de la capacité d'ingestion
intake_capacity =   ((14.25 +
                    (0.015 * (live_weight - 600)) +
                    (0.11 * potential_milk_prod) + 
                    ((2.5 - body_condition))) 
                    * ind_lactation * ind_gestation 
                    * ind_pdi_initial_BL
                     #* ind_pdi
                     )



#### besoin PDI (A APPROFONDIR)
eff_proteique = 1 ### a précisé

unproductive_pdi_need = (0.312 * live_weight) + ((0.2*live_weight**0.6)/eff_proteique)  ## + besPDI_PEF = MSI × [5 × (0,57 + 0,0074 × MOND)]/EffPDI
productive_pdi_need = (tp * milk_production_day)/eff_proteique
if gestation_week != 0:
    gestation_pdi_need = (0.0448 * LW_calf * mh.exp(0.111 * gestation_week)#/EffPDI
    ) 
else: gestation_pdi_need = 0

pdi_need = unproductive_pdi_need + productive_pdi_need + gestation_pdi_need 


#### besoin UFL 

### Récupéré l'index d'activité dans doc
activity_index = 1.1
maintenance_ufl_need = 0.0536 * (live_weight**0.75) * activity_index
production_ufl_need = milk_production_day *(0.42 + (0.0053 * (tb - 40)) +(0.0032 * (tp - 31))) 
if gestation_week != 0:
    gestation_ufl_need = 0.000695 * LW_calf * mh.exp(0.116 * gestation_week)
else: gestation_ufl_need = 0
if batch_age == None or batch_age > 40:
    gain_ufl_need = 0
else: gain_ufl_need = 3.14 - (0.077 * batch_age)

ufl_need = maintenance_ufl_need + production_ufl_need + gestation_ufl_need + gain_ufl_need

#### Besoin mineraux
# 
# ca_abs_need = ( (0.663 * dmi) +
#                 (0.008 * live_weight) + 
#                 (1.25 * milk_production_day ) +
#                 (23.5 / (1 + mh.exp(19.1 - 5.46 * mh.log(gestation_week)))) +
#                 (-0.189 * batch_age + 8.03)
#                 )
# 
# p_abs_need =((0.83 * dmi) + 
#              (0.002 * live_weight) + 
#              (0.9 * milk_production_day ) +
#              (7.38 / (1 + mh.exp(19.1 - 5.46 * mh.log(gestation_week)))) +
#              (-0.112 * batch_age + 4.76)
#              )
# 

if __name__ == "__main__":
    print(intake_capacity, maintenance_ufl_need,gain_ufl_need,production_ufl_need)
