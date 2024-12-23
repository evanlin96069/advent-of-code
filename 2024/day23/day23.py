import networkx as nx

cliques = None

with open("input.txt") as f:
    G = nx.Graph([l.split('-') for l in f.read().split('\n')])
    cliques = list(nx.enumerate_all_cliques(G))

def part1():
    print(sum(any(a.startswith("t") for a in c) for c in cliques if len(c) == 3))


def part2():
    print(",".join(sorted(max(cliques, key=len))))


part1()
part2()
