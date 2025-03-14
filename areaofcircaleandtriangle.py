class Shape:
    def area(self, radius=None, length=None, breadth=None):
        if radius is not None:
            return 3.14 * radius * radius  
        elif length is not None and breadth is not None:
            return length * breadth  
        else:
            return "Invalid input"

s = Shape()
print("Area of circle:", s.area(radius=5))
print("Area of rectangle:", s.area(length=4, breadth=6))
