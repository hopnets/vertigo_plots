import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
	'size'   : 28}
font_label = {'family' : 'normal',
	'size'   : 28}
font_annotate = {'family' : 'normal',
	'size'   : 24}
plt.rc('font', **font)
plt.rc('legend', fontsize=18)

dctcp = [
	0.535726381535511,
	0.56343997065293,
	0.574424007914262,
	0.585725007325065,
	0.605932117365172,
	0.652902998192679,
	0.733993532421939,
	0.762978697921337
]

dibs = [
	0.008135944631033,
	0.073079314621332,
	0.253127559147825,
	0.493395290397439,
	0.708709057531506,
	0.873589141767016,
	1.01011324054046,
	1.101359863739508
]


tcp = [
	0.664860671617698,
	0.658225226324686,
	0.640562593910546,
	0.628768844486613,
	0.626943424696413,
	0.660877890687106,
	0.757238807840083,
	0.848817774038801
]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Mean FCT (s)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_xticks(x)


for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed',  linewidth=7, label='TCP')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=7,label='DCTCP')
p2 = plt.plot(x, dibs, 'r:', linewidth=7, label='Random Deflection')

label_x = 25
label_y = 0.108135944631033
arrow_x = 25
arrow_y = 0.008135944631033

arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=5, shrink=0.4)

plt.annotate(
    "8ms", xy=(arrow_x, arrow_y),
    xytext=(label_x, label_y),
    arrowprops=arrow_properties, **font_annotate)

plt.savefig('cc5.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
