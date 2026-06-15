#nested loop
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range (rows):
    for j in range(columns):
        print("*", end=" ")
    print()  # Move to the next line after printing each row
    
