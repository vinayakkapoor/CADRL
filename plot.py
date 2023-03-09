import matplotlib.pyplot as plt
import sys
import argparse

parser = argparse.ArgumentParser("Parse output files")
parser.add_argument('--file',type=str)
parser.add_argument('--save', type=str)
parser.add_argument('--show', type=str, default='true')
args = parser.parse_args()

path = args.file
saveType = args.save
showType = args.show

success_rate = []
failure_rate = []


find_in_line = "train in "

if path==None:
    print('Please provide a path to plot data')
    exit(1)

if "_test" in path:
    find_in_line = "test in "

with open(path,"r") as f:
    for line in f.readlines():
        if find_in_line in line:            
            success_rate.append(float(line[line.index("success")+14:line.index("failure")-2]))
            failure_rate.append(float(line[line.index("failure")+14:line.index("average")-2]))        

episodes = range(1,len(success_rate)+1)

plt.plot(episodes,success_rate,label='Success rate')
plt.plot(episodes,failure_rate, label='Failure rate')
plt.xlabel("Episodes")
plt.ylabel("Probability")
plt.ylim([0,1])

plt.legend(loc='best')
if saveType == "train":
    plt.savefig(path[:path.rfind('/')]+"/train.png")
    print("Saved!")
elif saveType == "switch":
    plt.savefig(path[:path.rfind('/')]+"/test_switchPos.png")
    print("Saved!")
elif saveType == 'X':
    plt.savefig(path[:path.rfind('/')]+"/test_X.png")
    print("Saved!")

if showType=='true':
    plt.show()

#print(success_rate)
