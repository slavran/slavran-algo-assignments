import argparse
import pprint
parser = argparse.ArgumentParser()
#parser.add_argument("filename",help ="name of input file")
parser.add_argument("graphFile",help = "put your graph file")
parser.add_argument('parameter',help = "how logical is this guy to 0-1")
parser.add_argument("start",help = "First node")
parser.add_argument("end",help = "end node" )
args=parser.parse_args()
graph={}
#read the graphFile
cost=[]
with open(args.graphFile) as g:
    cost=[]
    for line in g:
        nodes=[str(x) for x in line.split()]
        if len(nodes)!=3:
            continue
        if nodes[0] not in graph:
            graph[nodes[0]] = []
        if nodes[1] not in graph:
            graph[nodes[1]] = []
        graph[nodes[0]].append(nodes[1])
        x = nodes[0],nodes[1],int(nodes[2])
        cost.append(x)
g.close()
way=[]
def findPaths(g,s,t,path=[],paths=[]):
    visit=[False for x in graph.keys()]
    stringIssues=list(g.keys())
    visit[stringIssues.index(s)]= True
    path.append(s)
    mid=[]
    if s==t:
        mid = path.copy()
        paths.append(mid)
    else:
        for x in g[s]:
            if not visit[stringIssues.index(x)]:
                paths =findPaths(g,x,t,path)
    path.pop()
    visit[stringIssues.index(s)]= False
    return paths

def findCost(path,price):
    pathCost=[]
    for x in path:
        cost = 0
        for i in range(len(x) - 1):
            sideA = x[i]
            sideB = x[i+1]
            for p in price:
                if p[0] ==sideA and p[1] ==sideB:
                    cost = cost + p[2]
        pathCost.append(cost)
    return pathCost

def findMinCostPath(minCost,path):
     cost =99999999999999999
     for x in range(len(minCost)-1):
         if  minCost[x]<cost :
            index = x
            cost=minCost[x]
     print(path[index],minCost[index])
     return len(path[index])

def findBiasCostPath(cost):
    min =10000
    index=0
    for c in range(len(cost)):
        if cost[c]!= -1:
            if cost[c] < min:
                min=cost[c]
                index =c
    return index

def findBiasCostAndPath(path,cost):
    costs = 0
    for p in range(len(path)-1):
        for c in cost:
            if path[p] == c[0] and path[p+1]==c[1]:
                costs = costs + c[2]
    print(path,costs)

def findGuyPath(paths,bias,pathCost,start,end):
    firstNode =start #take the Start node
    biasPath=[]
    biasPath.append(firstNode)
    while firstNode != end : #While start node != end node
        cost=[]
        bestNode=[]
        for x in paths :  #we take every path
            if x[0] == firstNode:
                 cost.append(getBiasCost(x,bias,pathCost))
                 x.remove(firstNode)
            else:
                cost.append(-1)
        firstNode=paths[findBiasCostPath(cost)][0]
        biasPath.append(firstNode)
    findBiasCostAndPath(biasPath,pathCost)

def getBiasCost(path,b,pathCost):
    counter = 1
    cost = 0
    k = float(b)
    for p in range(len(path) - 1) :
        for cp in pathCost :
            if path[p] == cp[0] and path[p+1] == cp[1]:
                if counter==1:
                    cost = cost + cp[2]
                    counter = counter+1
                else:
                    cost = cost + k*cp[2]
                    #print(type(cp[2]*b))
    return cost

way=findPaths(graph,args.start,args.end)
realCost=findCost(way,cost)
findMinCostPath(realCost,way)
way1=[]
for p in way:
    way1.append(p.copy())
index = findGuyPath(way1,args.parameter,cost,args.start,args.end)
