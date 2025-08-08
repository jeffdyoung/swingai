from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# Each inner list is a 1D vector (e.g., flattened landmarks)
a = [[1.0, 2.0], [3.0, 4.0]]
b = [[2.0, 3.0], [4.0, 5.0]]

alignment, distance = fastdtw(a, b, dist=euclidean)

print("Alignment:", alignment)
print("Distance:", distance)
