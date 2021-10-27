
data = [
    ("data/dibs25tcp.csv", "DIBS TCP", 'darkred', 'v'),
    ("data/dibs25.csv", "DIBS DCTCP", 'r', 'o'),
    ("data/dibs25_swift1_qct.csv", "DIBS Swift", 'lightcoral', 'x'),
    # ("data/ecmp25.csv", "ECMP DCTCP", 'dodgerblue', '1'),
    # ("data/ecmp25tcp.csv", "ECMP TCP", 'navy', '*'),
    ("data/ecmp_swift1_25_qct.csv", "ECMP Swift", 'navy', '*'),
    ("data/valinor_sch25tcp.csv", "Vertigo TCP", 'g', '|'),
    ("data/valinor_sch25.csv", "Vertigo DCTCP", 'springgreen', 'X'),
    ("data/valinor_sch25_swift1_qct.csv", "Vertigo Swift", 'greenyellow', 's')
]

config = {
    "name" : "qps25tcpdctcpswift",
    "xticks": 7,
    "x": [35, 45, 55, 65, 75, 85, 95],
    "xlabel": "Aggregate Network Load %",
    "ylabel": "Mean QCT",
    "legend": True,
    "ylim_min": 0.001,
    "ylim_max": 10
}
