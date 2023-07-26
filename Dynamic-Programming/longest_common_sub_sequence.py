# 給定X = "X1x2...xn"，Y = "y1y2...yn"，Z = "z1z2...zn"為三個字串
# (1)若存在遞增數列"i1i2...in"使得xi=zj，j=1,...,k，則稱Z為X的子序列
# (2)若Z為X之子序列且為Y之子序列，則稱Z為X與Y之共同子序列
# 如何求X與Y之最長的共同子序列(LCS)?

def LCS(X: str, Y: str):
    m = len(X)
    n = len(Y)
    s = [[0 for i in range(n + 1)] for j in range(m + 1)]
    r = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(n + 1):
        s[0][i] = 0
    for i in range(1, m + 1):
        s[i][0] = 0
        for j in range(1, n + 1):
            # 字符一樣
            if X[i - 1] == Y[j - 1]:
                # 共同長度+1
                s[i][j] = s[i - 1][j - 1] + 1
                r[i][j] = "↖"
            elif s[i - 1][j] > s[i][j - 1]:
                print(s[i - 1][j], s[i][j - 1])
                s[i][j] = s[i - 1][j]
                r[i][j] = "←"
            else:
                s[i][j] = s[i][j - 1]
                r[i][j] = "↑"
    return s, r

def print_LCS(X, Y, r, i, j):
    # none words
    if i == 0 or j == 0:
        return ""
    # same word in same idx
    # 往左上移動: x, y 座標個減一
    if r[i][j] == "↖":
        return print_LCS(X, Y, r, i - 1, j - 1) + X[i - 1]
    # 往左移動: x 座標個減一
    elif r[i][j] == "←":
        return print_LCS(X, Y, r, i - 1, j)
    # 往上移動: y 座標個減一
    else:
        return print_LCS(X, Y, r, i, j - 1)


X = "GTACG"
Y = "GTCA"

S, R = LCS(X, Y)

for i in range(len(Y) + 1):
    for j in range(len(X) + 1):
        print("{:3d}".format(S[j][i]), end=" ")
    print("")

print("======================================")

for i in range(len(Y) + 1):
    for j in range(len(X) + 1):
        print("{:3}".format(R[j][i]), end=" ")
    print("\n")

print("======================================")
print(f"X: {X}")
print(f"Y: {Y}")
print("Longest Common Subsequence:", print_LCS(X, Y, R, len(X), len(Y)))
