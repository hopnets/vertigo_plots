
data = [
    ("data/qct_swift_ecmp_cdf_50_25.csv", "Swift ECMP", 'k', 'solid', 'o'),
    ("data/qct_swift_dibs_cdf_50_25.csv", "Swift DIBS", 'darkred', 'solid', 'v'),
    ("data/qct_swift_valinor_cdf_50_25.csv", "Swift Valinor", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree50_25swiftqctcdf",
    # "xticks": 9,
    "x": ["", "", "10ms", "100ms", "1s"],
    "xlabel": "QCT",
    "ylabel": "CDF",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
