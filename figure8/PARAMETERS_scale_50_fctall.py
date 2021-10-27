
data = [
    ("data/dibs_scale50_fctall.csv", "DIBS", 'r', 'v'),
    ("data/ecmp_scale50_fctall.csv", "ECMP", 'k', 'o'),
    ("data/drill_scale50_fctall.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/valinor_sch_scale50_fctall.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "scale50fctall",
    "xticks": 5,
    "x": [50, 150, 250, 350, 450],
    "xlabel": "Incast Scale",
    "ylabel": "Mean FCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 2
}
