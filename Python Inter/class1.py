class calculator:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        self.box = Point()
        self.box.x = self.num1
        self.box.y = self.num2
        return self.box

    def multiply(self):
        return self.num1* self.num2

# result = calculator(3,3)

# print(result.multiply())

class Point:
    """Represents a point in 2-D space."""

# class Rectangle:
#     """Represents a point in 3-D space."""


# blank = Point()
# blank.x = 45

# blank.x +=  50

# x = blank.x

# # print(f"this is a {3} {3}")

import copy
# copy_x = copy.copy(blank.x)
# print(copy_x)
# Tensor(1080,1920,4)

x = calculator(3,4)
x.sum()
y = copy.copy(x)

print(y.box)
print(x.box)

