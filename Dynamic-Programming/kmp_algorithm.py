# The string matching problem
# 給定T[1...n]為一篇文章，P[1...m]為一段字串，m<n，若T[s+1...s+m] = p[1...m]，
# 0≤s≤n-m，則稱s為valid shift，如何找到所有的P在T之valid shift (即所有pattern
# P在文章中出現的位置)？

# KMP想法：利用已經已經比對過的資訊將pattern一次shift多個位置
# 0 | 1 2 3 4 5 | 6 7 8 | 9 10 11 12 13 14 15 16
# --------------------------------------------
# T | a b c a b | a b a | b  a  a  b  a  b  a  a
#               ---------
# P |       a b | a b a | a
#               ---------
#   |           | a b a | b  a  a     可配對的最大長度： 
#               ---------             由 prefix function 負責算出

def KMP(T: str, P: str):
    m = len(P)
    n = len(T)
    pi = prefix_function(P)
    result = []
    k = 0
    for i in range(1, n + 1):
        while k > 0 and P[k] != T[i - 1]:
            k = pi[k]
        if P[k] == T[i - 1]:
            k += 1
        if k == m:
            result.append(i - m)
            k = pi[k]
    return result

def prefix_function(P: str):
    m = len(P)
    pi = [0] * (m + 1)
    k = 0
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k]
        if P[k] == P[i]:
            k += 1
        pi[i + 1] = k
    return pi

T = "aababbababbbababbaaabbababbaaa"
P = "ababbaaa"
result = KMP(T, P)
print(result)
