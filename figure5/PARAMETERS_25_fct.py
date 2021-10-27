
data = [
    ("data/ecmp25_fct.csv", "ECMP", 'k', 'o'),
    ("data/drill25_fct.csv", "DRILL", 'dodgerblue', 'X'),
    ("data/dibs25_fct.csv", "DIBS", 'r', 'v'),
    ("data/valinor_sch25_fct.csv", "Vertigo", 'springgreen', '|')
]

config = {
    "name" : "qps25fct",
    "xticks": 7,
    "x": [35,45,55,65,75,85,95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean FCT (s)",
    "legend": False
}


# [55, 60, 65, 70, 75, 80, 85, 90, 95]
