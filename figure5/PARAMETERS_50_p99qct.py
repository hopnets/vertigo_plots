
data = [
    ("data/ecmp50_p99qct.csv", "ECMP", 'k', 'o'),
    ("data/drill50_p99qct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs50_p99qct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch50_p99qct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps50_p99qct",
    "xticks": 9,
    "x": [55, "", 65, "", 75, "", 85, "", 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 QCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 6
}
