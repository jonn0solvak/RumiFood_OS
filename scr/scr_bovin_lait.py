import sqlite3
import math as mh
#from data import class_lot_and_animals 



milk_production_year =5500 #l/year/Darry Cow
lactation_day_year = 305 
milk_production_day = milk_production_year/ lactation_day_year
pic_milk_mean = 23
tp = 32
tb = 38

lactation_week = 12
gestation_week = 6
# calculde la production lait potentiel

def potential_milk_prod_primipare (pic_milk, lactation_week, gestation_week):
    potential_milk_prod = ( pic_milk *
        ( -0.55 + (1.66 * mh.exp(-0.0065* lactation_week)) -
         (0.72 * mh.exp(-0.44 * lactation_week))-
         (0.69 * mh.exp(-0.16 * (45-gestation_week)))) 
         )
    return (potential_milk_prod)

def potential_milk_prod_multipare (pic_milk, lactation_week, gestation_week):
    potential_milk_prod = ( pic_milk *
        ( -0.83 + (1.92 * mh.exp(-0.0085* lactation_week)) -
         (0.74 * mh.exp(-0.88 * lactation_week))-
         (0.50 * mh.exp(-0.12 * (45-gestation_week)))) 
         )
    return potential_milk_prod

def potencial_tb (tb_mean, lactation_week):
    tb = ( tb_mean * 
          (0.87 + (0.52 * mh.exp(-0.62 * lactation_week))+ (0.005 * lactation_week)) 
        )
    return tb

def potencial_tp (tp_mean, lactation_week):
    tp = ( tp_mean * 
          (0.9 + (0.60 * mh.exp(-0.78 * lactation_week))+ (0.006 * lactation_week)) 
        )
    return tp