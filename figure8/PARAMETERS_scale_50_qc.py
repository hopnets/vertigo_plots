
data = [
    ("data/dibs_scale50_qc.csv", "DIBS", 'r', 'v'),
    ("data/ecmp_scale50_qc.csv", "ECMP", 'k', 'o'),
    ("data/drill_scale50_qc.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/valinor_sch_scale50_qc.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "scale50qc",
    "xticks": 5,
    "x": [50, 150, 250, 350, 450],
    "xlabel": "Incast Scale",
    "ylabel": "% Completed Queries",
    "legend": True
}
