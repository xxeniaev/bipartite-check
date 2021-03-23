from graph import ReadGraphsFromFile as Reader
from alg import Checker

if __name__ == '__main__':
    reader = Reader("in.txt")

    graph_list = reader.reading()

    f = open("out.txt", "w")
    f.close()

    for graph in graph_list:
        checker = Checker(graph)
        checker.color_dfs(1, 1)
        checker.print_results()
