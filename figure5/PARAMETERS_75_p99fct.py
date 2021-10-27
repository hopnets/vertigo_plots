
data = [
    ("data/ecmp75_p99fct.csv", "ECMP", 'k', 'o'),
    ("data/drill75_p99fct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs75_p99fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch75_p99fct.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "qps75p99fct",
    "xticks": 4,
    "x": [80,85,90,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 FCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 4
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]