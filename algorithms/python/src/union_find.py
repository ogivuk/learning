class UnionFind:

    def __init__(self, N):
        self.numberOfObjects = N
        objects = []
    
    def union(self, p, q):
        raise NotImplementedError()
    
    def connected(self, p, q):
        raise NotImplementedError() 