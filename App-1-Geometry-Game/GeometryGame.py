import turtle
from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):

        if  rectangle.lowleft.x < self.x < rectangle.upright.x and \
            rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):

        self.lowleft = Point(min(point1.x, point2.x), min(point1.y, point2.y))
        self.upright = Point(max(point1.x, point2.x), max(point1.y, point2.y))

    def area(self):
        return (self.upright.x- self.lowleft.x) * \
               (self.upright.y - self.lowleft.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):

        x_distance = self.upright.x - self.lowleft.x
        y_distance = self.upright.y - self.lowleft.y

        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(x_distance)
        canvas.left(90)
        canvas.forward(y_distance)
        canvas.left(90)
        canvas.forward(x_distance)
        canvas.left(90)
        canvas.forward(y_distance)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
              Point(randint(10, 400), randint(10, 400)))


# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()