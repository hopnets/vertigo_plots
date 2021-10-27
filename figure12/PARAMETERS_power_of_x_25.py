
data = [
    ("data/valinor_random_fw_random_bou_25.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_random_fw_pow_bou_25.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_pow_fw_random_25.csv", "75%", 'darkgreen', 'v'),
    ("data/valinor_sch25.csv", "25%", 'springgreen', 'X')
]

config = {
    "name" : "powerofx25",
    "xticks": 7,
    "x": [35, 45, 55, 65, 75, 85, 95],
    "xlabel": "Offered Load %",
    "ylabel": "Mean QCT (s)",
    "legend": True
}
