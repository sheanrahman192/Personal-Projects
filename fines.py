#nhc2cv
#Shean Rahman

def fine(speed_limit, my_speed, zone= ""):
    if my_speed < speed_limit - 10:
        return 30

    elif my_speed >= (speed_limit + 20):
        return 350

    elif my_speed > speed_limit and zone == "":
        return (my_speed - speed_limit) * 6

    elif my_speed > speed_limit and zone == "school" or zone == "work":
        return (my_speed - speed_limit) * 7

    elif my_speed > speed_limit and zone == "residential":
        return ((my_speed - speed_limit) * 8) + 200

    else:
        return 0


def demerits(speed_limit, my_speed):
    if my_speed <= speed_limit:
        return 0
    elif my_speed >= speed_limit + 20:
        return 6
    elif my_speed >= speed_limit + 10:
        return 4
    elif my_speed >= speed_limit + 1:
        return 3