
data = [
    ("data/ecmp25.csv", "ECMP", 'k', 'o'),
    ("data/drill25.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs25.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch25.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps25",
    "xticks": 7,
    "x": [35,45,55,65,75,85,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean QCT (s)",
    "legend": True
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]