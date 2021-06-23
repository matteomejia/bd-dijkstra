import random
density = 19

def print_graph(n):
    with open("graphs/graph_%d.txt" % n, "a") as f:
        graph = [[((i+1)%n, random.randint(1,100))] for i in range(n)]
        for i in range(n):
            new_connections = random.sample(range(n - 1), random.randint(0,density))
            if i in new_connections: new_connections.remove(i)
            for c in new_connections:
                graph[i].append((c, random.randint(1,100)))


        for i in range(n):
            node = graph[i]
            w = 0 if i == 0 else 999
            line = "{} {} ".format(i, w)
            for connection in node:
                line += str(connection[0]) + "," + str(connection[1]) + ":"
            print("{} / {}".format(i, n))
            f.write(line + "\n")

def print_safe_graph(n):
    with open("graphs/safe_graph_%d.txt" % n, "a") as f:
        graph = [[((i+1)%n, 1), ((n-1+i)%n, 2)] for i in range(n)]
        for i in range(n):
            w = 0 if i == 0 else 999
            line = "{} {} ".format(i, w)
            line += str(graph[i][0][0]) + "," + str(graph[i][0][1]) + ":" + str(graph[i][1][0]) + "," + str(graph[i][1][1]) + ":" + "\n"
            print("{} / {}".format(i, n))
            f.write(line)


# PC2
print_graph(100)
print_safe_graph(100)
# print_graph(1000)
# print_safe_graph(1000)
# print_graph(1000*1000)
# print_safe_graph(1000*1000)