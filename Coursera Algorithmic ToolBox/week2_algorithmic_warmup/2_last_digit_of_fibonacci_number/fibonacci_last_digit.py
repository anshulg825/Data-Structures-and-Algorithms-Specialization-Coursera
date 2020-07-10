# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2,n+1):
    	arr.append( (arr[i - 1]%10) + (arr[i - 2]%10) ) 
    return (arr[n]%10)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
