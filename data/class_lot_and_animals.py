from dataclasses import dataclass, fields

@dataclass
class lot:
    ID_lot: int
    animal_numbers:int
    age_mean:int
    weeks_lactation:int
    weeks_gestation:int
    body_condition:float
    live_weight:int
    age_first_calving:int
    turnover:float
    LW_calf:float
    milk_production_year:int
    lactation_day_year:float
    tp:float
    tb:float

@dataclass
class stock:
    ID_stock:int
    ID_code:str
    Quantite:float
