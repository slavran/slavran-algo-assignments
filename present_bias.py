import argparse
import pprint
parser = argparse.ArgumentParser()
#parser.add_argument("filename",help ="name of input file")
parser.add_argument("graphFile",help = "put your graph file")
parser.add_argument('-parameter',help = "how logical is this guy to 0-1",default=1)
parser.add_argument("start",help = "First node")
parser.add_argument("end",help = "end node" )
args=parser.parse_args()
graph={}

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
            
