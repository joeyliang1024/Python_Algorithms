#賣長度為i的道路可得pi元，如何切割一條長度為n之道路可使總輸入最大？
#pi: list P 的第i項
def road_cutting_DP(P: list, n: int):
    # R紀錄販售長度為i的道路所能獲的最大收入
    R = [0 for i in range(n + 1)]
    # C紀錄長度為i之最佳切法中第一段的長度，用來重建最佳切法
    C = [0 for i in range(n + 1)]
    R[0] = 0
    for j in range(1, n + 1): #這裡要記得+1
        s = float("-inf")
        for i in range(1, j + 1): #這裡要記得+1
            if s < P[i] + R[j - i]:
                s = P[i] + R[j - i]
                C[j] = i
        R[j] = s
    return R, C, R[-1]

P = [0, 1, 3, 8, 8, 9, 10, 18, 18, 23, 25]
R, C , max_cost = road_cutting_DP(P, 10)
print(f"價目表：{P}")
print(f"各長度的最大收入:{R}")
print(f"切法陣列：{C}")
print(f"最大收入：{max_cost}")
