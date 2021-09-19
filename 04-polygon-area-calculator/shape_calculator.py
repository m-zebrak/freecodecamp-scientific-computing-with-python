class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        return ('*' * self.width + '\n') * self.height if self.width <= 50 and self.height <= 50 else 'Too big for picture.'

    def get_amount_inside(self, shape: 'Rectangle') -> int:
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, width: int):
        super().__init__(width, width)

    def __str__(self) -> str:
        return f'Square(side={self.width})'

    def set_side(self, width: int):
        self.width = width
        self.height = width
