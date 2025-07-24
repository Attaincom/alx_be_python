def greet_user(name):
    """Function to greet the user with their name."""
    print(f"Hello, {name}! Welcome to the program.")

# Call the function
greet_user("Samuel")


def calculate_area(length, width):
    """Function to calculate the area of a rectangle."""
    area = length * width
    return area

def calculate_perimeter(length, width):
    """Function to calculate the perimeter of a rectangle."""
    perimeter = 2 * (length + width)
    return perimeter

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")


def check_even_odd(number):
    """Function to check if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage
num = int(input("Enter a number: "))
check_even_odd(num)
