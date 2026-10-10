import sys
import os

# Remonte jusqu'à la racine ton_projet/
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from scr.Rumifood.systems.INRA_2018.requirements.bovine.Dairy.scr_needs import *

body_condition = 2.5
live_weight = 650 #kg
lactation_week = 12 # week
gestation_week = 1 # week
turnover= 0.3 # Pourcentage
nb_darry_cow = 100 
LW_calf = 35 #kg


batch_age = 18 # months

dmi = 18 # kg MS/j
milk_production_year =5500 #l/year/Darry Cow
lactation_day_year = 305 
milk_production_day = milk_production_year/ lactation_day_year
tp = 32
tb = 38
# calculde la production lait potentiel
potential_milk_prod = 30.3 #data base

### Récupéré l'index d'activité dans doc
activity_index = 1.1
print(intake_capacity(live_weight,potential_milk_prod,body_condition,lactation_week,gestation_week))
ufl = ufl_need(live_weight,activity_index,milk_production_day,tb,tp,LW_calf,gestation_week,batch_age)
pdi = pdi_need(live_weight,eff_pdi,tp, milk_production_day, LW_calf, gestation_week, batch_age)
ic = intake_capacity(live_weight,potential_milk_prod,body_condition,lactation_week,gestation_week,pdi,ufl)
ca = ca_need(dmi,live_weight, milk_production_day,gestation_week, batch_age)
p = p_need(dmi,live_weight, milk_production_day,gestation_week, batch_age)
out= (ic,ufl,pdi,ca,p)


if __name__ == "__main__":
    print(out)