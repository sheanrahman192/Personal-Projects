#Shean Rahman
#nhc2cv

import random

def gellish2(age_min=1, age_max=100):
    Age = random.randint(age_min, age_max)
    return float(191.5-(0.007*(Age**2)))

def in_target_range(hr, age_min = 1, age_max = 100):
    LowHR = gellish2(age_min, age_max) * 0.65
    HighHR = gellish2(age_min, age_max) * 0.85
    return LowHR <= hr <= HighHR
