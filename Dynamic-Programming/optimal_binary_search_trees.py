# 給定n個key k1<k2<k3...<kn，以及n+1個dummy keys: d0, d1, ..., dn，
# 假設k1被搜尋到之frequency為p1，d1被搜尋到之frequency為q1，如何建立一個
# expected search cost 最小之 binary search tree?
# dummy keys: 失敗搜尋的結果
# 成功搜尋成本 = 內部節點的level值 * pi 
# 失敗搜尋成本 = (失敗節點的level值-1) * qi
# 搜尋總成本 = 成功搜尋成本 + 失敗搜尋成本
# 整顆樹的Cost: 左子樹 cost + 右子樹 cost + root cost 
def OBST(p:list, q:list, n:int):
    # 存儲部分樹的最小成本，s[i][j] 表示以 ki 到 kj 這些鍵所構成的子樹的最小成本
    s = [[0 for j in range(n + 2)] for i in range(n + 2)]
    # 存儲部分樹的權重和，w[i][j] 表示以 ki 到 kj 這些鍵為內部節點的部分樹的權重
    # 和，即包含這些鍵的搜尋成本。
    w = [[0 for j in range(n + 2)] for i in range(n + 2)]
    # 存儲樹的根節點，root[i][j] 表示以 ki 到 kj 這些鍵所構成的子樹的根節點是哪
    # 個鍵 (kr)。
    root = [[0 for j in range(n + 1)] for i in range(n + 1)]
    # 初始化矩陣: 填上初始值
    for i in range(1, n + 2):
        s[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            s[i][j] = float('inf')  # 初始化 s[i][j] 為無限大
            # 以下程式為取 minimum
            for r in range(i, j + 1):
                # 整顆樹的Cost: 左子樹 cost + 右子樹 cost + root cost 
                t = s[i][r - 1] + s[r + 1][j] + w[i][j]
                if t < s[i][j]:
                    s[i][j] = t
                    root[i][j] = r

    return s, root

p = [None, 5, 2, 4, 3]
q = [3, 2, 3, 4, 2]
n = 4
S, Root = OBST(p, q, n)

print("最小成本 s 陣列:")
for i in range(1, len(S)):
    for j in range(i):
        print("   ", end = " ")
    for j in range(i, len(S)-1):
        print("{:3d}".format(S[i][j]), end=" ")
    print("")

print("\n根節點 root 陣列:")
for i in range(1, len(Root)):
    for j in range(i):
        print("   ", end = " ")
    for j in range(i, len(Root)):
        print("{:3d}".format(Root[i][j]), end=" ")
    print("")
print(f"最小成本：{S[1][n]}")