import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
	'size'   : 36}
font_label = {'family' : 'normal',
	'size'   : 36}

plt.rc('font', **font)
plt.rc('legend', fontsize=27)

dctcp = [
	80.065,
	76.99942499,
	74.545,
	71.9225,
	68.34268343,
	61.0925,
	38.40285714,
	17.54135963
]

dibs = [
	98.615,
	89.7925,
	74.86666667,
	53.67625,
	29.7202972,
	12.03833333,
	3.500714286,
	0.682504266
]


tcp = [
	68.71,
	66.8116702917573,
	66.8816666666667,
	65.6725,
	61.9416194161942,
	47.3358333333333,
	18.1407142857143,
	5.54381929774122
]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Incast Query Completions (%)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_xticks(x)

for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed', linewidth=7, label='TCP Reno')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=7,label='DCTCP')
p2 = plt.plot(x, dibs, 'r:', linewidth=7, label='Random Deflection')

ax1.set_ylim(0, 100)

plt.savefig('cc1.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
