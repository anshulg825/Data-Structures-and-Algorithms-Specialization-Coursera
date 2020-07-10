# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, min(a,b)+1):
        if a % l == 0 and b % l == 0:
        	gcd = l
    lcm = (a*b / gcd)
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(lcm_naive(a, b)))

