day = input("Enter the day of the week: ")
age = input("Enter your age: ")

if day == "Monday":
    print("We are closed on Monday.")

elif age < 6 or age > 65:
    print("You get in free.")

elif day == "Tuesday" or day == "Thursday":
    print("You pay half price today!")

elif day == "Wednesday" and 13 <= age <= 20:
    print("You pay half price today!")

elif (6 <= age <= 12) and (day == "Saturday" or day == "Sunday"):
    print("You pay half price today!")

else:
    print("You pay full price.")
