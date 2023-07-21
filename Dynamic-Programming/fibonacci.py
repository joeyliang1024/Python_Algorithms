#使用DP解Fibonacci數列
def fibonacci(n:int)->int:
    if n == 0 or n == 1:
        return n
    F = [0 for i in range(n)]
    F[0], F[1] = 0, 1
    for i in range(2, n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]    

print("第{}項：{}".format(10, fibonacci(10)))