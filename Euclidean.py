## Definition of points:
points = [(1, 5), (4, 12), (3, 7), (0, 4)]

## Function for Euclidean:
def euclideanDistance(po1, po2):
    return round(((po2[0] - po1[0]) ** 2 + (po2[1] - po1[1]) ** 2) ** 0.5, 3)

## Calculating distances:
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

## Finding the minimum distance:
min_distance = min(distances)

## Logging:
print("Distances between points:", distances)
print("Shortest distance:", min_distance)
