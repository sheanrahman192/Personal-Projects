# Name - Shean Rahman
# Computing ID - nhc2cv


Name = input("What player would you like to calculate statistics for? ")

Team_Name = input("What team was the opponent in the game you would like to calculate statistics for? ")

AttemptsFor3 = float(input("How many 3's did " + Name + " attempt this game? "))

MadeFor3 = float(input("How many 3's did " + Name + " make this game? "))

AttemptsFor2 = float(input("How many 2's did " + Name + " attempt this game? "))

MadeFor2 = float(input("How many 2's did " + Name + " make this game? "))

AttemptForFT = float(input("How many free throws did " + Name + " attempt this game? "))

MadeForFT = float(input("How many free throws did " + Name + " make this game? "))

FieldGoalPercentage = (MadeFor2+MadeFor3) / (AttemptsFor2+AttemptsFor3) * 100

FreeThrowPercentage = MadeForFT / AttemptForFT * 100

TotalPoints = (3*int(MadeFor3))+(2*int(MadeFor2))+int(MadeForFT)

print(Name, "had a", str(FieldGoalPercentage) + "% field goal percentage and a", str(FreeThrowPercentage) + "% free throw percentage")

print(Name, "scored", TotalPoints, "points against", str(Team_Name) + ". Wahoowa!")