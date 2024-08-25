#Shean Rahman
#nhc2cv

def get_name(movie):
    return movie[0]

def get_gross(movie):
    return movie[1]


def get_rating(movie):
    return movie[3]


def get_num_ratings(movie):
    return movie[4]

def better_movies(movie_name, movies_list):
    better_list = []
    for movie in movies_list:
        if movie_name == get_name(movie):
            rating = get_rating(movie)
            for movie in movies_list:
                if get_rating(movie) > rating:
                    better_list.append(movie)
        else:
            pass
    return better_list


def average(category, movies_list):
    total_value = 0
    average_list = []
    if category == "rating":
        for movie in movies_list:
            average_list.append(get_rating(movie))
    elif category == "gross":
        for movie in movies_list:
            average_list.append(get_gross(movie))
    elif category == "number of ratings":
        for movie in movies_list:
            average_list.append(get_num_ratings(movie))
    else:
        pass

    for x in average_list:
        total_value += x
    average = (total_value/(len(average_list)))

    return average
