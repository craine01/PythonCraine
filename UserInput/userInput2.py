# userInput2
mother = input("What is your mother's name? ")
print(f"Your mother's name is {mother}.")

father = input("What is your father's name? ")
print(f"Your father's name is {father}.")

sibling = input("Do you have any siblings? (yes/no) ")
if sibling.lower() == "yes":
    sibling_name = input("What is your sibling's name? ")
    print(f"Your sibling's name is {sibling_name}.")
else:
    print("You don't have any siblings.")
    

