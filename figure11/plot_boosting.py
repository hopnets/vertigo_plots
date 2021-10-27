import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib

from PARAMETERS_boosting import *

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 24}
font_label = {'family' : 'normal',
        # 'weight' : 'bold',
        'size'   : 24}

plt.rc('font', **font)
plt.rc('legend', fontsize=24)

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

print(data_m_t)

fig, ax1 = plt.subplots(figsize=(8, 4))

# ax1.set_ylabel("Mean Response Time (" + r'$\mu$' + "s)" ,**font_label)
# ax1.set_xticklabels(["", "Baseline",  "+Marking", "", ""], rotation=-20)
ax1.grid(which='major', axis='y', linestyle='--')
# ax1.set_ylim(0,12)
# ax1.set_yticks(np.arange(0,37,4))
ax1.set_xticklabels(["", "25%", "", "75%"])
plt.ylabel(config["ylabel"], **font_label)
plt.xlabel(config["xlabel"], **font_label)


# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# ax1.grid()
# ax1.set_xticks(np.arange(0,91,10))
# ax1.set_xticklabels([])
# ax1.set_yticks(np.arange(1,1100000,250000))
# ax1.set_yticklabels(['0','.25','.50','.75','1'])
# ax1.set_xlim(0,89)
BAR_LEN = 0.2
B2 = 0.075
x = np.arange(len(data_m_t[0]))
p1 = ax1.bar(x - (3/2)*BAR_LEN, data_m_t[0], BAR_LEN, color='darkred', label="No Boosting")
p2 = ax1.bar(x - (1/2)*BAR_LEN, data_m_t[1], BAR_LEN, color='lightgreen', label="x2 Boosting")
p3 = ax1.bar(x + (1/2)*BAR_LEN, data_m_t[2], BAR_LEN, color='g', label="x4 Boosting")
p4 = ax1.bar(x + (3/2)*BAR_LEN, data_m_t[3], BAR_LEN, color='darkgreen', label="x8 Boosting")

plt.legend(bbox_to_anchor=(0,0.95,1,0.2), ncol=2)

plt.savefig('boosting.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()
