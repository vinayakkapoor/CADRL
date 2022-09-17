import matplotlib.pyplot as plt
import sys

success_rate = []
failure_rate = []

path = sys.argv[1]
find_in_line = "train in "

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
plt.show()

#print(success_rate)
