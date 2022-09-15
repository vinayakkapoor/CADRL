import matplotlib.pyplot as plt


def plotTraj(path):
  t, p1x,p2x,p1y,p2y = [], [], [], [], []
  with open(path,'r') as f:
      lines = f.readlines()
      for line in lines:
          if "(" in line:
              line_split = line.split(" ")
              #t.append(float(line_split[0]))
              p1x.append(float(line_split[1].split(",")[0][1:]))
              p1y.append(float(line_split[1].split(",")[1][:-1]))
              p2x.append(float(line_split[2].split(",")[0][1:]))
              p2y.append(float(line_split[2].split(",")[1][:-2]))

  return p1x,p1y,p2x,p2y



for i in range(180,200):
  p1x,p1y,p2x,p2y = plotTraj("./data/multi_sim/trajectoryData_v{}.txt".format(i))
  #plt.clf()
  for j in range(0,len(p1x)):

    plt.plot(p1x[0:j+2],p1y[0:j+2])
    plt.plot(p2x[0:j+2],p2y[0:j+2])
    plt.xlim([-4,4])
    plt.ylim([-4,4])
    plt.pause(0.25/20.0)
plt.show()
  #print("./trajectoryData_v{}.txt".format(i))


