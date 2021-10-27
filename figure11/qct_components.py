import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PARAMETERS import *

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family': 'normal',
        # 'weight' : 'bold',
        'size': 28}
font_label = {'family': 'normal',
              # 'weight' : 'bold',
              'size': 28}


plt.rc('font', **font)
plt.rc('legend', fontsize=22)

fig, ax = plt.subplots(figsize=(8, 4))


data_m = []
plots = []
labels = []
for i in range(len(data)):
    data_m.append(np.genfromtxt(data[i][0], delimiter=','))

N = 10

ind = np.arange(config["xticks"])

for i in range(len(data)):
    plots.append(plt.plot(ind[:len(data_m[i])], data_m[i], color=data[i][2], marker=data[i][3],
                linewidth=4, markevery=1, markersize=8, label=data[i][1])[0])
    labels.append(data[i][1])

plt.ylabel(config["ylabel"], **font_label)
plt.xlabel(config["xlabel"], **font_label)

plt.xticks(ind, config["x"], rotation=30, **font_label)

try:
    ax.set_ylim((config["ylim_min"], config["ylim_max"]))
except KeyError:
    pass


# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

ax.grid(axis='y', which='both')
# ax.set_yticks([0,1,2,3,4])

if config["legend"] == True:
    plt.legend(plots, labels,bbox_to_anchor=(0.12,0.98,1,0.2), ncol=2)

plt.savefig(config["name"] + ".pdf", format='pdf', dpi=300, bbox_inches='tight')

plt.show()