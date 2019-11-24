PI = 3.14

class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        """
        Calculate the AREA of the circle
        """
        area = PI * self.radius * self.radius
        return "%.2f" % area
    
    def get_perimeter(self):
        """
        Caclculate the perimeter of the circle
        """
        return 2 * PI * self.radius