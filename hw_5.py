# Author: Sunil Shah 
# Description: This is HW5 for CSCI 6221
# Date : 03/02/2020

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
def validate_input(params):
    try:
        new_params = [float(x) for x in params]
        for x in new_params:
            if x <= 0:
                print("Input parameters are incorrect. Please enter positive numers only.")
                print()
                return None
        return new_params
    except ValueError:
        print("Input parameters are incorrect. Please enter valid numeric input.")
        return None

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
            params = input("Please enter the base and height of the triangle separated by space:")
            validated_params = validate_input(params.split())
            print("Validate params",validated_params)
            print()
            if validated_params and len(validated_params) == 2:
                    triangle = Triangle(validated_params[0], validated_params[1])
                    print("The area of triangle with base {} and height {} is {}".format(triangle.base, triangle.height, triangle.calculate_area()))
            else:
                print("Please enter the correct number of parameters.")
                print()

        elif option == 'b':
            print("We are calculating the area of Rectangle.")
            params = input("Please enter the length and width of rectangle separated by space:")
            validated_params = validate_input(params.split())
            if validated_params and len(validated_params) == 2:
                rectangle = Rectangle(validated_params[0], validated_params[1])
                print("The area of rectangle with length {} and width {} is {}".format(rectangle.length, rectangle.width, rectangle.calculate_area()))
            else:
                print("Please enter the correct number of parameters.")

        elif option == 'c':
            print("We are calculating the area of Square.")
            params = input("Please enter the length of the square:")
            validated_params = validate_input(params.split())
            if validated_params and len(validated_params) == 1:
                square = Square(validated_params[0])
                print("The area of square with length {} is {}".format(square.length, square.calculate_area()))
            else:
                print("Please enter the correct number of parameters.")
                print()

        elif option == 'd':
            print("We are calculating the area of Circle.")
            params = input("Please enter the radius of the circle:")
            validated_params = validate_input(params.split())
            if validated_params and len(validated_params) == 1:
                circle = Circle(validated_params[0])
                print("The area of circle with radius {} is {}".format(circle.radius, circle.calculate_area()))
            else:
                print("Please enter the correct number of parameters.")
                print()
                
        elif option == 'e':
            print("We are calculating the area of Parallelogram.")
            params = input("Please enter the base and height of the parallelogram separated by space:")
            validated_params = validate_input(params.split())
            if validated_params and len(validated_params) == 2:
                parallelogram = Parallelogram(validated_params[0], validated_params[1])
                print("The area of parallelogram with base {} and height {} is {}".format(parallelogram.base, parallelogram.height, parallelogram.calculate_area()))
            else:
                print("Please enter the correct number of parameters.")
                print()

        elif option == 'f':
            print("Exiting the program.")
            break

main_menu()