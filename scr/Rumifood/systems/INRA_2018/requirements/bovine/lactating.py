
## ID : dictionaire pour les race


besUFL = besUFL_np + besUFL_gest + besUFL_PL + besUFL_RC

IC = ind_CIrace * ind_CIstade * (3.2 + (0.015 * live_weight))

def intake_capacity (breed:str,live_weight:int,milk_production:float,body_condition:float,gestation_week:int,lactation_week:int) ->float :

    if breed =="limousine":
        IC_breed=0.95
    if breed =="dairy crossbreeds":
        IC_breed=0.90
    IC_breed=1
    
    if gestation_week >=38 or lactation_week <=2:
        IC_stade = 0.93
    if lactation_week <= 4:
        IC_stade = 0.98
    if lactation_week <= 4:
        IC_stade = 0.98
    if lactation_week >4 and <=8:
        IC_stade = 1
    if lactation_week >8 and <=12:
        IC_stade = 1.02

    #SUMPLIFICATION
    IC_par = 1
    if gestation_week > 0 :
        IC_body = 0.002
    if lactation_week > 0 :
        IC_body = 0.0015
    intake_capacity= ( IC_breed *IC_stade *IC_par *
                      (3.2 + (0.015 * live_weight) + (0.25 * milk_production) -
                       IC_body * live_weight *(body_condition -2.5)) 
                       )
    return intake_capacity


#def ufl_need ()