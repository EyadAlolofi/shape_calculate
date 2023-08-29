
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle


def main():
    """
    The main function is the entry point of the program.
    """
    while True:
        print("\n----- Shape Calculator -----")
        print("1. Circle")
        print("2. Triangle")
        print("3. Rectangle")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            radius = float(input("Enter the radius of the circle: "))
            circleArea = Circle.calculateArea(radius)
            circlePerimeter = Circle.calculatePerimeter(radius)
            print(f"Circle Area: {circleArea:.2f}")
            print(f"Circle Perimeter: {circlePerimeter:.2f}")

        elif choice == 2:
            side1 = float(input("Enter the length of side 1: "))
            side2 = float(input("Enter the length of side 2: "))
            side3 = float(input("Enter the length of side 3: "))
            triangleArea = Triangle.calculateArea(side1, side2, side3)
            trianglePerimeter = Triangle.calculatePerimeter(side1, side2, side3)
            print(f"Triangle Area: {triangleArea:.2f}")
            print(f"Triangle Perimeter: {trianglePerimeter:.2f}")

        elif choice == 3:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangleArea = Rectangle.calculateArea(length, width)
            rectanglePerimeter = Rectangle.calculatePerimeter(length, width)
            print(f"Rectangle Area: {rectangleArea:.2f}")
            print(f"Rectangle Perimeter: {rectanglePerimeter:.2f}")

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()