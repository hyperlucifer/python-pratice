# command line utility can be used to excute comands in terminal
# they are programs that can be run by the termal

import argparse as ag
parser =ag.ArgumentParser()
parser.add_argument("arg1",help="description of arg1")
parser.add_argument("arg2",help="description of arg2")

args= parser.parse_args()

print(args.arg1)
print(args.arg2)