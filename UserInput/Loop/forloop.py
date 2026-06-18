# for loop 
# for variable in sequence:
for caffaine in["coffee", "tea", "coke"]:
    print(caffaine)
    print("I like " + caffaine)
# range() function
for number in range(1, 6 + 1):
    print(f"{caffaine} is for table {number}")
# for loop with list
for number in range(1, 6 + 1):
    print(f"{number} {caffaine} is {number**2}")
# for loop with list
squares = []
for number in range(1, 6 + 1):
    squares.append(number**2)       
print(squares)
# for loop with list comprehension
squares = [number**2 for number in range(1, 6 + 1)]
print(squares)