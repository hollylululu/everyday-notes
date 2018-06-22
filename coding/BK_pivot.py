import sys
sys.setrecursionlimit(100)

class BkPivot:
    def __init__(self, G):
        self.data = G

    def find_best_pivot(self, graph):
        high = 0
        vertex = None
        for v in graph:
            if len(graph[v]) > high:
                high = len(graph[v])
                vertex = v
        return v

    def get_neighbors(self, v):
        neighbors = set()
        for ele in self.data[v]:
            neighbors.add(ele)
        for ele in self.data:
            for s in self.data[ele]:
                if s == v:
                    neighbors.add(ele)
        return neighbors

    def BkMain(self, R, P, X):
        if not P and not X:
            return R
        for v in self.data:
            neighbors = self.get_neighbors(v)
            R.update(v)
            P - neighbors
            X - neighbors
            self.BkMain(R, P, X)
            P.remove(v)
            X.update(v)

    def get_args(self):
        vertex_set = {'start'}
        for v in self.data:
            vertex_set.update(v)
        vertex_set.remove('start')
        return vertex_set

def main():
    import json
    with open(sys.argv[1]) as f:
        data = json.load(f)
    tester = BkPivot(data)
    #print tester.find_best_pivot(data)
    print tester.get_neighbors('c')

if __name__ == "__main__":
    main()


