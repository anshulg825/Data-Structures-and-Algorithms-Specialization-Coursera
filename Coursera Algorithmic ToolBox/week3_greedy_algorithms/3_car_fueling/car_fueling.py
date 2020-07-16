# python3
import sys


def compute_min_refills(distance, tank, n,stops):
    stops.append(distance)
    stops.insert(0,0)
    numrefills, current = 0, 0
    if distance<=tank:
        return 0
    else:
        while current<=n:
            lastrefill = current
            while (current<=n and (stops[current+1] - stops[lastrefill])<=tank ):
                current += 1
            if current == numrefills:
                return -1 
            if current<=n:
                numrefills = numrefills + 1
    return numrefills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n,stops))
