#給定一個陣列，其中具有最大元素和之subarray為何？
#Divide: 分成兩個小的陣列，B & C
#Conquer: 分別計算B & C的 max-subarray
#Combine: 合併時也要計算跨B & C的陣列以免漏掉
import math

def max_subarray(A: list):
    if len(A) == 1:
        return A[0]

    mid = math.floor(len(A) / 2)
    B = A[:mid]
    C = A[mid:]

    lmax = max_subarray(B)
    rmax = max_subarray(C)
    cmax = max_crossing_subarray(A, mid)

    return max(lmax, rmax, cmax)

def max_crossing_subarray(A: list, mid: int):
    #計算包含floor(len(A)/2) 和 floor(len(A)/2)這兩個值的max-subarray
    left_sum = float('-inf')
    right_sum = float('-inf')
    current_sum = 0

    for i in range(mid - 1, -1, -1):
        current_sum += A[i]
        if current_sum > left_sum:
            left_sum = current_sum

    current_sum = 0
    for i in range(mid, len(A)):
        current_sum += A[i]
        if current_sum > right_sum:
            right_sum = current_sum

    return left_sum + right_sum

A = [12, 4, 544, 23, 7, 1, 123, 3, 1, 6]
result = max_subarray(A)
print("Maximum Subarray Sum:", result)
