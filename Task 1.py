def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    result = calculate_area(length, width)

    if isinstance(result, (int, float)):
        print("The area of the rectangle is:",result)
    else:
        print(result)

main()