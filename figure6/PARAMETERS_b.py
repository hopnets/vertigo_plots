
data = [
    ("data/qct_dctcp_dibs_cdf_25.csv", "DIBS DCTCP", 'r', 'solid', 'o'),
    ("data/qct_tcp_srpt_sch_srpt_ord_cdf_25.csv", "Vertigo DCTCP", 'springgreen', 'solid', 'X'),
    ("data/qct_tcp_dibs_cdf_25.csv", "DIBS TCP", 'darkred', 'solid','v'),
    ("data/qct_tcp_ecmp_cdf_25.csv", "ECMP Swift", 'navy', 'solid', '*'),
    ("data/qct_dctcp_srpt_sch_srpt_ord_cdf_25.csv", "Vertigo TCP", 'g', 'solid','|'),
    ("data/qct_swift1_dibs_cdf_25.csv", "DIBS Swift", 'lightcoral', 'solid','x'),
    ("data/qct_swift1_valinor_cdf_25.csv", "Vertigo Swift", 'greenyellow', 'solid', 's')
]

config = {
    "name" : "qps25tcpdctcpcdf",
    # "xticks": 9,
    # "x": [55, 60, 65, 70, 75, 80, 85, 90, 95],
    "xlabel": "QCT (s)",
    "ylabel": "CDF",
    "legend": False,
    "ylim_min": -0.01,
    "ylim_max": 1.1
}
