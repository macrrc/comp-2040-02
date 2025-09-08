# code file for exercise 1.1 
# Calculating area of rectangles

def area_rectangle(length, width):
    return length * width

rectangles = [
    {"length": 10, "width": 5},
    {"length": 15, "width": 7}
]

area_rectangle1 = area_rectangle(rectangles[0]["length"], rectangles[0]["width"])
area_rectangle2 = area_rectangle(rectangles[1]["length"], rectangles[1]["width"])

# Calculating area of circles
radius1 = 4
area_circle1 = 3.14 * (radius1 ** 2)

radius2 = 6
area_circle2 = 3.14 * (radius2 ** 2)

print("Area of first rectangle:", area_rectangle1)
print("Area of second rectangle:", area_rectangle2)
print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)