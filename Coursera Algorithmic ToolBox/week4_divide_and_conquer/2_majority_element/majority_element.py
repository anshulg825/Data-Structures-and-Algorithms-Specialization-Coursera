# Uses python3
import sys
from collections import Counter

def get_majority_element(a, left, right):
    counts = Counter()
    for x in a:
        counts[x] += 1
        if counts[x] > len(a) // 2:
            return 1
    return -1
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
