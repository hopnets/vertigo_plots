
data = [
    ("data/valinor_sch50.csv", "Vertigo", 'springgreen', '|'),
    ("data/valinor_nodeflection50_qct.csv", "No Deflection", 'magenta', 'D'),
    ("data/valinor_noscheduling50_qct.csv", "No Scheduling", 'crimson', 'v'),
    ("data/valinor_noordering50_qct.csv", "No Ordering", 'navy', 'X')
]

config = {
    "name" : "components50qct",
    "xticks": 9,
    "x": [55, 60, 65, 70, 75, 80, 85, 90, 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean QCT (s)",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 2
}
