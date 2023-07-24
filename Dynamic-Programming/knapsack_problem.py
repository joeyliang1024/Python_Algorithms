# 給定n件物品：I1...In，第i件之價值為vi，負重為wi，在總重為正整數W之限制下
# 取物（每件物品可取部分），如何取物可使得獲利最大？

# Greedy
def fractional_knapsack(v:list, w:list, W:int):
    fractional_list = [(v[i]/w[i], i) for i in range(len(v))]
    fractional_list = sorted(fractional_list, reverse = True)
    total_cost = 0
    remaining_weight = W
    for fraction, index in fractional_list:
        weight = w[index]
        cost = v[index]
        # 放得下
        if remaining_weight >= weight:
            total_cost += cost
            remaining_weight -= weight
        # 放不下，將物品部分放入背包，並終止循環    
        else:
            fraction_taken = remaining_weight / weight
            total_value += fraction_taken * cost
            break

# Not Greedy
def zero_one_knapsack(n:int, v:list, w:list, W:int):
    s = [[0 for j in range(W+1)] for i in range(n+1)]
    # 沒有物品，一件不取
    for k in range(W+1):
        s[0, k] = 0
    # 物品數隨環圈遞增
    for i in range(n+1):
        s[i, 0] = 0 # 沒有負重
        for k in range(1, W+1):
            if k < w[i]:
                s[i, k] = s[i-1, k]
            else:
                s[i, k] = max(s[i-1, k], v[i] + s[i - 1, k - w[i]])
    return s[n, W]                