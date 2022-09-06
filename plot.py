import matplotlib.pyplot as plt
success_rate = []
failure_rate = []
with open('./plot/plot_model_4.log') as f:
    for line in f.readlines():
        if "test" in line:
            continue
        success_rate.append(float(line[line.index("success")+14:line.index("failure")-2]))
        failure_rate.append(float(line[line.index("failure")+14:line.index("average")-2]))        
episodes = range(1,len(success_rate)+1)

plt.plot(episodes,success_rate)
plt.ylim([0,1])
plt.plot(episodes,failure_rate)
plt.show()

#print(success_rate)
