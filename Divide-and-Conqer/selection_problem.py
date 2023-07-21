#n個相異數，求第k小的數
import math
import statistics
from merge_sort import merge_sort

def select(A: list, k: int):
    piece_size = 5
    # 將A分成五個一堆
    split_A = [A[i:i + piece_size] for i in range(0, len(A), piece_size)]
    # 每組做sorting (這裡使用之前寫過的merge sort)
    for split in split_A:
        merge_sort(split, 0, len(split) - 1)
    medians_A = [statistics.median_low(split) for split in split_A]
    p = statistics.median_low(medians_A)
    S1 = [i for i in A if i < p]  # 蒐集比p小的數
    S2 = [i for i in A if i > p]  # 蒐集比p大的數
    # 要知道p是第幾小算S1的長度就知道了
    if k <= len(S1):
        return select(S1, k)
    elif k > len(A) - len(S2):
        return select(S2, k - len(S1) - 1) # -1是減去p
    else:
        return p


A = [12, 4, 544, 23, 7, 1, 123, 3]
print(A)
print("第{}小的數是：{}".format(7, select(A, 7)))
