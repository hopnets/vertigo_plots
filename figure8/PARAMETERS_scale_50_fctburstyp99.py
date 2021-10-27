
data = [
    ("data/ecmp_scale50_fctburstyp99.csv", "ECMP", 'k', 'o'),
    ("data/drill_scale50_fctburstyp99.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/dibs_scale50_fctburstyp99.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch_scale50_fctburstyp99.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "scale50fctallp99",
    "xticks": 5,
    "x": [50, 150, 250, 350, 450],
    "xlabel": "Incast Scale",
    "ylabel": "p99 FCT (s)",
    "legend": False
}
