import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'family' : 'normal',
	'size'   : 36}
font_label = {'family' : 'normal',
	'size'   : 36}
font_annotate = {'family' : 'normal',
	'size'   : 24}
plt.rc('font', **font)
plt.rc('legend', fontsize=18)

dctcp = [
	1.006391991,
	1.107629352,
	1.207112679,
	1.32740719,
	1.480457704,
	1.725803846,
	2.417456248,
	3.029012144
]


dibs = [
	0.059086993,
	0.465812668,
	1.124137063,
	1.96885861,
	2.742481583,
	3.321759026,
	3.782103808,
	4.046981679
]

tcp = [
	1.58586684050603,
	1.59032952518682,
	1.57664061461599,
	1.60911715343506,
	1.75578900388102,
	2.20169797760024,
	2.94913181509436,
	3.39656815619524
]

x = [25,35,45,55,65,75,85,95]

fig, (ax1) = plt.subplots(figsize=(10, 5))
plt.grid(axis="y")
plt.ylabel('Mean QCT (s)',**font_label)
plt.xlabel("Aggregate Network Load (%)",**font_label)

ax1.set_xticks(x)

for spine in ax1.spines.values():
	spine.set_visible(False)

p0 = plt.plot(x, tcp, 'gold', linestyle='dashed',  linewidth=7, label='TCP')
p1 = plt.plot(x, dctcp, 'steelblue', linewidth=7,label='DCTCP')
p2 = plt.plot(x, dibs, 'r:', linewidth=7, label='Random Deflection')

label_x = 25
label_y = 0.459086993
arrow_x = 25
arrow_y = 0.059086993

arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=5, shrink=0.4)

plt.annotate(
    "59ms", xy=(arrow_x, arrow_y),
    xytext=(label_x, label_y),
    arrowprops=arrow_properties, **font_annotate)

plt.savefig('cc2.pdf', format='pdf', dpi=300, bbox_inches='tight')

plt.show()
