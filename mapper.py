import sys

graph = {}

for line in sys.stdin:
    line = line.rstrip().split(' ')
    
    node = line[0]
    idx = int(node)

    graph[idx] = {
        'dist': int(line[1]),
        'neighbors': None,
        'path': node
    }

    if len(line) > 2:
        graph[idx]['neighbors'] = line[2]

    if len(line) > 3:
        graph[idx]['path'] = line[3]
        elements = graph[idx]['path'].split('->')
        if elements[len(elements) - 1] != node:
            graph[idx]['path'] = graph[idx]['path'] + '->' + node

    print("('{}', 'A', '{}', '{}', '{}')".format(node, graph[idx]['dist'], graph[idx]['neighbors'], graph[idx]['path']))


    if len(graph[idx]['neighbors']):
        elems = graph[idx]['neighbors'].split(':')
        for i in range(len(elems) - 1):
            elem = elems[i].split(',')
            neighbor = elem[0]
            weight = elem[1]
            curr_path = graph[idx]['path'] + '->' + neighbor
            new_dist = graph[idx]['dist'] + int(weight)
            print("('{}', 'B', '{}', '{}')".format(neighbor, new_dist, curr_path))