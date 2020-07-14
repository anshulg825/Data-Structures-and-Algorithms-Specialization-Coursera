# Uses python3
from sys import stdin
def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    p = 1
    previous , current = 0 ,1
    for i in range(2,m*m):
        previous, current = current, (previous+current)%m
    
        if (previous == 0 and current == 1):
            p = i+1
    z = n%p
    previous = 0
    current = 1
    for j in range(z-1):
        previous , current = current , previous + current        
    f = current%m
    return f  

if __name__ == '__main__':
    n = int(stdin.read())
    m = int(stdin.read())
    print(int(get_fibonacci_huge(n, m)))