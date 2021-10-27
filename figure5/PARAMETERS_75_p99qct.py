
data = [
    ("data/dibs75_p99qct.csv", "DIBS", 'r', 'v'),
    ("data/ecmp75_p99qct.csv", "ECMP", 'k', 'o'),
    ("data/drill75_p99qct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/valinor_sch75_p99qct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps75_p99qct",
    "xticks": 4,
    "x": [80,85,90,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 QCT (s)",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 6
}
