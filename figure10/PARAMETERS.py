
data = [
    ("data/tcp_ecmp_burst_80.csv", "TCP ECMP", 'gold', 'X'),
    ("data/dibs_burst_80.csv", "DIBS", 'r', 'v'),
    ("data/ecmp_burst_80.csv", "ECMP", 'k', 'o'),
    ("data/drill_burst_80.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/valinor_sch_burst_80.csv", "Vertigo", 'springgreen', '|'),
]

config = {
    "name" : "burst80",
    "xticks": 8,
    "x": [2, 4, 8, 12, 16, 20, 24, 28],
    "xlabel": "Incast Arrival Rate (kQPS)",
    "ylabel": "Mean QCT (s)",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 4
}
