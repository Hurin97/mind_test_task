from Figures.Shape import Shape
import math as m

class Triangle(Shape):

    def __init__(self, a, b, c) -> None:
        super().__init__()
        if (a + b) > c and (a + c) > b and (b + c) > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise Exception("Please check triangle inequality before entering")
    
    def get_perimeter(self):
        return self.a + self.b + self.c     
    

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2
        area = m.sqrt((half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c) * half_perimeter)
        return area


    def is_right_triangle(self):
        longest_side = self.c
        b = self.b
        a = self.a
        if (longest_side - a) < 0:
            longest_side, a = a, longest_side
        if (longest_side - b) < 0:
             longest_side, b = b, longest_side
        print(longest_side,a , b)
        if longest_side ** 2 == a ** 2 + b ** 2:
            return True
        else:
            return False