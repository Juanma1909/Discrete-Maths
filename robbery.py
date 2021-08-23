from heapq import heappop,heappush
from sys import stdin

INF = float('inf')

def solve(srcs, banks):
    n = len(G)    
    heap = []
    visited = [0 for _ in range(n)]
    dist = [INF for _ in range(n)]
    for i in range(len(srcs)):
        heap.append([0, srcs[i]])
        dist[srcs[i]] = 0
    while len(heap):
        d, u = heappop(heap)
        if not visited[u]:
            for v, dv in G[u]:
                disT = d + dv
                if disT < dist[v]:
                    dist[v] = disT
                    heappush(heap,[dist[v],v])
            visited[u] = 1
    banksDist = []
    for i in range(len(banks)):
        banksDist.append([dist[banks[i]],banks[i]])
    banksDist.sort()
    if(len(banksDist)):
        resul = []
        i = len(banksDist) - 1
        tmp = banksDist[i] 
        resul.append(tmp)
        i -= 1
        while(i >= 0 and tmp[0] == banksDist[i][0]):
            resul.append(banksDist[i])
            i-= 1
        if(resul[0][0] == INF):
            print(len(resul),"*")
        else:
            print(len(resul), resul[0][0])

        i = len(resul) - 1
        resul.sort(reverse = True)
        while(i >= 0):
            print(resul[i][1], end ="")
            if(i):
                print(" ", end= "")
            i -= 1
        print()
    return


def main():
    global G
    G = []
    line = stdin.readline().strip()
    while len(line):
        line = line.split()
        N,M,P= int(line[0]),int(line[1]),int(line[3])        
        G = [[] for _ in range(N)]
        for i in range(M):
            line = stdin.readline().split()
            u, v, w = int(line[0]), int(line[1]), int(line[2]) 
            G[u].append([v, w])
            G[v].append([u, w])
        line = stdin.readline().split()
        banks = []
        for i in range(len(line)):
            banks.append(int(line[i]))
        srcs = []
        if P >=1:
            line = stdin.readline().split()
            for i in range(len(line)):
                srcs.append(int(line[i]))
            solve(srcs, banks)
        else:
            banks.sort(reverse = True)
            i = len(banks)-1
            print(len(banks), "*")
            while i >= 0:
                print(banks[i], end = "")
                if i:
                    print(" ", end = "")
                i -= 1
            print()
        line = stdin.readline().strip()
main()