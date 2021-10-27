
data = [
    ("data/ecmp75.csv", "ECMP", 'k', 'o'),
    ("data/dibs75.csv", "DIBS", 'r', 'v'),
    ("data/drill75.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/valinor_sch75.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps75",
    "xticks": 4,
    "x": [80,85,90,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean QCT (s)",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 4
}
