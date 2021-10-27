
data = [
    ("data/fct_dctcp_ecmp_cdf_25_35.csv", "DCTCP ECMP", 'k', 'solid', 'o'),
    ("data/fct_dctcp_dibs_cdf_25_35.csv", "DCTCP DIBS", 'r', 'solid', 'v'),
    ("data/fct_dctcp_valinor_cdf_25_35.csv", "DCTCP Vertigo", 'springgreen', 'solid','|')
]

config = {
    "name" : "fattree25_35dctcpfctcdf",
    # "xticks": 9,
    "x": ["", "", r'100$\mu$s', "1ms", "10ms", "100ms", "1s"],
    "xlabel": "FCT",
    "ylabel": "CDF",
    "legend": True,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
