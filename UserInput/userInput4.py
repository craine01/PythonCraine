# userInput4 

country = input("What is your dream country? ")
print("Your dream country is " + country + ". I would also love to visit " + country + " someday!")
visa = input("Do you think you will need a visa to go to " + country + "? (yes/no) ")
if visa.lower() == "yes":
    print("You will need a visa to go to " + country + ". Please check the requirements for the country you plan to go to.")
else:
    print("You may not need a visa to go to " + country + ". Please check the requirements for the country you plan to go to.")
nature = input("Do you like nature? (yes/no) ")
if nature.lower() == "yes":
    print("That's great! " + country + " has many beautiful natural attractions to explore.")
else:
    print("That's okay! " + country + " also has many cultural and historical attractions to explore.")
year = input("When do you plan to go to " + country + "? ")
print("If you're planning to go to " + country + " in " + year + ". It also means that you have a lot of time to prepare for your trip! Make sure to research the culture, customs, and language of " + country + " to make the most of your experience.")
