import math

# 素数判定関数
def isPrimeNum(n):
    # √nまで確認すればok
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
        else:
            return True

n = int(input())

print(isPrimeNum(n))