class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2   #calculate the radius

    def calculate_circumference(self):
        return 2 * Circle.pi * self.radius  #use the formula for circle circumference

    def calculate_area(self):
        return Circle.pi * self.radius ** 2   #use the formula for circle area

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.pi * self.radius ** 2

# Test Code
circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")