import matplotlib.pyplot as plt
import sys

def calcRates(path):
    success_rate = []
    failure_rate = []
    with open(path,"r") as f:
        for line in f.readlines():
            if "train in " in line:            
                success_rate.append(float(line[line.index("success")+14:line.index("failure")-2]))
                failure_rate.append(float(line[line.index("failure")+14:line.index("average")-2])) 

    return success_rate, failure_rate        


success_rate_1, failure_rate_1 = calcRates("./data/model_gamma_batch_cap_dataset4_episodes_env_1/output.log")
success_rate_2, failure_rate_2 = calcRates("./data/model_gamma_batch_cap_dataset4_episodes_env_2/output.log")
success_rate_3, failure_rate_3 = calcRates("./data/model_gamma_batch_cap_dataset4_episodes_env_3/output.log")
success_rate_4, failure_rate_4 = calcRates("./data/model_gamma_batch_cap_dataset4_episodes_env_4/output.log")

final_success_rate = []
final_failure_rate = []
for i in range(min(len(success_rate_1),len(success_rate_2),len(success_rate_3))):
    final_success_rate.append((success_rate_1[i] + success_rate_2[i] + success_rate_3[i] + success_rate_4[i])/4.0)
    final_failure_rate.append((failure_rate_1[i] + failure_rate_2[i] + failure_rate_3[i] + failure_rate_4[i])/4.0)


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
plt.show()

#print(success_rate)
