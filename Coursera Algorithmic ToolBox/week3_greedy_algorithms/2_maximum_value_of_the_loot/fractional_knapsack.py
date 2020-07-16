# Uses python3
import sys

def get_optimal_value(capacity, weights, values,n):
    lst = []
    value = 0.
    for i in range(n):
        lst.append((values[i], weights[i]))
    
    lst.sort(key = lambda x: x[0]/x[1], reverse = True)

    for v,w in lst:
    	if capacity == 0:
    		return value
    	a = min(w,capacity)
    	value += a*(v/w)
    	capacity -= a
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values,n)
    print("{:.4f}".format(opt_value))
