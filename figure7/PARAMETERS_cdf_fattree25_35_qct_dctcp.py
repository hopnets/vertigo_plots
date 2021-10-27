
data = [
    ("data/qct_dctcp_ecmp_cdf_25_35.csv", "DCTCP ECMP", 'k', 'solid', 'o'),
    ("data/qct_dctcp_dibs_cdf_25_35.csv", "DCTCP DIBS", 'r', 'solid', 'v'),
    ("data/qct_dctcp_valinor_cdf_25_35.csv", "DCTCP Vertigo", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree25_35dctcpqctcdf",
    # "xticks": 9,
    "x": ["", "", "10ms", "100ms", "1s"],
    "xlabel": "QCT",
    "ylabel": "CDF",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
