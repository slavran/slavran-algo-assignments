import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename",help ="name of input file")
parser.add_argument("graphFile",help = "put your graph file")
parser.add_argument('-parameter',help = "how logical is this guy to 0-1",default=1)
parser.add_argument("start",help = "First node")
parser.add_argument("end",help = "end node" )
args=parser.parse_args()
graph{}
