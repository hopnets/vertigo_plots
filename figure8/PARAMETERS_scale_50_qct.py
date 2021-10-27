
data = [
    ("data/dibs_scale50_qct.csv", "DIBS", 'r', 'v'),
    ("data/ecmp_scale50_qct.csv", "ECMP", 'k', 'o'),
    ("data/drill_scale50_qct.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/valinor_sch_scale50_qct.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "scale50qct",
    "xticks": 5,
    "x": [50, 150, 250, 350, 450],
    "xlabel": "Incast Scale",
    "ylabel": "Mean QCT (s)",
    "legend": False
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]