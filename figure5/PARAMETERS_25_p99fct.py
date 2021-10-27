
data = [
    ("data/ecmp25tcp_p99fct.csv", "ECMP", 'k', 'o'),
    ("data/drill25tcp_p99fct.csv", "DRILL", 'dodgerblue', 'D'),
    ("data/dibs25tcp_p99fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch25tcp_p99fct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps25tcpp99fct",
    "xticks": 7,
    "x": [35,45,55,65,75,85,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "p99 FCT (s)",
    "legend": False,
    "ylim_min": -0.001,
    "ylim_max": 4
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]