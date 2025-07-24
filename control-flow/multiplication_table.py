# multiplication_table.py

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 13):
    print(f"{number} * {i} = {number * i}")
