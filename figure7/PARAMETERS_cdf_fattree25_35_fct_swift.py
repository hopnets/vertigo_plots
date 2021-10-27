
data = [
    ("data/fct_swift_ecmp_cdf_25_35.csv", "Swift ECMP", 'k', 'solid', 'o'),
    ("data/fct_swift_dibs_cdf_25_35.csv", "Swift DIBS", 'r', 'solid', 'v'),
    ("data/fct_swift_valinor_cdf_25_35.csv", "Swift Vertigo", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree25_35swiftfctcdf",
    # "xticks": 9,
    "x": ["", "", r'100$\mu$s', "1ms", "10ms", "100ms", "1s"],
    "xlabel": "FCT",
    "ylabel": "CDF",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
