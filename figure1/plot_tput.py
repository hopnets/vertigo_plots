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
	236.9438010553846,
	344.2460104430769,
	453.2158765676923,
	563.0060190476923,
	671.1222709384615,
	773.6143759123076,
	850.3060371584615,
	891.177515410
]


dibs = [
	251.96404219692306,
	371.8277290830769,
	482.4864527184615,
	573.8355440753846,
	633.5629316415384,
	671.99876944,
	699.5843651415385,
	721.9707091384615
]


tcp = [
	236.9438010553846,
	344.2460104430769,
	453.2158765676923,
	563.0060190476923,
	671.1222709384615,
	773.6143759123076,
	850.3060371584615,
	891.177515410
]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Overall Goodput (Gbps)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_ylim(0, 1000)
plt.xticks(x)
	
for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed',  linewidth=8, label='TCP')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=8,label='DCTCP')
p2 = plt.plot(x, dibs, 'r:', linewidth=8, label='Random Deflection')


plt.savefig('cc3.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
