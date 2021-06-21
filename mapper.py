import sys

for line in sys.stdin:
    line = line.strip().split()

    source = line[0]
    distance = line[1]

    neighbors = 0
    if len(line) > 2:
        neighbors = line[2]
    
    path = source
    
    if len(line) > 3:
        path = line[3]
        elements = path.split('->')
        if elements[len(elements) - 1] !+ source:
            path = line[3] + '->' + source
    print(source + ' node ' + str(distance) + ' ' + neighbors + ' ' + str(path))

    if neighbors:
        adj_list = neighbors.split(':')
        for i in range(len(adj_list) - 1):
            neighbor_data = adj_list[i].split(',')
            neighbor = neighbor_data[0]
            curr_path = path + '->' + neighbor
            neighbor_dist = distance + int(neighbor_data[1])
            print(neighbor + ' value ' + str(neighbor_dist) + ' ' + curr_path)

    

