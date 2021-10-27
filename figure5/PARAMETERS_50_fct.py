
data = [
    ("data/ecmp50_fct.csv", "ECMP", 'k', 'o'),
    ("data/drill50_fct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs50_fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch50_fct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps50fct",
    "xticks": 9,
    "x": [55, "", 65, "", 75, "", 85, "", 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean FCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]