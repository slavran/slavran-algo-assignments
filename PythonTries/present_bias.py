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
#print(cost)
#visited=[False for x in graph.keys()]
def findPaths(g,s,t,path=[],paths=[]):
    visit=[False for x in graph.keys()]
    stringIssues=list(g.keys())
    visit[stringIssues.index(s)]= True
    path.append(s)
    mid=[]
    #print(path)
    if s==t:
        mid = path.copy()
        paths.append(mid)
        #print(paths)
    else:
        for x in g[s]:
            if not visit[stringIssues.index(x)]:
                paths =findPaths(g,x,t,path)
    path.pop()
    visit[stringIssues.index(s)]= False
    return paths
####stop here
#
#
# continue
def findCost( path, price):
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
  ###$stop here
  ###
  ###continue
  ##stop here
  ###
  ###continue
def findMinCostPath(minCost,path):
     cost =99999999999999999
     for x in range(len(minCost)-1):

         if  minCost[x]<cost :
            index = x
            cost=minCost[x]
     print(path[index],minCost[index])
####stop here
###
###continue
def bestPath(costs):
    ex=-1
    for i in range(len(costs)) :
        #print("help!")
        if costs[i] != -1:
            ex=i
            break #WE NEED TO FIND AN I THAT ITS NOT -1

    for k in range(ex,len(costs)):
        if costs[k] != -1 and costs[k] <=costs[ex] :
            ex = k
        #    print("help!!!")
    return ex
####stop here
###
###continue
def findGuyPath(paths,bias,pathCost):
    firstNode=paths[0][0]
    while firstNode!=paths[0][len(paths)-1]:
        biasCost=[]
    #    print("hel")
        for x in paths :
            #print("help")
            if x[0] ==firstNode:
                biasCost.append(getBiasCost(x,bias,pathCost))
                x.remove(firstNode)
            else:
                biasCost.append(-1)
        guyPath=bestPath(biasCost)
        firstNode=paths[guyPath][0]
    return guyPath
####stop here
###
###
def getBiasCost(path,b,pathCost):
    counter = 1
    cost=0
    cost1=0
    for k in range(len(path)-1):
    #    print("h")
        for p in pathCost:
    #        print("he")
            if p[0]==path[k] and p[1]==path[k+1] :
                if counter == 1:
                    cost1 =  int(p[2])
#                    print(cost1)
                else :
                    cost1 =p[2]*b
                    # print(cost1)
                cost= cost + int(cost1)
        counter = counter + 1
    return cost
####stop here
###
###
way=findPaths(graph,args.start,args.end)
realCost=findCost(way,cost)
findMinCostPath(realCost,way)
b=args.parameter
way1=[]
for p in way:
    way1.append(p.copy())

#print(way1)
index = findGuyPath(way1,b,cost)
#print (index,way)
print (way[index],realCost[index])
