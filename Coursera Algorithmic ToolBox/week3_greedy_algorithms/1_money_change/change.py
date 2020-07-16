# Uses python3
import sys

def get_change(m):
    #write your code here
    no_ten = int(m/10)
    no_five = int((m - no_ten*10)/5)
    no_one = m - no_ten*10 - no_five*5
    sum = no_five + no_ten + no_one
    return sum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
