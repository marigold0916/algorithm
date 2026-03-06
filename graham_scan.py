import numpy as np
import matplotlib.pyplot as plt

# 임의 점들 생성: P는 최저점
points = np.array([
    [2, 4],   # 0번
    [5, 2],   # 1번
    [0, 2],   # 2번
    [1, 1],   # 3번 -> P (최저점)
    [4, 5],   # 4번
    [3, 3],
    [7, 2],
    [3, 5]    # 5번
])
p_idx = np.lexsort((points[:,0], points[:,1]))[0]
P = points[p_idx]
def polar_angle(p):
    return np.arctan2(p[1] - P[1], p[0] - P[0])
def dist_p(p):
    return (p[0] - P[0])**2 + (p[1] - P[1])**2
other_point = np.delete(points, p_idx ,axis=0)
sorted_indices = np.lexsort((dist_p(other_point),polar_angle(other_point)))
sorted_points = other_point[sorted_indices]
def ccw(a, b, c):
    val = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if val > 0: return 1
    if val < 0: return -1
    return 0
stack = [P, sorted_points[0]]
for next_points in sorted_points[1:]:
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], next_points)<=0:
        stack.pop
    stack.append(next_points)
convex_hull = np.array(stack)
print(convex_hull)
plt.figure(figsize=(8,6))
plt.scatter(points[:, 0], points[:, 1], color='gray', label='All Points')
hull_plot = np.vstack([convex_hull, convex_hull[0]])
plt.plot(hull_plot[:, 0], hull_plot[:, 1], 'r-', linewidth=2, label='Convex Hull')
plt.legend()
plt.show()