#1010

'''can use
import math

def calculate_combinations(m, n):
    return math.comb(m,n)
'''

#manual implementation
def factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def calculate_combinations(m, n):
    return factorial(m) // (factorial(n) * factorial(m-n))

t = int(input())
for i in range(t):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    print(calculate_combinations(m, n))