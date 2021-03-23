def invert(c):
    return 2 if c == 1 else 1


class Checker:
    def __init__(self, graph):
        self.graph = graph
        self.coloring = [0] * graph.size
        self.flag = True
        # visited = [False] * V
        # for i in range(len(graph.points)):
        #     self.coloring.append(0)

    def color_dfs(self, v, color):
        self.coloring[v] = color

        for u in self.graph.points[v]:
            if self.coloring[u] == 0:
                self.color_dfs(u, invert(color))
            elif self.coloring[u] == color:
                self.flag = False
                break

    def print_results(self):
        if self.flag:
            print('Y')
            result = {1: [], 2: []}
            for v in range(len(self.coloring)):
                result[self.coloring[v]].append(v+1)

            result[1].sort()
            result[2].sort()

            f = open("out.txt", "a")
            result_string = str(result[1]) + "\n0\n" + str(result[2]) if result[1][0] < result[2][0] else str(result[2]) + "\n0\n" + str(result[1])
            f.write("Y\n" + result_string + "\n")
            f.close()
        else:
            print('N')
            f = open("out.txt", "a")
            f.write("N\n")
