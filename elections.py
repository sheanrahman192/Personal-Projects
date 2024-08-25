#Shean Rahman
#nhc2cv

country_winners = {}

def add_country_winner(country,votes):
    country_winner = ""
    count = 0
    for person,vote in votes.items():
        if vote > count:
            count = vote
            country_winner = person

    country_winners[country] = country_winner


def winner(population):
    cand_points = {}
    count = 0
    world_winner = ""

    if not population or not country_winners:
        return "No Winner"

    for pop_country, points in population.items():
        if pop_country in country_winners:
            candidate_winner = country_winners[pop_country]
            if candidate_winner in cand_points:
                cand_points[candidate_winner] += points
            else:
                cand_points[candidate_winner] = points

    for candidate, score in cand_points.items():
        if score > count:
            count = score
            world_winner = candidate

    return world_winner

def clear():
    global country_winners
    country_winners = {}

