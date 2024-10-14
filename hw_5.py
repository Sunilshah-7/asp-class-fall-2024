# Author: Sunil Shah 
# Description: This is HW5 for CSCI 6221
# Date : 03/02/2020
# If you get any indentation error while running this code, you can directly copy the code from this repository
# https://github.com/Sunilshah-7/asp-class-fall-2024/blob/main/hw_5.py
# Shape class with an abstract method to calculate area
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass
    

# Triangle class that inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
# Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
# Square class that inherits from Shape
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return self.length * self.length
    
# Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
# Parallelogram class that inherits from Shape
class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height 

    def calculate_area(self):
        return self.base * self.height

#  Validation of input for any shape
def validate_input(params, expected_length):
    try:
        new_params = [float(x) for x in params]
        if len(new_params) != expected_length:
            print("Input parameters are incorrect. Please enter correct number of parameters.")
            return None
        for x in new_params:
            if x <= 0:
                print("Input parameters are incorrect. Please enter positive numbers only.")
                print()
                return None   
        return new_params
    except ValueError:
        print("Input parameters are incorrect. Please enter valid numeric input.")
        return None

def get_validated_input(prompt, expected_length):
    while True:
        params = input(prompt)
        validated_params = validate_input(params.split(), expected_length)
        if validated_params and len(validated_params) == expected_length:
            return validated_params


# Main Menu to select the shape
def main_menu():
    while True:
        print("#################################################################")
        print("Select the shape of polygon you want to compute the area:")
        print("a. Triangle")
        print("b. Rectangle")
        print("c. Square")
        print("d. Circle")
        print("e. Parallelogram")
        print("f. Exit")
        print("#################################################################")
        print()
        option = input("Enter your choice:")
        if option == 'a':
            print("We are calculating area of Triangle.")
            validated_params = get_validated_input("Please enter the base and height of triangle separated by space (in ft):", 2)
            triangle = Triangle(validated_params[0], validated_params[1])
            print("The area of triangle with base {} and height {} is {} sq ft.".format(triangle.base, triangle.height, triangle.calculate_area()))
            print()

        elif option == 'b':
            print("We are calculating the area of Rectangle.")
            validated_params = get_validated_input("Please enter the length and width of rectangle separated by space (in ft):", 2)
            rectangle = Rectangle(validated_params[0], validated_params[1])
            print("The area of rectangle with length {} and width {} is {} sq ft.".format(rectangle.length, rectangle.width, rectangle.calculate_area()))
            print()

        elif option == 'c':
            print("We are calculating the area of Square.")
            validated_params = get_validated_input("Please enter the length of the square (in ft):", 1)
            square = Square(validated_params[0])
            print("The area of square with length {} is {} sq ft.".format(square.length, square.calculate_area()))
            print()

        elif option == 'd':
            print("We are calculating the area of Circle.")
            validated_params = get_validated_input("Please enter the radius of the circle (in ft):", 1)
            circle = Circle(validated_params[0])
            print("The area of circle with radius {} is {} sq ft.".format(circle.radius, circle.calculate_area()))
            print()
                
        elif option == 'e':
            print("We are calculating the area of Parallelogram.")
            validated_params = get_validated_input("Please enter the base and height of parallelogram separated by space (in ft):", 2)
            parallelogram = Parallelogram(validated_params[0], validated_params[1])
            print("The area of parallelogram with base {} and height {} is {} sq ft.".format(parallelogram.base, parallelogram.height, parallelogram.calculate_area()))
            print()

        elif option == 'f':
            print("Exiting the program.")
            break

main_menu()