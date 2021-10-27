
data = [
    ("data/ecmp50_p99fct.csv", "ECMP", 'k', 'o'),
    ("data/drill50_p99fct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs50_p99fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch50_p99fct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps50p99fct",
    "xticks": 9,
    "x": [55, "", 65, "", 75, "", 85, "", 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 FCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 4
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]