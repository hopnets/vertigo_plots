import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PARAMETERS_b import *

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family': 'normal',
        # 'weight' : 'bold',
        'size': 30}
font_label = {'family': 'normal',
              # 'weight' : 'bold',
              'size': 30}


plt.rc('font', **font)
plt.rc('legend', fontsize=22)

fig, ax = plt.subplots(figsize=(10, 4))


data_m = []
plots = []
labels = []
counts = []
bin_edges = []
cdf = []
for i in range(len(data)):
    data_m.append(np.genfromtxt(data[i][0], delimiter=','))

num_bins = 1000

# ind = np.arange(config["xticks"])

for i in range(len(data)):
    counts1, bin_edges1 = np.histogram(data_m[i], bins=num_bins, normed=True)
    counts.append(counts1)
    bin_edges.append(bin_edges1)
    cdf.append(np.cumsum(counts1))
    cdf[i] /= np.sum(counts1)
    plots.append(plt.plot(bin_edges[i][1:], cdf[i], color=data[i][2],
                linewidth=6, label=data[i][1], linestyle=data[i][3], marker=data[i][4], markersize=16, markevery=0.08)[0])
    labels.append(data[i][1])


plt.ylabel(config["ylabel"], **font_label)
plt.xlabel(config["xlabel"], **font_label)

# plt.xticks(ind, config["x"], rotation=30, **font_label)

# try:
#     ax.set_ylim((config["ylim_min"], config["ylim_max"]))
# except KeyError:
#     pass


# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
print(bin_edges[0])
print(bin_edges[4][-10:])
# ax.set_yticklabels()
# ax.set_ylim(0, 1.05)
ax.grid(axis='y', which='both')

if config["legend"] == True:
    plt.legend(plots, labels, ncol=2, bbox_to_anchor=(0.15, 1))

plt.savefig(config["name"] + ".pdf", format='pdf', dpi=300, bbox_inches='tight')

plt.show()
