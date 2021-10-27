
data = [
    ("data/dibs_fs50_qct.csv", "DIBS", 'r', 'v'),
    ("data/ecmp_fs50_qct.csv", "ECMP", 'k', 'o'),
    ("data/drill_fs50_qct.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/valinor_sch_fs50_qct.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "flowsize50qct",
    "xticks": 9,
    "x": [1, 10, 20, 40, 60, 100, 140, 160, 180],
    "xlabel": "Incast Flow Size (KB)",
    "ylabel": "Mean QCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 2
}
