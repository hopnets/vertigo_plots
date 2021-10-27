import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
	'size'   : 40}
font_label = {'family' : 'normal',
	'size'   : 40}

plt.rc('font', **font)
plt.rc('legend', fontsize=28)

dctcp = [
	144.13902213017752,
	144.0506197633136,
	144.16271071005917,
	143.98326355029585,
	143.36030642011832,
	139.73934831360947,
	89.95511189349112,
	56.77702204142012
]


dibs = [
	144.09927372781064,
	142.70773426035504,
	129.05812763313608,
	85.36305798816568,
	50.286460680473375,
	38.34088112426035,
	33.014883816568044,
	29.623408698224853
]


tcp = [
	144.13902213017752,
	144.0506197633136,
	144.16271071005917,
	143.98326355029585,
	143.36030642011832,
	139.73934831360947,
	89.95511189349112,
	56.77702204142012
]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Elephant Goodput (Mbps)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_ylim(0, 150)
plt.xticks(x)
	
for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed',  linewidth=8, label='TCP')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=8,label='DCTCP')
p2 = plt.plot(x, dibs, 'r:', linewidth=8, label='Random Deflection')


plt.savefig('cc6.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
