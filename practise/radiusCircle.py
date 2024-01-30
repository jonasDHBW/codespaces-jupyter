import math

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    area = math.pi * radius**2
    return area

def main():
    try:
        # Get user input for radius
        radius = float(input("Enter the radius of the circle: "))
        
        # Calculate and display the area
        area = calculate_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
