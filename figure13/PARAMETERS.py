
data = [
    ("data/valinor_sch_timeouts_mfct.csv", "Mean", 'springgreen', 'X'),
    ("data/valinor_sch_timeouts_p99fct.csv", "p99", 'darkgreen', 'X')
]

config = {
    "name" : "timeouts",
    "xticks": 9,
    "x": [120, 240, 360, 480, 600, 720, 840, 960, 1080],
    "y": [10, 100, 1000, 5000],
    "yticks" : 4,
    "xlabel": "Ordering Timeout " + r'($\mu s$)',
    "ylabel": "FCT (ms)",
    "legend": True,
    "ylim_min": 10,
    "ylim_max": 5000
}
