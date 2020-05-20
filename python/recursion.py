# 再帰関数を理解するためのサンプル
# 1...nまでの整数の和を求めるための関数
def sum(n):

    if n <= 0:
        return n
    else :
        return n + sum(n-1)
        # 10 + 9 + 8 + 7 + 6 .... 1

n = 10

# フォボナッチ数列(実用的ではない書き方。。)
def fibo(n):

    # 0 1 2 3 5 8 13....

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)                #  


MAX_N = 100
MEMO = [None] * (MAX_N + 1)  # 計算結果を保存する配列

# メモ化(一度計算した結果を保存して置く)
def fibo2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 計算済み？
    if MEMO[n]:
        return MEMO[n]

    r = fibo2(n-1) + fibo2(n-2)
    MEMO[n] = r  # 計算結果を保存
    return r

print(fibo2(100))



# 1 1 3 4 6 6 

# nums = list(map(int,input().split()))

# pre = 0
# tmp = []

# for num in nums:
#     if (num%2) != 0:
#         tmp.append(num)

#         pre = num
#         continue

#     elif num == pre:
#         tmp.append(num)
    
#     pre = num

# [print(t) for t in list(set(tmp))]
