"""
Best Line: Given a two-dimensional graph with points on it, find a line which passes the most
number of points. 
"""

from collections import defaultdict

def find_line_with_most_points(points):
    max_count = 0  # Maximum number of points on a line
    best_line = None  # Line with the most points

    # Iterate over each pair of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Calculate the slope and y-intercept of the line
            if x2 - x1 == 0:  # Handle vertical lines
                slope = float('inf')
                y_intercept = x1
            else:
                slope = (y2 - y1) / (x2 - x1)
                y_intercept = y1 - slope * x1

            # Count the number of points on the line
            count = 0
            for k in range(len(points)):
                x, y = points[k]
                if y == slope * x + y_intercept:
                    count += 1

            # Update the line with the most points if necessary
            if count > max_count:
                max_count = count
                best_line = (slope, y_intercept)

    return best_line[0], best_line[1]


# Example usage
points = [(1, 2), (2, 4), (3, 6), (5, 8), (5, 10), (6, 12), (7, 14), (8, 16), (3, 18), (10, 10)]
best_slope, best_intercept = find_line_with_most_points(points)

print("Line with the most points:")
print(f"Slope: {best_slope}")
print(f"Intercept: {best_intercept}")


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(0, 10, 2)
ypoints = xpoints * best_slope + best_intercept
plt.plot(xpoints,ypoints)
plt.plot([point[0] for point in points], [point[1] for point in points], 'kx')
plt.show()