class Graph:
    def __init__(self, n, adj_matrix):
        self.size = n
        self.points = {}
        for i in range(n):
            self.points[i] = []
        for j in range(n):
            for k in range(n):
                if adj_matrix[j][k] == '1' and k != j:
                    self.points[j].append(k)

    def __str__(self):
        return str(self.points)


class ReadGraphsFromFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading(self):
        graph_list = []
        with open(self.file_name, 'r') as f:
            while True:
                n = f.readline().replace('\\n', '')
                if not n:
                    break
                if len(n.split(" ")) > 1:
                    print("first string should consist one number")
                    quit()
                n = int(n)

                i = 0
                adj_matrix = []
                while i < n:
                    line = f.readline()
                    adj_matrix.append(line.replace('\\n', '').split())
                    i += 1

                graph_list.append(Graph(n, adj_matrix))

        return graph_list
