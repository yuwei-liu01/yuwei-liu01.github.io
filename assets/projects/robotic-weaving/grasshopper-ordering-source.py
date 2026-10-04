# Extracted from 0831/IK模型最终调试0831.gh.
import ghpythonlib.treehelpers as th

# Assume points_A and points_B are the two input sets of points
points_A = list(points_A)
points_B = list(points_B)

# Initialize an empty list to store the ordered points
combined_points = []

# Assume both sets have an equal number of points (e.g., 27points each)
for i in range(len(points_A)):
    if i % 2 == 0:  # When i is even
        combined_points.append(points_A[i])
        combined_points.append(points_B[i])
    else:  # When i is odd
        combined_points.append(points_B[i])
        combined_points.append(points_A[i])

# Output the ordered points
a = th.list_to_tree(combined_points)
