# exception handling error, exception = an event that interrupts the flow of a program 
#           (ZeroDivisionError, TypeError, ValueError)
#           1. Try 2. Except, 3. Finally

try:
    number = int(input("Enter a number: "))
    print(10/number)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed.")
