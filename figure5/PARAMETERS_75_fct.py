
data = [
    ("data/ecmp75_fct.csv", "ECMP", 'k', 'o'),
    ("data/drill75_fct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs75_fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch75_fct.csv", "Valinor", 'springgreen', '|')
]

config = {
    "name" : "qps75fct",
    "xticks": 4,
    "x": [80,85,90,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean FCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]