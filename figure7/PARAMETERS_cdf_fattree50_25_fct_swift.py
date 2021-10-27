
data = [
    ("data/fct_swift_ecmp_cdf_50_25.csv", "Swift ECMP", 'k', 'solid', 'o'),
    ("data/fct_swift_dibs_cdf_50_25.csv", "Swift DIBS", 'r', 'solid', 'v'),
    ("data/fct_swift_valinor_cdf_50_25.csv", "Swift Vertigo", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree50_25swiftfctcdf",
    # "xticks": 9,
    "x": ["", "", r'100$\mu$s', "1ms", "10ms", "100ms", "1s"],
    "xlabel": "FCT",
    "ylabel": "CDF",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
