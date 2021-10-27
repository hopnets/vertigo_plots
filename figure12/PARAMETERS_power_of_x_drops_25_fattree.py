
data = [
    ("data/valinor_random_fw_random_bou_25_drops_fattree.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_random_fw_pow_bou_25_drops_fattree.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_pow_fw_random_25_drops_fattree.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_sch25_drops_fattree.csv", "25%", 'springgreen', 'X')
]

config = {
    "name" : "powerofxdrops25fattree",
    "xticks": 7,
    "x": [35, 45, 55, 65, 75, 85, 95],
    "xlabel": "Offered Load %",
    "ylabel": "Drop %",
    "legend": True,
    # "ylim_min": 0,
    # "ylim_max": 1.01
}
