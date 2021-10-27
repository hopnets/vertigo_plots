
data = [
    ("data/ecmp25_p99qct.csv", "ECMP", 'k', 'o'),
    ("data/drill25_p99qct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs25_p99qct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch25_p99qct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps25p99qct",
    "xticks": 7,
    "x": [35,45,55,65,75,85,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 QCT (s)",
    "legend": False,
    "ylim_min": -0.001,
    "ylim_max": 6
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]