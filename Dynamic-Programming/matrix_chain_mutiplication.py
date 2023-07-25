# 給定n個矩陣A1...An，其中Ai大小為pi-1xpi，以何種括號法計算A1A2...An可使得純量
# 乘法次數最少？
# P矩陣表示說明：
# 若有四個矩陣，A1: 2x3, A2: 3x5, A3: 5x4, A4: 4x2
# 則P矩陣表示為 [2, 3, 5, 4, 2] （長度為矩陣數加一）

def matrix_chain(P: list):
    # P儲存n個矩陣之大小
    n = len(P)
    # 這裡n+1是為了方便計算迴圈值
    S = [[0 for i in range(n+1)] for j in range(n+1)] # 計算次數矩陣
    C = [[0 for i in range(n+1)] for j in range(n+1)] # 印出解法矩陣

    for i in range(1, n):
        S[i][i] = 0
    for l in range(2, n+1):
        for i in range(1, n - l + 1):  
            j = i + l - 1  
            S[i][j] = S[i][i] + S[i+1][j] + P[i-1] * P[i] * P[j] # 先乘後兩個
            C[i][j] = i # 補上這一行，書上沒有，沒這行C矩陣的值不對
            for k in range(i, j - 1):
                k += 1  # 實測下來要加一，少一數值不對 (書上沒有這行)
                r = S[i][k] + S[k + 1][j] + P[i-1] * P[k] * P[j] # 先乘前兩個
                if r < S[i][j]: # 比較次數
                    S[i][j] = r
                    C[i][j] = k  
    for i in range(len(S)):
        for j in range(len(S)):
            print("{:3d}".format(S[i][j]), end = " ")
        print("")
    print()
    for i in range(len(C)):
        for j in range(len(C)):
            print("{:3d}".format(C[i][j]), end = " ")
        print("")
    return S[1][n - 1], C

def print_parens(C: list, i: int, j: int):
    if i == j:
        print("A{}".format(i), end="")
    else:
        print("(", end="")
        print_parens(C, i, C[i][j])
        print_parens(C, C[i][j] + 1, j)
        print(")", end="")

# 測試程式
P = [2, 3, 5, 4, 2]
result, C = matrix_chain(P)
print("最少純量乘法次數:", result)
print("最佳的括號法:", end="")
print_parens(C, 1, len(P)-1)
