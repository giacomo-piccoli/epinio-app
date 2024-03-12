import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle given its length and width.
    
    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    
    Args:
    base (float): The base of the triangle.
    height (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def main():
    print("Welcome to the Area Calculator!")
    print("Choose a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        if radius <= 0:
            print("Error: Radius must be a positive number.")
        else:
            area = calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is: {area:.2f}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive numbers.")
        else:
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base <= 0 or height <= 0:
            print("Error: Base and height must be positive numbers.")
        else:
            area = calculate_triangle_area(base, height)
            print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
