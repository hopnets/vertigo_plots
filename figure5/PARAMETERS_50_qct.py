
data = [
    ("data/ecmp50.csv", "ECMP", 'k', 'o'),
    ("data/drill50.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs50.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch50.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps50",
    "xticks": 9,
    "x": [55, "", 65, "", 75, "", 85, "", 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean QCT (s)",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 4
}
