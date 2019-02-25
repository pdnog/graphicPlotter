import matplotlib.pyplot as plt

import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", help = "Path to the file with the data for plot \n must be a \" xdata ydata\" format")
ap.add_argument("-u", "--file2", help = "Path to the second file with the data for plot \n must be a \" xdata ydata\" format")
ap.add_argument("-x", "--xline", help = "Name to assing to the x line")
ap.add_argument("-y", "--yline", help = "Name to assing to the y line")
ap.add_argument("-g", "--graphic", help = "Name of the graphic")
ap.add_argument("-fm", "--fileMeaning", help = "name for function 1")
ap.add_argument("-um", "--file2Meaning", help = "Name for function 2")

args = vars(ap.parse_args())

bns = []
btimes = []

if args["file2"]:
    lns = []
    ltimes = []
    l = open(args["file2"],"r")
    for lines in l.readlines():
        n, times = lines.split()
        lns.append(int(n))
        ltimes.append(int(times))
    plt.plot(lns,ltimes, label=args["file2Meaning"], color ='red')
    l.close()

f = open(args["file"],"r")
for lines in f.readlines():
    n,time = lines.split()
    bns.append(int(n))
    btimes.append(int(time))

plt.plot(bns,btimes, label= args["fileMeaning"], color ='green')


plt.legend()

plt.xlabel(args["xline"])

plt.ylabel(args["yline"])

plt.title(args["graphic"])

f.close()

plt.show()


