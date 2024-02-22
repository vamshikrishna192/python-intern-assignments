def calculating_area(length, width):
    if length == width:
        return "square"
    else:
        return length * width


length = float(input("Enter the length value: "))
width = float(input("Enter the width value: "))
result = calculating_area(length, width)
print("Area:", result)