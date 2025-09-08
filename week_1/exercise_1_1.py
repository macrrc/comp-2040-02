# code file for exercise 1.1 
# Calculating area of rectangles

def area_rectangle(length, width):
    return length * width

rectangles = [
    {"name": "first", "length": 10, "width": 5},
    {"name": "second", "length": 15, "width": 7}
]

for rectangle in rectangles:
    # calculate the area
    area = area_rectangle(rectangle["length"], rectangle["width"])
    # print the output
    print(f"Area of {rectangle["name"]} rectangle: {area}")

# Calculating area of circles
radius1 = 4
area_circle1 = 3.14 * (radius1 ** 2)

radius2 = 6
area_circle2 = 3.14 * (radius2 ** 2)

print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)