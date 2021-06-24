import sys

data = {
    'min_dist': 1000,
    'curr_node': None,
    'curr_min_node': None,
    'neighbors': None
}

for line in sys.stdin:
    line = line.rstrip().split(' ')

    line_type = line[1]
    node = int(line[0])
    distance = int(line[2])

    if line_type == 'A':
        if data['curr_node'] is not None:
            if data['curr_min_node'] is None:
                data['curr_min_node'] = node
            print("{} {} {} {}".format(data['curr_node'], data['min_dist'], data['neighbors'], path))

        data['neighbors'] = line[3]
        path = line[4]

        data['curr_node'] = node
        data['curr_min_node'] = node
        data['min_dist'] = distance

    elif line_type == 'B':
        if distance < data['min_dist']:
            data['min_dist'] = distance
            data['curr_min_node'] = node
            path = line[3]


print("{} {} {} {}".format(data['curr_node'], data['min_dist'], data['neighbors'], path))