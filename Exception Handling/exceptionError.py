# file handling error

try:
    teyvat = input("Enter which region of teyvat you want to join: ")
    
    if teyvat.isdigit():
        raise ValueError("Please enter a valid region name, not a number.")

except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"You have successfully joined the {teyvat} region of Teyvat!")

finally:
    print("Thank you for using the abyss.")