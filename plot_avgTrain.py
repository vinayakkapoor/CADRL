import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("Parse output files")
parser.add_argument('--save', type=str)
parser.add_argument('--show', type=str,default='true')
args = parser.parse_args()
saveType = args.save
showType = args.show


def calcRates(path):
    success_rate = []
    failure_rate = []
    with open(path,"r") as f:
        for line in f.readlines():
            if "train in " in line:            
                success_rate.append(float(line[line.index("success")+14:line.index("failure")-2]))
                failure_rate.append(float(line[line.index("failure")+14:line.index("average")-2])) 

    return success_rate, failure_rate        

modelName = "model_Sep30_p09_gamma05_cap100000_batch_10000_{}"
noOfSimilarModels = 4.0

success_rate_1, failure_rate_1 = calcRates("./data/"+modelName.format(1)+"/output.log")
success_rate_2, failure_rate_2 = calcRates("./data/"+modelName.format(2)+"/output.log")
success_rate_3, failure_rate_3 = calcRates("./data/"+modelName.format(3)+"/output.log")
success_rate_4, failure_rate_4 = calcRates("./data/"+modelName.format(4)+"/output.log")

final_success_rate = []
final_failure_rate = []
for i in range(min(len(success_rate_1),len(success_rate_2),len(success_rate_3))):
    final_success_rate.append((success_rate_1[i] + success_rate_2[i] + success_rate_3[i] + success_rate_4[i])/noOfSimilarModels)
    final_failure_rate.append((failure_rate_1[i] + failure_rate_2[i] + failure_rate_3[i] + failure_rate_4[i])/noOfSimilarModels)


episodes = range(1,len(final_success_rate)+1)

print("On average, ", len(final_success_rate)," episodes were run, with ", len(final_success_rate)*10, "iterations")
print("No of successful runs :", 10*sum(final_success_rate), "  ", 10*sum(final_success_rate)/ len(final_success_rate)*10,"%")
print("No of unsuccessful runs :", 10*sum(final_failure_rate),"  ", 10*sum(final_failure_rate)/ len(final_success_rate)*10,"%")
noOfNoResults = 10*len(final_success_rate) - 10*sum(final_success_rate) - 10*sum(final_failure_rate)
print("No of no result runs :", noOfNoResults, "  ", 10*noOfNoResults/len(final_success_rate))


plt.plot(episodes,final_success_rate,label='Success rate')
plt.plot(episodes,final_failure_rate, label='Failure rate')
plt.xlabel("Episodes")
plt.ylabel("Probability")
plt.ylim([0,1])
plt.legend(loc='best')

if saveType == "true":
    plt.savefig("./data/"+modelName[:-3]+"_avgTrain.png")
    print("Saved!")
if showType == 'true':
    plt.show()

#print(success_rate)
