import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
	'size'   : 28}
font_label = {'family' : 'normal',
	'size'   : 28}

plt.rc('font', **font)
plt.rc('legend', fontsize=28)

dctcp = [
	89.2145786609404,
	88.147238878201,
	88.0350446919285,
	87.9594975482855,
	87.4038578648549,
	83.8927784092234,
	77.9604110661783,
	76.9575328565793
]


dibs = [
	99.873466359276,
	98.2133920082478,
	93.7866106615643,
	86.0367276769626,
	77.6281029139732,
	69.1418895253659,
	61.3206179944146,
	57.1269627489746
]


tcp = [
	86.5055083770516,
	86.1123853657776,
	86.5907706828756,
	87.0973877992692,
	87.1103484948664,
	85.3379823119086,
	78.7542261793779,
	71.3151855701744

]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Flow Completions (%)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_xticks(x)

for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed', linewidth=7, label='TCP Reno+ECMP')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=7,label='DCTCP+ECMP')
p2 = plt.plot(x, dibs, 'r:', linewidth=7, label='Random Deflection+DCTCP')

ax1.set_ylim(0, 100)
plt.legend()

plt.savefig('cc4.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
