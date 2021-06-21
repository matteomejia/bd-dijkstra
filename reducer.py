import sys
import math

min_dist = math.inf
curr_min_node = None
neighbors = None
curr_node = None

def emit(path):
    print(str(curr_node) + ' ' + str(min_dist) + ' ' + neighbors + ' ' + path)

for line in sys.stdin:
    line = line.strip().split()
    source = int(line[0])
    obj_type = line[1]
    dist = int(line[2])

    if obj_type == 'node':
        if curr_node:
            if curr_min_node:
                curr_min_node = source
            emit(path)
        path = line[4]
        neighbors = line[3]
        curr_node = source
        min_dist = dist
        curr_min_node = source
    else:
        if dist < min_dist:
            min_dist = dist
            curr_min_node = source
            path = line[3]

emit(path)
