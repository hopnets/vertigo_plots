
data = [
    ("data/qct_swift_ecmp_cdf_25_85.csv", "Swift ECMP", 'k', 'solid', 'o'),
    ("data/qct_swift_dibs_cdf_25_85.csv", "Swift DIBS", 'r', 'solid', 'v'),
    ("data/qct_swift_valinor_cdf_25_85.csv", "Swift Vertigo", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree25_85swiftqctcdf",
    # "xticks": 9,
    "x": ["", "", "10ms", "100ms", "1s"],
    "xlabel": "QCT",
    "ylabel": "CDF",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
