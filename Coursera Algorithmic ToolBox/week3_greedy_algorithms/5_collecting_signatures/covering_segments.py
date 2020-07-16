# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments,n):
    points = []
    segments.sort(key = lambda x: x[1])
    i = 0
    #print(segments)
    if segments[0][1]==segments[n-1][0]:
        points.append(segments[0][1])
    else:
        while i<n:
            curr = segments[i]
            while i< n-1 and curr[1]>=segments[i+1][0]:
                i = i+1
            points.append(curr[1])
            i = i +1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments,n)
    print(len(points))
    print(*points)
