from collections import Counter

def solution(n, wires):
    def find(x):
        if x == par[x]:
            return x
        return find(par[x])
    
    def unite(x, y):
        x, y = find(par[x]), find(par[y])
        if x == y:
            return
        
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
                
    edges = len(wires)
    answer = edges
    for i in range(edges):
        par = [i for i in range(n+1)]
        rank = [0]*(n+1)
        for j in range(edges):
            if j != i:
                a, b = wires[j]
                unite(a, b)
        
        for k in range(n+1):
            parent = par[k]
            while par[k] != par[parent]:
                par[k] = par[parent]
                parent = par[k]
                
        counter = Counter(par[1:])
        c_list = [c for c in counter]
        answer = min(answer, abs(counter[c_list[0]] - counter[c_list[1]]))
    
    return answer