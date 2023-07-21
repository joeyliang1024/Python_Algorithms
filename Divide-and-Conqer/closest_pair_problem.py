#給定平面上一堆點，找出最近的兩個點
import math

class point:
    #定義出平面的座標點
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

def compare_X_axis(a:point, b:point)->int:
    return (a.x_axis-b.x_axis)

def compare_Y_axis(a:point, b:point)->int:
    return (a.y_axis-b.y_axis)

def point_distance(a:point, b:point)->float:
    return math.sqrt(compare_X_axis(a, b)**2 + compare_Y_axis(a, b)**2)

def min(x, y):
    return x if x < y else y

def get_minimum_distance(P:list, n:int):
    #calculate the minimum distance in list P
    min_dist = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if point_distance(P[i], P[j]) < min_dist:
                min_dist = point_distance(P[i], P[j])
    return min_dist

def closest_pair(P):
    # 前置步驟：將點依據y軸排序
    P = sorted(P, key=lambda point: point.y_axis)
    if len(P) <= 3:
        return get_minimum_distance(P, len(P))
    # 將P均勻分布到左右
    mid = len(P) // 2
    L = P[:mid]
    R = P[mid:]
    # 遞迴分別求出左右的最短距離
    L_min_dist = closest_pair(L)
    R_min_dist = closest_pair(R)
    d = min(L_min_dist, R_min_dist)
    # 蒐集所有在 |point.x_axis - 中間點|<d 的點
    strip = []
    for i in range(len(strip)):
        if abs(P[i].x_axis - p[mid].x_axis) < d:
            strip.append(P[i])
    # 檢查其中的點
    min_dist = float("inf")
    strip = sorted(strip, key=lambda point: point.x_axis)
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j].y_axis - strip[i].y_axis) >= min_dist:
                break
            if point_distance(strip[i], strip[j]) < min_dist:
                min_dist = point_distance(strip[i], strip[j])

    return min(d, min_dist)

P = [point(0, 0), point(1,1), point(100, 100), point(25, 70), point(25,75)]
print("minimum distance:{}".format(closest_pair(P)))