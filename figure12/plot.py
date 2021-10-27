import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import ScalarFormatter

#####
from PARAMETERS import *
#####

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 30}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 30}

plt.rc('font', **font)
plt.rc('legend', fontsize=22)

# convertfunc = lambda x: float(x[0:-2])
data_m = []
data_m_t = []
plots = []
labels = []
for i in range(len(data)):
    data_m.append(np.genfromtxt(data[i][0], delimiter=','))

for i in range(len(data_m[0])):
        data_m_t.append([])

for i in range(len(data_m[0])):
        for j in range(len(data_m)):
                data_m_t[i].append(data_m[j][i])

print(data_m)

fig, ax1 = plt.subplots(figsize=(10, 4))

# ax1.set_ylabel("Mean Response Time (" + r'$\mu$' + "s)" ,**font_label)
# ax1.set_xticklabels(["", "Baseline",  "+Marking", "", ""], rotation=-20)
ax1.grid(which='major', axis='y', linestyle='--')
ax1.set_ylim(config["ylim_min"], config["ylim_max"])
# ax1.set_yticks(np.arange(0,37,4))
# ax1.set_xticks(np.arange(len(config["x"])), config["x"])
# ax1.set_xticklabels(["", 55, 65, 75, 85, 95])
ax1.set_xticklabels(["", 35, 55, 75, 95])
plt.ylabel(config["ylabel"], **font_label)
plt.xlabel(config["xlabel"], **font_label)

ax1.set_yscale('log')
ax1.yaxis.set_major_formatter(ScalarFormatter())

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# ax1.grid()
# ax1.set_xticks(np.arange(0,91,10))
# ax1.set_xticklabels([])
# ax1.set_yticks(np.arange(1,1100000,250000))
ax1.set_yticklabels(['','0.1','1.0','10'])
# ax1.set_xlim(0,89)
BAR_LEN = 0.2
B2 = 0.075
x = np.arange(len(data_m[0]))
p1 = ax1.bar(x - (3/2)*BAR_LEN, data_m[0], BAR_LEN, color='lime', hatch="//", label="^1 FW ^1 DEF", alpha=0.9)
p2 = ax1.bar(x - (1/2)*BAR_LEN, data_m[1], BAR_LEN, color='palegreen', hatch="/\\", label="^1 FW ^2 DEF", alpha=0.9)
p3 = ax1.bar(x + (1/2)*BAR_LEN, data_m[2], BAR_LEN, color='g', hatch="++", label="^2 FW ^1 DEF", alpha=0.9)
p4 = ax1.bar(x + (3/2)*BAR_LEN, data_m[3], BAR_LEN, color='springgreen', label="Vertigo")

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)

plt.savefig(config["name"] + '.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()
