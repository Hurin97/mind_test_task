from Figures.Shape import Shape


class Circle(Shape):

    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
        self.pi = 3.14


    def get_area(self):
        super().get_area()
        return self.pi * self.radius ** 2