import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import ScalarFormatter

####
from PARAMETERS import *
####

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family': 'normal',
        # 'weight' : 'bold',
        'size': 28}
font_label = {'family': 'normal',
              # 'weight' : 'bold',
              'size': 28}


plt.rc('font', **font)
plt.rc('legend', fontsize=23)

fig, ax = plt.subplots(figsize=(10, 4))


data_m = []
plots = []
labels = []
counts = []
bin_edges = []
cdf = []
for i in range(len(data)):
    data_m.append(np.genfromtxt(data[i][0], delimiter=','))

# ind = np.arange(config["xticks"])

for i in range(len(data)):
    data_set=sorted(set(data_m[i]))
    bins=np.append(data_set, data_set[-1]+1)
    counts1, bin_edges1 = np.histogram(data_m[i], bins=bins, density=False, normed=True)
    counts.append(counts1)
    bin_edges.append(bin_edges1)
    counts1=counts1.astype(float)/len(data_set)
    cdf.append(np.cumsum(counts1))
    # cdf[i] *= 1000
    plots.append(plt.plot(bin_edges[i][1:], cdf[i], color=data[i][2],
                linewidth=5, label=data[i][1], linestyle=data[i][3], markevery=0.08, markersize=18, marker=data[i][4])[0])
    labels.append(data[i][1])

plt.xscale("log")
plt.ylim(0,1.05)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.set_xticklabels(config["x"], rotation=0)

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

# ax.set_yticklabels()
# ax.set_ylim(0, 1.05)
ax.grid(axis='y', which='both')

if config["legend"] == True:
    plt.legend(plots, labels, ncol=1, loc="upper left") #, bbox_to_anchor=(0.25, 1))

plt.savefig(config["name"] + ".pdf", format='pdf', dpi=300, bbox_inches='tight')

plt.show()
