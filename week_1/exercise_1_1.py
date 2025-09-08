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
def area_circle(radius):
    return 3.14 * (radius ** 2)
 
# List of dictionaries for circles
circles = [
    {"name": "first", "radius": 4},
    {"name": "second", "radius": 6}
]
 
# For loop to read variable and print
for circle in circles:
    # calculate area
    area = area_circle(circle["radius"])
    # print the output
    print(f"Area of {circle['name']} circle: {area}")