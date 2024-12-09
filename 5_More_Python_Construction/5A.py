import numpy as np
from matplotlib import pyplot as plt
# measurements.py
def crow(pointA, pointB):
    """
    Distance between points A and B "as the crow flies."
        PointA = (x1, y1, z1)
        PointB = (x2, y2, z2)
    Returns sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    """
    distance = np.sqrt( (pointA[0] - pointB[0])**2 + \
                        (pointA[1] - pointB[1])**2 + \
                        (pointA[2] - pointB[2])**2 )
    return distance


if __name__ == '__main__':
    test_points = np.array([
        [-1, 0, -1],
        [2, 4, -1],
    ])

    distance_AB = crow(test_points[0], test_points[1])
    print(f"Distance between points {test_points[0]} and {test_points[1]} is {distance_AB}")

