import sqlite3
import math as mh
# NB: mh.log = ln

### Donnée
body_condition = 2.5
live_weight = 650 #kg
batch_age = 18 # months
lactation_week = 12 # week
gestation_week = 1 # week
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

### Récupéré l'index d'activité dans doc
activity_index = 1.1

#### besoin UFL 
def ufl_need (live_weight, activity_index, milk_production_day, tb, tp, LW_calf, gestation_week, batch_age ):
    maintenance_ufl_need = 0.0536 * (live_weight**0.75) * activity_index
    production_ufl_need = milk_production_day *(0.42 + (0.0053 * (tb - 40)) +(0.0032 * (tp - 31))) 
    if gestation_week != 0:
        gestation_ufl_need = 0.000695 * LW_calf * mh.exp(0.116 * gestation_week)
    else: gestation_ufl_need = 0

    if batch_age == None or batch_age > 40:
        gain_ufl_need = 0
    else: gain_ufl_need = 3.14 - (0.077 * batch_age)

    ufl_need = maintenance_ufl_need + production_ufl_need + gestation_ufl_need + gain_ufl_need
    return ufl_need



#### besoin PDI 
eff_pdi = 0.67 ### a précisé

def pdi_need (live_weight, eff_pdi, tp, milk_production_day, LW_calf, gestation_week, batch_age,dmi=None,MOND=None):

    if eff_pdi <= 0:
        raise ValueError("eff_pdi doit être strictement positif.")

    unproductive_pdi_need = ( 0.312 * live_weight + 
                          ((0.2*live_weight**0.6)/eff_pdi))
    if dmi is not None or MOND is not None :
         unproductive_pdi_need = unproductive_pdi_need + (dmi * (5 * (0.57 + 0.0074 * MOND))/eff_pdi)
    
    productive_pdi_need = (tp * milk_production_day)/eff_pdi
    
    if gestation_week != 0:
        gestation_pdi_need = (0.0448 * LW_calf * mh.exp(0.111 * gestation_week) /eff_pdi) 
    else: gestation_pdi_need = 0

    if batch_age == None or batch_age > 40:
            gain_ufl_need = 0
    else: gain_ufl_need = (270 - 6.66 * batch_age) /eff_pdi

    pdi_need = unproductive_pdi_need + productive_pdi_need + gestation_pdi_need + gain_ufl_need
    return pdi_need



#### calcule de la capacité d'ingestion

def intake_capacity (live_weight,potential_milk_prod,body_condition,lactation_week, gestation_week, total_pdi= None, total_ufl = None):
     # calucle incice CI

    ind_lactation = 0.65 + (1 - 0.65) * (1 - mh.exp(-0.25 * lactation_week))
    ind_gestation = 0.8 + 0.2*(1 - mh.exp(-0.25*(40-gestation_week)))
    
    if total_pdi is None or total_ufl is None:
         ind_pdi = 0.67
    else:
        ind_pdi = 0.91 + (0.115 / (1+ mh.exp(0.13*(90- total_pdi/total_ufl))))
    
    intake_capacity =( (14.25 +
                    (0.015 * (live_weight - 600)) +
                    (0.11 * potential_milk_prod) + 
                    ((2.5 - body_condition))) *
                    ind_lactation * ind_gestation * ind_pdi
                     )
    return intake_capacity



##### quand on a une ration equilibré energie et prot, on peu passé au mineraux en conaisant la MSI 

### Besoin mineraux

def ca_need (dmi, live_weight, milk_production_day, gestation_week, batch_age):
    ca_maintenance = 0.663 * dmi + 0.008 * live_weight
    ca_lactation = 1.25 * milk_production_day
    ca_grow = -0.189 * batch_age + 8.03
    ca_abs_need = ca_maintenance + ca_lactation + ca_grow
     
    if gestation_week >=25:
        ca_abs_need = ca_abs_need + (23.5 / (1 + mh.exp(18.8 - 5.03 * mh.log(gestation_week))))
    return ca_abs_need 

def p_need (dmi, live_weight, milk_production_day, gestation_week, batch_age):
    p_maintenance = 0.83*dmi+0.002*live_weight
    p_lactation = 0.90 * milk_production_day
    p_grow = -0.112 * batch_age + 4.76
    p_abs_need =p_maintenance + p_lactation + p_grow
    if gestation_week >=25:
        p_abs_need = p_abs_need + (7.38 / (1 + mh.exp(19.1 - 5.46 * mh.log(gestation_week))))
    return p_abs_need 



if __name__ == "__main__":

    ufl = ufl_need(live_weight,activity_index,milk_production_day,tb,tp,LW_calf,gestation_week,batch_age)
    pdi = pdi_need(live_weight,eff_pdi,tp, milk_production_day, LW_calf, gestation_week, batch_age)
    ic = intake_capacity(live_weight,potential_milk_prod,body_condition,lactation_week,gestation_week,pdi,ufl)
    ca = ca_need(dmi,live_weight, milk_production_day,gestation_week, batch_age)
    p = p_need(dmi,live_weight, milk_production_day,gestation_week, batch_age)

    out= (ic,ufl,pdi,ca,p)


    print(out)