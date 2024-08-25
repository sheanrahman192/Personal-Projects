#Shean Rahman
#nhc2cv

def instructor_lectures(department, instructor):
    class_list = []
    data_file = open((str(department)+".txt"), "r")
    for course in data_file.readlines():
        list_course = course.strip("\n").split('|')
        if list_course[4] == instructor and list_course[5] == "Lecture" and list_course[3] not in class_list:
            class_list.append(str(list_course[3]))
    data_file.close()
    return class_list

def compatible_classes(first_class, second_class, needs_open_space = False):
    course1_number = str(first_class.split("-")[0][-4:])
    course2_number = str(second_class.split("-")[0][-4:])
    section1 = str(first_class.split("-")[1])
    section2 = str(second_class.split("-")[1])
    department1 = str(first_class.split()[0])
    department2 = str(second_class.split()[0])
    datafile1 = open((department1 + ".txt"), "r")
    datafile2 = open((department2 + ".txt"), "r")
    for course1 in datafile1.readlines():
        course1_list = course1.strip("\n").split('|')
        if section1 == course1_list[2] and course1_number == course1_list[1]:
            for course2 in datafile2.readlines():
                course2_list = course2.strip("\n").split('|')
                if section2 == course2_list[2] and course2_number == course2_list[1]:
                    first_start_time = int(course1_list[12])
                    second_start_time = int(course2_list[12])
                    first_end_time = int(course1_list[13])
                    second_end_time = int(course2_list[13])
                    for i in range(7, 12):
                        if course1_list[i] == course2_list[i]:
                            if (second_start_time <= first_start_time <= second_end_time) or (second_start_time <= first_end_time <= second_end_time):
                                return False
                    if needs_open_space == True:
                        if int(course1_list[15]) >= int(course1_list[16]) or int(course2_list[15]) >= int(course2_list[16]):
                            return False
                    return True

    datafile1.close()
    datafile2.close()







