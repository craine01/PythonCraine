#userInput3 

work = input("Are you currently working? (yes/no) ")
if work.lower() == "yes":
    job = input("What is your job? ")
    print("You work as a " + job + ". That's great!")
else:
    print("Flagged as unemployed. Please consider finding a job before going abroad.")

visa = input("What is your purpose of going abroad? (work/study/travel) ")
if visa.lower() == "work":
    print("You will need a work visa. Please check the requirements for the country you plan to go to.")
elif visa.lower() == "study":
    print("You will need a student visa. Please check the requirements for the country you plan to go to.")
elif visa.lower() == "travel":
    print("You will need a tourist visa. Please check the requirements for the country you plan to go to.")
else:
    print("Invalid input. Please enter 'work', 'study', or 'travel'.")
