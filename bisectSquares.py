"""
Bisect Squares: Given two squares on a two-dimensional plane, find a line that would cut these two
squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis. 
"""

# the imporant thing here is to recognise that for this to be true 
# the intersect line must go through both centres of squares

class Square:
    # generate squares
    # x, y and length
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l


def find_cutting_line(square1, square2):
    # Calculate the centers
    center1 = (square1.x + square1.l / 2, square1.y + square1.l / 2)
    center2 = (square2.x + square2.l / 2, square2.y + square2.l / 2)

    # in case centers overlap
    if center1 == center2:
        print('Centers overlap')
        return float('inf'),float('inf')

    # in case the x position of the centers is the same
    if center1[0] - center2[0] == 0:
        print('infinite gradent')
        return float('inf'),float('inf')
    
    # Calculate the line
    slope = (center2[1] - center1[1]) / (center2[0] - center1[0])
    intercept = center1[1] - slope * center1[0]
    return slope, intercept


square1 = Square(1, 2, 3)
square2 = Square(4, 5, 6)
slope, intercept = find_cutting_line(square1, square2)


print(f"The equation of the line is y = {slope}*x + {intercept}")


square1 = Square(1, 1, 3)
square2 = Square(1, 1, 3)
slope, intercept = find_cutting_line(square1, square2)
print(f"The equation of the line is y = {slope}*x + {intercept}")

square1 = Square(1, 1, 3)
square2 = Square(1, 2, 3)
slope, intercept = find_cutting_line(square1, square2)
print(f"The equation of the line is y = {slope}*x + {intercept}")