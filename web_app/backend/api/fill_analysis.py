import datetime
from api.models import Analysis, CottonType, Market

PREDICTIONS = [
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3996.80",
                "Lower_Bound": "3134.51",
                "Upper_Bound": "4859.08",
            },
            "02/08/2020": {
                "Forecast_Price": "3984.23",
                "Lower_Bound": "3219.18",
                "Upper_Bound": "4749.28",
            },
            "03/08/2020": {
                "Forecast_Price": "3992.91",
                "Lower_Bound": "3416.59",
                "Upper_Bound": "4569.24",
            },
            "04/08/2020": {
                "Forecast_Price": "3899.86",
                "Lower_Bound": "3439.67",
                "Upper_Bound": "4360.04",
            },
            "05/08/2020": {
                "Forecast_Price": "3976.83",
                "Lower_Bound": "3419.08",
                "Upper_Bound": "4534.57",
            },
            "06/08/2020": {
                "Forecast_Price": "3995.21",
                "Lower_Bound": "3464.82",
                "Upper_Bound": "4525.61",
            },
            "07/08/2020": {
                "Forecast_Price": "3996.87",
                "Lower_Bound": "3540.96",
                "Upper_Bound": "4452.78",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4860.52",
                "Lower_Bound": "2366.68",
                "Upper_Bound": "7354.36",
            },
            "15/08/2020": {
                "Forecast_Price": "4845.02",
                "Lower_Bound": "2350.71",
                "Upper_Bound": "7339.34",
            },
            "22/08/2020": {
                "Forecast_Price": "4835.87",
                "Lower_Bound": "2342.12",
                "Upper_Bound": "7329.63",
            },
            "29/08/2020": {
                "Forecast_Price": "4832.41",
                "Lower_Bound": "2341.33",
                "Upper_Bound": "7323.49",
            },
            "05/09/2020": {
                "Forecast_Price": "4819.43",
                "Lower_Bound": "2323.24",
                "Upper_Bound": "7315.62",
            },
            "12/09/2020": {
                "Forecast_Price": "4804.11",
                "Lower_Bound": "2307.33",
                "Upper_Bound": "7300.89",
            },
            "19/09/2020": {
                "Forecast_Price": "4795.05",
                "Lower_Bound": "2298.77",
                "Upper_Bound": "7291.32",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4938.33",
                "Lower_Bound": "2473.71",
                "Upper_Bound": "7402.95",
            },
            "30/09/2020": {
                "Forecast_Price": "5114.91",
                "Lower_Bound": "2586.23",
                "Upper_Bound": "7643.59",
            },
            "30/10/2020": {
                "Forecast_Price": "5215.28",
                "Lower_Bound": "2661.66",
                "Upper_Bound": "7768.89",
            },
            "29/11/2020": {
                "Forecast_Price": "5301.91",
                "Lower_Bound": "2724.94",
                "Upper_Bound": "7878.88",
            },
            "29/12/2020": {
                "Forecast_Price": "5403.57",
                "Lower_Bound": "2796.63",
                "Upper_Bound": "8010.51",
            },
            "28/01/2021": {
                "Forecast_Price": "5430.19",
                "Lower_Bound": "2834.06",
                "Upper_Bound": "8026.33",
            },
            "27/02/2021": {
                "Forecast_Price": "5446.09",
                "Lower_Bound": "2844.34",
                "Upper_Bound": "8047.83",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4188.20",
                "Lower_Bound": "3503.11",
                "Upper_Bound": "4873.30",
            },
            "02/08/2020": {
                "Forecast_Price": "4182.08",
                "Lower_Bound": "2903.76",
                "Upper_Bound": "5460.40",
            },
            "03/08/2020": {
                "Forecast_Price": "4191.17",
                "Lower_Bound": "3570.42",
                "Upper_Bound": "4811.92",
            },
            "04/08/2020": {
                "Forecast_Price": "4195.07",
                "Lower_Bound": "3428.70",
                "Upper_Bound": "4961.44",
            },
            "05/08/2020": {
                "Forecast_Price": "4194.33",
                "Lower_Bound": "3438.23",
                "Upper_Bound": "4950.43",
            },
            "06/08/2020": {
                "Forecast_Price": "4191.84",
                "Lower_Bound": "3433.73",
                "Upper_Bound": "4949.95",
            },
            "07/08/2020": {
                "Forecast_Price": "4197.98",
                "Lower_Bound": "3412.71",
                "Upper_Bound": "4983.26",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4292.45",
                "Lower_Bound": "2097.24",
                "Upper_Bound": "6487.67",
            },
            "15/08/2020": {
                "Forecast_Price": "4226.84",
                "Lower_Bound": "2076.78",
                "Upper_Bound": "6376.91",
            },
            "22/08/2020": {
                "Forecast_Price": "4248.10",
                "Lower_Bound": "2084.63",
                "Upper_Bound": "6411.57",
            },
            "29/08/2020": {
                "Forecast_Price": "4316.70",
                "Lower_Bound": "2104.59",
                "Upper_Bound": "6528.82",
            },
            "05/09/2020": {
                "Forecast_Price": "4322.96",
                "Lower_Bound": "2109.13",
                "Upper_Bound": "6536.80",
            },
            "12/09/2020": {
                "Forecast_Price": "4257.18",
                "Lower_Bound": "2088.38",
                "Upper_Bound": "6425.98",
            },
            "19/09/2020": {
                "Forecast_Price": "4278.34",
                "Lower_Bound": "2096.06",
                "Upper_Bound": "6460.61",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4299.85",
                "Lower_Bound": "2067.43",
                "Upper_Bound": "6532.27",
            },
            "30/09/2020": {
                "Forecast_Price": "4230.61",
                "Lower_Bound": "2023.10",
                "Upper_Bound": "6438.12",
            },
            "30/10/2020": {
                "Forecast_Price": "4270.64",
                "Lower_Bound": "2051.47",
                "Upper_Bound": "6489.82",
            },
            "29/11/2020": {
                "Forecast_Price": "4250.10",
                "Lower_Bound": "2053.87",
                "Upper_Bound": "6446.34",
            },
            "29/12/2020": {
                "Forecast_Price": "4257.36",
                "Lower_Bound": "2081.75",
                "Upper_Bound": "6432.97",
            },
            "28/01/2021": {
                "Forecast_Price": "4248.80",
                "Lower_Bound": "2095.10",
                "Upper_Bound": "6402.50",
            },
            "27/02/2021": {
                "Forecast_Price": "4219.39",
                "Lower_Bound": "2077.92",
                "Upper_Bound": "6360.87",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3922.08",
                "Lower_Bound": "3193.90",
                "Upper_Bound": "4650.26",
            },
            "02/08/2020": {
                "Forecast_Price": "3924.71",
                "Lower_Bound": "3426.35",
                "Upper_Bound": "4423.08",
            },
            "03/08/2020": {
                "Forecast_Price": "3977.11",
                "Lower_Bound": "3216.79",
                "Upper_Bound": "4737.42",
            },
            "04/08/2020": {
                "Forecast_Price": "3777.45",
                "Lower_Bound": "3093.86",
                "Upper_Bound": "4461.04",
            },
            "05/08/2020": {
                "Forecast_Price": "3995.03",
                "Lower_Bound": "3402.36",
                "Upper_Bound": "4587.71",
            },
            "06/08/2020": {
                "Forecast_Price": "3898.46",
                "Lower_Bound": "3187.07",
                "Upper_Bound": "4609.85",
            },
            "07/08/2020": {
                "Forecast_Price": "3792.07",
                "Lower_Bound": "3151.46",
                "Upper_Bound": "4432.67",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4524.95",
                "Lower_Bound": "2177.57",
                "Upper_Bound": "6872.33",
            },
            "15/08/2020": {
                "Forecast_Price": "4489.32",
                "Lower_Bound": "2126.98",
                "Upper_Bound": "6851.67",
            },
            "22/08/2020": {
                "Forecast_Price": "4503.07",
                "Lower_Bound": "2158.85",
                "Upper_Bound": "6847.30",
            },
            "29/08/2020": {
                "Forecast_Price": "4526.48",
                "Lower_Bound": "2206.75",
                "Upper_Bound": "6846.20",
            },
            "05/09/2020": {
                "Forecast_Price": "4486.07",
                "Lower_Bound": "2147.80",
                "Upper_Bound": "6824.34",
            },
            "12/09/2020": {
                "Forecast_Price": "4450.79",
                "Lower_Bound": "2097.32",
                "Upper_Bound": "6804.26",
            },
            "19/09/2020": {
                "Forecast_Price": "4464.89",
                "Lower_Bound": "2129.31",
                "Upper_Bound": "6800.47",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4368.71",
                "Lower_Bound": "2166.33",
                "Upper_Bound": "6571.10",
            },
            "30/09/2020": {
                "Forecast_Price": "4403.48",
                "Lower_Bound": "2238.55",
                "Upper_Bound": "6568.40",
            },
            "30/10/2020": {
                "Forecast_Price": "4416.87",
                "Lower_Bound": "2274.70",
                "Upper_Bound": "6559.03",
            },
            "29/11/2020": {
                "Forecast_Price": "4418.00",
                "Lower_Bound": "2290.04",
                "Upper_Bound": "6545.97",
            },
            "29/12/2020": {
                "Forecast_Price": "4419.41",
                "Lower_Bound": "2305.51",
                "Upper_Bound": "6533.31",
            },
            "28/01/2021": {
                "Forecast_Price": "4411.62",
                "Lower_Bound": "2300.16",
                "Upper_Bound": "6523.07",
            },
            "27/02/2021": {
                "Forecast_Price": "4326.51",
                "Lower_Bound": "2200.81",
                "Upper_Bound": "6452.21",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4849.64",
                "Lower_Bound": "4022.52",
                "Upper_Bound": "5676.76",
            },
            "02/08/2020": {
                "Forecast_Price": "4844.05",
                "Lower_Bound": "4067.79",
                "Upper_Bound": "5620.31",
            },
            "03/08/2020": {
                "Forecast_Price": "4843.10",
                "Lower_Bound": "3977.97",
                "Upper_Bound": "5708.23",
            },
            "04/08/2020": {
                "Forecast_Price": "4849.17",
                "Lower_Bound": "4261.86",
                "Upper_Bound": "5436.48",
            },
            "05/08/2020": {
                "Forecast_Price": "4839.08",
                "Lower_Bound": "3991.56",
                "Upper_Bound": "5686.60",
            },
            "06/08/2020": {
                "Forecast_Price": "4833.71",
                "Lower_Bound": "3897.24",
                "Upper_Bound": "5770.19",
            },
            "07/08/2020": {
                "Forecast_Price": "4846.65",
                "Lower_Bound": "3442.42",
                "Upper_Bound": "6250.87",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4577.66",
                "Lower_Bound": "2257.44",
                "Upper_Bound": "6897.89",
            },
            "15/08/2020": {
                "Forecast_Price": "4602.85",
                "Lower_Bound": "2291.17",
                "Upper_Bound": "6914.54",
            },
            "22/08/2020": {
                "Forecast_Price": "4607.07",
                "Lower_Bound": "2292.44",
                "Upper_Bound": "6921.70",
            },
            "29/08/2020": {
                "Forecast_Price": "4614.65",
                "Lower_Bound": "2307.44",
                "Upper_Bound": "6921.85",
            },
            "05/09/2020": {
                "Forecast_Price": "4636.04",
                "Lower_Bound": "2343.34",
                "Upper_Bound": "6928.73",
            },
            "12/09/2020": {
                "Forecast_Price": "4661.23",
                "Lower_Bound": "2377.07",
                "Upper_Bound": "6945.38",
            },
            "19/09/2020": {
                "Forecast_Price": "4665.44",
                "Lower_Bound": "2378.34",
                "Upper_Bound": "6952.55",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4434.05",
                "Lower_Bound": "2183.59",
                "Upper_Bound": "6684.52",
            },
            "30/09/2020": {
                "Forecast_Price": "4423.39",
                "Lower_Bound": "2179.36",
                "Upper_Bound": "6667.43",
            },
            "30/10/2020": {
                "Forecast_Price": "4364.63",
                "Lower_Bound": "2159.34",
                "Upper_Bound": "6569.91",
            },
            "29/11/2020": {
                "Forecast_Price": "4377.42",
                "Lower_Bound": "2162.83",
                "Upper_Bound": "6592.01",
            },
            "29/12/2020": {
                "Forecast_Price": "4424.11",
                "Lower_Bound": "2177.45",
                "Upper_Bound": "6670.76",
            },
            "28/01/2021": {
                "Forecast_Price": "4569.37",
                "Lower_Bound": "2222.74",
                "Upper_Bound": "6916.00",
            },
            "27/02/2021": {
                "Forecast_Price": "4500.48",
                "Lower_Bound": "2200.40",
                "Upper_Bound": "6800.56",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4950.86",
                "Lower_Bound": "4165.15",
                "Upper_Bound": "5736.57",
            },
            "02/08/2020": {
                "Forecast_Price": "4944.42",
                "Lower_Bound": "3916.34",
                "Upper_Bound": "5972.51",
            },
            "03/08/2020": {
                "Forecast_Price": "4946.73",
                "Lower_Bound": "4208.22",
                "Upper_Bound": "5685.24",
            },
            "04/08/2020": {
                "Forecast_Price": "4950.16",
                "Lower_Bound": "4274.73",
                "Upper_Bound": "5625.60",
            },
            "05/08/2020": {
                "Forecast_Price": "4960.75",
                "Lower_Bound": "4236.17",
                "Upper_Bound": "5685.33",
            },
            "06/08/2020": {
                "Forecast_Price": "4939.27",
                "Lower_Bound": "4095.49",
                "Upper_Bound": "5783.04",
            },
            "07/08/2020": {
                "Forecast_Price": "4924.85",
                "Lower_Bound": "4195.41",
                "Upper_Bound": "5654.28",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4358.65",
                "Lower_Bound": "2129.85",
                "Upper_Bound": "6587.45",
            },
            "15/08/2020": {
                "Forecast_Price": "4369.60",
                "Lower_Bound": "2139.10",
                "Upper_Bound": "6600.10",
            },
            "22/08/2020": {
                "Forecast_Price": "4380.49",
                "Lower_Bound": "2148.32",
                "Upper_Bound": "6612.66",
            },
            "29/08/2020": {
                "Forecast_Price": "4389.13",
                "Lower_Bound": "2153.86",
                "Upper_Bound": "6624.39",
            },
            "05/09/2020": {
                "Forecast_Price": "4398.19",
                "Lower_Bound": "2162.21",
                "Upper_Bound": "6634.16",
            },
            "12/09/2020": {
                "Forecast_Price": "4407.39",
                "Lower_Bound": "2170.89",
                "Upper_Bound": "6643.89",
            },
            "19/09/2020": {
                "Forecast_Price": "4416.53",
                "Lower_Bound": "2179.54",
                "Upper_Bound": "6653.53",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4494.91",
                "Lower_Bound": "2113.01",
                "Upper_Bound": "6876.81",
            },
            "30/09/2020": {
                "Forecast_Price": "4607.07",
                "Lower_Bound": "2127.07",
                "Upper_Bound": "7087.07",
            },
            "30/10/2020": {
                "Forecast_Price": "4689.06",
                "Lower_Bound": "2138.26",
                "Upper_Bound": "7239.85",
            },
            "29/11/2020": {
                "Forecast_Price": "4703.42",
                "Lower_Bound": "2115.72",
                "Upper_Bound": "7291.13",
            },
            "29/12/2020": {
                "Forecast_Price": "4701.13",
                "Lower_Bound": "2097.51",
                "Upper_Bound": "7304.75",
            },
            "28/01/2021": {
                "Forecast_Price": "4704.10",
                "Lower_Bound": "2085.86",
                "Upper_Bound": "7322.34",
            },
            "27/02/2021": {
                "Forecast_Price": "4684.07",
                "Lower_Bound": "2050.76",
                "Upper_Bound": "7317.38",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5407.88",
                "Lower_Bound": "4657.11",
                "Upper_Bound": "6158.66",
            },
            "02/08/2020": {
                "Forecast_Price": "5413.40",
                "Lower_Bound": "4693.58",
                "Upper_Bound": "6133.22",
            },
            "03/08/2020": {
                "Forecast_Price": "5417.01",
                "Lower_Bound": "4674.20",
                "Upper_Bound": "6159.82",
            },
            "04/08/2020": {
                "Forecast_Price": "5394.89",
                "Lower_Bound": "4696.07",
                "Upper_Bound": "6093.71",
            },
            "05/08/2020": {
                "Forecast_Price": "5393.73",
                "Lower_Bound": "4737.30",
                "Upper_Bound": "6050.16",
            },
            "06/08/2020": {
                "Forecast_Price": "5391.11",
                "Lower_Bound": "4767.03",
                "Upper_Bound": "6015.19",
            },
            "07/08/2020": {
                "Forecast_Price": "5390.79",
                "Lower_Bound": "4741.88",
                "Upper_Bound": "6039.70",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4756.42",
                "Lower_Bound": "2294.45",
                "Upper_Bound": "7218.39",
            },
            "15/08/2020": {
                "Forecast_Price": "4765.08",
                "Lower_Bound": "2311.21",
                "Upper_Bound": "7218.95",
            },
            "22/08/2020": {
                "Forecast_Price": "4759.06",
                "Lower_Bound": "2309.21",
                "Upper_Bound": "7208.92",
            },
            "29/08/2020": {
                "Forecast_Price": "4729.55",
                "Lower_Bound": "2274.20",
                "Upper_Bound": "7184.90",
            },
            "05/09/2020": {
                "Forecast_Price": "4701.93",
                "Lower_Bound": "2239.60",
                "Upper_Bound": "7164.26",
            },
            "12/09/2020": {
                "Forecast_Price": "4710.40",
                "Lower_Bound": "2256.29",
                "Upper_Bound": "7164.50",
            },
            "19/09/2020": {
                "Forecast_Price": "4704.52",
                "Lower_Bound": "2254.34",
                "Upper_Bound": "7154.70",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4752.43",
                "Lower_Bound": "2289.01",
                "Upper_Bound": "7215.86",
            },
            "30/09/2020": {
                "Forecast_Price": "4743.99",
                "Lower_Bound": "2295.94",
                "Upper_Bound": "7192.04",
            },
            "30/10/2020": {
                "Forecast_Price": "4762.03",
                "Lower_Bound": "2346.94",
                "Upper_Bound": "7177.13",
            },
            "29/11/2020": {
                "Forecast_Price": "4763.29",
                "Lower_Bound": "2369.66",
                "Upper_Bound": "7156.91",
            },
            "29/12/2020": {
                "Forecast_Price": "4768.80",
                "Lower_Bound": "2399.29",
                "Upper_Bound": "7138.30",
            },
            "28/01/2021": {
                "Forecast_Price": "4809.70",
                "Lower_Bound": "2443.11",
                "Upper_Bound": "7176.30",
            },
            "27/02/2021": {
                "Forecast_Price": "4804.68",
                "Lower_Bound": "2441.71",
                "Upper_Bound": "7167.66",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5094.95",
                "Lower_Bound": "4272.92",
                "Upper_Bound": "5916.97",
            },
            "02/08/2020": {
                "Forecast_Price": "5096.84",
                "Lower_Bound": "4171.44",
                "Upper_Bound": "6022.25",
            },
            "03/08/2020": {
                "Forecast_Price": "5109.09",
                "Lower_Bound": "4309.55",
                "Upper_Bound": "5908.64",
            },
            "04/08/2020": {
                "Forecast_Price": "5103.59",
                "Lower_Bound": "4016.63",
                "Upper_Bound": "6190.56",
            },
            "05/08/2020": {
                "Forecast_Price": "5117.35",
                "Lower_Bound": "3712.11",
                "Upper_Bound": "6522.59",
            },
            "06/08/2020": {
                "Forecast_Price": "5127.18",
                "Lower_Bound": "4221.12",
                "Upper_Bound": "6033.23",
            },
            "07/08/2020": {
                "Forecast_Price": "5156.81",
                "Lower_Bound": "4244.36",
                "Upper_Bound": "6069.25",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5215.98",
                "Lower_Bound": "2547.97",
                "Upper_Bound": "7883.99",
            },
            "15/08/2020": {
                "Forecast_Price": "5211.26",
                "Lower_Bound": "2546.60",
                "Upper_Bound": "7875.93",
            },
            "22/08/2020": {
                "Forecast_Price": "5209.82",
                "Lower_Bound": "2546.07",
                "Upper_Bound": "7873.57",
            },
            "29/08/2020": {
                "Forecast_Price": "5205.07",
                "Lower_Bound": "2545.04",
                "Upper_Bound": "7865.09",
            },
            "05/09/2020": {
                "Forecast_Price": "5201.51",
                "Lower_Bound": "2543.96",
                "Upper_Bound": "7859.06",
            },
            "12/09/2020": {
                "Forecast_Price": "5195.98",
                "Lower_Bound": "2542.32",
                "Upper_Bound": "7849.64",
            },
            "19/09/2020": {
                "Forecast_Price": "5194.12",
                "Lower_Bound": "2541.66",
                "Upper_Bound": "7846.59",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5210.20",
                "Lower_Bound": "2544.43",
                "Upper_Bound": "7875.96",
            },
            "30/09/2020": {
                "Forecast_Price": "5190.18",
                "Lower_Bound": "2524.93",
                "Upper_Bound": "7855.42",
            },
            "30/10/2020": {
                "Forecast_Price": "5174.63",
                "Lower_Bound": "2506.91",
                "Upper_Bound": "7842.35",
            },
            "29/11/2020": {
                "Forecast_Price": "5137.79",
                "Lower_Bound": "2476.58",
                "Upper_Bound": "7799.00",
            },
            "29/12/2020": {
                "Forecast_Price": "5137.00",
                "Lower_Bound": "2473.87",
                "Upper_Bound": "7800.12",
            },
            "28/01/2021": {
                "Forecast_Price": "5119.75",
                "Lower_Bound": "2466.51",
                "Upper_Bound": "7772.98",
            },
            "27/02/2021": {
                "Forecast_Price": "5090.16",
                "Lower_Bound": "2452.48",
                "Upper_Bound": "7727.84",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4167.18",
                "Lower_Bound": "3593.60",
                "Upper_Bound": "4740.77",
            },
            "02/08/2020": {
                "Forecast_Price": "4177.61",
                "Lower_Bound": "3477.90",
                "Upper_Bound": "4877.32",
            },
            "03/08/2020": {
                "Forecast_Price": "4171.07",
                "Lower_Bound": "3377.99",
                "Upper_Bound": "4964.14",
            },
            "04/08/2020": {
                "Forecast_Price": "4197.08",
                "Lower_Bound": "3508.96",
                "Upper_Bound": "4885.20",
            },
            "05/08/2020": {
                "Forecast_Price": "4106.45",
                "Lower_Bound": "3227.85",
                "Upper_Bound": "4985.04",
            },
            "06/08/2020": {
                "Forecast_Price": "4167.90",
                "Lower_Bound": "3398.88",
                "Upper_Bound": "4936.92",
            },
            "07/08/2020": {
                "Forecast_Price": "4108.36",
                "Lower_Bound": "3483.34",
                "Upper_Bound": "4733.39",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3840.92",
                "Lower_Bound": "1872.12",
                "Upper_Bound": "5809.72",
            },
            "15/08/2020": {
                "Forecast_Price": "3855.16",
                "Lower_Bound": "1881.83",
                "Upper_Bound": "5828.49",
            },
            "22/08/2020": {
                "Forecast_Price": "3867.95",
                "Lower_Bound": "1889.12",
                "Upper_Bound": "5846.78",
            },
            "29/08/2020": {
                "Forecast_Price": "3882.76",
                "Lower_Bound": "1899.78",
                "Upper_Bound": "5865.74",
            },
            "05/09/2020": {
                "Forecast_Price": "3888.79",
                "Lower_Bound": "1895.77",
                "Upper_Bound": "5881.81",
            },
            "12/09/2020": {
                "Forecast_Price": "3903.03",
                "Lower_Bound": "1905.49",
                "Upper_Bound": "5900.58",
            },
            "19/09/2020": {
                "Forecast_Price": "3915.82",
                "Lower_Bound": "1912.77",
                "Upper_Bound": "5918.88",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3787.79",
                "Lower_Bound": "1801.21",
                "Upper_Bound": "5774.36",
            },
            "30/09/2020": {
                "Forecast_Price": "3771.65",
                "Lower_Bound": "1777.97",
                "Upper_Bound": "5765.32",
            },
            "30/10/2020": {
                "Forecast_Price": "3766.85",
                "Lower_Bound": "1773.62",
                "Upper_Bound": "5760.09",
            },
            "29/11/2020": {
                "Forecast_Price": "3748.75",
                "Lower_Bound": "1746.94",
                "Upper_Bound": "5750.57",
            },
            "29/12/2020": {
                "Forecast_Price": "3743.75",
                "Lower_Bound": "1742.09",
                "Upper_Bound": "5745.42",
            },
            "28/01/2021": {
                "Forecast_Price": "3737.40",
                "Lower_Bound": "1734.18",
                "Upper_Bound": "5740.62",
            },
            "27/02/2021": {
                "Forecast_Price": "3692.21",
                "Lower_Bound": "1671.27",
                "Upper_Bound": "5713.15",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4519.22",
                "Lower_Bound": "3840.57",
                "Upper_Bound": "5197.86",
            },
            "02/08/2020": {
                "Forecast_Price": "4495.64",
                "Lower_Bound": "3700.94",
                "Upper_Bound": "5290.33",
            },
            "03/08/2020": {
                "Forecast_Price": "4526.25",
                "Lower_Bound": "3689.66",
                "Upper_Bound": "5362.84",
            },
            "04/08/2020": {
                "Forecast_Price": "4495.48",
                "Lower_Bound": "3668.96",
                "Upper_Bound": "5322.00",
            },
            "05/08/2020": {
                "Forecast_Price": "4526.75",
                "Lower_Bound": "3771.74",
                "Upper_Bound": "5281.76",
            },
            "06/08/2020": {
                "Forecast_Price": "4501.86",
                "Lower_Bound": "3818.35",
                "Upper_Bound": "5185.38",
            },
            "07/08/2020": {
                "Forecast_Price": "4526.46",
                "Lower_Bound": "3910.49",
                "Upper_Bound": "5142.44",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3081.83",
                "Lower_Bound": "1505.57",
                "Upper_Bound": "4658.08",
            },
            "15/08/2020": {
                "Forecast_Price": "3094.79",
                "Lower_Bound": "1535.82",
                "Upper_Bound": "4653.77",
            },
            "22/08/2020": {
                "Forecast_Price": "3108.35",
                "Lower_Bound": "1537.01",
                "Upper_Bound": "4679.69",
            },
            "29/08/2020": {
                "Forecast_Price": "3102.75",
                "Lower_Bound": "1540.86",
                "Upper_Bound": "4664.64",
            },
            "05/09/2020": {
                "Forecast_Price": "3108.75",
                "Lower_Bound": "1545.44",
                "Upper_Bound": "4672.06",
            },
            "12/09/2020": {
                "Forecast_Price": "3121.71",
                "Lower_Bound": "1575.68",
                "Upper_Bound": "4667.75",
            },
            "19/09/2020": {
                "Forecast_Price": "3135.27",
                "Lower_Bound": "1576.87",
                "Upper_Bound": "4693.66",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3169.30",
                "Lower_Bound": "1465.92",
                "Upper_Bound": "4872.68",
            },
            "30/09/2020": {
                "Forecast_Price": "3320.00",
                "Lower_Bound": "1481.73",
                "Upper_Bound": "5158.26",
            },
            "30/10/2020": {
                "Forecast_Price": "3491.66",
                "Lower_Bound": "1521.74",
                "Upper_Bound": "5461.59",
            },
            "29/11/2020": {
                "Forecast_Price": "3478.62",
                "Lower_Bound": "1496.95",
                "Upper_Bound": "5460.29",
            },
            "29/12/2020": {
                "Forecast_Price": "3402.26",
                "Lower_Bound": "1448.14",
                "Upper_Bound": "5356.38",
            },
            "28/01/2021": {
                "Forecast_Price": "3368.87",
                "Lower_Bound": "1416.87",
                "Upper_Bound": "5320.88",
            },
            "27/02/2021": {
                "Forecast_Price": "3244.24",
                "Lower_Bound": "1322.26",
                "Upper_Bound": "5166.22",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5096.50",
                "Lower_Bound": "4430.06",
                "Upper_Bound": "5762.93",
            },
            "02/08/2020": {
                "Forecast_Price": "5098.23",
                "Lower_Bound": "4470.29",
                "Upper_Bound": "5726.16",
            },
            "03/08/2020": {
                "Forecast_Price": "5109.77",
                "Lower_Bound": "4470.39",
                "Upper_Bound": "5749.14",
            },
            "04/08/2020": {
                "Forecast_Price": "5091.98",
                "Lower_Bound": "4504.69",
                "Upper_Bound": "5679.28",
            },
            "05/08/2020": {
                "Forecast_Price": "5101.79",
                "Lower_Bound": "4395.76",
                "Upper_Bound": "5807.82",
            },
            "06/08/2020": {
                "Forecast_Price": "5081.18",
                "Lower_Bound": "4248.61",
                "Upper_Bound": "5913.76",
            },
            "07/08/2020": {
                "Forecast_Price": "5087.78",
                "Lower_Bound": "4293.74",
                "Upper_Bound": "5881.82",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5192.59",
                "Lower_Bound": "2535.88",
                "Upper_Bound": "7849.30",
            },
            "15/08/2020": {
                "Forecast_Price": "5195.70",
                "Lower_Bound": "2536.87",
                "Upper_Bound": "7854.53",
            },
            "22/08/2020": {
                "Forecast_Price": "5200.43",
                "Lower_Bound": "2537.46",
                "Upper_Bound": "7863.41",
            },
            "29/08/2020": {
                "Forecast_Price": "5203.81",
                "Lower_Bound": "2539.03",
                "Upper_Bound": "7868.59",
            },
            "05/09/2020": {
                "Forecast_Price": "5208.24",
                "Lower_Bound": "2541.00",
                "Upper_Bound": "7875.48",
            },
            "12/09/2020": {
                "Forecast_Price": "5211.35",
                "Lower_Bound": "2541.99",
                "Upper_Bound": "7880.72",
            },
            "19/09/2020": {
                "Forecast_Price": "5216.09",
                "Lower_Bound": "2542.57",
                "Upper_Bound": "7889.60",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5156.94",
                "Lower_Bound": "2497.64",
                "Upper_Bound": "7816.24",
            },
            "30/09/2020": {
                "Forecast_Price": "5109.90",
                "Lower_Bound": "2478.62",
                "Upper_Bound": "7741.18",
            },
            "30/10/2020": {
                "Forecast_Price": "5122.65",
                "Lower_Bound": "2504.92",
                "Upper_Bound": "7740.37",
            },
            "29/11/2020": {
                "Forecast_Price": "5151.34",
                "Lower_Bound": "2520.71",
                "Upper_Bound": "7781.97",
            },
            "29/12/2020": {
                "Forecast_Price": "5171.95",
                "Lower_Bound": "2501.48",
                "Upper_Bound": "7842.41",
            },
            "28/01/2021": {
                "Forecast_Price": "5140.01",
                "Lower_Bound": "2448.38",
                "Upper_Bound": "7831.63",
            },
            "27/02/2021": {
                "Forecast_Price": "5096.23",
                "Lower_Bound": "2395.66",
                "Upper_Bound": "7796.79",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3989.65",
                "Lower_Bound": "3353.08",
                "Upper_Bound": "4626.22",
            },
            "02/08/2020": {
                "Forecast_Price": "3986.07",
                "Lower_Bound": "3232.64",
                "Upper_Bound": "4739.51",
            },
            "03/08/2020": {
                "Forecast_Price": "3984.65",
                "Lower_Bound": "3320.53",
                "Upper_Bound": "4648.76",
            },
            "04/08/2020": {
                "Forecast_Price": "3990.53",
                "Lower_Bound": "3209.41",
                "Upper_Bound": "4771.64",
            },
            "05/08/2020": {
                "Forecast_Price": "3990.61",
                "Lower_Bound": "3254.43",
                "Upper_Bound": "4726.78",
            },
            "06/08/2020": {
                "Forecast_Price": "3985.52",
                "Lower_Bound": "3264.84",
                "Upper_Bound": "4706.20",
            },
            "07/08/2020": {
                "Forecast_Price": "3947.58",
                "Lower_Bound": "3307.08",
                "Upper_Bound": "4588.08",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3905.29",
                "Lower_Bound": "1928.75",
                "Upper_Bound": "5881.84",
            },
            "15/08/2020": {
                "Forecast_Price": "3908.84",
                "Lower_Bound": "1915.74",
                "Upper_Bound": "5901.94",
            },
            "22/08/2020": {
                "Forecast_Price": "3894.86",
                "Lower_Bound": "1899.08",
                "Upper_Bound": "5890.64",
            },
            "29/08/2020": {
                "Forecast_Price": "3916.37",
                "Lower_Bound": "1923.12",
                "Upper_Bound": "5909.61",
            },
            "05/09/2020": {
                "Forecast_Price": "3920.60",
                "Lower_Bound": "1928.44",
                "Upper_Bound": "5912.76",
            },
            "12/09/2020": {
                "Forecast_Price": "3919.57",
                "Lower_Bound": "1913.93",
                "Upper_Bound": "5925.21",
            },
            "19/09/2020": {
                "Forecast_Price": "3902.99",
                "Lower_Bound": "1896.42",
                "Upper_Bound": "5909.57",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4017.86",
                "Lower_Bound": "1929.57",
                "Upper_Bound": "6106.14",
            },
            "30/09/2020": {
                "Forecast_Price": "4086.59",
                "Lower_Bound": "1977.26",
                "Upper_Bound": "6195.92",
            },
            "30/10/2020": {
                "Forecast_Price": "4196.06",
                "Lower_Bound": "2057.69",
                "Upper_Bound": "6334.43",
            },
            "29/11/2020": {
                "Forecast_Price": "4239.01",
                "Lower_Bound": "2078.84",
                "Upper_Bound": "6399.19",
            },
            "29/12/2020": {
                "Forecast_Price": "4330.27",
                "Lower_Bound": "2116.97",
                "Upper_Bound": "6543.57",
            },
            "28/01/2021": {
                "Forecast_Price": "4373.31",
                "Lower_Bound": "2135.18",
                "Upper_Bound": "6611.43",
            },
            "27/02/2021": {
                "Forecast_Price": "4250.45",
                "Lower_Bound": "2053.11",
                "Upper_Bound": "6447.79",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4357.49",
                "Lower_Bound": "3722.56",
                "Upper_Bound": "4992.41",
            },
            "02/08/2020": {
                "Forecast_Price": "4352.52",
                "Lower_Bound": "3789.89",
                "Upper_Bound": "4915.14",
            },
            "03/08/2020": {
                "Forecast_Price": "4358.76",
                "Lower_Bound": "3762.85",
                "Upper_Bound": "4954.68",
            },
            "04/08/2020": {
                "Forecast_Price": "4351.99",
                "Lower_Bound": "3706.70",
                "Upper_Bound": "4997.27",
            },
            "05/08/2020": {
                "Forecast_Price": "4356.77",
                "Lower_Bound": "3754.83",
                "Upper_Bound": "4958.72",
            },
            "06/08/2020": {
                "Forecast_Price": "4351.97",
                "Lower_Bound": "3777.57",
                "Upper_Bound": "4926.38",
            },
            "07/08/2020": {
                "Forecast_Price": "4340.60",
                "Lower_Bound": "3515.65",
                "Upper_Bound": "5165.56",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3574.93",
                "Lower_Bound": "1747.90",
                "Upper_Bound": "5401.97",
            },
            "15/08/2020": {
                "Forecast_Price": "3372.17",
                "Lower_Bound": "1620.35",
                "Upper_Bound": "5124.00",
            },
            "22/08/2020": {
                "Forecast_Price": "3355.03",
                "Lower_Bound": "1594.37",
                "Upper_Bound": "5115.69",
            },
            "29/08/2020": {
                "Forecast_Price": "3545.42",
                "Lower_Bound": "1688.32",
                "Upper_Bound": "5402.52",
            },
            "05/09/2020": {
                "Forecast_Price": "3701.18",
                "Lower_Bound": "1762.46",
                "Upper_Bound": "5639.89",
            },
            "12/09/2020": {
                "Forecast_Price": "3527.08",
                "Lower_Bound": "1682.84",
                "Upper_Bound": "5371.33",
            },
            "19/09/2020": {
                "Forecast_Price": "3522.83",
                "Lower_Bound": "1678.40",
                "Upper_Bound": "5367.25",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3205.44",
                "Lower_Bound": "1538.26",
                "Upper_Bound": "4872.63",
            },
            "30/09/2020": {
                "Forecast_Price": "3211.98",
                "Lower_Bound": "1531.81",
                "Upper_Bound": "4892.15",
            },
            "30/10/2020": {
                "Forecast_Price": "3220.77",
                "Lower_Bound": "1529.53",
                "Upper_Bound": "4912.01",
            },
            "29/11/2020": {
                "Forecast_Price": "3233.02",
                "Lower_Bound": "1533.43",
                "Upper_Bound": "4932.61",
            },
            "29/12/2020": {
                "Forecast_Price": "3243.87",
                "Lower_Bound": "1535.39",
                "Upper_Bound": "4952.35",
            },
            "28/01/2021": {
                "Forecast_Price": "3254.31",
                "Lower_Bound": "1533.28",
                "Upper_Bound": "4975.34",
            },
            "27/02/2021": {
                "Forecast_Price": "3238.92",
                "Lower_Bound": "1501.34",
                "Upper_Bound": "4976.50",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4872.20",
                "Lower_Bound": "3829.77",
                "Upper_Bound": "5914.62",
            },
            "02/08/2020": {
                "Forecast_Price": "4860.96",
                "Lower_Bound": "4153.31",
                "Upper_Bound": "5568.60",
            },
            "03/08/2020": {
                "Forecast_Price": "4866.92",
                "Lower_Bound": "4112.84",
                "Upper_Bound": "5620.99",
            },
            "04/08/2020": {
                "Forecast_Price": "4852.80",
                "Lower_Bound": "4039.02",
                "Upper_Bound": "5666.59",
            },
            "05/08/2020": {
                "Forecast_Price": "4959.04",
                "Lower_Bound": "3837.95",
                "Upper_Bound": "6080.13",
            },
            "06/08/2020": {
                "Forecast_Price": "4844.96",
                "Lower_Bound": "4231.93",
                "Upper_Bound": "5457.99",
            },
            "07/08/2020": {
                "Forecast_Price": "4854.31",
                "Lower_Bound": "4184.51",
                "Upper_Bound": "5524.11",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4795.32",
                "Lower_Bound": "2340.82",
                "Upper_Bound": "7249.82",
            },
            "15/08/2020": {
                "Forecast_Price": "4795.94",
                "Lower_Bound": "2339.99",
                "Upper_Bound": "7251.88",
            },
            "22/08/2020": {
                "Forecast_Price": "4787.52",
                "Lower_Bound": "2336.21",
                "Upper_Bound": "7238.83",
            },
            "29/08/2020": {
                "Forecast_Price": "4770.61",
                "Lower_Bound": "2329.63",
                "Upper_Bound": "7211.59",
            },
            "05/09/2020": {
                "Forecast_Price": "4777.18",
                "Lower_Bound": "2330.76",
                "Upper_Bound": "7223.60",
            },
            "12/09/2020": {
                "Forecast_Price": "4777.79",
                "Lower_Bound": "2329.93",
                "Upper_Bound": "7225.65",
            },
            "19/09/2020": {
                "Forecast_Price": "4769.38",
                "Lower_Bound": "2326.14",
                "Upper_Bound": "7212.61",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4745.84",
                "Lower_Bound": "2277.22",
                "Upper_Bound": "7214.46",
            },
            "30/09/2020": {
                "Forecast_Price": "4642.93",
                "Lower_Bound": "2108.06",
                "Upper_Bound": "7177.81",
            },
            "30/10/2020": {
                "Forecast_Price": "4563.69",
                "Lower_Bound": "1983.22",
                "Upper_Bound": "7144.16",
            },
            "29/11/2020": {
                "Forecast_Price": "4478.32",
                "Lower_Bound": "1887.99",
                "Upper_Bound": "7068.65",
            },
            "29/12/2020": {
                "Forecast_Price": "4390.93",
                "Lower_Bound": "1794.42",
                "Upper_Bound": "6987.44",
            },
            "28/01/2021": {
                "Forecast_Price": "4310.54",
                "Lower_Bound": "1725.56",
                "Upper_Bound": "6895.52",
            },
            "27/02/2021": {
                "Forecast_Price": "4257.91",
                "Lower_Bound": "1705.58",
                "Upper_Bound": "6810.25",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4314.35",
                "Lower_Bound": "3493.71",
                "Upper_Bound": "5135.00",
            },
            "02/08/2020": {
                "Forecast_Price": "4312.66",
                "Lower_Bound": "3349.55",
                "Upper_Bound": "5275.78",
            },
            "03/08/2020": {
                "Forecast_Price": "4312.47",
                "Lower_Bound": "3573.32",
                "Upper_Bound": "5051.61",
            },
            "04/08/2020": {
                "Forecast_Price": "4315.12",
                "Lower_Bound": "3611.27",
                "Upper_Bound": "5018.98",
            },
            "05/08/2020": {
                "Forecast_Price": "4332.65",
                "Lower_Bound": "3667.46",
                "Upper_Bound": "4997.84",
            },
            "06/08/2020": {
                "Forecast_Price": "4315.02",
                "Lower_Bound": "3565.10",
                "Upper_Bound": "5064.95",
            },
            "07/08/2020": {
                "Forecast_Price": "4340.72",
                "Lower_Bound": "3618.60",
                "Upper_Bound": "5062.83",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4255.83",
                "Lower_Bound": "2100.68",
                "Upper_Bound": "6410.97",
            },
            "15/08/2020": {
                "Forecast_Price": "4220.21",
                "Lower_Bound": "2075.98",
                "Upper_Bound": "6364.43",
            },
            "22/08/2020": {
                "Forecast_Price": "4198.69",
                "Lower_Bound": "2059.04",
                "Upper_Bound": "6338.33",
            },
            "29/08/2020": {
                "Forecast_Price": "4183.10",
                "Lower_Bound": "2056.65",
                "Upper_Bound": "6309.55",
            },
            "05/09/2020": {
                "Forecast_Price": "4201.30",
                "Lower_Bound": "2094.34",
                "Upper_Bound": "6308.26",
            },
            "12/09/2020": {
                "Forecast_Price": "4187.71",
                "Lower_Bound": "2076.87",
                "Upper_Bound": "6298.55",
            },
            "19/09/2020": {
                "Forecast_Price": "4176.02",
                "Lower_Bound": "2063.16",
                "Upper_Bound": "6288.88",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4073.00",
                "Lower_Bound": "1863.86",
                "Upper_Bound": "6282.14",
            },
            "30/09/2020": {
                "Forecast_Price": "3995.57",
                "Lower_Bound": "1750.90",
                "Upper_Bound": "6240.23",
            },
            "30/10/2020": {
                "Forecast_Price": "3924.30",
                "Lower_Bound": "1647.71",
                "Upper_Bound": "6200.89",
            },
            "29/11/2020": {
                "Forecast_Price": "3847.76",
                "Lower_Bound": "1535.19",
                "Upper_Bound": "6160.34",
            },
            "29/12/2020": {
                "Forecast_Price": "3782.95",
                "Lower_Bound": "1441.77",
                "Upper_Bound": "6124.14",
            },
            "28/01/2021": {
                "Forecast_Price": "3695.13",
                "Lower_Bound": "1317.08",
                "Upper_Bound": "6073.18",
            },
            "27/02/2021": {
                "Forecast_Price": "3558.80",
                "Lower_Bound": "1151.89",
                "Upper_Bound": "5965.71",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5198.81",
                "Lower_Bound": "4343.61",
                "Upper_Bound": "6054.01",
            },
            "02/08/2020": {
                "Forecast_Price": "5213.49",
                "Lower_Bound": "4461.32",
                "Upper_Bound": "5965.66",
            },
            "03/08/2020": {
                "Forecast_Price": "5197.80",
                "Lower_Bound": "4052.54",
                "Upper_Bound": "6343.06",
            },
            "04/08/2020": {
                "Forecast_Price": "5206.79",
                "Lower_Bound": "4338.21",
                "Upper_Bound": "6075.36",
            },
            "05/08/2020": {
                "Forecast_Price": "5186.17",
                "Lower_Bound": "4258.70",
                "Upper_Bound": "6113.65",
            },
            "06/08/2020": {
                "Forecast_Price": "5174.93",
                "Lower_Bound": "4086.98",
                "Upper_Bound": "6262.87",
            },
            "07/08/2020": {
                "Forecast_Price": "5207.98",
                "Lower_Bound": "4196.01",
                "Upper_Bound": "6219.95",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5177.99",
                "Lower_Bound": "2529.17",
                "Upper_Bound": "7826.82",
            },
            "15/08/2020": {
                "Forecast_Price": "5172.21",
                "Lower_Bound": "2527.01",
                "Upper_Bound": "7817.42",
            },
            "22/08/2020": {
                "Forecast_Price": "5167.58",
                "Lower_Bound": "2525.16",
                "Upper_Bound": "7810.00",
            },
            "29/08/2020": {
                "Forecast_Price": "5161.86",
                "Lower_Bound": "2522.92",
                "Upper_Bound": "7800.80",
            },
            "05/09/2020": {
                "Forecast_Price": "5158.20",
                "Lower_Bound": "2521.50",
                "Upper_Bound": "7794.91",
            },
            "12/09/2020": {
                "Forecast_Price": "5152.76",
                "Lower_Bound": "2519.45",
                "Upper_Bound": "7786.07",
            },
            "19/09/2020": {
                "Forecast_Price": "5148.28",
                "Lower_Bound": "2517.65",
                "Upper_Bound": "7778.91",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5142.54",
                "Lower_Bound": "2503.84",
                "Upper_Bound": "7781.25",
            },
            "30/09/2020": {
                "Forecast_Price": "5127.22",
                "Lower_Bound": "2522.91",
                "Upper_Bound": "7731.53",
            },
            "30/10/2020": {
                "Forecast_Price": "5132.64",
                "Lower_Bound": "2558.61",
                "Upper_Bound": "7706.68",
            },
            "29/11/2020": {
                "Forecast_Price": "5129.25",
                "Lower_Bound": "2583.85",
                "Upper_Bound": "7674.65",
            },
            "29/12/2020": {
                "Forecast_Price": "5127.61",
                "Lower_Bound": "2613.47",
                "Upper_Bound": "7641.76",
            },
            "28/01/2021": {
                "Forecast_Price": "5110.73",
                "Lower_Bound": "2626.33",
                "Upper_Bound": "7595.13",
            },
            "27/02/2021": {
                "Forecast_Price": "5093.99",
                "Lower_Bound": "2633.42",
                "Upper_Bound": "7554.56",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4804.30",
                "Lower_Bound": "3687.07",
                "Upper_Bound": "5921.53",
            },
            "02/08/2020": {
                "Forecast_Price": "4814.86",
                "Lower_Bound": "4057.91",
                "Upper_Bound": "5571.80",
            },
            "03/08/2020": {
                "Forecast_Price": "4755.71",
                "Lower_Bound": "4070.40",
                "Upper_Bound": "5441.03",
            },
            "04/08/2020": {
                "Forecast_Price": "4724.69",
                "Lower_Bound": "4092.06",
                "Upper_Bound": "5357.31",
            },
            "05/08/2020": {
                "Forecast_Price": "4803.46",
                "Lower_Bound": "4136.66",
                "Upper_Bound": "5470.27",
            },
            "06/08/2020": {
                "Forecast_Price": "4725.24",
                "Lower_Bound": "4147.76",
                "Upper_Bound": "5302.73",
            },
            "07/08/2020": {
                "Forecast_Price": "4683.21",
                "Lower_Bound": "4143.35",
                "Upper_Bound": "5223.07",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4810.43",
                "Lower_Bound": "2355.43",
                "Upper_Bound": "7265.44",
            },
            "15/08/2020": {
                "Forecast_Price": "4911.56",
                "Lower_Bound": "2391.18",
                "Upper_Bound": "7431.93",
            },
            "22/08/2020": {
                "Forecast_Price": "4890.41",
                "Lower_Bound": "2384.34",
                "Upper_Bound": "7396.49",
            },
            "29/08/2020": {
                "Forecast_Price": "4804.45",
                "Lower_Bound": "2357.29",
                "Upper_Bound": "7251.60",
            },
            "05/09/2020": {
                "Forecast_Price": "4869.53",
                "Lower_Bound": "2376.62",
                "Upper_Bound": "7362.44",
            },
            "12/09/2020": {
                "Forecast_Price": "4970.65",
                "Lower_Bound": "2412.37",
                "Upper_Bound": "7528.93",
            },
            "19/09/2020": {
                "Forecast_Price": "4949.51",
                "Lower_Bound": "2405.53",
                "Upper_Bound": "7493.49",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4808.78",
                "Lower_Bound": "2364.06",
                "Upper_Bound": "7253.51",
            },
            "30/09/2020": {
                "Forecast_Price": "4971.17",
                "Lower_Bound": "2480.91",
                "Upper_Bound": "7461.43",
            },
            "30/10/2020": {
                "Forecast_Price": "5275.51",
                "Lower_Bound": "2598.43",
                "Upper_Bound": "7952.59",
            },
            "29/11/2020": {
                "Forecast_Price": "5558.26",
                "Lower_Bound": "2706.00",
                "Upper_Bound": "8410.52",
            },
            "29/12/2020": {
                "Forecast_Price": "5830.84",
                "Lower_Bound": "2813.93",
                "Upper_Bound": "8847.74",
            },
            "28/01/2021": {
                "Forecast_Price": "6051.13",
                "Lower_Bound": "2900.92",
                "Upper_Bound": "9201.34",
            },
            "27/02/2021": {
                "Forecast_Price": "6070.55",
                "Lower_Bound": "2901.90",
                "Upper_Bound": "9239.21",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4801.30",
                "Lower_Bound": "3967.00",
                "Upper_Bound": "5635.59",
            },
            "02/08/2020": {
                "Forecast_Price": "4796.05",
                "Lower_Bound": "4166.50",
                "Upper_Bound": "5425.59",
            },
            "03/08/2020": {
                "Forecast_Price": "4777.11",
                "Lower_Bound": "3941.77",
                "Upper_Bound": "5612.45",
            },
            "04/08/2020": {
                "Forecast_Price": "4747.30",
                "Lower_Bound": "4035.89",
                "Upper_Bound": "5458.71",
            },
            "05/08/2020": {
                "Forecast_Price": "4762.36",
                "Lower_Bound": "4073.49",
                "Upper_Bound": "5451.23",
            },
            "06/08/2020": {
                "Forecast_Price": "4744.83",
                "Lower_Bound": "3921.98",
                "Upper_Bound": "5567.67",
            },
            "07/08/2020": {
                "Forecast_Price": "4731.06",
                "Lower_Bound": "4139.25",
                "Upper_Bound": "5322.87",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4874.26",
                "Lower_Bound": "2389.67",
                "Upper_Bound": "7358.85",
            },
            "15/08/2020": {
                "Forecast_Price": "4905.20",
                "Lower_Bound": "2421.28",
                "Upper_Bound": "7389.13",
            },
            "22/08/2020": {
                "Forecast_Price": "4920.30",
                "Lower_Bound": "2427.54",
                "Upper_Bound": "7413.07",
            },
            "29/08/2020": {
                "Forecast_Price": "4931.25",
                "Lower_Bound": "2430.90",
                "Upper_Bound": "7431.60",
            },
            "05/09/2020": {
                "Forecast_Price": "4946.73",
                "Lower_Bound": "2454.96",
                "Upper_Bound": "7438.50",
            },
            "12/09/2020": {
                "Forecast_Price": "4977.71",
                "Lower_Bound": "2486.58",
                "Upper_Bound": "7468.84",
            },
            "19/09/2020": {
                "Forecast_Price": "4989.88",
                "Lower_Bound": "2491.88",
                "Upper_Bound": "7487.87",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4837.82",
                "Lower_Bound": "2406.69",
                "Upper_Bound": "7268.96",
            },
            "30/09/2020": {
                "Forecast_Price": "4820.42",
                "Lower_Bound": "2408.16",
                "Upper_Bound": "7232.68",
            },
            "30/10/2020": {
                "Forecast_Price": "4815.20",
                "Lower_Bound": "2413.94",
                "Upper_Bound": "7216.47",
            },
            "29/11/2020": {
                "Forecast_Price": "4791.48",
                "Lower_Bound": "2404.54",
                "Upper_Bound": "7178.41",
            },
            "29/12/2020": {
                "Forecast_Price": "4778.02",
                "Lower_Bound": "2408.94",
                "Upper_Bound": "7147.09",
            },
            "28/01/2021": {
                "Forecast_Price": "4837.00",
                "Lower_Bound": "2458.61",
                "Upper_Bound": "7215.39",
            },
            "27/02/2021": {
                "Forecast_Price": "4792.36",
                "Lower_Bound": "2423.94",
                "Upper_Bound": "7160.79",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4798.47",
                "Lower_Bound": "3987.92",
                "Upper_Bound": "5609.03",
            },
            "02/08/2020": {
                "Forecast_Price": "4805.70",
                "Lower_Bound": "4029.42",
                "Upper_Bound": "5581.99",
            },
            "03/08/2020": {
                "Forecast_Price": "4811.62",
                "Lower_Bound": "3969.73",
                "Upper_Bound": "5653.51",
            },
            "04/08/2020": {
                "Forecast_Price": "4818.60",
                "Lower_Bound": "3953.30",
                "Upper_Bound": "5683.90",
            },
            "05/08/2020": {
                "Forecast_Price": "4779.71",
                "Lower_Bound": "4083.24",
                "Upper_Bound": "5476.18",
            },
            "06/08/2020": {
                "Forecast_Price": "4776.15",
                "Lower_Bound": "3879.05",
                "Upper_Bound": "5673.24",
            },
            "07/08/2020": {
                "Forecast_Price": "4753.55",
                "Lower_Bound": "4049.29",
                "Upper_Bound": "5457.81",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4852.06",
                "Lower_Bound": "2361.74",
                "Upper_Bound": "7342.39",
            },
            "15/08/2020": {
                "Forecast_Price": "4877.18",
                "Lower_Bound": "2376.53",
                "Upper_Bound": "7377.83",
            },
            "22/08/2020": {
                "Forecast_Price": "4878.17",
                "Lower_Bound": "2365.67",
                "Upper_Bound": "7390.67",
            },
            "29/08/2020": {
                "Forecast_Price": "4870.49",
                "Lower_Bound": "2362.89",
                "Upper_Bound": "7378.09",
            },
            "05/09/2020": {
                "Forecast_Price": "4855.99",
                "Lower_Bound": "2351.66",
                "Upper_Bound": "7360.32",
            },
            "12/09/2020": {
                "Forecast_Price": "4881.11",
                "Lower_Bound": "2366.45",
                "Upper_Bound": "7395.76",
            },
            "19/09/2020": {
                "Forecast_Price": "4882.09",
                "Lower_Bound": "2355.58",
                "Upper_Bound": "7408.60",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4415.71",
                "Lower_Bound": "2226.49",
                "Upper_Bound": "6604.93",
            },
            "30/09/2020": {
                "Forecast_Price": "4506.05",
                "Lower_Bound": "2256.89",
                "Upper_Bound": "6755.20",
            },
            "30/10/2020": {
                "Forecast_Price": "4540.99",
                "Lower_Bound": "2270.13",
                "Upper_Bound": "6811.85",
            },
            "29/11/2020": {
                "Forecast_Price": "4592.11",
                "Lower_Bound": "2283.77",
                "Upper_Bound": "6900.45",
            },
            "29/12/2020": {
                "Forecast_Price": "4711.88",
                "Lower_Bound": "2320.49",
                "Upper_Bound": "7103.26",
            },
            "28/01/2021": {
                "Forecast_Price": "4816.19",
                "Lower_Bound": "2336.20",
                "Upper_Bound": "7296.18",
            },
            "27/02/2021": {
                "Forecast_Price": "4875.08",
                "Lower_Bound": "2332.92",
                "Upper_Bound": "7417.25",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4807.54",
                "Lower_Bound": "3893.75",
                "Upper_Bound": "5721.34",
            },
            "02/08/2020": {
                "Forecast_Price": "4803.76",
                "Lower_Bound": "3809.67",
                "Upper_Bound": "5797.85",
            },
            "03/08/2020": {
                "Forecast_Price": "4773.66",
                "Lower_Bound": "4045.05",
                "Upper_Bound": "5502.27",
            },
            "04/08/2020": {
                "Forecast_Price": "4763.68",
                "Lower_Bound": "4109.04",
                "Upper_Bound": "5418.32",
            },
            "05/08/2020": {
                "Forecast_Price": "4756.62",
                "Lower_Bound": "4188.46",
                "Upper_Bound": "5324.78",
            },
            "06/08/2020": {
                "Forecast_Price": "4712.96",
                "Lower_Bound": "4088.23",
                "Upper_Bound": "5337.68",
            },
            "07/08/2020": {
                "Forecast_Price": "4729.77",
                "Lower_Bound": "4223.84",
                "Upper_Bound": "5235.70",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4772.56",
                "Lower_Bound": "2323.12",
                "Upper_Bound": "7222.01",
            },
            "15/08/2020": {
                "Forecast_Price": "4781.98",
                "Lower_Bound": "2332.85",
                "Upper_Bound": "7231.11",
            },
            "22/08/2020": {
                "Forecast_Price": "4675.11",
                "Lower_Bound": "2269.46",
                "Upper_Bound": "7080.76",
            },
            "29/08/2020": {
                "Forecast_Price": "4720.23",
                "Lower_Bound": "2284.00",
                "Upper_Bound": "7156.46",
            },
            "05/09/2020": {
                "Forecast_Price": "4641.05",
                "Lower_Bound": "2248.38",
                "Upper_Bound": "7033.73",
            },
            "12/09/2020": {
                "Forecast_Price": "4648.81",
                "Lower_Bound": "2255.34",
                "Upper_Bound": "7042.29",
            },
            "19/09/2020": {
                "Forecast_Price": "4552.70",
                "Lower_Bound": "2209.93",
                "Upper_Bound": "6895.47",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4883.04",
                "Lower_Bound": "2372.32",
                "Upper_Bound": "7393.76",
            },
            "30/09/2020": {
                "Forecast_Price": "4864.42",
                "Lower_Bound": "2360.86",
                "Upper_Bound": "7367.98",
            },
            "30/10/2020": {
                "Forecast_Price": "5241.41",
                "Lower_Bound": "2480.62",
                "Upper_Bound": "8002.20",
            },
            "29/11/2020": {
                "Forecast_Price": "5317.15",
                "Lower_Bound": "2498.62",
                "Upper_Bound": "8135.68",
            },
            "29/12/2020": {
                "Forecast_Price": "4858.09",
                "Lower_Bound": "2341.63",
                "Upper_Bound": "7374.56",
            },
            "28/01/2021": {
                "Forecast_Price": "4342.85",
                "Lower_Bound": "2167.45",
                "Upper_Bound": "6518.24",
            },
            "27/02/2021": {
                "Forecast_Price": "3902.09",
                "Lower_Bound": "2017.71",
                "Upper_Bound": "5786.46",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4176.54",
                "Lower_Bound": "3515.00",
                "Upper_Bound": "4838.09",
            },
            "02/08/2020": {
                "Forecast_Price": "4171.10",
                "Lower_Bound": "3713.37",
                "Upper_Bound": "4628.82",
            },
            "03/08/2020": {
                "Forecast_Price": "4165.14",
                "Lower_Bound": "3678.85",
                "Upper_Bound": "4651.44",
            },
            "04/08/2020": {
                "Forecast_Price": "4145.45",
                "Lower_Bound": "3618.39",
                "Upper_Bound": "4672.51",
            },
            "05/08/2020": {
                "Forecast_Price": "4159.91",
                "Lower_Bound": "3671.61",
                "Upper_Bound": "4648.21",
            },
            "06/08/2020": {
                "Forecast_Price": "4156.13",
                "Lower_Bound": "3653.32",
                "Upper_Bound": "4658.95",
            },
            "07/08/2020": {
                "Forecast_Price": "4145.19",
                "Lower_Bound": "3669.50",
                "Upper_Bound": "4620.89",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4190.42",
                "Lower_Bound": "2040.38",
                "Upper_Bound": "6340.45",
            },
            "15/08/2020": {
                "Forecast_Price": "4151.40",
                "Lower_Bound": "2029.94",
                "Upper_Bound": "6272.86",
            },
            "22/08/2020": {
                "Forecast_Price": "4151.71",
                "Lower_Bound": "2032.57",
                "Upper_Bound": "6270.86",
            },
            "29/08/2020": {
                "Forecast_Price": "4125.80",
                "Lower_Bound": "2026.33",
                "Upper_Bound": "6225.27",
            },
            "05/09/2020": {
                "Forecast_Price": "4192.86",
                "Lower_Bound": "2050.87",
                "Upper_Bound": "6334.86",
            },
            "12/09/2020": {
                "Forecast_Price": "4153.73",
                "Lower_Bound": "2040.24",
                "Upper_Bound": "6267.23",
            },
            "19/09/2020": {
                "Forecast_Price": "4153.75",
                "Lower_Bound": "2042.38",
                "Upper_Bound": "6265.13",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4137.41",
                "Lower_Bound": "2016.95",
                "Upper_Bound": "6257.87",
            },
            "30/09/2020": {
                "Forecast_Price": "4075.36",
                "Lower_Bound": "1953.24",
                "Upper_Bound": "6197.48",
            },
            "30/10/2020": {
                "Forecast_Price": "4243.76",
                "Lower_Bound": "1976.40",
                "Upper_Bound": "6511.11",
            },
            "29/11/2020": {
                "Forecast_Price": "4152.17",
                "Lower_Bound": "1902.98",
                "Upper_Bound": "6401.35",
            },
            "29/12/2020": {
                "Forecast_Price": "4075.25",
                "Lower_Bound": "1838.49",
                "Upper_Bound": "6312.02",
            },
            "28/01/2021": {
                "Forecast_Price": "4041.17",
                "Lower_Bound": "1797.66",
                "Upper_Bound": "6284.69",
            },
            "27/02/2021": {
                "Forecast_Price": "3888.73",
                "Lower_Bound": "1700.56",
                "Upper_Bound": "6076.90",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4480.45",
                "Lower_Bound": "3719.28",
                "Upper_Bound": "5241.62",
            },
            "02/08/2020": {
                "Forecast_Price": "4486.09",
                "Lower_Bound": "3481.33",
                "Upper_Bound": "5490.85",
            },
            "03/08/2020": {
                "Forecast_Price": "4473.27",
                "Lower_Bound": "3855.28",
                "Upper_Bound": "5091.26",
            },
            "04/08/2020": {
                "Forecast_Price": "4480.18",
                "Lower_Bound": "3867.49",
                "Upper_Bound": "5092.88",
            },
            "05/08/2020": {
                "Forecast_Price": "4469.02",
                "Lower_Bound": "3695.13",
                "Upper_Bound": "5242.90",
            },
            "06/08/2020": {
                "Forecast_Price": "4481.95",
                "Lower_Bound": "3568.06",
                "Upper_Bound": "5395.83",
            },
            "07/08/2020": {
                "Forecast_Price": "4488.12",
                "Lower_Bound": "3793.77",
                "Upper_Bound": "5182.46",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3984.34",
                "Lower_Bound": "1947.21",
                "Upper_Bound": "6021.47",
            },
            "15/08/2020": {
                "Forecast_Price": "3983.68",
                "Lower_Bound": "1948.13",
                "Upper_Bound": "6019.23",
            },
            "22/08/2020": {
                "Forecast_Price": "3983.02",
                "Lower_Bound": "1949.05",
                "Upper_Bound": "6017.00",
            },
            "29/08/2020": {
                "Forecast_Price": "3982.40",
                "Lower_Bound": "1950.00",
                "Upper_Bound": "6014.79",
            },
            "05/09/2020": {
                "Forecast_Price": "3981.58",
                "Lower_Bound": "1950.88",
                "Upper_Bound": "6012.29",
            },
            "12/09/2020": {
                "Forecast_Price": "3980.77",
                "Lower_Bound": "1951.74",
                "Upper_Bound": "6009.80",
            },
            "19/09/2020": {
                "Forecast_Price": "3979.97",
                "Lower_Bound": "1952.62",
                "Upper_Bound": "6007.33",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3959.17",
                "Lower_Bound": "1939.76",
                "Upper_Bound": "5978.58",
            },
            "30/09/2020": {
                "Forecast_Price": "3907.98",
                "Lower_Bound": "1890.95",
                "Upper_Bound": "5925.01",
            },
            "30/10/2020": {
                "Forecast_Price": "3984.78",
                "Lower_Bound": "1927.64",
                "Upper_Bound": "6041.91",
            },
            "29/11/2020": {
                "Forecast_Price": "3960.85",
                "Lower_Bound": "1899.78",
                "Upper_Bound": "6021.91",
            },
            "29/12/2020": {
                "Forecast_Price": "3951.66",
                "Lower_Bound": "1891.73",
                "Upper_Bound": "6011.59",
            },
            "28/01/2021": {
                "Forecast_Price": "3939.14",
                "Lower_Bound": "1893.74",
                "Upper_Bound": "5984.53",
            },
            "27/02/2021": {
                "Forecast_Price": "3862.53",
                "Lower_Bound": "1837.44",
                "Upper_Bound": "5887.62",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4508.80",
                "Lower_Bound": "3356.33",
                "Upper_Bound": "5661.26",
            },
            "02/08/2020": {
                "Forecast_Price": "4484.70",
                "Lower_Bound": "3851.94",
                "Upper_Bound": "5117.46",
            },
            "03/08/2020": {
                "Forecast_Price": "4481.21",
                "Lower_Bound": "3267.54",
                "Upper_Bound": "5694.87",
            },
            "04/08/2020": {
                "Forecast_Price": "4458.23",
                "Lower_Bound": "3504.59",
                "Upper_Bound": "5411.86",
            },
            "05/08/2020": {
                "Forecast_Price": "4451.71",
                "Lower_Bound": "3380.10",
                "Upper_Bound": "5523.32",
            },
            "06/08/2020": {
                "Forecast_Price": "4453.89",
                "Lower_Bound": "3651.00",
                "Upper_Bound": "5256.78",
            },
            "07/08/2020": {
                "Forecast_Price": "4519.94",
                "Lower_Bound": "3832.89",
                "Upper_Bound": "5206.98",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3973.89",
                "Lower_Bound": "1955.77",
                "Upper_Bound": "5992.01",
            },
            "15/08/2020": {
                "Forecast_Price": "3963.74",
                "Lower_Bound": "1946.47",
                "Upper_Bound": "5981.01",
            },
            "22/08/2020": {
                "Forecast_Price": "3968.07",
                "Lower_Bound": "1940.84",
                "Upper_Bound": "5995.30",
            },
            "29/08/2020": {
                "Forecast_Price": "3985.20",
                "Lower_Bound": "1970.73",
                "Upper_Bound": "5999.68",
            },
            "05/09/2020": {
                "Forecast_Price": "3990.02",
                "Lower_Bound": "1969.85",
                "Upper_Bound": "6010.18",
            },
            "12/09/2020": {
                "Forecast_Price": "3979.86",
                "Lower_Bound": "1960.55",
                "Upper_Bound": "5999.18",
            },
            "19/09/2020": {
                "Forecast_Price": "3984.19",
                "Lower_Bound": "1954.92",
                "Upper_Bound": "6013.47",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4064.82",
                "Lower_Bound": "1964.21",
                "Upper_Bound": "6165.42",
            },
            "30/09/2020": {
                "Forecast_Price": "4115.53",
                "Lower_Bound": "1982.82",
                "Upper_Bound": "6248.25",
            },
            "30/10/2020": {
                "Forecast_Price": "4153.22",
                "Lower_Bound": "1988.79",
                "Upper_Bound": "6317.65",
            },
            "29/11/2020": {
                "Forecast_Price": "4166.57",
                "Lower_Bound": "1992.95",
                "Upper_Bound": "6340.20",
            },
            "29/12/2020": {
                "Forecast_Price": "4191.14",
                "Lower_Bound": "2010.29",
                "Upper_Bound": "6372.00",
            },
            "28/01/2021": {
                "Forecast_Price": "4162.13",
                "Lower_Bound": "2008.25",
                "Upper_Bound": "6316.00",
            },
            "27/02/2021": {
                "Forecast_Price": "4041.65",
                "Lower_Bound": "1953.64",
                "Upper_Bound": "6129.66",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3742.68",
                "Lower_Bound": "3134.05",
                "Upper_Bound": "4351.31",
            },
            "02/08/2020": {
                "Forecast_Price": "3305.45",
                "Lower_Bound": "2740.27",
                "Upper_Bound": "3870.64",
            },
            "03/08/2020": {
                "Forecast_Price": "3310.70",
                "Lower_Bound": "2718.55",
                "Upper_Bound": "3902.86",
            },
            "04/08/2020": {
                "Forecast_Price": "3282.58",
                "Lower_Bound": "2733.74",
                "Upper_Bound": "3831.43",
            },
            "05/08/2020": {
                "Forecast_Price": "3302.38",
                "Lower_Bound": "2751.53",
                "Upper_Bound": "3853.24",
            },
            "06/08/2020": {
                "Forecast_Price": "3329.54",
                "Lower_Bound": "2924.22",
                "Upper_Bound": "3734.86",
            },
            "07/08/2020": {
                "Forecast_Price": "3180.62",
                "Lower_Bound": "2648.35",
                "Upper_Bound": "3712.89",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3745.83",
                "Lower_Bound": "1815.48",
                "Upper_Bound": "5676.19",
            },
            "15/08/2020": {
                "Forecast_Price": "3635.84",
                "Lower_Bound": "1779.31",
                "Upper_Bound": "5492.37",
            },
            "22/08/2020": {
                "Forecast_Price": "3460.48",
                "Lower_Bound": "1723.82",
                "Upper_Bound": "5197.14",
            },
            "29/08/2020": {
                "Forecast_Price": "3680.30",
                "Lower_Bound": "1787.70",
                "Upper_Bound": "5572.90",
            },
            "05/09/2020": {
                "Forecast_Price": "3649.01",
                "Lower_Bound": "1779.23",
                "Upper_Bound": "5518.79",
            },
            "12/09/2020": {
                "Forecast_Price": "3539.92",
                "Lower_Bound": "1744.56",
                "Upper_Bound": "5335.27",
            },
            "19/09/2020": {
                "Forecast_Price": "3365.03",
                "Lower_Bound": "1689.87",
                "Upper_Bound": "5040.19",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3645.43",
                "Lower_Bound": "1782.69",
                "Upper_Bound": "5508.16",
            },
            "30/09/2020": {
                "Forecast_Price": "3705.77",
                "Lower_Bound": "1782.62",
                "Upper_Bound": "5628.92",
            },
            "30/10/2020": {
                "Forecast_Price": "3727.91",
                "Lower_Bound": "1748.60",
                "Upper_Bound": "5707.21",
            },
            "29/11/2020": {
                "Forecast_Price": "3668.74",
                "Lower_Bound": "1680.99",
                "Upper_Bound": "5656.48",
            },
            "29/12/2020": {
                "Forecast_Price": "3629.48",
                "Lower_Bound": "1642.41",
                "Upper_Bound": "5616.56",
            },
            "28/01/2021": {
                "Forecast_Price": "3678.50",
                "Lower_Bound": "1673.77",
                "Upper_Bound": "5683.24",
            },
            "27/02/2021": {
                "Forecast_Price": "3493.56",
                "Lower_Bound": "1494.60",
                "Upper_Bound": "5492.52",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4384.13",
                "Lower_Bound": "3657.43",
                "Upper_Bound": "5110.84",
            },
            "02/08/2020": {
                "Forecast_Price": "4375.59",
                "Lower_Bound": "3585.90",
                "Upper_Bound": "5165.28",
            },
            "03/08/2020": {
                "Forecast_Price": "4359.29",
                "Lower_Bound": "3537.50",
                "Upper_Bound": "5181.07",
            },
            "04/08/2020": {
                "Forecast_Price": "4428.14",
                "Lower_Bound": "3590.22",
                "Upper_Bound": "5266.05",
            },
            "05/08/2020": {
                "Forecast_Price": "4384.44",
                "Lower_Bound": "3648.59",
                "Upper_Bound": "5120.29",
            },
            "06/08/2020": {
                "Forecast_Price": "4335.49",
                "Lower_Bound": "3677.02",
                "Upper_Bound": "4993.95",
            },
            "07/08/2020": {
                "Forecast_Price": "4409.80",
                "Lower_Bound": "3600.37",
                "Upper_Bound": "5219.23",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4657.07",
                "Lower_Bound": "2274.49",
                "Upper_Bound": "7039.65",
            },
            "15/08/2020": {
                "Forecast_Price": "4671.68",
                "Lower_Bound": "2281.66",
                "Upper_Bound": "7061.71",
            },
            "22/08/2020": {
                "Forecast_Price": "4686.28",
                "Lower_Bound": "2288.81",
                "Upper_Bound": "7083.75",
            },
            "29/08/2020": {
                "Forecast_Price": "4700.78",
                "Lower_Bound": "2295.78",
                "Upper_Bound": "7105.77",
            },
            "05/09/2020": {
                "Forecast_Price": "4715.42",
                "Lower_Bound": "2303.00",
                "Upper_Bound": "7127.83",
            },
            "12/09/2020": {
                "Forecast_Price": "4730.03",
                "Lower_Bound": "2310.17",
                "Upper_Bound": "7149.89",
            },
            "19/09/2020": {
                "Forecast_Price": "4744.63",
                "Lower_Bound": "2317.32",
                "Upper_Bound": "7171.94",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4616.91",
                "Lower_Bound": "2237.50",
                "Upper_Bound": "6996.31",
            },
            "30/09/2020": {
                "Forecast_Price": "4599.71",
                "Lower_Bound": "2221.66",
                "Upper_Bound": "6977.77",
            },
            "30/10/2020": {
                "Forecast_Price": "4616.49",
                "Lower_Bound": "2262.60",
                "Upper_Bound": "6970.38",
            },
            "29/11/2020": {
                "Forecast_Price": "4586.67",
                "Lower_Bound": "2225.65",
                "Upper_Bound": "6947.69",
            },
            "29/12/2020": {
                "Forecast_Price": "4564.12",
                "Lower_Bound": "2200.85",
                "Upper_Bound": "6927.39",
            },
            "28/01/2021": {
                "Forecast_Price": "4529.21",
                "Lower_Bound": "2166.41",
                "Upper_Bound": "6892.01",
            },
            "27/02/2021": {
                "Forecast_Price": "4134.77",
                "Lower_Bound": "1998.40",
                "Upper_Bound": "6271.14",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4372.18",
                "Lower_Bound": "3765.72",
                "Upper_Bound": "4978.65",
            },
            "02/08/2020": {
                "Forecast_Price": "4363.01",
                "Lower_Bound": "3448.03",
                "Upper_Bound": "5278.00",
            },
            "03/08/2020": {
                "Forecast_Price": "4315.07",
                "Lower_Bound": "3665.52",
                "Upper_Bound": "4964.62",
            },
            "04/08/2020": {
                "Forecast_Price": "4311.82",
                "Lower_Bound": "3571.30",
                "Upper_Bound": "5052.33",
            },
            "05/08/2020": {
                "Forecast_Price": "4261.68",
                "Lower_Bound": "3024.59",
                "Upper_Bound": "5498.77",
            },
            "06/08/2020": {
                "Forecast_Price": "4293.56",
                "Lower_Bound": "3616.36",
                "Upper_Bound": "4970.76",
            },
            "07/08/2020": {
                "Forecast_Price": "4278.25",
                "Lower_Bound": "3662.66",
                "Upper_Bound": "4893.84",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4523.55",
                "Lower_Bound": "2211.10",
                "Upper_Bound": "6835.99",
            },
            "15/08/2020": {
                "Forecast_Price": "4527.02",
                "Lower_Bound": "2211.13",
                "Upper_Bound": "6842.92",
            },
            "22/08/2020": {
                "Forecast_Price": "4528.85",
                "Lower_Bound": "2211.52",
                "Upper_Bound": "6846.18",
            },
            "29/08/2020": {
                "Forecast_Price": "4533.50",
                "Lower_Bound": "2216.42",
                "Upper_Bound": "6850.58",
            },
            "05/09/2020": {
                "Forecast_Price": "4538.18",
                "Lower_Bound": "2219.67",
                "Upper_Bound": "6856.68",
            },
            "12/09/2020": {
                "Forecast_Price": "4541.21",
                "Lower_Bound": "2219.55",
                "Upper_Bound": "6862.86",
            },
            "19/09/2020": {
                "Forecast_Price": "4542.85",
                "Lower_Bound": "2219.89",
                "Upper_Bound": "6865.80",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4583.13",
                "Lower_Bound": "2298.95",
                "Upper_Bound": "6867.32",
            },
            "30/09/2020": {
                "Forecast_Price": "4607.60",
                "Lower_Bound": "2316.92",
                "Upper_Bound": "6898.27",
            },
            "30/10/2020": {
                "Forecast_Price": "4636.52",
                "Lower_Bound": "2344.03",
                "Upper_Bound": "6929.02",
            },
            "29/11/2020": {
                "Forecast_Price": "4635.69",
                "Lower_Bound": "2326.78",
                "Upper_Bound": "6944.59",
            },
            "29/12/2020": {
                "Forecast_Price": "4625.77",
                "Lower_Bound": "2296.36",
                "Upper_Bound": "6955.18",
            },
            "28/01/2021": {
                "Forecast_Price": "4603.39",
                "Lower_Bound": "2244.78",
                "Upper_Bound": "6962.00",
            },
            "27/02/2021": {
                "Forecast_Price": "4557.00",
                "Lower_Bound": "2137.47",
                "Upper_Bound": "6976.53",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4184.48",
                "Lower_Bound": "3547.68",
                "Upper_Bound": "4821.29",
            },
            "02/08/2020": {
                "Forecast_Price": "4179.55",
                "Lower_Bound": "3424.93",
                "Upper_Bound": "4934.18",
            },
            "03/08/2020": {
                "Forecast_Price": "4181.23",
                "Lower_Bound": "3379.68",
                "Upper_Bound": "4982.79",
            },
            "04/08/2020": {
                "Forecast_Price": "4176.32",
                "Lower_Bound": "3410.33",
                "Upper_Bound": "4942.31",
            },
            "05/08/2020": {
                "Forecast_Price": "4179.14",
                "Lower_Bound": "3349.93",
                "Upper_Bound": "5008.34",
            },
            "06/08/2020": {
                "Forecast_Price": "4186.20",
                "Lower_Bound": "3393.47",
                "Upper_Bound": "4978.93",
            },
            "07/08/2020": {
                "Forecast_Price": "4193.81",
                "Lower_Bound": "3460.30",
                "Upper_Bound": "4927.32",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4105.02",
                "Lower_Bound": "2028.01",
                "Upper_Bound": "6182.02",
            },
            "15/08/2020": {
                "Forecast_Price": "4155.23",
                "Lower_Bound": "2083.18",
                "Upper_Bound": "6227.29",
            },
            "22/08/2020": {
                "Forecast_Price": "4190.77",
                "Lower_Bound": "2111.66",
                "Upper_Bound": "6269.88",
            },
            "29/08/2020": {
                "Forecast_Price": "4195.92",
                "Lower_Bound": "2123.83",
                "Upper_Bound": "6268.02",
            },
            "05/09/2020": {
                "Forecast_Price": "4222.07",
                "Lower_Bound": "2161.67",
                "Upper_Bound": "6282.47",
            },
            "12/09/2020": {
                "Forecast_Price": "4260.89",
                "Lower_Bound": "2213.10",
                "Upper_Bound": "6308.69",
            },
            "19/09/2020": {
                "Forecast_Price": "4285.30",
                "Lower_Bound": "2237.92",
                "Upper_Bound": "6332.68",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3795.31",
                "Lower_Bound": "1870.61",
                "Upper_Bound": "5720.00",
            },
            "30/09/2020": {
                "Forecast_Price": "3831.45",
                "Lower_Bound": "1863.10",
                "Upper_Bound": "5799.79",
            },
            "30/10/2020": {
                "Forecast_Price": "3873.73",
                "Lower_Bound": "1873.05",
                "Upper_Bound": "5874.41",
            },
            "29/11/2020": {
                "Forecast_Price": "3892.09",
                "Lower_Bound": "1849.43",
                "Upper_Bound": "5934.74",
            },
            "29/12/2020": {
                "Forecast_Price": "3903.18",
                "Lower_Bound": "1819.42",
                "Upper_Bound": "5986.95",
            },
            "28/01/2021": {
                "Forecast_Price": "3915.14",
                "Lower_Bound": "1796.45",
                "Upper_Bound": "6033.84",
            },
            "27/02/2021": {
                "Forecast_Price": "3883.18",
                "Lower_Bound": "1701.49",
                "Upper_Bound": "6064.86",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5086.87",
                "Lower_Bound": "4011.99",
                "Upper_Bound": "6161.75",
            },
            "02/08/2020": {
                "Forecast_Price": "5147.79",
                "Lower_Bound": "3941.72",
                "Upper_Bound": "6353.86",
            },
            "03/08/2020": {
                "Forecast_Price": "5140.02",
                "Lower_Bound": "4311.26",
                "Upper_Bound": "5968.78",
            },
            "04/08/2020": {
                "Forecast_Price": "5142.76",
                "Lower_Bound": "4425.27",
                "Upper_Bound": "5860.25",
            },
            "05/08/2020": {
                "Forecast_Price": "5186.69",
                "Lower_Bound": "4435.00",
                "Upper_Bound": "5938.38",
            },
            "06/08/2020": {
                "Forecast_Price": "5167.32",
                "Lower_Bound": "4347.84",
                "Upper_Bound": "5986.80",
            },
            "07/08/2020": {
                "Forecast_Price": "5093.28",
                "Lower_Bound": "4407.03",
                "Upper_Bound": "5779.53",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4621.87",
                "Lower_Bound": "2254.52",
                "Upper_Bound": "6989.23",
            },
            "15/08/2020": {
                "Forecast_Price": "4621.14",
                "Lower_Bound": "2251.13",
                "Upper_Bound": "6991.14",
            },
            "22/08/2020": {
                "Forecast_Price": "4614.79",
                "Lower_Bound": "2245.80",
                "Upper_Bound": "6983.78",
            },
            "29/08/2020": {
                "Forecast_Price": "4609.56",
                "Lower_Bound": "2240.98",
                "Upper_Bound": "6978.14",
            },
            "05/09/2020": {
                "Forecast_Price": "4609.39",
                "Lower_Bound": "2237.84",
                "Upper_Bound": "6980.93",
            },
            "12/09/2020": {
                "Forecast_Price": "4608.89",
                "Lower_Bound": "2234.53",
                "Upper_Bound": "6983.24",
            },
            "19/09/2020": {
                "Forecast_Price": "4603.00",
                "Lower_Bound": "2229.35",
                "Upper_Bound": "6976.64",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4645.70",
                "Lower_Bound": "2248.62",
                "Upper_Bound": "7042.77",
            },
            "30/09/2020": {
                "Forecast_Price": "4559.46",
                "Lower_Bound": "2195.79",
                "Upper_Bound": "6923.13",
            },
            "30/10/2020": {
                "Forecast_Price": "4599.59",
                "Lower_Bound": "2201.50",
                "Upper_Bound": "6997.69",
            },
            "29/11/2020": {
                "Forecast_Price": "4551.62",
                "Lower_Bound": "2172.94",
                "Upper_Bound": "6930.31",
            },
            "29/12/2020": {
                "Forecast_Price": "4592.78",
                "Lower_Bound": "2170.46",
                "Upper_Bound": "7015.10",
            },
            "28/01/2021": {
                "Forecast_Price": "4567.31",
                "Lower_Bound": "2162.78",
                "Upper_Bound": "6971.85",
            },
            "27/02/2021": {
                "Forecast_Price": "4656.21",
                "Lower_Bound": "2128.79",
                "Upper_Bound": "7183.62",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5296.44",
                "Lower_Bound": "4444.39",
                "Upper_Bound": "6148.48",
            },
            "02/08/2020": {
                "Forecast_Price": "5293.26",
                "Lower_Bound": "4116.33",
                "Upper_Bound": "6470.18",
            },
            "03/08/2020": {
                "Forecast_Price": "5291.13",
                "Lower_Bound": "4439.81",
                "Upper_Bound": "6142.45",
            },
            "04/08/2020": {
                "Forecast_Price": "5290.42",
                "Lower_Bound": "4389.29",
                "Upper_Bound": "6191.56",
            },
            "05/08/2020": {
                "Forecast_Price": "5285.95",
                "Lower_Bound": "4538.44",
                "Upper_Bound": "6033.46",
            },
            "06/08/2020": {
                "Forecast_Price": "5280.89",
                "Lower_Bound": "4432.49",
                "Upper_Bound": "6129.29",
            },
            "07/08/2020": {
                "Forecast_Price": "5282.97",
                "Lower_Bound": "4477.63",
                "Upper_Bound": "6088.30",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5278.91",
                "Lower_Bound": "2578.21",
                "Upper_Bound": "7979.61",
            },
            "15/08/2020": {
                "Forecast_Price": "5277.10",
                "Lower_Bound": "2576.42",
                "Upper_Bound": "7977.79",
            },
            "22/08/2020": {
                "Forecast_Price": "5275.40",
                "Lower_Bound": "2574.80",
                "Upper_Bound": "7975.99",
            },
            "29/08/2020": {
                "Forecast_Price": "5275.02",
                "Lower_Bound": "2575.40",
                "Upper_Bound": "7974.64",
            },
            "05/09/2020": {
                "Forecast_Price": "5273.51",
                "Lower_Bound": "2574.06",
                "Upper_Bound": "7972.96",
            },
            "12/09/2020": {
                "Forecast_Price": "5271.75",
                "Lower_Bound": "2572.29",
                "Upper_Bound": "7971.21",
            },
            "19/09/2020": {
                "Forecast_Price": "5270.08",
                "Lower_Bound": "2570.68",
                "Upper_Bound": "7969.48",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5282.51",
                "Lower_Bound": "2599.56",
                "Upper_Bound": "7965.45",
            },
            "30/09/2020": {
                "Forecast_Price": "5291.32",
                "Lower_Bound": "2624.08",
                "Upper_Bound": "7958.56",
            },
            "30/10/2020": {
                "Forecast_Price": "5340.48",
                "Lower_Bound": "2674.14",
                "Upper_Bound": "8006.81",
            },
            "29/11/2020": {
                "Forecast_Price": "5399.88",
                "Lower_Bound": "2707.89",
                "Upper_Bound": "8091.87",
            },
            "29/12/2020": {
                "Forecast_Price": "5438.71",
                "Lower_Bound": "2729.57",
                "Upper_Bound": "8147.85",
            },
            "28/01/2021": {
                "Forecast_Price": "5430.30",
                "Lower_Bound": "2719.24",
                "Upper_Bound": "8141.35",
            },
            "27/02/2021": {
                "Forecast_Price": "5375.89",
                "Lower_Bound": "2678.87",
                "Upper_Bound": "8072.91",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5038.31",
                "Lower_Bound": "4107.55",
                "Upper_Bound": "5969.07",
            },
            "02/08/2020": {
                "Forecast_Price": "5025.58",
                "Lower_Bound": "4230.17",
                "Upper_Bound": "5820.99",
            },
            "03/08/2020": {
                "Forecast_Price": "5020.70",
                "Lower_Bound": "4324.16",
                "Upper_Bound": "5717.25",
            },
            "04/08/2020": {
                "Forecast_Price": "5010.23",
                "Lower_Bound": "3872.05",
                "Upper_Bound": "6148.40",
            },
            "05/08/2020": {
                "Forecast_Price": "5032.34",
                "Lower_Bound": "4251.19",
                "Upper_Bound": "5813.48",
            },
            "06/08/2020": {
                "Forecast_Price": "5008.09",
                "Lower_Bound": "4090.91",
                "Upper_Bound": "5925.27",
            },
            "07/08/2020": {
                "Forecast_Price": "5015.88",
                "Lower_Bound": "3934.04",
                "Upper_Bound": "6097.72",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4938.34",
                "Lower_Bound": "2412.60",
                "Upper_Bound": "7464.07",
            },
            "15/08/2020": {
                "Forecast_Price": "4935.89",
                "Lower_Bound": "2412.14",
                "Upper_Bound": "7459.64",
            },
            "22/08/2020": {
                "Forecast_Price": "4933.44",
                "Lower_Bound": "2411.67",
                "Upper_Bound": "7455.21",
            },
            "29/08/2020": {
                "Forecast_Price": "4931.00",
                "Lower_Bound": "2411.21",
                "Upper_Bound": "7450.79",
            },
            "05/09/2020": {
                "Forecast_Price": "4928.60",
                "Lower_Bound": "2410.76",
                "Upper_Bound": "7446.45",
            },
            "12/09/2020": {
                "Forecast_Price": "4926.21",
                "Lower_Bound": "2410.31",
                "Upper_Bound": "7442.11",
            },
            "19/09/2020": {
                "Forecast_Price": "4923.83",
                "Lower_Bound": "2409.86",
                "Upper_Bound": "7437.79",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4946.16",
                "Lower_Bound": "2432.28",
                "Upper_Bound": "7460.04",
            },
            "30/09/2020": {
                "Forecast_Price": "5022.75",
                "Lower_Bound": "2469.77",
                "Upper_Bound": "7575.72",
            },
            "30/10/2020": {
                "Forecast_Price": "5047.63",
                "Lower_Bound": "2486.47",
                "Upper_Bound": "7608.80",
            },
            "29/11/2020": {
                "Forecast_Price": "5098.77",
                "Lower_Bound": "2512.76",
                "Upper_Bound": "7684.79",
            },
            "29/12/2020": {
                "Forecast_Price": "5240.49",
                "Lower_Bound": "2576.96",
                "Upper_Bound": "7904.03",
            },
            "28/01/2021": {
                "Forecast_Price": "5290.23",
                "Lower_Bound": "2634.58",
                "Upper_Bound": "7945.87",
            },
            "27/02/2021": {
                "Forecast_Price": "5223.87",
                "Lower_Bound": "2602.86",
                "Upper_Bound": "7844.88",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4424.77",
                "Lower_Bound": "3652.40",
                "Upper_Bound": "5197.14",
            },
            "02/08/2020": {
                "Forecast_Price": "4411.62",
                "Lower_Bound": "3517.10",
                "Upper_Bound": "5306.15",
            },
            "03/08/2020": {
                "Forecast_Price": "4419.26",
                "Lower_Bound": "3561.43",
                "Upper_Bound": "5277.08",
            },
            "04/08/2020": {
                "Forecast_Price": "4444.98",
                "Lower_Bound": "3431.27",
                "Upper_Bound": "5458.68",
            },
            "05/08/2020": {
                "Forecast_Price": "4534.98",
                "Lower_Bound": "2776.01",
                "Upper_Bound": "6293.94",
            },
            "06/08/2020": {
                "Forecast_Price": "4480.01",
                "Lower_Bound": "3816.48",
                "Upper_Bound": "5143.53",
            },
            "07/08/2020": {
                "Forecast_Price": "4482.97",
                "Lower_Bound": "3794.38",
                "Upper_Bound": "5171.55",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4814.50",
                "Lower_Bound": "2350.76",
                "Upper_Bound": "7278.24",
            },
            "15/08/2020": {
                "Forecast_Price": "4820.64",
                "Lower_Bound": "2354.63",
                "Upper_Bound": "7286.65",
            },
            "22/08/2020": {
                "Forecast_Price": "4831.40",
                "Lower_Bound": "2358.99",
                "Upper_Bound": "7303.81",
            },
            "29/08/2020": {
                "Forecast_Price": "4848.56",
                "Lower_Bound": "2364.35",
                "Upper_Bound": "7332.77",
            },
            "05/09/2020": {
                "Forecast_Price": "4840.05",
                "Lower_Bound": "2360.99",
                "Upper_Bound": "7319.12",
            },
            "12/09/2020": {
                "Forecast_Price": "4846.25",
                "Lower_Bound": "2364.96",
                "Upper_Bound": "7327.55",
            },
            "19/09/2020": {
                "Forecast_Price": "4856.99",
                "Lower_Bound": "2369.28",
                "Upper_Bound": "7344.70",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4822.84",
                "Lower_Bound": "2363.17",
                "Upper_Bound": "7282.51",
            },
            "30/09/2020": {
                "Forecast_Price": "4827.05",
                "Lower_Bound": "2362.17",
                "Upper_Bound": "7291.92",
            },
            "30/10/2020": {
                "Forecast_Price": "4796.28",
                "Lower_Bound": "2339.22",
                "Upper_Bound": "7253.34",
            },
            "29/11/2020": {
                "Forecast_Price": "4826.80",
                "Lower_Bound": "2339.79",
                "Upper_Bound": "7313.81",
            },
            "29/12/2020": {
                "Forecast_Price": "4771.84",
                "Lower_Bound": "2320.56",
                "Upper_Bound": "7223.12",
            },
            "28/01/2021": {
                "Forecast_Price": "4791.29",
                "Lower_Bound": "2346.24",
                "Upper_Bound": "7236.35",
            },
            "27/02/2021": {
                "Forecast_Price": "4689.28",
                "Lower_Bound": "2293.76",
                "Upper_Bound": "7084.80",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4544.04",
                "Lower_Bound": "3975.92",
                "Upper_Bound": "5112.15",
            },
            "02/08/2020": {
                "Forecast_Price": "4578.43",
                "Lower_Bound": "4032.32",
                "Upper_Bound": "5124.54",
            },
            "03/08/2020": {
                "Forecast_Price": "4503.21",
                "Lower_Bound": "3960.23",
                "Upper_Bound": "5046.18",
            },
            "04/08/2020": {
                "Forecast_Price": "4593.99",
                "Lower_Bound": "3923.76",
                "Upper_Bound": "5264.23",
            },
            "05/08/2020": {
                "Forecast_Price": "4540.31",
                "Lower_Bound": "4013.48",
                "Upper_Bound": "5067.15",
            },
            "06/08/2020": {
                "Forecast_Price": "4528.56",
                "Lower_Bound": "3852.45",
                "Upper_Bound": "5204.67",
            },
            "07/08/2020": {
                "Forecast_Price": "4578.97",
                "Lower_Bound": "3988.32",
                "Upper_Bound": "5169.61",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5010.37",
                "Lower_Bound": "2457.24",
                "Upper_Bound": "7563.49",
            },
            "15/08/2020": {
                "Forecast_Price": "5047.34",
                "Lower_Bound": "2482.58",
                "Upper_Bound": "7612.11",
            },
            "22/08/2020": {
                "Forecast_Price": "4780.94",
                "Lower_Bound": "2381.99",
                "Upper_Bound": "7179.90",
            },
            "29/08/2020": {
                "Forecast_Price": "4833.62",
                "Lower_Bound": "2410.21",
                "Upper_Bound": "7257.03",
            },
            "05/09/2020": {
                "Forecast_Price": "4893.77",
                "Lower_Bound": "2450.48",
                "Upper_Bound": "7337.05",
            },
            "12/09/2020": {
                "Forecast_Price": "4942.61",
                "Lower_Bound": "2479.72",
                "Upper_Bound": "7405.51",
            },
            "19/09/2020": {
                "Forecast_Price": "4881.88",
                "Lower_Bound": "2446.64",
                "Upper_Bound": "7317.13",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4939.23",
                "Lower_Bound": "2405.79",
                "Upper_Bound": "7472.67",
            },
            "30/09/2020": {
                "Forecast_Price": "4926.79",
                "Lower_Bound": "2391.19",
                "Upper_Bound": "7462.39",
            },
            "30/10/2020": {
                "Forecast_Price": "4905.19",
                "Lower_Bound": "2361.24",
                "Upper_Bound": "7449.14",
            },
            "29/11/2020": {
                "Forecast_Price": "4890.34",
                "Lower_Bound": "2342.54",
                "Upper_Bound": "7438.14",
            },
            "29/12/2020": {
                "Forecast_Price": "4880.94",
                "Lower_Bound": "2332.91",
                "Upper_Bound": "7428.97",
            },
            "28/01/2021": {
                "Forecast_Price": "4878.80",
                "Lower_Bound": "2334.79",
                "Upper_Bound": "7422.81",
            },
            "27/02/2021": {
                "Forecast_Price": "4860.85",
                "Lower_Bound": "2312.37",
                "Upper_Bound": "7409.33",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5704.92",
                "Lower_Bound": "4248.35",
                "Upper_Bound": "7161.48",
            },
            "02/08/2020": {
                "Forecast_Price": "5647.24",
                "Lower_Bound": "4680.40",
                "Upper_Bound": "6614.08",
            },
            "03/08/2020": {
                "Forecast_Price": "5662.21",
                "Lower_Bound": "4704.53",
                "Upper_Bound": "6619.89",
            },
            "04/08/2020": {
                "Forecast_Price": "5651.33",
                "Lower_Bound": "4659.71",
                "Upper_Bound": "6642.95",
            },
            "05/08/2020": {
                "Forecast_Price": "5605.48",
                "Lower_Bound": "4853.85",
                "Upper_Bound": "6357.11",
            },
            "06/08/2020": {
                "Forecast_Price": "5644.04",
                "Lower_Bound": "4879.20",
                "Upper_Bound": "6408.87",
            },
            "07/08/2020": {
                "Forecast_Price": "5620.26",
                "Lower_Bound": "4716.36",
                "Upper_Bound": "6524.16",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5454.50",
                "Lower_Bound": "2663.96",
                "Upper_Bound": "8245.03",
            },
            "15/08/2020": {
                "Forecast_Price": "5471.78",
                "Lower_Bound": "2670.08",
                "Upper_Bound": "8273.47",
            },
            "22/08/2020": {
                "Forecast_Price": "5476.87",
                "Lower_Bound": "2672.19",
                "Upper_Bound": "8281.56",
            },
            "29/08/2020": {
                "Forecast_Price": "5470.97",
                "Lower_Bound": "2670.76",
                "Upper_Bound": "8271.18",
            },
            "05/09/2020": {
                "Forecast_Price": "5473.52",
                "Lower_Bound": "2671.92",
                "Upper_Bound": "8275.11",
            },
            "12/09/2020": {
                "Forecast_Price": "5490.79",
                "Lower_Bound": "2678.03",
                "Upper_Bound": "8303.56",
            },
            "19/09/2020": {
                "Forecast_Price": "5495.89",
                "Lower_Bound": "2680.15",
                "Upper_Bound": "8311.64",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5486.09",
                "Lower_Bound": "2673.13",
                "Upper_Bound": "8299.05",
            },
            "30/09/2020": {
                "Forecast_Price": "5731.94",
                "Lower_Bound": "2754.98",
                "Upper_Bound": "8708.90",
            },
            "30/10/2020": {
                "Forecast_Price": "5849.69",
                "Lower_Bound": "2808.67",
                "Upper_Bound": "8890.71",
            },
            "29/11/2020": {
                "Forecast_Price": "5923.82",
                "Lower_Bound": "2852.03",
                "Upper_Bound": "8995.62",
            },
            "29/12/2020": {
                "Forecast_Price": "6022.37",
                "Lower_Bound": "2896.83",
                "Upper_Bound": "9147.91",
            },
            "28/01/2021": {
                "Forecast_Price": "6007.41",
                "Lower_Bound": "2912.04",
                "Upper_Bound": "9102.78",
            },
            "27/02/2021": {
                "Forecast_Price": "5870.73",
                "Lower_Bound": "2848.86",
                "Upper_Bound": "8892.60",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3928.60",
                "Lower_Bound": "3340.52",
                "Upper_Bound": "4516.68",
            },
            "02/08/2020": {
                "Forecast_Price": "3912.69",
                "Lower_Bound": "3290.85",
                "Upper_Bound": "4534.54",
            },
            "03/08/2020": {
                "Forecast_Price": "3897.93",
                "Lower_Bound": "3296.85",
                "Upper_Bound": "4499.01",
            },
            "04/08/2020": {
                "Forecast_Price": "3889.84",
                "Lower_Bound": "3133.66",
                "Upper_Bound": "4646.02",
            },
            "05/08/2020": {
                "Forecast_Price": "3915.24",
                "Lower_Bound": "3091.19",
                "Upper_Bound": "4739.28",
            },
            "06/08/2020": {
                "Forecast_Price": "3874.43",
                "Lower_Bound": "3142.99",
                "Upper_Bound": "4605.87",
            },
            "07/08/2020": {
                "Forecast_Price": "3878.64",
                "Lower_Bound": "3367.98",
                "Upper_Bound": "4389.29",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3954.05",
                "Lower_Bound": "1942.72",
                "Upper_Bound": "5965.38",
            },
            "15/08/2020": {
                "Forecast_Price": "3940.26",
                "Lower_Bound": "1926.68",
                "Upper_Bound": "5953.84",
            },
            "22/08/2020": {
                "Forecast_Price": "3934.54",
                "Lower_Bound": "1910.54",
                "Upper_Bound": "5958.54",
            },
            "29/08/2020": {
                "Forecast_Price": "3977.73",
                "Lower_Bound": "1959.11",
                "Upper_Bound": "5996.35",
            },
            "05/09/2020": {
                "Forecast_Price": "3968.95",
                "Lower_Bound": "1941.50",
                "Upper_Bound": "5996.40",
            },
            "12/09/2020": {
                "Forecast_Price": "3959.13",
                "Lower_Bound": "1926.77",
                "Upper_Bound": "5991.49",
            },
            "19/09/2020": {
                "Forecast_Price": "3947.06",
                "Lower_Bound": "1908.54",
                "Upper_Bound": "5985.57",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3973.92",
                "Lower_Bound": "1846.58",
                "Upper_Bound": "6101.27",
            },
            "30/09/2020": {
                "Forecast_Price": "3925.23",
                "Lower_Bound": "1769.80",
                "Upper_Bound": "6080.66",
            },
            "30/10/2020": {
                "Forecast_Price": "3882.02",
                "Lower_Bound": "1702.19",
                "Upper_Bound": "6061.86",
            },
            "29/11/2020": {
                "Forecast_Price": "3834.37",
                "Lower_Bound": "1627.14",
                "Upper_Bound": "6041.59",
            },
            "29/12/2020": {
                "Forecast_Price": "3795.10",
                "Lower_Bound": "1566.12",
                "Upper_Bound": "6024.08",
            },
            "28/01/2021": {
                "Forecast_Price": "3673.06",
                "Lower_Bound": "1470.09",
                "Upper_Bound": "5876.04",
            },
            "27/02/2021": {
                "Forecast_Price": "3065.87",
                "Lower_Bound": "1197.74",
                "Upper_Bound": "4934.01",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4241.75",
                "Lower_Bound": "3601.80",
                "Upper_Bound": "4881.71",
            },
            "02/08/2020": {
                "Forecast_Price": "4242.71",
                "Lower_Bound": "3617.86",
                "Upper_Bound": "4867.55",
            },
            "03/08/2020": {
                "Forecast_Price": "4227.06",
                "Lower_Bound": "3577.05",
                "Upper_Bound": "4877.07",
            },
            "04/08/2020": {
                "Forecast_Price": "4234.59",
                "Lower_Bound": "3528.51",
                "Upper_Bound": "4940.68",
            },
            "05/08/2020": {
                "Forecast_Price": "4208.80",
                "Lower_Bound": "3333.34",
                "Upper_Bound": "5084.26",
            },
            "06/08/2020": {
                "Forecast_Price": "4207.62",
                "Lower_Bound": "3452.66",
                "Upper_Bound": "4962.58",
            },
            "07/08/2020": {
                "Forecast_Price": "4202.54",
                "Lower_Bound": "3317.50",
                "Upper_Bound": "5087.58",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3971.13",
                "Lower_Bound": "1952.12",
                "Upper_Bound": "5990.13",
            },
            "15/08/2020": {
                "Forecast_Price": "3984.97",
                "Lower_Bound": "1962.49",
                "Upper_Bound": "6007.44",
            },
            "22/08/2020": {
                "Forecast_Price": "3969.58",
                "Lower_Bound": "1952.39",
                "Upper_Bound": "5986.77",
            },
            "29/08/2020": {
                "Forecast_Price": "3984.03",
                "Lower_Bound": "1967.43",
                "Upper_Bound": "6000.63",
            },
            "05/09/2020": {
                "Forecast_Price": "4000.99",
                "Lower_Bound": "1985.93",
                "Upper_Bound": "6016.05",
            },
            "12/09/2020": {
                "Forecast_Price": "4014.67",
                "Lower_Bound": "1996.24",
                "Upper_Bound": "6033.10",
            },
            "19/09/2020": {
                "Forecast_Price": "3998.63",
                "Lower_Bound": "1985.93",
                "Upper_Bound": "6011.33",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4094.83",
                "Lower_Bound": "1974.98",
                "Upper_Bound": "6214.69",
            },
            "30/09/2020": {
                "Forecast_Price": "4075.11",
                "Lower_Bound": "1922.50",
                "Upper_Bound": "6227.73",
            },
            "30/10/2020": {
                "Forecast_Price": "4083.04",
                "Lower_Bound": "1923.84",
                "Upper_Bound": "6242.24",
            },
            "29/11/2020": {
                "Forecast_Price": "4159.57",
                "Lower_Bound": "1948.20",
                "Upper_Bound": "6370.93",
            },
            "29/12/2020": {
                "Forecast_Price": "4337.79",
                "Lower_Bound": "2020.44",
                "Upper_Bound": "6655.13",
            },
            "28/01/2021": {
                "Forecast_Price": "4386.32",
                "Lower_Bound": "2038.38",
                "Upper_Bound": "6734.25",
            },
            "27/02/2021": {
                "Forecast_Price": "4247.98",
                "Lower_Bound": "1935.49",
                "Upper_Bound": "6560.47",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4998.68",
                "Lower_Bound": "4195.60",
                "Upper_Bound": "5801.75",
            },
            "02/08/2020": {
                "Forecast_Price": "4999.70",
                "Lower_Bound": "4212.98",
                "Upper_Bound": "5786.42",
            },
            "03/08/2020": {
                "Forecast_Price": "4984.29",
                "Lower_Bound": "4225.93",
                "Upper_Bound": "5742.64",
            },
            "04/08/2020": {
                "Forecast_Price": "4966.24",
                "Lower_Bound": "4280.58",
                "Upper_Bound": "5651.89",
            },
            "05/08/2020": {
                "Forecast_Price": "4991.94",
                "Lower_Bound": "4350.19",
                "Upper_Bound": "5633.68",
            },
            "06/08/2020": {
                "Forecast_Price": "4958.93",
                "Lower_Bound": "4100.60",
                "Upper_Bound": "5817.25",
            },
            "07/08/2020": {
                "Forecast_Price": "4946.35",
                "Lower_Bound": "4220.87",
                "Upper_Bound": "5671.82",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5077.64",
                "Lower_Bound": "2481.86",
                "Upper_Bound": "7673.42",
            },
            "15/08/2020": {
                "Forecast_Price": "5077.78",
                "Lower_Bound": "2481.98",
                "Upper_Bound": "7673.58",
            },
            "22/08/2020": {
                "Forecast_Price": "5074.05",
                "Lower_Bound": "2480.89",
                "Upper_Bound": "7667.22",
            },
            "29/08/2020": {
                "Forecast_Price": "5067.67",
                "Lower_Bound": "2480.29",
                "Upper_Bound": "7655.05",
            },
            "05/09/2020": {
                "Forecast_Price": "5063.06",
                "Lower_Bound": "2479.70",
                "Upper_Bound": "7646.42",
            },
            "12/09/2020": {
                "Forecast_Price": "5063.05",
                "Lower_Bound": "2479.77",
                "Upper_Bound": "7646.34",
            },
            "19/09/2020": {
                "Forecast_Price": "5058.68",
                "Lower_Bound": "2478.47",
                "Upper_Bound": "7638.90",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5081.21",
                "Lower_Bound": "2481.97",
                "Upper_Bound": "7680.45",
            },
            "30/09/2020": {
                "Forecast_Price": "5112.23",
                "Lower_Bound": "2502.70",
                "Upper_Bound": "7721.77",
            },
            "30/10/2020": {
                "Forecast_Price": "5107.12",
                "Lower_Bound": "2509.47",
                "Upper_Bound": "7704.77",
            },
            "29/11/2020": {
                "Forecast_Price": "5074.32",
                "Lower_Bound": "2498.76",
                "Upper_Bound": "7649.89",
            },
            "29/12/2020": {
                "Forecast_Price": "5124.90",
                "Lower_Bound": "2528.37",
                "Upper_Bound": "7721.42",
            },
            "28/01/2021": {
                "Forecast_Price": "5082.58",
                "Lower_Bound": "2520.43",
                "Upper_Bound": "7644.72",
            },
            "27/02/2021": {
                "Forecast_Price": "5107.91",
                "Lower_Bound": "2534.21",
                "Upper_Bound": "7681.61",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5251.84",
                "Lower_Bound": "4233.52",
                "Upper_Bound": "6270.17",
            },
            "02/08/2020": {
                "Forecast_Price": "5276.67",
                "Lower_Bound": "4267.71",
                "Upper_Bound": "6285.64",
            },
            "03/08/2020": {
                "Forecast_Price": "5224.67",
                "Lower_Bound": "4523.71",
                "Upper_Bound": "5925.62",
            },
            "04/08/2020": {
                "Forecast_Price": "5205.04",
                "Lower_Bound": "3894.54",
                "Upper_Bound": "6515.55",
            },
            "05/08/2020": {
                "Forecast_Price": "5257.04",
                "Lower_Bound": "4396.01",
                "Upper_Bound": "6118.08",
            },
            "06/08/2020": {
                "Forecast_Price": "5222.06",
                "Lower_Bound": "4334.61",
                "Upper_Bound": "6109.50",
            },
            "07/08/2020": {
                "Forecast_Price": "5292.41",
                "Lower_Bound": "4368.94",
                "Upper_Bound": "6215.88",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4017.20",
                "Lower_Bound": "2033.66",
                "Upper_Bound": "6000.74",
            },
            "15/08/2020": {
                "Forecast_Price": "3911.40",
                "Lower_Bound": "1908.65",
                "Upper_Bound": "5914.16",
            },
            "22/08/2020": {
                "Forecast_Price": "3818.61",
                "Lower_Bound": "1741.86",
                "Upper_Bound": "5895.36",
            },
            "29/08/2020": {
                "Forecast_Price": "3873.97",
                "Lower_Bound": "1798.77",
                "Upper_Bound": "5949.16",
            },
            "05/09/2020": {
                "Forecast_Price": "3949.03",
                "Lower_Bound": "1898.33",
                "Upper_Bound": "5999.72",
            },
            "12/09/2020": {
                "Forecast_Price": "3843.48",
                "Lower_Bound": "1773.40",
                "Upper_Bound": "5913.56",
            },
            "19/09/2020": {
                "Forecast_Price": "3749.95",
                "Lower_Bound": "1606.37",
                "Upper_Bound": "5893.52",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4227.11",
                "Lower_Bound": "2104.97",
                "Upper_Bound": "6349.25",
            },
            "30/09/2020": {
                "Forecast_Price": "4333.19",
                "Lower_Bound": "2201.05",
                "Upper_Bound": "6465.34",
            },
            "30/10/2020": {
                "Forecast_Price": "4264.98",
                "Lower_Bound": "2199.21",
                "Upper_Bound": "6330.75",
            },
            "29/11/2020": {
                "Forecast_Price": "4348.30",
                "Lower_Bound": "2224.59",
                "Upper_Bound": "6472.01",
            },
            "29/12/2020": {
                "Forecast_Price": "4477.30",
                "Lower_Bound": "2275.98",
                "Upper_Bound": "6678.61",
            },
            "28/01/2021": {
                "Forecast_Price": "4433.94",
                "Lower_Bound": "2266.05",
                "Upper_Bound": "6601.84",
            },
            "27/02/2021": {
                "Forecast_Price": "4303.18",
                "Lower_Bound": "2149.74",
                "Upper_Bound": "6456.62",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5948.15",
                "Lower_Bound": "5225.54",
                "Upper_Bound": "6670.75",
            },
            "02/08/2020": {
                "Forecast_Price": "5524.79",
                "Lower_Bound": "4819.81",
                "Upper_Bound": "6229.77",
            },
            "03/08/2020": {
                "Forecast_Price": "5454.67",
                "Lower_Bound": "4760.01",
                "Upper_Bound": "6149.33",
            },
            "04/08/2020": {
                "Forecast_Price": "5331.44",
                "Lower_Bound": "4566.41",
                "Upper_Bound": "6096.48",
            },
            "05/08/2020": {
                "Forecast_Price": "5337.77",
                "Lower_Bound": "4443.66",
                "Upper_Bound": "6231.89",
            },
            "06/08/2020": {
                "Forecast_Price": "5153.04",
                "Lower_Bound": "4265.86",
                "Upper_Bound": "6040.23",
            },
            "07/08/2020": {
                "Forecast_Price": "4890.85",
                "Lower_Bound": "4203.31",
                "Upper_Bound": "5578.39",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3553.69",
                "Lower_Bound": "1741.55",
                "Upper_Bound": "5365.82",
            },
            "15/08/2020": {
                "Forecast_Price": "3606.13",
                "Lower_Bound": "1777.85",
                "Upper_Bound": "5434.42",
            },
            "22/08/2020": {
                "Forecast_Price": "3524.58",
                "Lower_Bound": "1735.47",
                "Upper_Bound": "5313.70",
            },
            "29/08/2020": {
                "Forecast_Price": "3511.74",
                "Lower_Bound": "1728.49",
                "Upper_Bound": "5294.99",
            },
            "05/09/2020": {
                "Forecast_Price": "3539.46",
                "Lower_Bound": "1743.62",
                "Upper_Bound": "5335.30",
            },
            "12/09/2020": {
                "Forecast_Price": "3591.55",
                "Lower_Bound": "1779.80",
                "Upper_Bound": "5403.31",
            },
            "19/09/2020": {
                "Forecast_Price": "3510.47",
                "Lower_Bound": "1737.57",
                "Upper_Bound": "5283.37",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3681.41",
                "Lower_Bound": "1793.13",
                "Upper_Bound": "5569.70",
            },
            "30/09/2020": {
                "Forecast_Price": "3928.82",
                "Lower_Bound": "1950.27",
                "Upper_Bound": "5907.36",
            },
            "30/10/2020": {
                "Forecast_Price": "4149.29",
                "Lower_Bound": "2096.22",
                "Upper_Bound": "6202.36",
            },
            "29/11/2020": {
                "Forecast_Price": "4252.08",
                "Lower_Bound": "2142.09",
                "Upper_Bound": "6362.06",
            },
            "29/12/2020": {
                "Forecast_Price": "4361.06",
                "Lower_Bound": "2187.52",
                "Upper_Bound": "6534.61",
            },
            "28/01/2021": {
                "Forecast_Price": "4337.18",
                "Lower_Bound": "2155.04",
                "Upper_Bound": "6519.32",
            },
            "27/02/2021": {
                "Forecast_Price": "4071.60",
                "Lower_Bound": "1976.94",
                "Upper_Bound": "6166.26",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4350.62",
                "Lower_Bound": "3665.71",
                "Upper_Bound": "5035.54",
            },
            "02/08/2020": {
                "Forecast_Price": "4353.63",
                "Lower_Bound": "3688.17",
                "Upper_Bound": "5019.09",
            },
            "03/08/2020": {
                "Forecast_Price": "4347.76",
                "Lower_Bound": "3833.63",
                "Upper_Bound": "4861.89",
            },
            "04/08/2020": {
                "Forecast_Price": "4352.35",
                "Lower_Bound": "3747.97",
                "Upper_Bound": "4956.73",
            },
            "05/08/2020": {
                "Forecast_Price": "4361.43",
                "Lower_Bound": "3868.78",
                "Upper_Bound": "4854.08",
            },
            "06/08/2020": {
                "Forecast_Price": "4347.76",
                "Lower_Bound": "3819.35",
                "Upper_Bound": "4876.16",
            },
            "07/08/2020": {
                "Forecast_Price": "4340.21",
                "Lower_Bound": "3830.73",
                "Upper_Bound": "4849.69",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4404.95",
                "Lower_Bound": "2152.03",
                "Upper_Bound": "6657.87",
            },
            "15/08/2020": {
                "Forecast_Price": "4404.02",
                "Lower_Bound": "2151.25",
                "Upper_Bound": "6656.79",
            },
            "22/08/2020": {
                "Forecast_Price": "4405.72",
                "Lower_Bound": "2154.99",
                "Upper_Bound": "6656.45",
            },
            "29/08/2020": {
                "Forecast_Price": "4405.41",
                "Lower_Bound": "2155.23",
                "Upper_Bound": "6655.59",
            },
            "05/09/2020": {
                "Forecast_Price": "4405.56",
                "Lower_Bound": "2156.22",
                "Upper_Bound": "6654.91",
            },
            "12/09/2020": {
                "Forecast_Price": "4404.71",
                "Lower_Bound": "2155.58",
                "Upper_Bound": "6653.85",
            },
            "19/09/2020": {
                "Forecast_Price": "4406.53",
                "Lower_Bound": "2159.52",
                "Upper_Bound": "6653.55",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4286.60",
                "Lower_Bound": "2109.93",
                "Upper_Bound": "6463.27",
            },
            "30/09/2020": {
                "Forecast_Price": "4285.04",
                "Lower_Bound": "2105.03",
                "Upper_Bound": "6465.05",
            },
            "30/10/2020": {
                "Forecast_Price": "4559.75",
                "Lower_Bound": "2203.04",
                "Upper_Bound": "6916.45",
            },
            "29/11/2020": {
                "Forecast_Price": "4842.23",
                "Lower_Bound": "2302.19",
                "Upper_Bound": "7382.27",
            },
            "29/12/2020": {
                "Forecast_Price": "5088.06",
                "Lower_Bound": "2390.47",
                "Upper_Bound": "7785.66",
            },
            "28/01/2021": {
                "Forecast_Price": "5119.65",
                "Lower_Bound": "2397.55",
                "Upper_Bound": "7841.74",
            },
            "27/02/2021": {
                "Forecast_Price": "5018.66",
                "Lower_Bound": "2355.05",
                "Upper_Bound": "7682.27",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5055.55",
                "Lower_Bound": "4053.39",
                "Upper_Bound": "6057.71",
            },
            "02/08/2020": {
                "Forecast_Price": "5052.63",
                "Lower_Bound": "4143.55",
                "Upper_Bound": "5961.71",
            },
            "03/08/2020": {
                "Forecast_Price": "5049.07",
                "Lower_Bound": "4234.50",
                "Upper_Bound": "5863.64",
            },
            "04/08/2020": {
                "Forecast_Price": "5050.04",
                "Lower_Bound": "3627.39",
                "Upper_Bound": "6472.69",
            },
            "05/08/2020": {
                "Forecast_Price": "5047.12",
                "Lower_Bound": "4320.35",
                "Upper_Bound": "5773.88",
            },
            "06/08/2020": {
                "Forecast_Price": "5047.00",
                "Lower_Bound": "4289.01",
                "Upper_Bound": "5804.99",
            },
            "07/08/2020": {
                "Forecast_Price": "5048.46",
                "Lower_Bound": "4198.07",
                "Upper_Bound": "5898.85",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4916.35",
                "Lower_Bound": "2403.62",
                "Upper_Bound": "7429.07",
            },
            "15/08/2020": {
                "Forecast_Price": "4928.27",
                "Lower_Bound": "2410.99",
                "Upper_Bound": "7445.55",
            },
            "22/08/2020": {
                "Forecast_Price": "4958.51",
                "Lower_Bound": "2425.61",
                "Upper_Bound": "7491.40",
            },
            "29/08/2020": {
                "Forecast_Price": "4989.12",
                "Lower_Bound": "2440.87",
                "Upper_Bound": "7537.38",
            },
            "05/09/2020": {
                "Forecast_Price": "5013.81",
                "Lower_Bound": "2453.37",
                "Upper_Bound": "7574.25",
            },
            "12/09/2020": {
                "Forecast_Price": "5037.79",
                "Lower_Bound": "2464.70",
                "Upper_Bound": "7610.88",
            },
            "19/09/2020": {
                "Forecast_Price": "5068.03",
                "Lower_Bound": "2479.32",
                "Upper_Bound": "7656.74",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4943.75",
                "Lower_Bound": "2382.54",
                "Upper_Bound": "7504.96",
            },
            "30/09/2020": {
                "Forecast_Price": "4971.09",
                "Lower_Bound": "2393.47",
                "Upper_Bound": "7548.71",
            },
            "30/10/2020": {
                "Forecast_Price": "4959.33",
                "Lower_Bound": "2393.10",
                "Upper_Bound": "7525.56",
            },
            "29/11/2020": {
                "Forecast_Price": "4981.55",
                "Lower_Bound": "2410.98",
                "Upper_Bound": "7552.12",
            },
            "29/12/2020": {
                "Forecast_Price": "5045.55",
                "Lower_Bound": "2451.42",
                "Upper_Bound": "7639.67",
            },
            "28/01/2021": {
                "Forecast_Price": "5151.42",
                "Lower_Bound": "2524.28",
                "Upper_Bound": "7778.57",
            },
            "27/02/2021": {
                "Forecast_Price": "5094.70",
                "Lower_Bound": "2510.58",
                "Upper_Bound": "7678.82",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4115.47",
                "Lower_Bound": "3476.21",
                "Upper_Bound": "4754.74",
            },
            "02/08/2020": {
                "Forecast_Price": "4122.95",
                "Lower_Bound": "3501.74",
                "Upper_Bound": "4744.16",
            },
            "03/08/2020": {
                "Forecast_Price": "4127.89",
                "Lower_Bound": "3136.41",
                "Upper_Bound": "5119.37",
            },
            "04/08/2020": {
                "Forecast_Price": "4101.10",
                "Lower_Bound": "3448.37",
                "Upper_Bound": "4753.82",
            },
            "05/08/2020": {
                "Forecast_Price": "4113.28",
                "Lower_Bound": "3413.66",
                "Upper_Bound": "4812.91",
            },
            "06/08/2020": {
                "Forecast_Price": "4130.68",
                "Lower_Bound": "2976.55",
                "Upper_Bound": "5284.81",
            },
            "07/08/2020": {
                "Forecast_Price": "4118.32",
                "Lower_Bound": "3443.21",
                "Upper_Bound": "4793.43",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3980.30",
                "Lower_Bound": "1956.51",
                "Upper_Bound": "6004.08",
            },
            "15/08/2020": {
                "Forecast_Price": "4080.23",
                "Lower_Bound": "2016.20",
                "Upper_Bound": "6144.26",
            },
            "22/08/2020": {
                "Forecast_Price": "3827.70",
                "Lower_Bound": "1889.53",
                "Upper_Bound": "5765.86",
            },
            "29/08/2020": {
                "Forecast_Price": "3718.16",
                "Lower_Bound": "1839.90",
                "Upper_Bound": "5596.41",
            },
            "05/09/2020": {
                "Forecast_Price": "3870.96",
                "Lower_Bound": "1923.90",
                "Upper_Bound": "5818.02",
            },
            "12/09/2020": {
                "Forecast_Price": "3978.40",
                "Lower_Bound": "1996.15",
                "Upper_Bound": "5960.66",
            },
            "19/09/2020": {
                "Forecast_Price": "3717.81",
                "Lower_Bound": "1856.01",
                "Upper_Bound": "5579.61",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3548.62",
                "Lower_Bound": "1721.26",
                "Upper_Bound": "5375.99",
            },
            "30/09/2020": {
                "Forecast_Price": "3881.96",
                "Lower_Bound": "1840.51",
                "Upper_Bound": "5923.40",
            },
            "30/10/2020": {
                "Forecast_Price": "4184.00",
                "Lower_Bound": "1963.59",
                "Upper_Bound": "6404.40",
            },
            "29/11/2020": {
                "Forecast_Price": "4106.65",
                "Lower_Bound": "1933.43",
                "Upper_Bound": "6279.86",
            },
            "29/12/2020": {
                "Forecast_Price": "4053.23",
                "Lower_Bound": "1913.67",
                "Upper_Bound": "6192.79",
            },
            "28/01/2021": {
                "Forecast_Price": "4015.19",
                "Lower_Bound": "1892.66",
                "Upper_Bound": "6137.72",
            },
            "27/02/2021": {
                "Forecast_Price": "3831.99",
                "Lower_Bound": "1786.84",
                "Upper_Bound": "5877.14",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5386.41",
                "Lower_Bound": "4561.26",
                "Upper_Bound": "6211.55",
            },
            "02/08/2020": {
                "Forecast_Price": "5375.81",
                "Lower_Bound": "4596.71",
                "Upper_Bound": "6154.91",
            },
            "03/08/2020": {
                "Forecast_Price": "5381.64",
                "Lower_Bound": "4701.75",
                "Upper_Bound": "6061.54",
            },
            "04/08/2020": {
                "Forecast_Price": "5384.30",
                "Lower_Bound": "4560.94",
                "Upper_Bound": "6207.67",
            },
            "05/08/2020": {
                "Forecast_Price": "5388.02",
                "Lower_Bound": "4779.85",
                "Upper_Bound": "5996.18",
            },
            "06/08/2020": {
                "Forecast_Price": "5390.92",
                "Lower_Bound": "4753.78",
                "Upper_Bound": "6028.07",
            },
            "07/08/2020": {
                "Forecast_Price": "5384.07",
                "Lower_Bound": "4732.60",
                "Upper_Bound": "6035.54",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5393.52",
                "Lower_Bound": "2633.49",
                "Upper_Bound": "8153.55",
            },
            "15/08/2020": {
                "Forecast_Price": "5400.09",
                "Lower_Bound": "2645.47",
                "Upper_Bound": "8154.71",
            },
            "22/08/2020": {
                "Forecast_Price": "5403.65",
                "Lower_Bound": "2652.42",
                "Upper_Bound": "8154.88",
            },
            "29/08/2020": {
                "Forecast_Price": "5396.26",
                "Lower_Bound": "2641.07",
                "Upper_Bound": "8151.46",
            },
            "05/09/2020": {
                "Forecast_Price": "5398.36",
                "Lower_Bound": "2645.55",
                "Upper_Bound": "8151.17",
            },
            "12/09/2020": {
                "Forecast_Price": "5404.94",
                "Lower_Bound": "2657.53",
                "Upper_Bound": "8152.34",
            },
            "19/09/2020": {
                "Forecast_Price": "5408.51",
                "Lower_Bound": "2664.48",
                "Upper_Bound": "8152.53",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5398.70",
                "Lower_Bound": "2638.78",
                "Upper_Bound": "8158.63",
            },
            "30/09/2020": {
                "Forecast_Price": "5556.00",
                "Lower_Bound": "2705.68",
                "Upper_Bound": "8406.32",
            },
            "30/10/2020": {
                "Forecast_Price": "6048.49",
                "Lower_Bound": "2901.13",
                "Upper_Bound": "9195.85",
            },
            "29/11/2020": {
                "Forecast_Price": "5989.95",
                "Lower_Bound": "2871.96",
                "Upper_Bound": "9107.94",
            },
            "29/12/2020": {
                "Forecast_Price": "5933.76",
                "Lower_Bound": "2846.72",
                "Upper_Bound": "9020.81",
            },
            "28/01/2021": {
                "Forecast_Price": "6038.09",
                "Lower_Bound": "2887.13",
                "Upper_Bound": "9189.06",
            },
            "27/02/2021": {
                "Forecast_Price": "6025.65",
                "Lower_Bound": "2877.98",
                "Upper_Bound": "9173.31",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4689.41",
                "Lower_Bound": "3995.81",
                "Upper_Bound": "5383.00",
            },
            "02/08/2020": {
                "Forecast_Price": "4712.65",
                "Lower_Bound": "4109.59",
                "Upper_Bound": "5315.71",
            },
            "03/08/2020": {
                "Forecast_Price": "4721.80",
                "Lower_Bound": "4051.52",
                "Upper_Bound": "5392.09",
            },
            "04/08/2020": {
                "Forecast_Price": "4706.32",
                "Lower_Bound": "4000.77",
                "Upper_Bound": "5411.88",
            },
            "05/08/2020": {
                "Forecast_Price": "4746.76",
                "Lower_Bound": "4028.31",
                "Upper_Bound": "5465.22",
            },
            "06/08/2020": {
                "Forecast_Price": "4690.94",
                "Lower_Bound": "4071.74",
                "Upper_Bound": "5310.14",
            },
            "07/08/2020": {
                "Forecast_Price": "4713.99",
                "Lower_Bound": "3800.12",
                "Upper_Bound": "5627.86",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4509.18",
                "Lower_Bound": "2198.00",
                "Upper_Bound": "6820.37",
            },
            "15/08/2020": {
                "Forecast_Price": "4506.97",
                "Lower_Bound": "2197.27",
                "Upper_Bound": "6816.66",
            },
            "22/08/2020": {
                "Forecast_Price": "4509.68",
                "Lower_Bound": "2196.32",
                "Upper_Bound": "6823.05",
            },
            "29/08/2020": {
                "Forecast_Price": "4511.50",
                "Lower_Bound": "2196.05",
                "Upper_Bound": "6826.95",
            },
            "05/09/2020": {
                "Forecast_Price": "4516.10",
                "Lower_Bound": "2192.91",
                "Upper_Bound": "6839.30",
            },
            "12/09/2020": {
                "Forecast_Price": "4516.30",
                "Lower_Bound": "2192.97",
                "Upper_Bound": "6839.62",
            },
            "19/09/2020": {
                "Forecast_Price": "4519.01",
                "Lower_Bound": "2192.02",
                "Upper_Bound": "6846.00",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4388.45",
                "Lower_Bound": "2092.38",
                "Upper_Bound": "6684.52",
            },
            "30/09/2020": {
                "Forecast_Price": "4228.72",
                "Lower_Bound": "1974.82",
                "Upper_Bound": "6482.63",
            },
            "30/10/2020": {
                "Forecast_Price": "4164.33",
                "Lower_Bound": "1896.37",
                "Upper_Bound": "6432.28",
            },
            "29/11/2020": {
                "Forecast_Price": "4248.26",
                "Lower_Bound": "1899.34",
                "Upper_Bound": "6597.19",
            },
            "29/12/2020": {
                "Forecast_Price": "4370.15",
                "Lower_Bound": "1933.61",
                "Upper_Bound": "6806.68",
            },
            "28/01/2021": {
                "Forecast_Price": "4429.83",
                "Lower_Bound": "1960.24",
                "Upper_Bound": "6899.41",
            },
            "27/02/2021": {
                "Forecast_Price": "4338.57",
                "Lower_Bound": "1901.87",
                "Upper_Bound": "6775.27",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5960.85",
                "Lower_Bound": "5294.63",
                "Upper_Bound": "6627.07",
            },
            "02/08/2020": {
                "Forecast_Price": "5944.13",
                "Lower_Bound": "5195.90",
                "Upper_Bound": "6692.36",
            },
            "03/08/2020": {
                "Forecast_Price": "5928.60",
                "Lower_Bound": "5337.19",
                "Upper_Bound": "6520.01",
            },
            "04/08/2020": {
                "Forecast_Price": "5923.57",
                "Lower_Bound": "5120.50",
                "Upper_Bound": "6726.65",
            },
            "05/08/2020": {
                "Forecast_Price": "5904.45",
                "Lower_Bound": "5168.08",
                "Upper_Bound": "6640.83",
            },
            "06/08/2020": {
                "Forecast_Price": "5903.05",
                "Lower_Bound": "5138.19",
                "Upper_Bound": "6667.91",
            },
            "07/08/2020": {
                "Forecast_Price": "5929.78",
                "Lower_Bound": "5215.12",
                "Upper_Bound": "6644.45",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5721.77",
                "Lower_Bound": "2793.47",
                "Upper_Bound": "8650.07",
            },
            "15/08/2020": {
                "Forecast_Price": "5717.92",
                "Lower_Bound": "2791.95",
                "Upper_Bound": "8643.88",
            },
            "22/08/2020": {
                "Forecast_Price": "5718.62",
                "Lower_Bound": "2789.17",
                "Upper_Bound": "8648.06",
            },
            "29/08/2020": {
                "Forecast_Price": "5713.21",
                "Lower_Bound": "2787.11",
                "Upper_Bound": "8639.32",
            },
            "05/09/2020": {
                "Forecast_Price": "5723.63",
                "Lower_Bound": "2791.09",
                "Upper_Bound": "8656.17",
            },
            "12/09/2020": {
                "Forecast_Price": "5720.85",
                "Lower_Bound": "2789.92",
                "Upper_Bound": "8651.78",
            },
            "19/09/2020": {
                "Forecast_Price": "5722.70",
                "Lower_Bound": "2787.52",
                "Upper_Bound": "8657.87",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5815.20",
                "Lower_Bound": "2848.35",
                "Upper_Bound": "8782.05",
            },
            "30/09/2020": {
                "Forecast_Price": "5929.24",
                "Lower_Bound": "2908.51",
                "Upper_Bound": "8949.96",
            },
            "30/10/2020": {
                "Forecast_Price": "6044.71",
                "Lower_Bound": "2972.83",
                "Upper_Bound": "9116.59",
            },
            "29/11/2020": {
                "Forecast_Price": "6374.78",
                "Lower_Bound": "3150.33",
                "Upper_Bound": "9599.22",
            },
            "29/12/2020": {
                "Forecast_Price": "6394.12",
                "Lower_Bound": "3161.58",
                "Upper_Bound": "9626.66",
            },
            "28/01/2021": {
                "Forecast_Price": "6181.26",
                "Lower_Bound": "3090.72",
                "Upper_Bound": "9271.80",
            },
            "27/02/2021": {
                "Forecast_Price": "6001.31",
                "Lower_Bound": "3017.39",
                "Upper_Bound": "8985.22",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4298.70",
                "Lower_Bound": "3628.22",
                "Upper_Bound": "4969.18",
            },
            "02/08/2020": {
                "Forecast_Price": "4296.57",
                "Lower_Bound": "3718.12",
                "Upper_Bound": "4875.02",
            },
            "03/08/2020": {
                "Forecast_Price": "4297.86",
                "Lower_Bound": "3668.56",
                "Upper_Bound": "4927.16",
            },
            "04/08/2020": {
                "Forecast_Price": "4300.96",
                "Lower_Bound": "3313.91",
                "Upper_Bound": "5288.02",
            },
            "05/08/2020": {
                "Forecast_Price": "4292.30",
                "Lower_Bound": "3556.29",
                "Upper_Bound": "5028.31",
            },
            "06/08/2020": {
                "Forecast_Price": "4274.34",
                "Lower_Bound": "3450.89",
                "Upper_Bound": "5097.79",
            },
            "07/08/2020": {
                "Forecast_Price": "4267.82",
                "Lower_Bound": "3467.04",
                "Upper_Bound": "5068.60",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4156.79",
                "Lower_Bound": "2035.02",
                "Upper_Bound": "6278.55",
            },
            "15/08/2020": {
                "Forecast_Price": "4142.29",
                "Lower_Bound": "2019.42",
                "Upper_Bound": "6265.16",
            },
            "22/08/2020": {
                "Forecast_Price": "4140.58",
                "Lower_Bound": "2025.18",
                "Upper_Bound": "6255.99",
            },
            "29/08/2020": {
                "Forecast_Price": "4134.85",
                "Lower_Bound": "2024.18",
                "Upper_Bound": "6245.51",
            },
            "05/09/2020": {
                "Forecast_Price": "4130.87",
                "Lower_Bound": "2022.66",
                "Upper_Bound": "6239.08",
            },
            "12/09/2020": {
                "Forecast_Price": "4119.00",
                "Lower_Bound": "2007.92",
                "Upper_Bound": "6230.08",
            },
            "19/09/2020": {
                "Forecast_Price": "4119.92",
                "Lower_Bound": "2014.54",
                "Upper_Bound": "6225.30",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4160.45",
                "Lower_Bound": "2017.07",
                "Upper_Bound": "6303.84",
            },
            "30/09/2020": {
                "Forecast_Price": "4179.66",
                "Lower_Bound": "2043.59",
                "Upper_Bound": "6315.73",
            },
            "30/10/2020": {
                "Forecast_Price": "4200.50",
                "Lower_Bound": "2075.81",
                "Upper_Bound": "6325.19",
            },
            "29/11/2020": {
                "Forecast_Price": "4199.18",
                "Lower_Bound": "2085.82",
                "Upper_Bound": "6312.53",
            },
            "29/12/2020": {
                "Forecast_Price": "4178.40",
                "Lower_Bound": "2084.32",
                "Upper_Bound": "6272.47",
            },
            "28/01/2021": {
                "Forecast_Price": "4159.22",
                "Lower_Bound": "2083.70",
                "Upper_Bound": "6234.74",
            },
            "27/02/2021": {
                "Forecast_Price": "4116.15",
                "Lower_Bound": "2065.97",
                "Upper_Bound": "6166.33",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4849.44",
                "Lower_Bound": "3850.82",
                "Upper_Bound": "5848.06",
            },
            "02/08/2020": {
                "Forecast_Price": "4847.36",
                "Lower_Bound": "3496.06",
                "Upper_Bound": "6198.67",
            },
            "03/08/2020": {
                "Forecast_Price": "4851.77",
                "Lower_Bound": "3882.61",
                "Upper_Bound": "5820.92",
            },
            "04/08/2020": {
                "Forecast_Price": "4844.54",
                "Lower_Bound": "4102.13",
                "Upper_Bound": "5586.94",
            },
            "05/08/2020": {
                "Forecast_Price": "4852.82",
                "Lower_Bound": "3969.29",
                "Upper_Bound": "5736.34",
            },
            "06/08/2020": {
                "Forecast_Price": "4857.26",
                "Lower_Bound": "4019.60",
                "Upper_Bound": "5694.91",
            },
            "07/08/2020": {
                "Forecast_Price": "4868.34",
                "Lower_Bound": "4011.57",
                "Upper_Bound": "5725.10",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4109.98",
                "Lower_Bound": "2013.28",
                "Upper_Bound": "6206.69",
            },
            "15/08/2020": {
                "Forecast_Price": "4119.45",
                "Lower_Bound": "2019.54",
                "Upper_Bound": "6219.37",
            },
            "22/08/2020": {
                "Forecast_Price": "4121.97",
                "Lower_Bound": "2017.44",
                "Upper_Bound": "6226.50",
            },
            "29/08/2020": {
                "Forecast_Price": "4120.11",
                "Lower_Bound": "2012.13",
                "Upper_Bound": "6228.09",
            },
            "05/09/2020": {
                "Forecast_Price": "4121.45",
                "Lower_Bound": "2019.45",
                "Upper_Bound": "6223.45",
            },
            "12/09/2020": {
                "Forecast_Price": "4130.92",
                "Lower_Bound": "2025.71",
                "Upper_Bound": "6236.13",
            },
            "19/09/2020": {
                "Forecast_Price": "4133.43",
                "Lower_Bound": "2023.61",
                "Upper_Bound": "6243.26",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4087.54",
                "Lower_Bound": "1973.98",
                "Upper_Bound": "6201.11",
            },
            "30/09/2020": {
                "Forecast_Price": "4095.68",
                "Lower_Bound": "1985.89",
                "Upper_Bound": "6205.47",
            },
            "30/10/2020": {
                "Forecast_Price": "4098.38",
                "Lower_Bound": "1993.97",
                "Upper_Bound": "6202.78",
            },
            "29/11/2020": {
                "Forecast_Price": "4096.38",
                "Lower_Bound": "1987.00",
                "Upper_Bound": "6205.75",
            },
            "29/12/2020": {
                "Forecast_Price": "4086.84",
                "Lower_Bound": "1967.34",
                "Upper_Bound": "6206.35",
            },
            "28/01/2021": {
                "Forecast_Price": "4074.76",
                "Lower_Bound": "1948.38",
                "Upper_Bound": "6201.15",
            },
            "27/02/2021": {
                "Forecast_Price": "4057.35",
                "Lower_Bound": "1924.80",
                "Upper_Bound": "6189.90",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3558.63",
                "Lower_Bound": "2888.60",
                "Upper_Bound": "4228.66",
            },
            "02/08/2020": {
                "Forecast_Price": "3562.98",
                "Lower_Bound": "2966.09",
                "Upper_Bound": "4159.87",
            },
            "03/08/2020": {
                "Forecast_Price": "3588.41",
                "Lower_Bound": "3075.66",
                "Upper_Bound": "4101.16",
            },
            "04/08/2020": {
                "Forecast_Price": "3598.61",
                "Lower_Bound": "2804.54",
                "Upper_Bound": "4392.69",
            },
            "05/08/2020": {
                "Forecast_Price": "3669.78",
                "Lower_Bound": "2953.38",
                "Upper_Bound": "4386.18",
            },
            "06/08/2020": {
                "Forecast_Price": "3595.62",
                "Lower_Bound": "3038.40",
                "Upper_Bound": "4152.83",
            },
            "07/08/2020": {
                "Forecast_Price": "3702.83",
                "Lower_Bound": "3155.93",
                "Upper_Bound": "4249.74",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3838.03",
                "Lower_Bound": "1874.60",
                "Upper_Bound": "5801.45",
            },
            "15/08/2020": {
                "Forecast_Price": "3889.77",
                "Lower_Bound": "1899.89",
                "Upper_Bound": "5879.65",
            },
            "22/08/2020": {
                "Forecast_Price": "3941.45",
                "Lower_Bound": "1925.07",
                "Upper_Bound": "5957.83",
            },
            "29/08/2020": {
                "Forecast_Price": "3993.08",
                "Lower_Bound": "1950.18",
                "Upper_Bound": "6035.99",
            },
            "05/09/2020": {
                "Forecast_Price": "4045.02",
                "Lower_Bound": "1975.78",
                "Upper_Bound": "6114.25",
            },
            "12/09/2020": {
                "Forecast_Price": "4096.76",
                "Lower_Bound": "2001.07",
                "Upper_Bound": "6192.45",
            },
            "19/09/2020": {
                "Forecast_Price": "4148.44",
                "Lower_Bound": "2026.25",
                "Upper_Bound": "6270.62",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3736.48",
                "Lower_Bound": "1733.87",
                "Upper_Bound": "5739.09",
            },
            "30/09/2020": {
                "Forecast_Price": "3651.33",
                "Lower_Bound": "1676.67",
                "Upper_Bound": "5625.99",
            },
            "30/10/2020": {
                "Forecast_Price": "3602.63",
                "Lower_Bound": "1650.15",
                "Upper_Bound": "5555.11",
            },
            "29/11/2020": {
                "Forecast_Price": "3584.62",
                "Lower_Bound": "1646.66",
                "Upper_Bound": "5522.57",
            },
            "29/12/2020": {
                "Forecast_Price": "3520.01",
                "Lower_Bound": "1634.71",
                "Upper_Bound": "5405.30",
            },
            "28/01/2021": {
                "Forecast_Price": "3403.39",
                "Lower_Bound": "1600.89",
                "Upper_Bound": "5205.90",
            },
            "27/02/2021": {
                "Forecast_Price": "3362.67",
                "Lower_Bound": "1597.60",
                "Upper_Bound": "5127.73",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4341.23",
                "Lower_Bound": "3572.33",
                "Upper_Bound": "5110.13",
            },
            "02/08/2020": {
                "Forecast_Price": "4333.95",
                "Lower_Bound": "3672.26",
                "Upper_Bound": "4995.64",
            },
            "03/08/2020": {
                "Forecast_Price": "4318.54",
                "Lower_Bound": "3359.48",
                "Upper_Bound": "5277.59",
            },
            "04/08/2020": {
                "Forecast_Price": "4348.98",
                "Lower_Bound": "3578.59",
                "Upper_Bound": "5119.37",
            },
            "05/08/2020": {
                "Forecast_Price": "4338.69",
                "Lower_Bound": "3642.03",
                "Upper_Bound": "5035.36",
            },
            "06/08/2020": {
                "Forecast_Price": "4331.96",
                "Lower_Bound": "3682.35",
                "Upper_Bound": "4981.57",
            },
            "07/08/2020": {
                "Forecast_Price": "4445.45",
                "Lower_Bound": "3622.56",
                "Upper_Bound": "5268.35",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4539.63",
                "Lower_Bound": "2218.12",
                "Upper_Bound": "6861.14",
            },
            "15/08/2020": {
                "Forecast_Price": "4554.95",
                "Lower_Bound": "2224.18",
                "Upper_Bound": "6885.72",
            },
            "22/08/2020": {
                "Forecast_Price": "4542.17",
                "Lower_Bound": "2221.11",
                "Upper_Bound": "6863.24",
            },
            "29/08/2020": {
                "Forecast_Price": "4528.69",
                "Lower_Bound": "2217.51",
                "Upper_Bound": "6839.86",
            },
            "05/09/2020": {
                "Forecast_Price": "4520.94",
                "Lower_Bound": "2214.53",
                "Upper_Bound": "6827.36",
            },
            "12/09/2020": {
                "Forecast_Price": "4536.18",
                "Lower_Bound": "2220.56",
                "Upper_Bound": "6851.79",
            },
            "19/09/2020": {
                "Forecast_Price": "4523.74",
                "Lower_Bound": "2217.61",
                "Upper_Bound": "6829.87",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4461.94",
                "Lower_Bound": "2121.17",
                "Upper_Bound": "6802.72",
            },
            "30/09/2020": {
                "Forecast_Price": "4331.29",
                "Lower_Bound": "1975.55",
                "Upper_Bound": "6687.04",
            },
            "30/10/2020": {
                "Forecast_Price": "4314.56",
                "Lower_Bound": "1922.87",
                "Upper_Bound": "6706.25",
            },
            "29/11/2020": {
                "Forecast_Price": "4222.80",
                "Lower_Bound": "1809.45",
                "Upper_Bound": "6636.14",
            },
            "29/12/2020": {
                "Forecast_Price": "4152.16",
                "Lower_Bound": "1722.93",
                "Upper_Bound": "6581.38",
            },
            "28/01/2021": {
                "Forecast_Price": "4078.07",
                "Lower_Bound": "1640.91",
                "Upper_Bound": "6515.22",
            },
            "27/02/2021": {
                "Forecast_Price": "3964.69",
                "Lower_Bound": "1535.78",
                "Upper_Bound": "6393.60",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5346.81",
                "Lower_Bound": "3971.39",
                "Upper_Bound": "6722.24",
            },
            "02/08/2020": {
                "Forecast_Price": "5314.34",
                "Lower_Bound": "4475.12",
                "Upper_Bound": "6153.57",
            },
            "03/08/2020": {
                "Forecast_Price": "5310.87",
                "Lower_Bound": "4569.41",
                "Upper_Bound": "6052.33",
            },
            "04/08/2020": {
                "Forecast_Price": "5327.88",
                "Lower_Bound": "4489.33",
                "Upper_Bound": "6166.44",
            },
            "05/08/2020": {
                "Forecast_Price": "5321.97",
                "Lower_Bound": "4624.12",
                "Upper_Bound": "6019.82",
            },
            "06/08/2020": {
                "Forecast_Price": "5290.24",
                "Lower_Bound": "4421.15",
                "Upper_Bound": "6159.34",
            },
            "07/08/2020": {
                "Forecast_Price": "5267.41",
                "Lower_Bound": "4407.92",
                "Upper_Bound": "6126.90",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5351.12",
                "Lower_Bound": "2613.48",
                "Upper_Bound": "8088.75",
            },
            "15/08/2020": {
                "Forecast_Price": "5352.23",
                "Lower_Bound": "2614.03",
                "Upper_Bound": "8090.43",
            },
            "22/08/2020": {
                "Forecast_Price": "5353.34",
                "Lower_Bound": "2614.57",
                "Upper_Bound": "8092.11",
            },
            "29/08/2020": {
                "Forecast_Price": "5354.45",
                "Lower_Bound": "2615.11",
                "Upper_Bound": "8093.79",
            },
            "05/09/2020": {
                "Forecast_Price": "5355.57",
                "Lower_Bound": "2615.67",
                "Upper_Bound": "8095.47",
            },
            "12/09/2020": {
                "Forecast_Price": "5356.69",
                "Lower_Bound": "2616.22",
                "Upper_Bound": "8097.15",
            },
            "19/09/2020": {
                "Forecast_Price": "5357.80",
                "Lower_Bound": "2616.77",
                "Upper_Bound": "8098.83",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5388.84",
                "Lower_Bound": "2677.14",
                "Upper_Bound": "8100.53",
            },
            "30/09/2020": {
                "Forecast_Price": "5416.60",
                "Lower_Bound": "2719.96",
                "Upper_Bound": "8113.24",
            },
            "30/10/2020": {
                "Forecast_Price": "5449.93",
                "Lower_Bound": "2763.81",
                "Upper_Bound": "8136.05",
            },
            "29/11/2020": {
                "Forecast_Price": "5404.56",
                "Lower_Bound": "2764.25",
                "Upper_Bound": "8044.87",
            },
            "29/12/2020": {
                "Forecast_Price": "5366.85",
                "Lower_Bound": "2773.78",
                "Upper_Bound": "7959.92",
            },
            "28/01/2021": {
                "Forecast_Price": "5350.97",
                "Lower_Bound": "2796.65",
                "Upper_Bound": "7905.28",
            },
            "27/02/2021": {
                "Forecast_Price": "5234.77",
                "Lower_Bound": "2750.33",
                "Upper_Bound": "7719.20",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4493.85",
                "Lower_Bound": "3912.53",
                "Upper_Bound": "5075.17",
            },
            "02/08/2020": {
                "Forecast_Price": "4511.01",
                "Lower_Bound": "3881.42",
                "Upper_Bound": "5140.60",
            },
            "03/08/2020": {
                "Forecast_Price": "4515.16",
                "Lower_Bound": "3919.18",
                "Upper_Bound": "5111.15",
            },
            "04/08/2020": {
                "Forecast_Price": "4499.93",
                "Lower_Bound": "3922.89",
                "Upper_Bound": "5076.97",
            },
            "05/08/2020": {
                "Forecast_Price": "4502.69",
                "Lower_Bound": "3258.29",
                "Upper_Bound": "5747.08",
            },
            "06/08/2020": {
                "Forecast_Price": "4482.09",
                "Lower_Bound": "3757.92",
                "Upper_Bound": "5206.25",
            },
            "07/08/2020": {
                "Forecast_Price": "4463.11",
                "Lower_Bound": "3729.44",
                "Upper_Bound": "5196.77",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4593.58",
                "Lower_Bound": "2243.51",
                "Upper_Bound": "6943.65",
            },
            "15/08/2020": {
                "Forecast_Price": "4597.64",
                "Lower_Bound": "2245.48",
                "Upper_Bound": "6949.80",
            },
            "22/08/2020": {
                "Forecast_Price": "4601.71",
                "Lower_Bound": "2247.47",
                "Upper_Bound": "6955.95",
            },
            "29/08/2020": {
                "Forecast_Price": "4605.78",
                "Lower_Bound": "2249.46",
                "Upper_Bound": "6962.10",
            },
            "05/09/2020": {
                "Forecast_Price": "4609.85",
                "Lower_Bound": "2251.46",
                "Upper_Bound": "6968.25",
            },
            "12/09/2020": {
                "Forecast_Price": "4613.91",
                "Lower_Bound": "2253.43",
                "Upper_Bound": "6974.40",
            },
            "19/09/2020": {
                "Forecast_Price": "4617.99",
                "Lower_Bound": "2255.42",
                "Upper_Bound": "6980.55",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4612.42",
                "Lower_Bound": "2212.02",
                "Upper_Bound": "7012.82",
            },
            "30/09/2020": {
                "Forecast_Price": "4692.21",
                "Lower_Bound": "2220.14",
                "Upper_Bound": "7164.27",
            },
            "30/10/2020": {
                "Forecast_Price": "4668.97",
                "Lower_Bound": "2189.90",
                "Upper_Bound": "7148.04",
            },
            "29/11/2020": {
                "Forecast_Price": "4624.49",
                "Lower_Bound": "2120.66",
                "Upper_Bound": "7128.32",
            },
            "29/12/2020": {
                "Forecast_Price": "4759.44",
                "Lower_Bound": "2167.55",
                "Upper_Bound": "7351.32",
            },
            "28/01/2021": {
                "Forecast_Price": "4775.46",
                "Lower_Bound": "2170.50",
                "Upper_Bound": "7380.42",
            },
            "27/02/2021": {
                "Forecast_Price": "4627.59",
                "Lower_Bound": "2082.50",
                "Upper_Bound": "7172.69",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4800.29",
                "Lower_Bound": "4138.62",
                "Upper_Bound": "5461.96",
            },
            "02/08/2020": {
                "Forecast_Price": "4796.37",
                "Lower_Bound": "4158.07",
                "Upper_Bound": "5434.68",
            },
            "03/08/2020": {
                "Forecast_Price": "4802.80",
                "Lower_Bound": "4004.73",
                "Upper_Bound": "5600.86",
            },
            "04/08/2020": {
                "Forecast_Price": "4787.93",
                "Lower_Bound": "3916.16",
                "Upper_Bound": "5659.70",
            },
            "05/08/2020": {
                "Forecast_Price": "4773.51",
                "Lower_Bound": "4044.88",
                "Upper_Bound": "5502.15",
            },
            "06/08/2020": {
                "Forecast_Price": "4778.17",
                "Lower_Bound": "3887.12",
                "Upper_Bound": "5669.23",
            },
            "07/08/2020": {
                "Forecast_Price": "4771.13",
                "Lower_Bound": "3911.85",
                "Upper_Bound": "5630.40",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4738.27",
                "Lower_Bound": "2313.78",
                "Upper_Bound": "7162.77",
            },
            "15/08/2020": {
                "Forecast_Price": "4751.36",
                "Lower_Bound": "2319.56",
                "Upper_Bound": "7183.15",
            },
            "22/08/2020": {
                "Forecast_Price": "4764.67",
                "Lower_Bound": "2325.73",
                "Upper_Bound": "7203.61",
            },
            "29/08/2020": {
                "Forecast_Price": "4778.30",
                "Lower_Bound": "2332.42",
                "Upper_Bound": "7224.17",
            },
            "05/09/2020": {
                "Forecast_Price": "4791.52",
                "Lower_Bound": "2338.43",
                "Upper_Bound": "7244.60",
            },
            "12/09/2020": {
                "Forecast_Price": "4804.60",
                "Lower_Bound": "2344.22",
                "Upper_Bound": "7264.98",
            },
            "19/09/2020": {
                "Forecast_Price": "4817.91",
                "Lower_Bound": "2350.38",
                "Upper_Bound": "7285.44",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4638.22",
                "Lower_Bound": "2260.20",
                "Upper_Bound": "7016.25",
            },
            "30/09/2020": {
                "Forecast_Price": "4736.82",
                "Lower_Bound": "2302.25",
                "Upper_Bound": "7171.40",
            },
            "30/10/2020": {
                "Forecast_Price": "4841.99",
                "Lower_Bound": "2347.55",
                "Upper_Bound": "7336.43",
            },
            "29/11/2020": {
                "Forecast_Price": "4950.55",
                "Lower_Bound": "2394.56",
                "Upper_Bound": "7506.55",
            },
            "29/12/2020": {
                "Forecast_Price": "5061.84",
                "Lower_Bound": "2444.77",
                "Upper_Bound": "7678.91",
            },
            "28/01/2021": {
                "Forecast_Price": "5003.58",
                "Lower_Bound": "2423.37",
                "Upper_Bound": "7583.80",
            },
            "27/02/2021": {
                "Forecast_Price": "4955.96",
                "Lower_Bound": "2422.73",
                "Upper_Bound": "7489.18",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4845.18",
                "Lower_Bound": "4131.16",
                "Upper_Bound": "5559.21",
            },
            "02/08/2020": {
                "Forecast_Price": "4822.57",
                "Lower_Bound": "4110.68",
                "Upper_Bound": "5534.45",
            },
            "03/08/2020": {
                "Forecast_Price": "4845.18",
                "Lower_Bound": "4250.33",
                "Upper_Bound": "5440.03",
            },
            "04/08/2020": {
                "Forecast_Price": "4839.72",
                "Lower_Bound": "4032.45",
                "Upper_Bound": "5646.98",
            },
            "05/08/2020": {
                "Forecast_Price": "4836.94",
                "Lower_Bound": "3997.06",
                "Upper_Bound": "5676.82",
            },
            "06/08/2020": {
                "Forecast_Price": "4799.85",
                "Lower_Bound": "4108.48",
                "Upper_Bound": "5491.22",
            },
            "07/08/2020": {
                "Forecast_Price": "4819.94",
                "Lower_Bound": "3882.74",
                "Upper_Bound": "5757.14",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4491.75",
                "Lower_Bound": "2194.98",
                "Upper_Bound": "6788.53",
            },
            "15/08/2020": {
                "Forecast_Price": "4512.19",
                "Lower_Bound": "2208.59",
                "Upper_Bound": "6815.79",
            },
            "22/08/2020": {
                "Forecast_Price": "4520.26",
                "Lower_Bound": "2215.00",
                "Upper_Bound": "6825.51",
            },
            "29/08/2020": {
                "Forecast_Price": "4507.87",
                "Lower_Bound": "2208.85",
                "Upper_Bound": "6806.89",
            },
            "05/09/2020": {
                "Forecast_Price": "4519.73",
                "Lower_Bound": "2218.15",
                "Upper_Bound": "6821.31",
            },
            "12/09/2020": {
                "Forecast_Price": "4540.05",
                "Lower_Bound": "2231.72",
                "Upper_Bound": "6848.38",
            },
            "19/09/2020": {
                "Forecast_Price": "4546.07",
                "Lower_Bound": "2237.46",
                "Upper_Bound": "6854.67",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4211.41",
                "Lower_Bound": "2036.85",
                "Upper_Bound": "6385.97",
            },
            "30/09/2020": {
                "Forecast_Price": "4102.82",
                "Lower_Bound": "1941.91",
                "Upper_Bound": "6263.72",
            },
            "30/10/2020": {
                "Forecast_Price": "4090.79",
                "Lower_Bound": "1907.91",
                "Upper_Bound": "6273.67",
            },
            "29/11/2020": {
                "Forecast_Price": "4157.27",
                "Lower_Bound": "1900.23",
                "Upper_Bound": "6414.30",
            },
            "29/12/2020": {
                "Forecast_Price": "4254.93",
                "Lower_Bound": "1921.34",
                "Upper_Bound": "6588.52",
            },
            "28/01/2021": {
                "Forecast_Price": "4276.23",
                "Lower_Bound": "1922.79",
                "Upper_Bound": "6629.66",
            },
            "27/02/2021": {
                "Forecast_Price": "4247.64",
                "Lower_Bound": "1897.04",
                "Upper_Bound": "6598.25",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3979.09",
                "Lower_Bound": "3031.69",
                "Upper_Bound": "4926.49",
            },
            "02/08/2020": {
                "Forecast_Price": "4021.33",
                "Lower_Bound": "3401.45",
                "Upper_Bound": "4641.21",
            },
            "03/08/2020": {
                "Forecast_Price": "4005.83",
                "Lower_Bound": "3366.55",
                "Upper_Bound": "4645.11",
            },
            "04/08/2020": {
                "Forecast_Price": "4040.72",
                "Lower_Bound": "2913.65",
                "Upper_Bound": "5167.79",
            },
            "05/08/2020": {
                "Forecast_Price": "4007.82",
                "Lower_Bound": "3262.44",
                "Upper_Bound": "4753.19",
            },
            "06/08/2020": {
                "Forecast_Price": "3987.03",
                "Lower_Bound": "3343.42",
                "Upper_Bound": "4630.64",
            },
            "07/08/2020": {
                "Forecast_Price": "4029.44",
                "Lower_Bound": "3396.36",
                "Upper_Bound": "4662.53",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4284.80",
                "Lower_Bound": "2089.53",
                "Upper_Bound": "6480.08",
            },
            "15/08/2020": {
                "Forecast_Price": "4278.74",
                "Lower_Bound": "2088.97",
                "Upper_Bound": "6468.51",
            },
            "22/08/2020": {
                "Forecast_Price": "4271.20",
                "Lower_Bound": "2086.44",
                "Upper_Bound": "6455.96",
            },
            "29/08/2020": {
                "Forecast_Price": "4237.69",
                "Lower_Bound": "2075.10",
                "Upper_Bound": "6400.28",
            },
            "05/09/2020": {
                "Forecast_Price": "4311.49",
                "Lower_Bound": "2100.13",
                "Upper_Bound": "6522.85",
            },
            "12/09/2020": {
                "Forecast_Price": "4305.43",
                "Lower_Bound": "2099.58",
                "Upper_Bound": "6511.28",
            },
            "19/09/2020": {
                "Forecast_Price": "4297.89",
                "Lower_Bound": "2097.04",
                "Upper_Bound": "6498.74",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4226.88",
                "Lower_Bound": "2029.99",
                "Upper_Bound": "6423.77",
            },
            "30/09/2020": {
                "Forecast_Price": "4201.58",
                "Lower_Bound": "1988.14",
                "Upper_Bound": "6415.02",
            },
            "30/10/2020": {
                "Forecast_Price": "4196.94",
                "Lower_Bound": "1963.25",
                "Upper_Bound": "6430.62",
            },
            "29/11/2020": {
                "Forecast_Price": "4166.31",
                "Lower_Bound": "1916.85",
                "Upper_Bound": "6415.78",
            },
            "29/12/2020": {
                "Forecast_Price": "4151.73",
                "Lower_Bound": "1889.20",
                "Upper_Bound": "6414.27",
            },
            "28/01/2021": {
                "Forecast_Price": "4132.53",
                "Lower_Bound": "1862.48",
                "Upper_Bound": "6402.58",
            },
            "27/02/2021": {
                "Forecast_Price": "4097.56",
                "Lower_Bound": "1825.90",
                "Upper_Bound": "6369.22",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5346.46",
                "Lower_Bound": "4570.87",
                "Upper_Bound": "6122.06",
            },
            "02/08/2020": {
                "Forecast_Price": "5344.95",
                "Lower_Bound": "4237.32",
                "Upper_Bound": "6452.57",
            },
            "03/08/2020": {
                "Forecast_Price": "5349.33",
                "Lower_Bound": "4237.88",
                "Upper_Bound": "6460.77",
            },
            "04/08/2020": {
                "Forecast_Price": "5366.99",
                "Lower_Bound": "4552.88",
                "Upper_Bound": "6181.10",
            },
            "05/08/2020": {
                "Forecast_Price": "5360.19",
                "Lower_Bound": "4475.26",
                "Upper_Bound": "6245.13",
            },
            "06/08/2020": {
                "Forecast_Price": "5357.27",
                "Lower_Bound": "4528.57",
                "Upper_Bound": "6185.97",
            },
            "07/08/2020": {
                "Forecast_Price": "5365.77",
                "Lower_Bound": "4556.39",
                "Upper_Bound": "6175.15",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5349.82",
                "Lower_Bound": "2612.87",
                "Upper_Bound": "8086.77",
            },
            "15/08/2020": {
                "Forecast_Price": "5349.62",
                "Lower_Bound": "2612.80",
                "Upper_Bound": "8086.43",
            },
            "22/08/2020": {
                "Forecast_Price": "5349.53",
                "Lower_Bound": "2612.78",
                "Upper_Bound": "8086.29",
            },
            "29/08/2020": {
                "Forecast_Price": "5349.57",
                "Lower_Bound": "2612.79",
                "Upper_Bound": "8086.34",
            },
            "05/09/2020": {
                "Forecast_Price": "5349.36",
                "Lower_Bound": "2612.72",
                "Upper_Bound": "8086.01",
            },
            "12/09/2020": {
                "Forecast_Price": "5349.16",
                "Lower_Bound": "2612.65",
                "Upper_Bound": "8085.67",
            },
            "19/09/2020": {
                "Forecast_Price": "5349.08",
                "Lower_Bound": "2612.63",
                "Upper_Bound": "8085.53",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5365.75",
                "Lower_Bound": "2624.53",
                "Upper_Bound": "8106.97",
            },
            "30/09/2020": {
                "Forecast_Price": "5390.60",
                "Lower_Bound": "2651.35",
                "Upper_Bound": "8129.85",
            },
            "30/10/2020": {
                "Forecast_Price": "5415.84",
                "Lower_Bound": "2678.82",
                "Upper_Bound": "8152.87",
            },
            "29/11/2020": {
                "Forecast_Price": "5431.66",
                "Lower_Bound": "2690.54",
                "Upper_Bound": "8172.79",
            },
            "29/12/2020": {
                "Forecast_Price": "5457.15",
                "Lower_Bound": "2718.42",
                "Upper_Bound": "8195.88",
            },
            "28/01/2021": {
                "Forecast_Price": "5474.11",
                "Lower_Bound": "2746.77",
                "Upper_Bound": "8201.45",
            },
            "27/02/2021": {
                "Forecast_Price": "5395.63",
                "Lower_Bound": "2733.90",
                "Upper_Bound": "8057.35",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3902.61",
                "Lower_Bound": "3106.45",
                "Upper_Bound": "4698.76",
            },
            "02/08/2020": {
                "Forecast_Price": "3911.51",
                "Lower_Bound": "3352.71",
                "Upper_Bound": "4470.31",
            },
            "03/08/2020": {
                "Forecast_Price": "3873.62",
                "Lower_Bound": "3306.17",
                "Upper_Bound": "4441.07",
            },
            "04/08/2020": {
                "Forecast_Price": "3870.47",
                "Lower_Bound": "3205.80",
                "Upper_Bound": "4535.14",
            },
            "05/08/2020": {
                "Forecast_Price": "3846.90",
                "Lower_Bound": "3349.63",
                "Upper_Bound": "4344.16",
            },
            "06/08/2020": {
                "Forecast_Price": "3857.42",
                "Lower_Bound": "3173.56",
                "Upper_Bound": "4541.27",
            },
            "07/08/2020": {
                "Forecast_Price": "3909.66",
                "Lower_Bound": "3164.21",
                "Upper_Bound": "4655.11",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3442.66",
                "Lower_Bound": "1702.19",
                "Upper_Bound": "5183.13",
            },
            "15/08/2020": {
                "Forecast_Price": "3455.44",
                "Lower_Bound": "1712.54",
                "Upper_Bound": "5198.34",
            },
            "22/08/2020": {
                "Forecast_Price": "3462.75",
                "Lower_Bound": "1716.43",
                "Upper_Bound": "5209.07",
            },
            "29/08/2020": {
                "Forecast_Price": "3460.37",
                "Lower_Bound": "1696.94",
                "Upper_Bound": "5223.79",
            },
            "05/09/2020": {
                "Forecast_Price": "3473.25",
                "Lower_Bound": "1731.14",
                "Upper_Bound": "5215.36",
            },
            "12/09/2020": {
                "Forecast_Price": "3483.16",
                "Lower_Bound": "1740.54",
                "Upper_Bound": "5225.78",
            },
            "19/09/2020": {
                "Forecast_Price": "3487.80",
                "Lower_Bound": "1743.56",
                "Upper_Bound": "5232.04",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3851.66",
                "Lower_Bound": "1962.24",
                "Upper_Bound": "5741.08",
            },
            "30/09/2020": {
                "Forecast_Price": "4155.63",
                "Lower_Bound": "2084.06",
                "Upper_Bound": "6227.21",
            },
            "30/10/2020": {
                "Forecast_Price": "4157.57",
                "Lower_Bound": "2105.69",
                "Upper_Bound": "6209.45",
            },
            "29/11/2020": {
                "Forecast_Price": "4156.50",
                "Lower_Bound": "2105.97",
                "Upper_Bound": "6207.04",
            },
            "29/12/2020": {
                "Forecast_Price": "4141.00",
                "Lower_Bound": "2120.66",
                "Upper_Bound": "6161.33",
            },
            "28/01/2021": {
                "Forecast_Price": "4232.82",
                "Lower_Bound": "2203.07",
                "Upper_Bound": "6262.57",
            },
            "27/02/2021": {
                "Forecast_Price": "4314.19",
                "Lower_Bound": "2259.39",
                "Upper_Bound": "6368.99",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3562.56",
                "Lower_Bound": "2964.94",
                "Upper_Bound": "4160.17",
            },
            "02/08/2020": {
                "Forecast_Price": "3508.02",
                "Lower_Bound": "2966.10",
                "Upper_Bound": "4049.93",
            },
            "03/08/2020": {
                "Forecast_Price": "3497.35",
                "Lower_Bound": "2923.28",
                "Upper_Bound": "4071.41",
            },
            "04/08/2020": {
                "Forecast_Price": "3524.70",
                "Lower_Bound": "2985.11",
                "Upper_Bound": "4064.29",
            },
            "05/08/2020": {
                "Forecast_Price": "3541.37",
                "Lower_Bound": "2885.49",
                "Upper_Bound": "4197.26",
            },
            "06/08/2020": {
                "Forecast_Price": "3534.79",
                "Lower_Bound": "3071.67",
                "Upper_Bound": "3997.90",
            },
            "07/08/2020": {
                "Forecast_Price": "3597.14",
                "Lower_Bound": "3119.42",
                "Upper_Bound": "4074.86",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3683.81",
                "Lower_Bound": "1751.05",
                "Upper_Bound": "5616.56",
            },
            "15/08/2020": {
                "Forecast_Price": "3682.24",
                "Lower_Bound": "1766.72",
                "Upper_Bound": "5597.76",
            },
            "22/08/2020": {
                "Forecast_Price": "3697.08",
                "Lower_Bound": "1786.15",
                "Upper_Bound": "5608.01",
            },
            "29/08/2020": {
                "Forecast_Price": "3663.11",
                "Lower_Bound": "1731.67",
                "Upper_Bound": "5594.55",
            },
            "05/09/2020": {
                "Forecast_Price": "3670.48",
                "Lower_Bound": "1718.94",
                "Upper_Bound": "5622.02",
            },
            "12/09/2020": {
                "Forecast_Price": "3668.92",
                "Lower_Bound": "1734.61",
                "Upper_Bound": "5603.22",
            },
            "19/09/2020": {
                "Forecast_Price": "3683.75",
                "Lower_Bound": "1754.03",
                "Upper_Bound": "5613.47",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3902.16",
                "Lower_Bound": "1886.86",
                "Upper_Bound": "5917.46",
            },
            "30/09/2020": {
                "Forecast_Price": "3728.48",
                "Lower_Bound": "1787.29",
                "Upper_Bound": "5669.68",
            },
            "30/10/2020": {
                "Forecast_Price": "3592.54",
                "Lower_Bound": "1697.56",
                "Upper_Bound": "5487.51",
            },
            "29/11/2020": {
                "Forecast_Price": "3469.95",
                "Lower_Bound": "1594.64",
                "Upper_Bound": "5345.25",
            },
            "29/12/2020": {
                "Forecast_Price": "3665.51",
                "Lower_Bound": "1632.74",
                "Upper_Bound": "5698.29",
            },
            "28/01/2021": {
                "Forecast_Price": "3726.09",
                "Lower_Bound": "1666.17",
                "Upper_Bound": "5786.02",
            },
            "27/02/2021": {
                "Forecast_Price": "3762.92",
                "Lower_Bound": "1675.54",
                "Upper_Bound": "5850.30",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5400.78",
                "Lower_Bound": "4474.31",
                "Upper_Bound": "6327.26",
            },
            "02/08/2020": {
                "Forecast_Price": "5401.15",
                "Lower_Bound": "4482.05",
                "Upper_Bound": "6320.25",
            },
            "03/08/2020": {
                "Forecast_Price": "5401.39",
                "Lower_Bound": "4211.60",
                "Upper_Bound": "6591.18",
            },
            "04/08/2020": {
                "Forecast_Price": "5405.90",
                "Lower_Bound": "4661.07",
                "Upper_Bound": "6150.73",
            },
            "05/08/2020": {
                "Forecast_Price": "5401.37",
                "Lower_Bound": "4292.45",
                "Upper_Bound": "6510.28",
            },
            "06/08/2020": {
                "Forecast_Price": "5395.81",
                "Lower_Bound": "4413.30",
                "Upper_Bound": "6378.31",
            },
            "07/08/2020": {
                "Forecast_Price": "5418.19",
                "Lower_Bound": "4746.22",
                "Upper_Bound": "6090.17",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5094.89",
                "Lower_Bound": "2486.25",
                "Upper_Bound": "7703.54",
            },
            "15/08/2020": {
                "Forecast_Price": "5093.37",
                "Lower_Bound": "2487.76",
                "Upper_Bound": "7698.98",
            },
            "22/08/2020": {
                "Forecast_Price": "5096.92",
                "Lower_Bound": "2490.54",
                "Upper_Bound": "7703.30",
            },
            "29/08/2020": {
                "Forecast_Price": "5111.11",
                "Lower_Bound": "2494.86",
                "Upper_Bound": "7727.35",
            },
            "05/09/2020": {
                "Forecast_Price": "5118.40",
                "Lower_Bound": "2499.95",
                "Upper_Bound": "7736.86",
            },
            "12/09/2020": {
                "Forecast_Price": "5115.06",
                "Lower_Bound": "2500.87",
                "Upper_Bound": "7729.26",
            },
            "19/09/2020": {
                "Forecast_Price": "5117.55",
                "Lower_Bound": "2503.30",
                "Upper_Bound": "7731.80",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5081.93",
                "Lower_Bound": "2484.33",
                "Upper_Bound": "7679.53",
            },
            "30/09/2020": {
                "Forecast_Price": "5072.47",
                "Lower_Bound": "2476.35",
                "Upper_Bound": "7668.59",
            },
            "30/10/2020": {
                "Forecast_Price": "5096.42",
                "Lower_Bound": "2482.21",
                "Upper_Bound": "7710.63",
            },
            "29/11/2020": {
                "Forecast_Price": "5218.15",
                "Lower_Bound": "2532.29",
                "Upper_Bound": "7904.01",
            },
            "29/12/2020": {
                "Forecast_Price": "5348.02",
                "Lower_Bound": "2578.30",
                "Upper_Bound": "8117.73",
            },
            "28/01/2021": {
                "Forecast_Price": "5383.07",
                "Lower_Bound": "2578.15",
                "Upper_Bound": "8187.99",
            },
            "27/02/2021": {
                "Forecast_Price": "5332.40",
                "Lower_Bound": "2544.29",
                "Upper_Bound": "8120.50",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5546.79",
                "Lower_Bound": "4476.75",
                "Upper_Bound": "6616.82",
            },
            "02/08/2020": {
                "Forecast_Price": "5545.04",
                "Lower_Bound": "4616.93",
                "Upper_Bound": "6473.16",
            },
            "03/08/2020": {
                "Forecast_Price": "5537.66",
                "Lower_Bound": "4720.20",
                "Upper_Bound": "6355.12",
            },
            "04/08/2020": {
                "Forecast_Price": "5545.10",
                "Lower_Bound": "4720.44",
                "Upper_Bound": "6369.76",
            },
            "05/08/2020": {
                "Forecast_Price": "5541.20",
                "Lower_Bound": "4842.65",
                "Upper_Bound": "6239.74",
            },
            "06/08/2020": {
                "Forecast_Price": "5549.52",
                "Lower_Bound": "4829.33",
                "Upper_Bound": "6269.72",
            },
            "07/08/2020": {
                "Forecast_Price": "5536.34",
                "Lower_Bound": "4899.42",
                "Upper_Bound": "6173.26",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5545.23",
                "Lower_Bound": "2709.31",
                "Upper_Bound": "8381.15",
            },
            "15/08/2020": {
                "Forecast_Price": "5538.45",
                "Lower_Bound": "2706.99",
                "Upper_Bound": "8369.92",
            },
            "22/08/2020": {
                "Forecast_Price": "5531.69",
                "Lower_Bound": "2704.79",
                "Upper_Bound": "8358.60",
            },
            "29/08/2020": {
                "Forecast_Price": "5526.37",
                "Lower_Bound": "2703.33",
                "Upper_Bound": "8349.42",
            },
            "05/09/2020": {
                "Forecast_Price": "5520.69",
                "Lower_Bound": "2701.50",
                "Upper_Bound": "8339.88",
            },
            "12/09/2020": {
                "Forecast_Price": "5514.25",
                "Lower_Bound": "2699.28",
                "Upper_Bound": "8329.21",
            },
            "19/09/2020": {
                "Forecast_Price": "5507.84",
                "Lower_Bound": "2697.20",
                "Upper_Bound": "8318.48",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5564.45",
                "Lower_Bound": "2728.05",
                "Upper_Bound": "8400.86",
            },
            "30/09/2020": {
                "Forecast_Price": "5581.60",
                "Lower_Bound": "2749.98",
                "Upper_Bound": "8413.21",
            },
            "30/10/2020": {
                "Forecast_Price": "5639.78",
                "Lower_Bound": "2840.53",
                "Upper_Bound": "8439.03",
            },
            "29/11/2020": {
                "Forecast_Price": "5661.23",
                "Lower_Bound": "2869.67",
                "Upper_Bound": "8452.80",
            },
            "29/12/2020": {
                "Forecast_Price": "5684.91",
                "Lower_Bound": "2902.53",
                "Upper_Bound": "8467.29",
            },
            "28/01/2021": {
                "Forecast_Price": "5705.58",
                "Lower_Bound": "2930.36",
                "Upper_Bound": "8480.80",
            },
            "27/02/2021": {
                "Forecast_Price": "5692.49",
                "Lower_Bound": "2935.37",
                "Upper_Bound": "8449.61",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4603.86",
                "Lower_Bound": "3777.50",
                "Upper_Bound": "5430.22",
            },
            "02/08/2020": {
                "Forecast_Price": "4596.89",
                "Lower_Bound": "3839.28",
                "Upper_Bound": "5354.49",
            },
            "03/08/2020": {
                "Forecast_Price": "4607.10",
                "Lower_Bound": "3708.30",
                "Upper_Bound": "5505.89",
            },
            "04/08/2020": {
                "Forecast_Price": "4598.38",
                "Lower_Bound": "3976.95",
                "Upper_Bound": "5219.80",
            },
            "05/08/2020": {
                "Forecast_Price": "4590.42",
                "Lower_Bound": "3806.76",
                "Upper_Bound": "5374.09",
            },
            "06/08/2020": {
                "Forecast_Price": "4607.09",
                "Lower_Bound": "3899.84",
                "Upper_Bound": "5314.34",
            },
            "07/08/2020": {
                "Forecast_Price": "4560.10",
                "Lower_Bound": "3763.23",
                "Upper_Bound": "5356.97",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4583.16",
                "Lower_Bound": "2238.21",
                "Upper_Bound": "6928.11",
            },
            "15/08/2020": {
                "Forecast_Price": "4584.50",
                "Lower_Bound": "2237.80",
                "Upper_Bound": "6931.20",
            },
            "22/08/2020": {
                "Forecast_Price": "4581.40",
                "Lower_Bound": "2236.50",
                "Upper_Bound": "6926.30",
            },
            "29/08/2020": {
                "Forecast_Price": "4576.58",
                "Lower_Bound": "2234.83",
                "Upper_Bound": "6918.33",
            },
            "05/09/2020": {
                "Forecast_Price": "4581.52",
                "Lower_Bound": "2237.18",
                "Upper_Bound": "6925.86",
            },
            "12/09/2020": {
                "Forecast_Price": "4582.84",
                "Lower_Bound": "2236.77",
                "Upper_Bound": "6928.92",
            },
            "19/09/2020": {
                "Forecast_Price": "4579.76",
                "Lower_Bound": "2235.48",
                "Upper_Bound": "6924.05",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4589.26",
                "Lower_Bound": "2269.25",
                "Upper_Bound": "6909.27",
            },
            "30/09/2020": {
                "Forecast_Price": "4571.86",
                "Lower_Bound": "2257.74",
                "Upper_Bound": "6885.97",
            },
            "30/10/2020": {
                "Forecast_Price": "4548.77",
                "Lower_Bound": "2237.30",
                "Upper_Bound": "6860.24",
            },
            "29/11/2020": {
                "Forecast_Price": "4507.27",
                "Lower_Bound": "2194.86",
                "Upper_Bound": "6819.68",
            },
            "29/12/2020": {
                "Forecast_Price": "4472.30",
                "Lower_Bound": "2161.53",
                "Upper_Bound": "6783.06",
            },
            "28/01/2021": {
                "Forecast_Price": "4428.54",
                "Lower_Bound": "2111.92",
                "Upper_Bound": "6745.15",
            },
            "27/02/2021": {
                "Forecast_Price": "4378.16",
                "Lower_Bound": "2048.58",
                "Upper_Bound": "6707.74",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3460.45",
                "Lower_Bound": "2887.05",
                "Upper_Bound": "4033.85",
            },
            "02/08/2020": {
                "Forecast_Price": "3415.78",
                "Lower_Bound": "2898.89",
                "Upper_Bound": "3932.67",
            },
            "03/08/2020": {
                "Forecast_Price": "3426.48",
                "Lower_Bound": "2834.56",
                "Upper_Bound": "4018.39",
            },
            "04/08/2020": {
                "Forecast_Price": "3462.41",
                "Lower_Bound": "2661.13",
                "Upper_Bound": "4263.69",
            },
            "05/08/2020": {
                "Forecast_Price": "3427.66",
                "Lower_Bound": "2280.00",
                "Upper_Bound": "4575.32",
            },
            "06/08/2020": {
                "Forecast_Price": "3437.01",
                "Lower_Bound": "2840.13",
                "Upper_Bound": "4033.88",
            },
            "07/08/2020": {
                "Forecast_Price": "3463.48",
                "Lower_Bound": "2532.06",
                "Upper_Bound": "4394.90",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3545.21",
                "Lower_Bound": "1733.30",
                "Upper_Bound": "5357.12",
            },
            "15/08/2020": {
                "Forecast_Price": "3511.92",
                "Lower_Bound": "1716.31",
                "Upper_Bound": "5307.54",
            },
            "22/08/2020": {
                "Forecast_Price": "3486.41",
                "Lower_Bound": "1712.32",
                "Upper_Bound": "5260.51",
            },
            "29/08/2020": {
                "Forecast_Price": "3460.09",
                "Lower_Bound": "1706.98",
                "Upper_Bound": "5213.21",
            },
            "05/09/2020": {
                "Forecast_Price": "3469.69",
                "Lower_Bound": "1703.29",
                "Upper_Bound": "5236.08",
            },
            "12/09/2020": {
                "Forecast_Price": "3436.40",
                "Lower_Bound": "1686.30",
                "Upper_Bound": "5186.50",
            },
            "19/09/2020": {
                "Forecast_Price": "3410.89",
                "Lower_Bound": "1682.31",
                "Upper_Bound": "5139.47",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3544.94",
                "Lower_Bound": "1704.80",
                "Upper_Bound": "5385.09",
            },
            "30/09/2020": {
                "Forecast_Price": "3510.49",
                "Lower_Bound": "1666.44",
                "Upper_Bound": "5354.55",
            },
            "30/10/2020": {
                "Forecast_Price": "3477.96",
                "Lower_Bound": "1665.60",
                "Upper_Bound": "5290.33",
            },
            "29/11/2020": {
                "Forecast_Price": "3452.14",
                "Lower_Bound": "1611.76",
                "Upper_Bound": "5292.52",
            },
            "29/12/2020": {
                "Forecast_Price": "3425.01",
                "Lower_Bound": "1562.16",
                "Upper_Bound": "5287.86",
            },
            "28/01/2021": {
                "Forecast_Price": "3381.52",
                "Lower_Bound": "1492.36",
                "Upper_Bound": "5270.68",
            },
            "27/02/2021": {
                "Forecast_Price": "3284.88",
                "Lower_Bound": "1372.38",
                "Upper_Bound": "5197.38",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5056.55",
                "Lower_Bound": "4024.88",
                "Upper_Bound": "6088.22",
            },
            "02/08/2020": {
                "Forecast_Price": "5056.26",
                "Lower_Bound": "4082.81",
                "Upper_Bound": "6029.71",
            },
            "03/08/2020": {
                "Forecast_Price": "5058.43",
                "Lower_Bound": "4341.12",
                "Upper_Bound": "5775.74",
            },
            "04/08/2020": {
                "Forecast_Price": "5042.97",
                "Lower_Bound": "4038.43",
                "Upper_Bound": "6047.51",
            },
            "05/08/2020": {
                "Forecast_Price": "5058.40",
                "Lower_Bound": "4177.35",
                "Upper_Bound": "5939.45",
            },
            "06/08/2020": {
                "Forecast_Price": "5065.75",
                "Lower_Bound": "4123.07",
                "Upper_Bound": "6008.44",
            },
            "07/08/2020": {
                "Forecast_Price": "5066.66",
                "Lower_Bound": "3610.03",
                "Upper_Bound": "6523.28",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5215.87",
                "Lower_Bound": "2547.20",
                "Upper_Bound": "7884.54",
            },
            "15/08/2020": {
                "Forecast_Price": "5212.96",
                "Lower_Bound": "2545.13",
                "Upper_Bound": "7880.78",
            },
            "22/08/2020": {
                "Forecast_Price": "5209.06",
                "Lower_Bound": "2542.75",
                "Upper_Bound": "7875.37",
            },
            "29/08/2020": {
                "Forecast_Price": "5207.85",
                "Lower_Bound": "2541.23",
                "Upper_Bound": "7874.47",
            },
            "05/09/2020": {
                "Forecast_Price": "5203.29",
                "Lower_Bound": "2538.62",
                "Upper_Bound": "7867.97",
            },
            "12/09/2020": {
                "Forecast_Price": "5200.39",
                "Lower_Bound": "2536.56",
                "Upper_Bound": "7864.23",
            },
            "19/09/2020": {
                "Forecast_Price": "5196.52",
                "Lower_Bound": "2534.18",
                "Upper_Bound": "7858.86",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5226.84",
                "Lower_Bound": "2567.33",
                "Upper_Bound": "7886.35",
            },
            "30/09/2020": {
                "Forecast_Price": "5226.67",
                "Lower_Bound": "2583.08",
                "Upper_Bound": "7870.26",
            },
            "30/10/2020": {
                "Forecast_Price": "5226.63",
                "Lower_Bound": "2599.04",
                "Upper_Bound": "7854.21",
            },
            "29/11/2020": {
                "Forecast_Price": "5235.81",
                "Lower_Bound": "2629.23",
                "Upper_Bound": "7842.40",
            },
            "29/12/2020": {
                "Forecast_Price": "5240.12",
                "Lower_Bound": "2652.43",
                "Upper_Bound": "7827.82",
            },
            "28/01/2021": {
                "Forecast_Price": "5242.38",
                "Lower_Bound": "2671.56",
                "Upper_Bound": "7813.21",
            },
            "27/02/2021": {
                "Forecast_Price": "5231.36",
                "Lower_Bound": "2666.13",
                "Upper_Bound": "7796.60",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4480.94",
                "Lower_Bound": "3767.72",
                "Upper_Bound": "5194.15",
            },
            "02/08/2020": {
                "Forecast_Price": "4488.84",
                "Lower_Bound": "3761.73",
                "Upper_Bound": "5215.95",
            },
            "03/08/2020": {
                "Forecast_Price": "4432.67",
                "Lower_Bound": "3517.73",
                "Upper_Bound": "5347.60",
            },
            "04/08/2020": {
                "Forecast_Price": "4464.56",
                "Lower_Bound": "3822.54",
                "Upper_Bound": "5106.59",
            },
            "05/08/2020": {
                "Forecast_Price": "4453.66",
                "Lower_Bound": "3421.62",
                "Upper_Bound": "5485.70",
            },
            "06/08/2020": {
                "Forecast_Price": "4471.49",
                "Lower_Bound": "2976.33",
                "Upper_Bound": "5966.65",
            },
            "07/08/2020": {
                "Forecast_Price": "4480.65",
                "Lower_Bound": "3862.31",
                "Upper_Bound": "5098.99",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3958.62",
                "Lower_Bound": "1950.59",
                "Upper_Bound": "5966.64",
            },
            "15/08/2020": {
                "Forecast_Price": "3892.95",
                "Lower_Bound": "1861.97",
                "Upper_Bound": "5923.93",
            },
            "22/08/2020": {
                "Forecast_Price": "3862.36",
                "Lower_Bound": "1821.51",
                "Upper_Bound": "5903.20",
            },
            "29/08/2020": {
                "Forecast_Price": "3943.37",
                "Lower_Bound": "1929.17",
                "Upper_Bound": "5957.57",
            },
            "05/09/2020": {
                "Forecast_Price": "3931.77",
                "Lower_Bound": "1896.87",
                "Upper_Bound": "5966.66",
            },
            "12/09/2020": {
                "Forecast_Price": "3877.55",
                "Lower_Bound": "1812.00",
                "Upper_Bound": "5943.09",
            },
            "19/09/2020": {
                "Forecast_Price": "3850.66",
                "Lower_Bound": "1772.76",
                "Upper_Bound": "5928.55",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4306.77",
                "Lower_Bound": "1996.17",
                "Upper_Bound": "6617.38",
            },
            "30/09/2020": {
                "Forecast_Price": "4281.25",
                "Lower_Bound": "1940.52",
                "Upper_Bound": "6621.98",
            },
            "30/10/2020": {
                "Forecast_Price": "4266.26",
                "Lower_Bound": "1896.80",
                "Upper_Bound": "6635.72",
            },
            "29/11/2020": {
                "Forecast_Price": "4300.18",
                "Lower_Bound": "1890.38",
                "Upper_Bound": "6709.98",
            },
            "29/12/2020": {
                "Forecast_Price": "4324.04",
                "Lower_Bound": "1883.46",
                "Upper_Bound": "6764.62",
            },
            "28/01/2021": {
                "Forecast_Price": "4307.07",
                "Lower_Bound": "1858.08",
                "Upper_Bound": "6756.07",
            },
            "27/02/2021": {
                "Forecast_Price": "4227.44",
                "Lower_Bound": "1791.19",
                "Upper_Bound": "6663.69",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5445.78",
                "Lower_Bound": "4253.96",
                "Upper_Bound": "6637.60",
            },
            "02/08/2020": {
                "Forecast_Price": "5455.36",
                "Lower_Bound": "4321.14",
                "Upper_Bound": "6589.57",
            },
            "03/08/2020": {
                "Forecast_Price": "5470.80",
                "Lower_Bound": "4482.60",
                "Upper_Bound": "6459.00",
            },
            "04/08/2020": {
                "Forecast_Price": "5458.42",
                "Lower_Bound": "4685.80",
                "Upper_Bound": "6231.04",
            },
            "05/08/2020": {
                "Forecast_Price": "5444.38",
                "Lower_Bound": "4507.79",
                "Upper_Bound": "6380.96",
            },
            "06/08/2020": {
                "Forecast_Price": "5471.13",
                "Lower_Bound": "4536.12",
                "Upper_Bound": "6406.14",
            },
            "07/08/2020": {
                "Forecast_Price": "5504.27",
                "Lower_Bound": "4753.92",
                "Upper_Bound": "6254.62",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4980.66",
                "Lower_Bound": "2435.80",
                "Upper_Bound": "7525.53",
            },
            "15/08/2020": {
                "Forecast_Price": "4973.69",
                "Lower_Bound": "2434.57",
                "Upper_Bound": "7512.81",
            },
            "22/08/2020": {
                "Forecast_Price": "4978.24",
                "Lower_Bound": "2436.60",
                "Upper_Bound": "7519.89",
            },
            "29/08/2020": {
                "Forecast_Price": "4975.18",
                "Lower_Bound": "2436.29",
                "Upper_Bound": "7514.07",
            },
            "05/09/2020": {
                "Forecast_Price": "4960.54",
                "Lower_Bound": "2431.81",
                "Upper_Bound": "7489.27",
            },
            "12/09/2020": {
                "Forecast_Price": "4953.57",
                "Lower_Bound": "2430.58",
                "Upper_Bound": "7476.55",
            },
            "19/09/2020": {
                "Forecast_Price": "4958.12",
                "Lower_Bound": "2432.61",
                "Upper_Bound": "7483.63",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4988.89",
                "Lower_Bound": "2429.18",
                "Upper_Bound": "7548.59",
            },
            "30/09/2020": {
                "Forecast_Price": "4985.33",
                "Lower_Bound": "2437.58",
                "Upper_Bound": "7533.08",
            },
            "30/10/2020": {
                "Forecast_Price": "4980.78",
                "Lower_Bound": "2444.57",
                "Upper_Bound": "7516.99",
            },
            "29/11/2020": {
                "Forecast_Price": "4964.99",
                "Lower_Bound": "2436.21",
                "Upper_Bound": "7493.77",
            },
            "29/12/2020": {
                "Forecast_Price": "4955.10",
                "Lower_Bound": "2437.96",
                "Upper_Bound": "7472.25",
            },
            "28/01/2021": {
                "Forecast_Price": "4950.58",
                "Lower_Bound": "2443.27",
                "Upper_Bound": "7457.89",
            },
            "27/02/2021": {
                "Forecast_Price": "4941.78",
                "Lower_Bound": "2442.92",
                "Upper_Bound": "7440.64",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5291.19",
                "Lower_Bound": "4497.97",
                "Upper_Bound": "6084.40",
            },
            "02/08/2020": {
                "Forecast_Price": "5214.44",
                "Lower_Bound": "4412.63",
                "Upper_Bound": "6016.25",
            },
            "03/08/2020": {
                "Forecast_Price": "5242.77",
                "Lower_Bound": "4198.28",
                "Upper_Bound": "6287.26",
            },
            "04/08/2020": {
                "Forecast_Price": "5224.15",
                "Lower_Bound": "4534.60",
                "Upper_Bound": "5913.71",
            },
            "05/08/2020": {
                "Forecast_Price": "5352.83",
                "Lower_Bound": "4591.79",
                "Upper_Bound": "6113.87",
            },
            "06/08/2020": {
                "Forecast_Price": "5310.54",
                "Lower_Bound": "4405.77",
                "Upper_Bound": "6215.30",
            },
            "07/08/2020": {
                "Forecast_Price": "5322.13",
                "Lower_Bound": "4303.18",
                "Upper_Bound": "6341.07",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5178.23",
                "Lower_Bound": "2529.30",
                "Upper_Bound": "7827.15",
            },
            "15/08/2020": {
                "Forecast_Price": "5169.76",
                "Lower_Bound": "2525.97",
                "Upper_Bound": "7813.56",
            },
            "22/08/2020": {
                "Forecast_Price": "5161.39",
                "Lower_Bound": "2523.81",
                "Upper_Bound": "7798.97",
            },
            "29/08/2020": {
                "Forecast_Price": "5155.40",
                "Lower_Bound": "2521.26",
                "Upper_Bound": "7789.54",
            },
            "05/09/2020": {
                "Forecast_Price": "5144.69",
                "Lower_Bound": "2516.59",
                "Upper_Bound": "7772.80",
            },
            "12/09/2020": {
                "Forecast_Price": "5135.52",
                "Lower_Bound": "2513.03",
                "Upper_Bound": "7758.00",
            },
            "19/09/2020": {
                "Forecast_Price": "5126.65",
                "Lower_Bound": "2510.70",
                "Upper_Bound": "7742.60",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5275.51",
                "Lower_Bound": "2536.25",
                "Upper_Bound": "8014.78",
            },
            "30/09/2020": {
                "Forecast_Price": "5156.22",
                "Lower_Bound": "2447.28",
                "Upper_Bound": "7865.16",
            },
            "30/10/2020": {
                "Forecast_Price": "5279.15",
                "Lower_Bound": "2496.91",
                "Upper_Bound": "8061.40",
            },
            "29/11/2020": {
                "Forecast_Price": "5354.90",
                "Lower_Bound": "2522.06",
                "Upper_Bound": "8187.73",
            },
            "29/12/2020": {
                "Forecast_Price": "5459.22",
                "Lower_Bound": "2561.56",
                "Upper_Bound": "8356.89",
            },
            "28/01/2021": {
                "Forecast_Price": "5486.41",
                "Lower_Bound": "2569.87",
                "Upper_Bound": "8402.95",
            },
            "27/02/2021": {
                "Forecast_Price": "5472.63",
                "Lower_Bound": "2565.64",
                "Upper_Bound": "8379.62",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4862.00",
                "Lower_Bound": "3967.57",
                "Upper_Bound": "5756.42",
            },
            "02/08/2020": {
                "Forecast_Price": "4895.67",
                "Lower_Bound": "4163.13",
                "Upper_Bound": "5628.21",
            },
            "03/08/2020": {
                "Forecast_Price": "4872.88",
                "Lower_Bound": "3987.00",
                "Upper_Bound": "5758.77",
            },
            "04/08/2020": {
                "Forecast_Price": "4900.41",
                "Lower_Bound": "4064.75",
                "Upper_Bound": "5736.06",
            },
            "05/08/2020": {
                "Forecast_Price": "4962.64",
                "Lower_Bound": "4262.65",
                "Upper_Bound": "5662.63",
            },
            "06/08/2020": {
                "Forecast_Price": "4881.43",
                "Lower_Bound": "4112.10",
                "Upper_Bound": "5650.77",
            },
            "07/08/2020": {
                "Forecast_Price": "4882.15",
                "Lower_Bound": "3688.61",
                "Upper_Bound": "6075.68",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4873.18",
                "Lower_Bound": "2380.04",
                "Upper_Bound": "7366.32",
            },
            "15/08/2020": {
                "Forecast_Price": "4870.75",
                "Lower_Bound": "2378.92",
                "Upper_Bound": "7362.59",
            },
            "22/08/2020": {
                "Forecast_Price": "4868.93",
                "Lower_Bound": "2377.98",
                "Upper_Bound": "7359.87",
            },
            "29/08/2020": {
                "Forecast_Price": "4866.97",
                "Lower_Bound": "2377.01",
                "Upper_Bound": "7356.93",
            },
            "05/09/2020": {
                "Forecast_Price": "4864.79",
                "Lower_Bound": "2375.96",
                "Upper_Bound": "7353.62",
            },
            "12/09/2020": {
                "Forecast_Price": "4862.36",
                "Lower_Bound": "2374.84",
                "Upper_Bound": "7349.88",
            },
            "19/09/2020": {
                "Forecast_Price": "4860.53",
                "Lower_Bound": "2373.90",
                "Upper_Bound": "7347.16",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4873.78",
                "Lower_Bound": "2391.22",
                "Upper_Bound": "7356.34",
            },
            "30/09/2020": {
                "Forecast_Price": "5133.04",
                "Lower_Bound": "2499.50",
                "Upper_Bound": "7766.59",
            },
            "30/10/2020": {
                "Forecast_Price": "5347.90",
                "Lower_Bound": "2574.57",
                "Upper_Bound": "8121.23",
            },
            "29/11/2020": {
                "Forecast_Price": "5551.29",
                "Lower_Bound": "2653.09",
                "Upper_Bound": "8449.50",
            },
            "29/12/2020": {
                "Forecast_Price": "5742.88",
                "Lower_Bound": "2734.89",
                "Upper_Bound": "8750.87",
            },
            "28/01/2021": {
                "Forecast_Price": "5896.18",
                "Lower_Bound": "2790.32",
                "Upper_Bound": "9002.03",
            },
            "27/02/2021": {
                "Forecast_Price": "5867.02",
                "Lower_Bound": "2771.94",
                "Upper_Bound": "8962.10",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4789.54",
                "Lower_Bound": "4052.04",
                "Upper_Bound": "5527.05",
            },
            "02/08/2020": {
                "Forecast_Price": "4787.51",
                "Lower_Bound": "3843.59",
                "Upper_Bound": "5731.42",
            },
            "03/08/2020": {
                "Forecast_Price": "4804.46",
                "Lower_Bound": "3574.07",
                "Upper_Bound": "6034.86",
            },
            "04/08/2020": {
                "Forecast_Price": "4829.44",
                "Lower_Bound": "3951.38",
                "Upper_Bound": "5707.50",
            },
            "05/08/2020": {
                "Forecast_Price": "4828.49",
                "Lower_Bound": "4090.43",
                "Upper_Bound": "5566.54",
            },
            "06/08/2020": {
                "Forecast_Price": "4701.33",
                "Lower_Bound": "3518.08",
                "Upper_Bound": "5884.58",
            },
            "07/08/2020": {
                "Forecast_Price": "4753.08",
                "Lower_Bound": "3942.71",
                "Upper_Bound": "5563.45",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4652.45",
                "Lower_Bound": "2268.03",
                "Upper_Bound": "7036.87",
            },
            "15/08/2020": {
                "Forecast_Price": "4655.27",
                "Lower_Bound": "2268.56",
                "Upper_Bound": "7041.97",
            },
            "22/08/2020": {
                "Forecast_Price": "4656.98",
                "Lower_Bound": "2268.74",
                "Upper_Bound": "7045.22",
            },
            "29/08/2020": {
                "Forecast_Price": "4679.64",
                "Lower_Bound": "2275.78",
                "Upper_Bound": "7083.49",
            },
            "05/09/2020": {
                "Forecast_Price": "4692.08",
                "Lower_Bound": "2279.37",
                "Upper_Bound": "7104.78",
            },
            "12/09/2020": {
                "Forecast_Price": "4694.81",
                "Lower_Bound": "2279.78",
                "Upper_Bound": "7109.85",
            },
            "19/09/2020": {
                "Forecast_Price": "4696.45",
                "Lower_Bound": "2279.82",
                "Upper_Bound": "7113.08",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4587.92",
                "Lower_Bound": "2213.66",
                "Upper_Bound": "6962.18",
            },
            "30/09/2020": {
                "Forecast_Price": "4553.71",
                "Lower_Bound": "2176.96",
                "Upper_Bound": "6930.45",
            },
            "30/10/2020": {
                "Forecast_Price": "4517.85",
                "Lower_Bound": "2136.95",
                "Upper_Bound": "6898.75",
            },
            "29/11/2020": {
                "Forecast_Price": "4481.88",
                "Lower_Bound": "2096.20",
                "Upper_Bound": "6867.55",
            },
            "29/12/2020": {
                "Forecast_Price": "4454.07",
                "Lower_Bound": "2068.58",
                "Upper_Bound": "6839.56",
            },
            "28/01/2021": {
                "Forecast_Price": "4427.90",
                "Lower_Bound": "2043.17",
                "Upper_Bound": "6812.62",
            },
            "27/02/2021": {
                "Forecast_Price": "4405.54",
                "Lower_Bound": "2022.98",
                "Upper_Bound": "6788.10",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4701.70",
                "Lower_Bound": "3382.79",
                "Upper_Bound": "6020.60",
            },
            "02/08/2020": {
                "Forecast_Price": "4692.89",
                "Lower_Bound": "4068.55",
                "Upper_Bound": "5317.24",
            },
            "03/08/2020": {
                "Forecast_Price": "4687.60",
                "Lower_Bound": "3885.33",
                "Upper_Bound": "5489.88",
            },
            "04/08/2020": {
                "Forecast_Price": "4674.41",
                "Lower_Bound": "4018.10",
                "Upper_Bound": "5330.72",
            },
            "05/08/2020": {
                "Forecast_Price": "4654.35",
                "Lower_Bound": "4015.26",
                "Upper_Bound": "5293.43",
            },
            "06/08/2020": {
                "Forecast_Price": "4649.48",
                "Lower_Bound": "3763.88",
                "Upper_Bound": "5535.07",
            },
            "07/08/2020": {
                "Forecast_Price": "4668.10",
                "Lower_Bound": "3894.38",
                "Upper_Bound": "5441.81",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4871.32",
                "Lower_Bound": "2378.99",
                "Upper_Bound": "7363.65",
            },
            "15/08/2020": {
                "Forecast_Price": "4874.05",
                "Lower_Bound": "2374.16",
                "Upper_Bound": "7373.95",
            },
            "22/08/2020": {
                "Forecast_Price": "4879.87",
                "Lower_Bound": "2374.48",
                "Upper_Bound": "7385.26",
            },
            "29/08/2020": {
                "Forecast_Price": "4892.34",
                "Lower_Bound": "2385.92",
                "Upper_Bound": "7398.76",
            },
            "05/09/2020": {
                "Forecast_Price": "4899.58",
                "Lower_Bound": "2388.61",
                "Upper_Bound": "7410.54",
            },
            "12/09/2020": {
                "Forecast_Price": "4902.31",
                "Lower_Bound": "2383.78",
                "Upper_Bound": "7420.84",
            },
            "19/09/2020": {
                "Forecast_Price": "4908.13",
                "Lower_Bound": "2384.11",
                "Upper_Bound": "7432.16",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4902.38",
                "Lower_Bound": "2451.69",
                "Upper_Bound": "7353.06",
            },
            "30/09/2020": {
                "Forecast_Price": "4916.98",
                "Lower_Bound": "2487.99",
                "Upper_Bound": "7345.97",
            },
            "30/10/2020": {
                "Forecast_Price": "4922.58",
                "Lower_Bound": "2517.12",
                "Upper_Bound": "7328.05",
            },
            "29/11/2020": {
                "Forecast_Price": "4924.83",
                "Lower_Bound": "2537.88",
                "Upper_Bound": "7311.79",
            },
            "29/12/2020": {
                "Forecast_Price": "4922.96",
                "Lower_Bound": "2545.30",
                "Upper_Bound": "7300.62",
            },
            "28/01/2021": {
                "Forecast_Price": "4912.14",
                "Lower_Bound": "2543.75",
                "Upper_Bound": "7280.52",
            },
            "27/02/2021": {
                "Forecast_Price": "4852.38",
                "Lower_Bound": "2477.93",
                "Upper_Bound": "7226.82",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4490.06",
                "Lower_Bound": "3422.23",
                "Upper_Bound": "5557.90",
            },
            "02/08/2020": {
                "Forecast_Price": "4494.36",
                "Lower_Bound": "3812.62",
                "Upper_Bound": "5176.10",
            },
            "03/08/2020": {
                "Forecast_Price": "4495.01",
                "Lower_Bound": "3866.55",
                "Upper_Bound": "5123.47",
            },
            "04/08/2020": {
                "Forecast_Price": "4494.12",
                "Lower_Bound": "3839.48",
                "Upper_Bound": "5148.75",
            },
            "05/08/2020": {
                "Forecast_Price": "4496.25",
                "Lower_Bound": "3257.52",
                "Upper_Bound": "5734.98",
            },
            "06/08/2020": {
                "Forecast_Price": "4494.78",
                "Lower_Bound": "3940.31",
                "Upper_Bound": "5049.25",
            },
            "07/08/2020": {
                "Forecast_Price": "4496.64",
                "Lower_Bound": "3839.70",
                "Upper_Bound": "5153.57",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4490.27",
                "Lower_Bound": "2194.14",
                "Upper_Bound": "6786.39",
            },
            "15/08/2020": {
                "Forecast_Price": "4490.43",
                "Lower_Bound": "2195.08",
                "Upper_Bound": "6785.77",
            },
            "22/08/2020": {
                "Forecast_Price": "4490.85",
                "Lower_Bound": "2196.34",
                "Upper_Bound": "6785.36",
            },
            "29/08/2020": {
                "Forecast_Price": "4489.62",
                "Lower_Bound": "2195.07",
                "Upper_Bound": "6784.17",
            },
            "05/09/2020": {
                "Forecast_Price": "4489.93",
                "Lower_Bound": "2196.22",
                "Upper_Bound": "6783.65",
            },
            "12/09/2020": {
                "Forecast_Price": "4490.09",
                "Lower_Bound": "2197.16",
                "Upper_Bound": "6783.02",
            },
            "19/09/2020": {
                "Forecast_Price": "4490.51",
                "Lower_Bound": "2198.41",
                "Upper_Bound": "6782.62",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4452.33",
                "Lower_Bound": "2160.11",
                "Upper_Bound": "6744.54",
            },
            "30/09/2020": {
                "Forecast_Price": "4384.51",
                "Lower_Bound": "2092.15",
                "Upper_Bound": "6676.87",
            },
            "30/10/2020": {
                "Forecast_Price": "4389.93",
                "Lower_Bound": "2084.60",
                "Upper_Bound": "6695.25",
            },
            "29/11/2020": {
                "Forecast_Price": "4339.67",
                "Lower_Bound": "2034.77",
                "Upper_Bound": "6644.57",
            },
            "29/12/2020": {
                "Forecast_Price": "4306.49",
                "Lower_Bound": "2011.23",
                "Upper_Bound": "6601.75",
            },
            "28/01/2021": {
                "Forecast_Price": "4281.39",
                "Lower_Bound": "2003.19",
                "Upper_Bound": "6559.58",
            },
            "27/02/2021": {
                "Forecast_Price": "4199.40",
                "Lower_Bound": "1949.23",
                "Upper_Bound": "6449.57",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4139.88",
                "Lower_Bound": "3153.31",
                "Upper_Bound": "5126.46",
            },
            "02/08/2020": {
                "Forecast_Price": "4145.68",
                "Lower_Bound": "3395.69",
                "Upper_Bound": "4895.67",
            },
            "03/08/2020": {
                "Forecast_Price": "4152.89",
                "Lower_Bound": "3519.05",
                "Upper_Bound": "4786.74",
            },
            "04/08/2020": {
                "Forecast_Price": "4145.12",
                "Lower_Bound": "3538.19",
                "Upper_Bound": "4752.05",
            },
            "05/08/2020": {
                "Forecast_Price": "4159.34",
                "Lower_Bound": "2867.54",
                "Upper_Bound": "5451.15",
            },
            "06/08/2020": {
                "Forecast_Price": "4158.02",
                "Lower_Bound": "3289.49",
                "Upper_Bound": "5026.56",
            },
            "07/08/2020": {
                "Forecast_Price": "4152.76",
                "Lower_Bound": "3511.82",
                "Upper_Bound": "4793.71",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3608.40",
                "Lower_Bound": "1764.06",
                "Upper_Bound": "5452.74",
            },
            "15/08/2020": {
                "Forecast_Price": "3586.01",
                "Lower_Bound": "1754.33",
                "Upper_Bound": "5417.68",
            },
            "22/08/2020": {
                "Forecast_Price": "3575.64",
                "Lower_Bound": "1748.56",
                "Upper_Bound": "5402.73",
            },
            "29/08/2020": {
                "Forecast_Price": "3574.69",
                "Lower_Bound": "1745.87",
                "Upper_Bound": "5403.52",
            },
            "05/09/2020": {
                "Forecast_Price": "3544.83",
                "Lower_Bound": "1733.69",
                "Upper_Bound": "5355.97",
            },
            "12/09/2020": {
                "Forecast_Price": "3522.43",
                "Lower_Bound": "1723.96",
                "Upper_Bound": "5320.90",
            },
            "19/09/2020": {
                "Forecast_Price": "3512.07",
                "Lower_Bound": "1718.19",
                "Upper_Bound": "5305.95",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3724.71",
                "Lower_Bound": "1814.94",
                "Upper_Bound": "5634.47",
            },
            "30/09/2020": {
                "Forecast_Price": "3831.33",
                "Lower_Bound": "1883.10",
                "Upper_Bound": "5779.55",
            },
            "30/10/2020": {
                "Forecast_Price": "3853.33",
                "Lower_Bound": "1919.81",
                "Upper_Bound": "5786.86",
            },
            "29/11/2020": {
                "Forecast_Price": "3911.09",
                "Lower_Bound": "1945.43",
                "Upper_Bound": "5876.75",
            },
            "29/12/2020": {
                "Forecast_Price": "4061.43",
                "Lower_Bound": "2006.78",
                "Upper_Bound": "6116.07",
            },
            "28/01/2021": {
                "Forecast_Price": "4049.79",
                "Lower_Bound": "2003.89",
                "Upper_Bound": "6095.70",
            },
            "27/02/2021": {
                "Forecast_Price": "3939.90",
                "Lower_Bound": "1927.70",
                "Upper_Bound": "5952.10",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4700.22",
                "Lower_Bound": "3998.86",
                "Upper_Bound": "5401.58",
            },
            "02/08/2020": {
                "Forecast_Price": "4679.54",
                "Lower_Bound": "3938.00",
                "Upper_Bound": "5421.09",
            },
            "03/08/2020": {
                "Forecast_Price": "4709.79",
                "Lower_Bound": "3923.77",
                "Upper_Bound": "5495.81",
            },
            "04/08/2020": {
                "Forecast_Price": "4729.83",
                "Lower_Bound": "3916.41",
                "Upper_Bound": "5543.25",
            },
            "05/08/2020": {
                "Forecast_Price": "4682.81",
                "Lower_Bound": "3994.12",
                "Upper_Bound": "5371.49",
            },
            "06/08/2020": {
                "Forecast_Price": "4690.42",
                "Lower_Bound": "3932.91",
                "Upper_Bound": "5447.93",
            },
            "07/08/2020": {
                "Forecast_Price": "4669.10",
                "Lower_Bound": "3652.18",
                "Upper_Bound": "5686.01",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5430.21",
                "Lower_Bound": "2652.22",
                "Upper_Bound": "8208.21",
            },
            "15/08/2020": {
                "Forecast_Price": "5432.28",
                "Lower_Bound": "2657.01",
                "Upper_Bound": "8207.55",
            },
            "22/08/2020": {
                "Forecast_Price": "5431.86",
                "Lower_Bound": "2656.53",
                "Upper_Bound": "8207.20",
            },
            "29/08/2020": {
                "Forecast_Price": "5429.53",
                "Lower_Bound": "2652.68",
                "Upper_Bound": "8206.37",
            },
            "05/09/2020": {
                "Forecast_Price": "5441.30",
                "Lower_Bound": "2661.67",
                "Upper_Bound": "8220.93",
            },
            "12/09/2020": {
                "Forecast_Price": "5444.00",
                "Lower_Bound": "2666.66",
                "Upper_Bound": "8221.33",
            },
            "19/09/2020": {
                "Forecast_Price": "5443.69",
                "Lower_Bound": "2666.22",
                "Upper_Bound": "8221.15",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5598.58",
                "Lower_Bound": "2700.06",
                "Upper_Bound": "8497.10",
            },
            "30/09/2020": {
                "Forecast_Price": "5716.33",
                "Lower_Bound": "2736.49",
                "Upper_Bound": "8696.16",
            },
            "30/10/2020": {
                "Forecast_Price": "5770.37",
                "Lower_Bound": "2751.96",
                "Upper_Bound": "8788.78",
            },
            "29/11/2020": {
                "Forecast_Price": "5855.96",
                "Lower_Bound": "2777.90",
                "Upper_Bound": "8934.02",
            },
            "29/12/2020": {
                "Forecast_Price": "5993.95",
                "Lower_Bound": "2821.00",
                "Upper_Bound": "9166.90",
            },
            "28/01/2021": {
                "Forecast_Price": "6244.18",
                "Lower_Bound": "2898.78",
                "Upper_Bound": "9589.57",
            },
            "27/02/2021": {
                "Forecast_Price": "6348.70",
                "Lower_Bound": "2932.17",
                "Upper_Bound": "9765.22",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5645.93",
                "Lower_Bound": "4647.40",
                "Upper_Bound": "6644.45",
            },
            "02/08/2020": {
                "Forecast_Price": "5649.55",
                "Lower_Bound": "4682.83",
                "Upper_Bound": "6616.27",
            },
            "03/08/2020": {
                "Forecast_Price": "5647.33",
                "Lower_Bound": "4641.99",
                "Upper_Bound": "6652.68",
            },
            "04/08/2020": {
                "Forecast_Price": "5695.56",
                "Lower_Bound": "4469.58",
                "Upper_Bound": "6921.54",
            },
            "05/08/2020": {
                "Forecast_Price": "5625.43",
                "Lower_Bound": "4769.54",
                "Upper_Bound": "6481.31",
            },
            "06/08/2020": {
                "Forecast_Price": "5634.89",
                "Lower_Bound": "4210.50",
                "Upper_Bound": "7059.27",
            },
            "07/08/2020": {
                "Forecast_Price": "5652.18",
                "Lower_Bound": "4599.15",
                "Upper_Bound": "6705.21",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5319.79",
                "Lower_Bound": "2594.18",
                "Upper_Bound": "8045.39",
            },
            "15/08/2020": {
                "Forecast_Price": "5324.96",
                "Lower_Bound": "2594.73",
                "Upper_Bound": "8055.19",
            },
            "22/08/2020": {
                "Forecast_Price": "5329.19",
                "Lower_Bound": "2595.03",
                "Upper_Bound": "8063.34",
            },
            "29/08/2020": {
                "Forecast_Price": "5319.12",
                "Lower_Bound": "2590.52",
                "Upper_Bound": "8047.73",
            },
            "05/09/2020": {
                "Forecast_Price": "5337.05",
                "Lower_Bound": "2595.33",
                "Upper_Bound": "8078.77",
            },
            "12/09/2020": {
                "Forecast_Price": "5342.23",
                "Lower_Bound": "2595.88",
                "Upper_Bound": "8088.57",
            },
            "19/09/2020": {
                "Forecast_Price": "5346.45",
                "Lower_Bound": "2596.18",
                "Upper_Bound": "8096.72",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5295.72",
                "Lower_Bound": "2589.85",
                "Upper_Bound": "8001.60",
            },
            "30/09/2020": {
                "Forecast_Price": "5295.04",
                "Lower_Bound": "2591.43",
                "Upper_Bound": "7998.66",
            },
            "30/10/2020": {
                "Forecast_Price": "5319.27",
                "Lower_Bound": "2614.98",
                "Upper_Bound": "8023.57",
            },
            "29/11/2020": {
                "Forecast_Price": "5310.68",
                "Lower_Bound": "2605.95",
                "Upper_Bound": "8015.41",
            },
            "29/12/2020": {
                "Forecast_Price": "5304.74",
                "Lower_Bound": "2596.95",
                "Upper_Bound": "8012.53",
            },
            "28/01/2021": {
                "Forecast_Price": "5303.25",
                "Lower_Bound": "2597.96",
                "Upper_Bound": "8008.53",
            },
            "27/02/2021": {
                "Forecast_Price": "5210.05",
                "Lower_Bound": "2525.68",
                "Upper_Bound": "7894.42",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5077.42",
                "Lower_Bound": "4401.38",
                "Upper_Bound": "5753.47",
            },
            "02/08/2020": {
                "Forecast_Price": "5081.89",
                "Lower_Bound": "4398.22",
                "Upper_Bound": "5765.56",
            },
            "03/08/2020": {
                "Forecast_Price": "5080.22",
                "Lower_Bound": "4235.12",
                "Upper_Bound": "5925.31",
            },
            "04/08/2020": {
                "Forecast_Price": "5085.82",
                "Lower_Bound": "4069.61",
                "Upper_Bound": "6102.04",
            },
            "05/08/2020": {
                "Forecast_Price": "5082.74",
                "Lower_Bound": "4099.27",
                "Upper_Bound": "6066.20",
            },
            "06/08/2020": {
                "Forecast_Price": "5092.47",
                "Lower_Bound": "4443.41",
                "Upper_Bound": "5741.52",
            },
            "07/08/2020": {
                "Forecast_Price": "5082.64",
                "Lower_Bound": "4224.78",
                "Upper_Bound": "5940.51",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5202.32",
                "Lower_Bound": "2541.74",
                "Upper_Bound": "7862.90",
            },
            "15/08/2020": {
                "Forecast_Price": "5213.70",
                "Lower_Bound": "2547.58",
                "Upper_Bound": "7879.82",
            },
            "22/08/2020": {
                "Forecast_Price": "5217.56",
                "Lower_Bound": "2548.83",
                "Upper_Bound": "7886.30",
            },
            "29/08/2020": {
                "Forecast_Price": "5199.38",
                "Lower_Bound": "2543.24",
                "Upper_Bound": "7855.52",
            },
            "05/09/2020": {
                "Forecast_Price": "5220.19",
                "Lower_Bound": "2550.92",
                "Upper_Bound": "7889.46",
            },
            "12/09/2020": {
                "Forecast_Price": "5231.64",
                "Lower_Bound": "2556.87",
                "Upper_Bound": "7906.41",
            },
            "19/09/2020": {
                "Forecast_Price": "5235.49",
                "Lower_Bound": "2558.10",
                "Upper_Bound": "7912.88",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5235.70",
                "Lower_Bound": "2553.83",
                "Upper_Bound": "7917.57",
            },
            "30/09/2020": {
                "Forecast_Price": "5289.81",
                "Lower_Bound": "2587.63",
                "Upper_Bound": "7991.99",
            },
            "30/10/2020": {
                "Forecast_Price": "5304.60",
                "Lower_Bound": "2615.22",
                "Upper_Bound": "7993.98",
            },
            "29/11/2020": {
                "Forecast_Price": "5353.56",
                "Lower_Bound": "2643.68",
                "Upper_Bound": "8063.44",
            },
            "29/12/2020": {
                "Forecast_Price": "5488.49",
                "Lower_Bound": "2707.48",
                "Upper_Bound": "8269.49",
            },
            "28/01/2021": {
                "Forecast_Price": "5519.60",
                "Lower_Bound": "2735.91",
                "Upper_Bound": "8303.29",
            },
            "27/02/2021": {
                "Forecast_Price": "5477.95",
                "Lower_Bound": "2719.73",
                "Upper_Bound": "8236.17",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4487.30",
                "Lower_Bound": "3286.21",
                "Upper_Bound": "5688.39",
            },
            "02/08/2020": {
                "Forecast_Price": "4498.14",
                "Lower_Bound": "3636.79",
                "Upper_Bound": "5359.49",
            },
            "03/08/2020": {
                "Forecast_Price": "4488.57",
                "Lower_Bound": "3799.02",
                "Upper_Bound": "5178.12",
            },
            "04/08/2020": {
                "Forecast_Price": "4505.21",
                "Lower_Bound": "3681.64",
                "Upper_Bound": "5328.79",
            },
            "05/08/2020": {
                "Forecast_Price": "4504.49",
                "Lower_Bound": "3642.65",
                "Upper_Bound": "5366.33",
            },
            "06/08/2020": {
                "Forecast_Price": "4498.07",
                "Lower_Bound": "3628.15",
                "Upper_Bound": "5367.99",
            },
            "07/08/2020": {
                "Forecast_Price": "4504.49",
                "Lower_Bound": "3938.19",
                "Upper_Bound": "5070.78",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4506.70",
                "Lower_Bound": "2204.72",
                "Upper_Bound": "6808.67",
            },
            "15/08/2020": {
                "Forecast_Price": "4501.65",
                "Lower_Bound": "2202.56",
                "Upper_Bound": "6800.74",
            },
            "22/08/2020": {
                "Forecast_Price": "4498.42",
                "Lower_Bound": "2202.97",
                "Upper_Bound": "6793.86",
            },
            "29/08/2020": {
                "Forecast_Price": "4498.28",
                "Lower_Bound": "2207.43",
                "Upper_Bound": "6789.13",
            },
            "05/09/2020": {
                "Forecast_Price": "4493.03",
                "Lower_Bound": "2206.93",
                "Upper_Bound": "6779.14",
            },
            "12/09/2020": {
                "Forecast_Price": "4486.67",
                "Lower_Bound": "2204.33",
                "Upper_Bound": "6769.00",
            },
            "19/09/2020": {
                "Forecast_Price": "4481.86",
                "Lower_Bound": "2204.23",
                "Upper_Bound": "6759.48",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4446.34",
                "Lower_Bound": "2154.44",
                "Upper_Bound": "6738.25",
            },
            "30/09/2020": {
                "Forecast_Price": "4362.99",
                "Lower_Bound": "2046.52",
                "Upper_Bound": "6679.45",
            },
            "30/10/2020": {
                "Forecast_Price": "4319.73",
                "Lower_Bound": "2004.84",
                "Upper_Bound": "6634.63",
            },
            "29/11/2020": {
                "Forecast_Price": "4283.49",
                "Lower_Bound": "1974.07",
                "Upper_Bound": "6592.91",
            },
            "29/12/2020": {
                "Forecast_Price": "4260.23",
                "Lower_Bound": "1964.24",
                "Upper_Bound": "6556.22",
            },
            "28/01/2021": {
                "Forecast_Price": "4247.18",
                "Lower_Bound": "1958.26",
                "Upper_Bound": "6536.09",
            },
            "27/02/2021": {
                "Forecast_Price": "4201.35",
                "Lower_Bound": "1918.91",
                "Upper_Bound": "6483.79",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4958.55",
                "Lower_Bound": "3150.87",
                "Upper_Bound": "6766.22",
            },
            "02/08/2020": {
                "Forecast_Price": "4962.23",
                "Lower_Bound": "4082.78",
                "Upper_Bound": "5841.67",
            },
            "03/08/2020": {
                "Forecast_Price": "4954.35",
                "Lower_Bound": "3973.81",
                "Upper_Bound": "5934.89",
            },
            "04/08/2020": {
                "Forecast_Price": "4957.05",
                "Lower_Bound": "4120.74",
                "Upper_Bound": "5793.36",
            },
            "05/08/2020": {
                "Forecast_Price": "4952.43",
                "Lower_Bound": "4057.61",
                "Upper_Bound": "5847.25",
            },
            "06/08/2020": {
                "Forecast_Price": "4960.91",
                "Lower_Bound": "4099.02",
                "Upper_Bound": "5822.79",
            },
            "07/08/2020": {
                "Forecast_Price": "4972.18",
                "Lower_Bound": "3992.73",
                "Upper_Bound": "5951.64",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4906.47",
                "Lower_Bound": "2396.08",
                "Upper_Bound": "7416.86",
            },
            "15/08/2020": {
                "Forecast_Price": "4907.97",
                "Lower_Bound": "2395.66",
                "Upper_Bound": "7420.29",
            },
            "22/08/2020": {
                "Forecast_Price": "4909.28",
                "Lower_Bound": "2395.37",
                "Upper_Bound": "7423.19",
            },
            "29/08/2020": {
                "Forecast_Price": "4920.50",
                "Lower_Bound": "2397.97",
                "Upper_Bound": "7443.02",
            },
            "05/09/2020": {
                "Forecast_Price": "4922.03",
                "Lower_Bound": "2398.93",
                "Upper_Bound": "7445.13",
            },
            "12/09/2020": {
                "Forecast_Price": "4923.38",
                "Lower_Bound": "2398.24",
                "Upper_Bound": "7448.51",
            },
            "19/09/2020": {
                "Forecast_Price": "4924.49",
                "Lower_Bound": "2397.64",
                "Upper_Bound": "7451.35",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4905.91",
                "Lower_Bound": "2405.32",
                "Upper_Bound": "7406.51",
            },
            "30/09/2020": {
                "Forecast_Price": "4909.35",
                "Lower_Bound": "2427.79",
                "Upper_Bound": "7390.90",
            },
            "30/10/2020": {
                "Forecast_Price": "4903.95",
                "Lower_Bound": "2446.07",
                "Upper_Bound": "7361.84",
            },
            "29/11/2020": {
                "Forecast_Price": "4899.92",
                "Lower_Bound": "2461.70",
                "Upper_Bound": "7338.14",
            },
            "29/12/2020": {
                "Forecast_Price": "4891.42",
                "Lower_Bound": "2471.49",
                "Upper_Bound": "7311.36",
            },
            "28/01/2021": {
                "Forecast_Price": "4897.45",
                "Lower_Bound": "2503.80",
                "Upper_Bound": "7291.10",
            },
            "27/02/2021": {
                "Forecast_Price": "4893.91",
                "Lower_Bound": "2507.50",
                "Upper_Bound": "7280.32",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4553.94",
                "Lower_Bound": "3818.05",
                "Upper_Bound": "5289.83",
            },
            "02/08/2020": {
                "Forecast_Price": "4550.03",
                "Lower_Bound": "3673.82",
                "Upper_Bound": "5426.24",
            },
            "03/08/2020": {
                "Forecast_Price": "4557.43",
                "Lower_Bound": "3827.73",
                "Upper_Bound": "5287.12",
            },
            "04/08/2020": {
                "Forecast_Price": "4550.42",
                "Lower_Bound": "3720.31",
                "Upper_Bound": "5380.54",
            },
            "05/08/2020": {
                "Forecast_Price": "4553.40",
                "Lower_Bound": "3822.35",
                "Upper_Bound": "5284.46",
            },
            "06/08/2020": {
                "Forecast_Price": "4572.59",
                "Lower_Bound": "3812.78",
                "Upper_Bound": "5332.41",
            },
            "07/08/2020": {
                "Forecast_Price": "4571.88",
                "Lower_Bound": "3876.15",
                "Upper_Bound": "5267.61",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4665.12",
                "Lower_Bound": "2280.50",
                "Upper_Bound": "7049.75",
            },
            "15/08/2020": {
                "Forecast_Price": "4703.83",
                "Lower_Bound": "2293.31",
                "Upper_Bound": "7114.36",
            },
            "22/08/2020": {
                "Forecast_Price": "4737.25",
                "Lower_Bound": "2304.03",
                "Upper_Bound": "7170.46",
            },
            "29/08/2020": {
                "Forecast_Price": "4704.02",
                "Lower_Bound": "2293.61",
                "Upper_Bound": "7114.43",
            },
            "05/09/2020": {
                "Forecast_Price": "4716.60",
                "Lower_Bound": "2298.19",
                "Upper_Bound": "7135.01",
            },
            "12/09/2020": {
                "Forecast_Price": "4755.21",
                "Lower_Bound": "2310.83",
                "Upper_Bound": "7199.58",
            },
            "19/09/2020": {
                "Forecast_Price": "4788.65",
                "Lower_Bound": "2321.61",
                "Upper_Bound": "7255.70",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4670.32",
                "Lower_Bound": "2265.34",
                "Upper_Bound": "7075.30",
            },
            "30/09/2020": {
                "Forecast_Price": "4680.52",
                "Lower_Bound": "2261.16",
                "Upper_Bound": "7099.88",
            },
            "30/10/2020": {
                "Forecast_Price": "4692.43",
                "Lower_Bound": "2256.64",
                "Upper_Bound": "7128.22",
            },
            "29/11/2020": {
                "Forecast_Price": "4680.13",
                "Lower_Bound": "2237.25",
                "Upper_Bound": "7123.00",
            },
            "29/12/2020": {
                "Forecast_Price": "4658.66",
                "Lower_Bound": "2220.30",
                "Upper_Bound": "7097.02",
            },
            "28/01/2021": {
                "Forecast_Price": "4650.40",
                "Lower_Bound": "2214.26",
                "Upper_Bound": "7086.55",
            },
            "27/02/2021": {
                "Forecast_Price": "4631.72",
                "Lower_Bound": "2187.53",
                "Upper_Bound": "7075.92",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4579.24",
                "Lower_Bound": "3594.47",
                "Upper_Bound": "5564.01",
            },
            "02/08/2020": {
                "Forecast_Price": "4566.48",
                "Lower_Bound": "3700.81",
                "Upper_Bound": "5432.15",
            },
            "03/08/2020": {
                "Forecast_Price": "4544.57",
                "Lower_Bound": "3758.89",
                "Upper_Bound": "5330.24",
            },
            "04/08/2020": {
                "Forecast_Price": "4530.16",
                "Lower_Bound": "3812.98",
                "Upper_Bound": "5247.34",
            },
            "05/08/2020": {
                "Forecast_Price": "4561.42",
                "Lower_Bound": "3781.08",
                "Upper_Bound": "5341.77",
            },
            "06/08/2020": {
                "Forecast_Price": "4494.11",
                "Lower_Bound": "3801.17",
                "Upper_Bound": "5187.05",
            },
            "07/08/2020": {
                "Forecast_Price": "4520.78",
                "Lower_Bound": "3944.87",
                "Upper_Bound": "5096.69",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4346.78",
                "Lower_Bound": "2119.97",
                "Upper_Bound": "6573.59",
            },
            "15/08/2020": {
                "Forecast_Price": "4359.93",
                "Lower_Bound": "2114.97",
                "Upper_Bound": "6604.88",
            },
            "22/08/2020": {
                "Forecast_Price": "4373.83",
                "Lower_Bound": "2125.16",
                "Upper_Bound": "6622.50",
            },
            "29/08/2020": {
                "Forecast_Price": "4386.64",
                "Lower_Bound": "2143.83",
                "Upper_Bound": "6629.45",
            },
            "05/09/2020": {
                "Forecast_Price": "4355.02",
                "Lower_Bound": "2118.13",
                "Upper_Bound": "6591.91",
            },
            "12/09/2020": {
                "Forecast_Price": "4368.16",
                "Lower_Bound": "2113.13",
                "Upper_Bound": "6623.20",
            },
            "19/09/2020": {
                "Forecast_Price": "4382.07",
                "Lower_Bound": "2123.32",
                "Upper_Bound": "6640.81",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4250.73",
                "Lower_Bound": "2014.50",
                "Upper_Bound": "6486.95",
            },
            "30/09/2020": {
                "Forecast_Price": "4218.48",
                "Lower_Bound": "1964.62",
                "Upper_Bound": "6472.34",
            },
            "30/10/2020": {
                "Forecast_Price": "4128.44",
                "Lower_Bound": "1890.57",
                "Upper_Bound": "6366.32",
            },
            "29/11/2020": {
                "Forecast_Price": "4213.88",
                "Lower_Bound": "1914.87",
                "Upper_Bound": "6512.88",
            },
            "29/12/2020": {
                "Forecast_Price": "4331.51",
                "Lower_Bound": "1954.87",
                "Upper_Bound": "6708.15",
            },
            "28/01/2021": {
                "Forecast_Price": "4333.12",
                "Lower_Bound": "1960.62",
                "Upper_Bound": "6705.63",
            },
            "27/02/2021": {
                "Forecast_Price": "4260.53",
                "Lower_Bound": "1878.54",
                "Upper_Bound": "6642.52",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5407.91",
                "Lower_Bound": "4553.96",
                "Upper_Bound": "6261.86",
            },
            "02/08/2020": {
                "Forecast_Price": "5411.06",
                "Lower_Bound": "4579.71",
                "Upper_Bound": "6242.41",
            },
            "03/08/2020": {
                "Forecast_Price": "5412.55",
                "Lower_Bound": "4825.21",
                "Upper_Bound": "5999.90",
            },
            "04/08/2020": {
                "Forecast_Price": "5424.32",
                "Lower_Bound": "4774.14",
                "Upper_Bound": "6074.51",
            },
            "05/08/2020": {
                "Forecast_Price": "5443.26",
                "Lower_Bound": "4756.84",
                "Upper_Bound": "6129.68",
            },
            "06/08/2020": {
                "Forecast_Price": "5413.95",
                "Lower_Bound": "4673.80",
                "Upper_Bound": "6154.10",
            },
            "07/08/2020": {
                "Forecast_Price": "5415.45",
                "Lower_Bound": "4824.08",
                "Upper_Bound": "6006.83",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5385.98",
                "Lower_Bound": "2611.59",
                "Upper_Bound": "8160.37",
            },
            "15/08/2020": {
                "Forecast_Price": "5388.61",
                "Lower_Bound": "2624.13",
                "Upper_Bound": "8153.08",
            },
            "22/08/2020": {
                "Forecast_Price": "5400.44",
                "Lower_Bound": "2640.25",
                "Upper_Bound": "8160.63",
            },
            "29/08/2020": {
                "Forecast_Price": "5374.15",
                "Lower_Bound": "2608.39",
                "Upper_Bound": "8139.90",
            },
            "05/09/2020": {
                "Forecast_Price": "5370.33",
                "Lower_Bound": "2604.93",
                "Upper_Bound": "8135.73",
            },
            "12/09/2020": {
                "Forecast_Price": "5372.99",
                "Lower_Bound": "2617.48",
                "Upper_Bound": "8128.50",
            },
            "19/09/2020": {
                "Forecast_Price": "5384.74",
                "Lower_Bound": "2633.58",
                "Upper_Bound": "8135.91",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5655.01",
                "Lower_Bound": "2746.83",
                "Upper_Bound": "8563.20",
            },
            "30/09/2020": {
                "Forecast_Price": "5686.97",
                "Lower_Bound": "2795.93",
                "Upper_Bound": "8578.01",
            },
            "30/10/2020": {
                "Forecast_Price": "5664.52",
                "Lower_Bound": "2806.14",
                "Upper_Bound": "8522.89",
            },
            "29/11/2020": {
                "Forecast_Price": "5650.64",
                "Lower_Bound": "2783.82",
                "Upper_Bound": "8517.46",
            },
            "29/12/2020": {
                "Forecast_Price": "5689.82",
                "Lower_Bound": "2762.65",
                "Upper_Bound": "8616.98",
            },
            "28/01/2021": {
                "Forecast_Price": "5731.99",
                "Lower_Bound": "2765.35",
                "Upper_Bound": "8698.63",
            },
            "27/02/2021": {
                "Forecast_Price": "5721.16",
                "Lower_Bound": "2746.55",
                "Upper_Bound": "8695.77",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4145.75",
                "Lower_Bound": "3331.42",
                "Upper_Bound": "4960.07",
            },
            "02/08/2020": {
                "Forecast_Price": "4147.33",
                "Lower_Bound": "3231.56",
                "Upper_Bound": "5063.10",
            },
            "03/08/2020": {
                "Forecast_Price": "4160.17",
                "Lower_Bound": "3366.29",
                "Upper_Bound": "4954.06",
            },
            "04/08/2020": {
                "Forecast_Price": "4140.40",
                "Lower_Bound": "3148.05",
                "Upper_Bound": "5132.76",
            },
            "05/08/2020": {
                "Forecast_Price": "4193.51",
                "Lower_Bound": "3242.70",
                "Upper_Bound": "5144.32",
            },
            "06/08/2020": {
                "Forecast_Price": "4224.32",
                "Lower_Bound": "3398.34",
                "Upper_Bound": "5050.30",
            },
            "07/08/2020": {
                "Forecast_Price": "4259.52",
                "Lower_Bound": "3518.54",
                "Upper_Bound": "5000.51",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4403.13",
                "Lower_Bound": "2150.14",
                "Upper_Bound": "6656.12",
            },
            "15/08/2020": {
                "Forecast_Price": "4398.36",
                "Lower_Bound": "2148.88",
                "Upper_Bound": "6647.85",
            },
            "22/08/2020": {
                "Forecast_Price": "4396.75",
                "Lower_Bound": "2148.66",
                "Upper_Bound": "6644.84",
            },
            "29/08/2020": {
                "Forecast_Price": "4405.93",
                "Lower_Bound": "2151.98",
                "Upper_Bound": "6659.88",
            },
            "05/09/2020": {
                "Forecast_Price": "4406.56",
                "Lower_Bound": "2152.49",
                "Upper_Bound": "6660.63",
            },
            "12/09/2020": {
                "Forecast_Price": "4401.79",
                "Lower_Bound": "2151.23",
                "Upper_Bound": "6652.36",
            },
            "19/09/2020": {
                "Forecast_Price": "4400.18",
                "Lower_Bound": "2151.01",
                "Upper_Bound": "6649.35",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4398.91",
                "Lower_Bound": "2114.79",
                "Upper_Bound": "6683.04",
            },
            "30/09/2020": {
                "Forecast_Price": "4424.13",
                "Lower_Bound": "2076.25",
                "Upper_Bound": "6772.02",
            },
            "30/10/2020": {
                "Forecast_Price": "4387.12",
                "Lower_Bound": "2005.20",
                "Upper_Bound": "6769.03",
            },
            "29/11/2020": {
                "Forecast_Price": "4356.79",
                "Lower_Bound": "1933.41",
                "Upper_Bound": "6780.17",
            },
            "29/12/2020": {
                "Forecast_Price": "4393.99",
                "Lower_Bound": "1888.65",
                "Upper_Bound": "6899.33",
            },
            "28/01/2021": {
                "Forecast_Price": "4408.04",
                "Lower_Bound": "1863.41",
                "Upper_Bound": "6952.67",
            },
            "27/02/2021": {
                "Forecast_Price": "4434.82",
                "Lower_Bound": "1811.29",
                "Upper_Bound": "7058.35",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5035.32",
                "Lower_Bound": "4370.32",
                "Upper_Bound": "5700.32",
            },
            "02/08/2020": {
                "Forecast_Price": "5020.02",
                "Lower_Bound": "4138.78",
                "Upper_Bound": "5901.25",
            },
            "03/08/2020": {
                "Forecast_Price": "4804.22",
                "Lower_Bound": "4175.55",
                "Upper_Bound": "5432.89",
            },
            "04/08/2020": {
                "Forecast_Price": "4488.32",
                "Lower_Bound": "3652.41",
                "Upper_Bound": "5324.22",
            },
            "05/08/2020": {
                "Forecast_Price": "4719.91",
                "Lower_Bound": "3914.80",
                "Upper_Bound": "5525.01",
            },
            "06/08/2020": {
                "Forecast_Price": "4887.87",
                "Lower_Bound": "3832.31",
                "Upper_Bound": "5943.43",
            },
            "07/08/2020": {
                "Forecast_Price": "4821.50",
                "Lower_Bound": "4307.09",
                "Upper_Bound": "5335.92",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5390.87",
                "Lower_Bound": "2629.97",
                "Upper_Bound": "8151.76",
            },
            "15/08/2020": {
                "Forecast_Price": "5386.74",
                "Lower_Bound": "2624.44",
                "Upper_Bound": "8149.03",
            },
            "22/08/2020": {
                "Forecast_Price": "5385.39",
                "Lower_Bound": "2623.58",
                "Upper_Bound": "8147.21",
            },
            "29/08/2020": {
                "Forecast_Price": "5387.99",
                "Lower_Bound": "2629.30",
                "Upper_Bound": "8146.68",
            },
            "05/09/2020": {
                "Forecast_Price": "5382.36",
                "Lower_Bound": "2621.28",
                "Upper_Bound": "8143.45",
            },
            "12/09/2020": {
                "Forecast_Price": "5378.23",
                "Lower_Bound": "2615.75",
                "Upper_Bound": "8140.71",
            },
            "19/09/2020": {
                "Forecast_Price": "5376.89",
                "Lower_Bound": "2614.89",
                "Upper_Bound": "8138.89",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5382.76",
                "Lower_Bound": "2592.36",
                "Upper_Bound": "8173.16",
            },
            "30/09/2020": {
                "Forecast_Price": "5539.68",
                "Lower_Bound": "2650.48",
                "Upper_Bound": "8428.87",
            },
            "30/10/2020": {
                "Forecast_Price": "5555.69",
                "Lower_Bound": "2657.40",
                "Upper_Bound": "8453.98",
            },
            "29/11/2020": {
                "Forecast_Price": "5656.45",
                "Lower_Bound": "2710.30",
                "Upper_Bound": "8602.61",
            },
            "29/12/2020": {
                "Forecast_Price": "5807.44",
                "Lower_Bound": "2775.32",
                "Upper_Bound": "8839.55",
            },
            "28/01/2021": {
                "Forecast_Price": "5880.28",
                "Lower_Bound": "2820.01",
                "Upper_Bound": "8940.55",
            },
            "27/02/2021": {
                "Forecast_Price": "5848.46",
                "Lower_Bound": "2812.65",
                "Upper_Bound": "8884.28",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4974.78",
                "Lower_Bound": "4118.26",
                "Upper_Bound": "5831.30",
            },
            "02/08/2020": {
                "Forecast_Price": "5012.29",
                "Lower_Bound": "4304.05",
                "Upper_Bound": "5720.53",
            },
            "03/08/2020": {
                "Forecast_Price": "4992.22",
                "Lower_Bound": "4226.91",
                "Upper_Bound": "5757.52",
            },
            "04/08/2020": {
                "Forecast_Price": "4975.59",
                "Lower_Bound": "4113.79",
                "Upper_Bound": "5837.40",
            },
            "05/08/2020": {
                "Forecast_Price": "4954.31",
                "Lower_Bound": "4125.10",
                "Upper_Bound": "5783.53",
            },
            "06/08/2020": {
                "Forecast_Price": "5002.93",
                "Lower_Bound": "4237.26",
                "Upper_Bound": "5768.61",
            },
            "07/08/2020": {
                "Forecast_Price": "4978.53",
                "Lower_Bound": "4063.46",
                "Upper_Bound": "5893.60",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4985.15",
                "Lower_Bound": "2434.73",
                "Upper_Bound": "7535.57",
            },
            "15/08/2020": {
                "Forecast_Price": "4990.64",
                "Lower_Bound": "2436.26",
                "Upper_Bound": "7545.02",
            },
            "22/08/2020": {
                "Forecast_Price": "4997.06",
                "Lower_Bound": "2439.35",
                "Upper_Bound": "7554.76",
            },
            "29/08/2020": {
                "Forecast_Price": "5004.55",
                "Lower_Bound": "2444.23",
                "Upper_Bound": "7564.87",
            },
            "05/09/2020": {
                "Forecast_Price": "5010.49",
                "Lower_Bound": "2446.52",
                "Upper_Bound": "7574.46",
            },
            "12/09/2020": {
                "Forecast_Price": "5015.98",
                "Lower_Bound": "2448.06",
                "Upper_Bound": "7583.90",
            },
            "19/09/2020": {
                "Forecast_Price": "5022.40",
                "Lower_Bound": "2451.15",
                "Upper_Bound": "7593.65",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4999.75",
                "Lower_Bound": "2402.42",
                "Upper_Bound": "7597.09",
            },
            "30/09/2020": {
                "Forecast_Price": "5087.07",
                "Lower_Bound": "2419.80",
                "Upper_Bound": "7754.34",
            },
            "30/10/2020": {
                "Forecast_Price": "5093.45",
                "Lower_Bound": "2431.55",
                "Upper_Bound": "7755.35",
            },
            "29/11/2020": {
                "Forecast_Price": "5178.06",
                "Lower_Bound": "2486.17",
                "Upper_Bound": "7869.95",
            },
            "29/12/2020": {
                "Forecast_Price": "5387.11",
                "Lower_Bound": "2588.43",
                "Upper_Bound": "8185.80",
            },
            "28/01/2021": {
                "Forecast_Price": "5467.13",
                "Lower_Bound": "2650.72",
                "Upper_Bound": "8283.54",
            },
            "27/02/2021": {
                "Forecast_Price": "5488.53",
                "Lower_Bound": "2662.94",
                "Upper_Bound": "8314.12",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5303.97",
                "Lower_Bound": "4386.80",
                "Upper_Bound": "6221.14",
            },
            "02/08/2020": {
                "Forecast_Price": "5305.41",
                "Lower_Bound": "4495.53",
                "Upper_Bound": "6115.29",
            },
            "03/08/2020": {
                "Forecast_Price": "5307.94",
                "Lower_Bound": "4435.63",
                "Upper_Bound": "6180.25",
            },
            "04/08/2020": {
                "Forecast_Price": "5307.14",
                "Lower_Bound": "4433.72",
                "Upper_Bound": "6180.56",
            },
            "05/08/2020": {
                "Forecast_Price": "5299.23",
                "Lower_Bound": "4311.95",
                "Upper_Bound": "6286.51",
            },
            "06/08/2020": {
                "Forecast_Price": "5301.48",
                "Lower_Bound": "4363.07",
                "Upper_Bound": "6239.89",
            },
            "07/08/2020": {
                "Forecast_Price": "5288.77",
                "Lower_Bound": "4096.41",
                "Upper_Bound": "6481.13",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5291.70",
                "Lower_Bound": "2577.79",
                "Upper_Bound": "8005.60",
            },
            "15/08/2020": {
                "Forecast_Price": "5287.78",
                "Lower_Bound": "2575.57",
                "Upper_Bound": "7999.99",
            },
            "22/08/2020": {
                "Forecast_Price": "5286.54",
                "Lower_Bound": "2577.82",
                "Upper_Bound": "7995.26",
            },
            "29/08/2020": {
                "Forecast_Price": "5281.45",
                "Lower_Bound": "2573.61",
                "Upper_Bound": "7989.29",
            },
            "05/09/2020": {
                "Forecast_Price": "5273.14",
                "Lower_Bound": "2564.16",
                "Upper_Bound": "7982.11",
            },
            "12/09/2020": {
                "Forecast_Price": "5269.14",
                "Lower_Bound": "2561.92",
                "Upper_Bound": "7976.36",
            },
            "19/09/2020": {
                "Forecast_Price": "5267.82",
                "Lower_Bound": "2564.14",
                "Upper_Bound": "7971.51",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5278.72",
                "Lower_Bound": "2568.03",
                "Upper_Bound": "7989.41",
            },
            "30/09/2020": {
                "Forecast_Price": "5258.54",
                "Lower_Bound": "2559.64",
                "Upper_Bound": "7957.44",
            },
            "30/10/2020": {
                "Forecast_Price": "5230.43",
                "Lower_Bound": "2548.79",
                "Upper_Bound": "7912.07",
            },
            "29/11/2020": {
                "Forecast_Price": "5218.90",
                "Lower_Bound": "2544.90",
                "Upper_Bound": "7892.90",
            },
            "29/12/2020": {
                "Forecast_Price": "5236.92",
                "Lower_Bound": "2564.02",
                "Upper_Bound": "7909.82",
            },
            "28/01/2021": {
                "Forecast_Price": "5237.07",
                "Lower_Bound": "2586.96",
                "Upper_Bound": "7887.17",
            },
            "27/02/2021": {
                "Forecast_Price": "5221.79",
                "Lower_Bound": "2603.04",
                "Upper_Bound": "7840.54",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5361.58",
                "Lower_Bound": "4573.03",
                "Upper_Bound": "6150.12",
            },
            "02/08/2020": {
                "Forecast_Price": "5349.88",
                "Lower_Bound": "4585.84",
                "Upper_Bound": "6113.91",
            },
            "03/08/2020": {
                "Forecast_Price": "5313.43",
                "Lower_Bound": "4455.01",
                "Upper_Bound": "6171.85",
            },
            "04/08/2020": {
                "Forecast_Price": "5346.90",
                "Lower_Bound": "4362.23",
                "Upper_Bound": "6331.58",
            },
            "05/08/2020": {
                "Forecast_Price": "5354.43",
                "Lower_Bound": "4475.61",
                "Upper_Bound": "6233.24",
            },
            "06/08/2020": {
                "Forecast_Price": "5390.24",
                "Lower_Bound": "4314.86",
                "Upper_Bound": "6465.61",
            },
            "07/08/2020": {
                "Forecast_Price": "5379.48",
                "Lower_Bound": "4507.90",
                "Upper_Bound": "6251.07",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4365.78",
                "Lower_Bound": "2129.84",
                "Upper_Bound": "6601.71",
            },
            "15/08/2020": {
                "Forecast_Price": "4409.28",
                "Lower_Bound": "2203.91",
                "Upper_Bound": "6614.64",
            },
            "22/08/2020": {
                "Forecast_Price": "4396.51",
                "Lower_Bound": "2187.52",
                "Upper_Bound": "6605.51",
            },
            "29/08/2020": {
                "Forecast_Price": "4402.21",
                "Lower_Bound": "2196.86",
                "Upper_Bound": "6607.55",
            },
            "05/09/2020": {
                "Forecast_Price": "4384.18",
                "Lower_Bound": "2184.92",
                "Upper_Bound": "6583.44",
            },
            "12/09/2020": {
                "Forecast_Price": "4424.37",
                "Lower_Bound": "2257.90",
                "Upper_Bound": "6590.84",
            },
            "19/09/2020": {
                "Forecast_Price": "4411.03",
                "Lower_Bound": "2241.32",
                "Upper_Bound": "6580.74",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4148.44",
                "Lower_Bound": "2026.26",
                "Upper_Bound": "6270.63",
            },
            "30/09/2020": {
                "Forecast_Price": "4433.01",
                "Lower_Bound": "2156.75",
                "Upper_Bound": "6709.27",
            },
            "30/10/2020": {
                "Forecast_Price": "4801.82",
                "Lower_Bound": "2285.69",
                "Upper_Bound": "7317.96",
            },
            "29/11/2020": {
                "Forecast_Price": "4989.28",
                "Lower_Bound": "2360.97",
                "Upper_Bound": "7617.58",
            },
            "29/12/2020": {
                "Forecast_Price": "5176.93",
                "Lower_Bound": "2434.18",
                "Upper_Bound": "7919.69",
            },
            "28/01/2021": {
                "Forecast_Price": "5023.52",
                "Lower_Bound": "2366.75",
                "Upper_Bound": "7680.30",
            },
            "27/02/2021": {
                "Forecast_Price": "4725.57",
                "Lower_Bound": "2248.56",
                "Upper_Bound": "7202.57",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4440.53",
                "Lower_Bound": "3842.47",
                "Upper_Bound": "5038.60",
            },
            "02/08/2020": {
                "Forecast_Price": "4460.10",
                "Lower_Bound": "3730.85",
                "Upper_Bound": "5189.34",
            },
            "03/08/2020": {
                "Forecast_Price": "4456.04",
                "Lower_Bound": "3795.97",
                "Upper_Bound": "5116.10",
            },
            "04/08/2020": {
                "Forecast_Price": "4442.65",
                "Lower_Bound": "3567.90",
                "Upper_Bound": "5317.41",
            },
            "05/08/2020": {
                "Forecast_Price": "4421.45",
                "Lower_Bound": "3702.06",
                "Upper_Bound": "5140.84",
            },
            "06/08/2020": {
                "Forecast_Price": "4467.25",
                "Lower_Bound": "3648.45",
                "Upper_Bound": "5286.05",
            },
            "07/08/2020": {
                "Forecast_Price": "4418.23",
                "Lower_Bound": "3753.33",
                "Upper_Bound": "5083.14",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4233.92",
                "Lower_Bound": "2062.97",
                "Upper_Bound": "6404.87",
            },
            "15/08/2020": {
                "Forecast_Price": "4284.32",
                "Lower_Bound": "2077.34",
                "Upper_Bound": "6491.30",
            },
            "22/08/2020": {
                "Forecast_Price": "4285.93",
                "Lower_Bound": "2081.19",
                "Upper_Bound": "6490.67",
            },
            "29/08/2020": {
                "Forecast_Price": "4199.51",
                "Lower_Bound": "2053.17",
                "Upper_Bound": "6345.85",
            },
            "05/09/2020": {
                "Forecast_Price": "4232.39",
                "Lower_Bound": "2058.36",
                "Upper_Bound": "6406.41",
            },
            "12/09/2020": {
                "Forecast_Price": "4283.05",
                "Lower_Bound": "2073.17",
                "Upper_Bound": "6492.92",
            },
            "19/09/2020": {
                "Forecast_Price": "4283.90",
                "Lower_Bound": "2075.75",
                "Upper_Bound": "6492.05",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4244.44",
                "Lower_Bound": "2127.21",
                "Upper_Bound": "6361.67",
            },
            "30/09/2020": {
                "Forecast_Price": "4295.06",
                "Lower_Bound": "2153.14",
                "Upper_Bound": "6436.98",
            },
            "30/10/2020": {
                "Forecast_Price": "4307.71",
                "Lower_Bound": "2164.22",
                "Upper_Bound": "6451.20",
            },
            "29/11/2020": {
                "Forecast_Price": "4318.58",
                "Lower_Bound": "2161.98",
                "Upper_Bound": "6475.18",
            },
            "29/12/2020": {
                "Forecast_Price": "4375.61",
                "Lower_Bound": "2162.68",
                "Upper_Bound": "6588.54",
            },
            "28/01/2021": {
                "Forecast_Price": "4386.46",
                "Lower_Bound": "2149.20",
                "Upper_Bound": "6623.72",
            },
            "27/02/2021": {
                "Forecast_Price": "4318.49",
                "Lower_Bound": "2078.47",
                "Upper_Bound": "6558.52",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4951.68",
                "Lower_Bound": "3937.35",
                "Upper_Bound": "5966.00",
            },
            "02/08/2020": {
                "Forecast_Price": "4939.68",
                "Lower_Bound": "3991.07",
                "Upper_Bound": "5888.30",
            },
            "03/08/2020": {
                "Forecast_Price": "4945.88",
                "Lower_Bound": "4282.04",
                "Upper_Bound": "5609.72",
            },
            "04/08/2020": {
                "Forecast_Price": "4944.71",
                "Lower_Bound": "4126.16",
                "Upper_Bound": "5763.26",
            },
            "05/08/2020": {
                "Forecast_Price": "4958.57",
                "Lower_Bound": "4286.33",
                "Upper_Bound": "5630.82",
            },
            "06/08/2020": {
                "Forecast_Price": "4929.42",
                "Lower_Bound": "4304.37",
                "Upper_Bound": "5554.48",
            },
            "07/08/2020": {
                "Forecast_Price": "4969.38",
                "Lower_Bound": "4115.39",
                "Upper_Bound": "5823.37",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5098.41",
                "Lower_Bound": "2490.13",
                "Upper_Bound": "7706.70",
            },
            "15/08/2020": {
                "Forecast_Price": "5093.03",
                "Lower_Bound": "2487.45",
                "Upper_Bound": "7698.60",
            },
            "22/08/2020": {
                "Forecast_Price": "5087.68",
                "Lower_Bound": "2484.85",
                "Upper_Bound": "7690.51",
            },
            "29/08/2020": {
                "Forecast_Price": "5082.45",
                "Lower_Bound": "2482.44",
                "Upper_Bound": "7682.47",
            },
            "05/09/2020": {
                "Forecast_Price": "5077.07",
                "Lower_Bound": "2479.77",
                "Upper_Bound": "7674.37",
            },
            "12/09/2020": {
                "Forecast_Price": "5071.68",
                "Lower_Bound": "2477.09",
                "Upper_Bound": "7666.27",
            },
            "19/09/2020": {
                "Forecast_Price": "5066.33",
                "Lower_Bound": "2474.48",
                "Upper_Bound": "7658.18",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5097.70",
                "Lower_Bound": "2496.53",
                "Upper_Bound": "7698.87",
            },
            "30/09/2020": {
                "Forecast_Price": "5120.06",
                "Lower_Bound": "2547.84",
                "Upper_Bound": "7692.28",
            },
            "30/10/2020": {
                "Forecast_Price": "5160.58",
                "Lower_Bound": "2629.50",
                "Upper_Bound": "7691.66",
            },
            "29/11/2020": {
                "Forecast_Price": "5188.87",
                "Lower_Bound": "2690.72",
                "Upper_Bound": "7687.01",
            },
            "29/12/2020": {
                "Forecast_Price": "5205.97",
                "Lower_Bound": "2733.24",
                "Upper_Bound": "7678.70",
            },
            "28/01/2021": {
                "Forecast_Price": "5215.60",
                "Lower_Bound": "2763.26",
                "Upper_Bound": "7667.94",
            },
            "27/02/2021": {
                "Forecast_Price": "4965.05",
                "Lower_Bound": "2662.88",
                "Upper_Bound": "7267.23",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5097.50",
                "Lower_Bound": "4297.52",
                "Upper_Bound": "5897.49",
            },
            "02/08/2020": {
                "Forecast_Price": "5089.30",
                "Lower_Bound": "3869.12",
                "Upper_Bound": "6309.48",
            },
            "03/08/2020": {
                "Forecast_Price": "5095.01",
                "Lower_Bound": "3890.86",
                "Upper_Bound": "6299.16",
            },
            "04/08/2020": {
                "Forecast_Price": "5093.43",
                "Lower_Bound": "4344.80",
                "Upper_Bound": "5842.06",
            },
            "05/08/2020": {
                "Forecast_Price": "5082.38",
                "Lower_Bound": "4200.46",
                "Upper_Bound": "5964.30",
            },
            "06/08/2020": {
                "Forecast_Price": "5058.29",
                "Lower_Bound": "4326.06",
                "Upper_Bound": "5790.52",
            },
            "07/08/2020": {
                "Forecast_Price": "5075.84",
                "Lower_Bound": "4212.78",
                "Upper_Bound": "5938.90",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4874.80",
                "Lower_Bound": "2381.40",
                "Upper_Bound": "7368.19",
            },
            "15/08/2020": {
                "Forecast_Price": "4915.47",
                "Lower_Bound": "2400.84",
                "Upper_Bound": "7430.09",
            },
            "22/08/2020": {
                "Forecast_Price": "4955.07",
                "Lower_Bound": "2418.50",
                "Upper_Bound": "7491.63",
            },
            "29/08/2020": {
                "Forecast_Price": "4996.56",
                "Lower_Bound": "2439.33",
                "Upper_Bound": "7553.80",
            },
            "05/09/2020": {
                "Forecast_Price": "5037.48",
                "Lower_Bound": "2459.20",
                "Upper_Bound": "7615.77",
            },
            "12/09/2020": {
                "Forecast_Price": "5078.15",
                "Lower_Bound": "2478.64",
                "Upper_Bound": "7677.67",
            },
            "19/09/2020": {
                "Forecast_Price": "5117.75",
                "Lower_Bound": "2496.30",
                "Upper_Bound": "7739.21",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4899.09",
                "Lower_Bound": "2396.08",
                "Upper_Bound": "7402.10",
            },
            "30/09/2020": {
                "Forecast_Price": "4959.08",
                "Lower_Bound": "2451.82",
                "Upper_Bound": "7466.33",
            },
            "30/10/2020": {
                "Forecast_Price": "4971.00",
                "Lower_Bound": "2479.01",
                "Upper_Bound": "7462.99",
            },
            "29/11/2020": {
                "Forecast_Price": "4980.18",
                "Lower_Bound": "2500.18",
                "Upper_Bound": "7460.17",
            },
            "29/12/2020": {
                "Forecast_Price": "4963.02",
                "Lower_Bound": "2518.93",
                "Upper_Bound": "7407.10",
            },
            "28/01/2021": {
                "Forecast_Price": "4977.74",
                "Lower_Bound": "2560.78",
                "Upper_Bound": "7394.69",
            },
            "27/02/2021": {
                "Forecast_Price": "4928.80",
                "Lower_Bound": "2577.77",
                "Upper_Bound": "7279.83",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4744.16",
                "Lower_Bound": "4082.23",
                "Upper_Bound": "5406.10",
            },
            "02/08/2020": {
                "Forecast_Price": "4788.56",
                "Lower_Bound": "3964.14",
                "Upper_Bound": "5612.97",
            },
            "03/08/2020": {
                "Forecast_Price": "4745.62",
                "Lower_Bound": "4027.79",
                "Upper_Bound": "5463.45",
            },
            "04/08/2020": {
                "Forecast_Price": "4745.51",
                "Lower_Bound": "3875.54",
                "Upper_Bound": "5615.49",
            },
            "05/08/2020": {
                "Forecast_Price": "4777.64",
                "Lower_Bound": "3940.19",
                "Upper_Bound": "5615.09",
            },
            "06/08/2020": {
                "Forecast_Price": "4770.16",
                "Lower_Bound": "3910.50",
                "Upper_Bound": "5629.81",
            },
            "07/08/2020": {
                "Forecast_Price": "4877.30",
                "Lower_Bound": "4089.33",
                "Upper_Bound": "5665.28",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4899.57",
                "Lower_Bound": "2394.52",
                "Upper_Bound": "7404.63",
            },
            "15/08/2020": {
                "Forecast_Price": "4895.24",
                "Lower_Bound": "2392.82",
                "Upper_Bound": "7397.66",
            },
            "22/08/2020": {
                "Forecast_Price": "4898.64",
                "Lower_Bound": "2393.30",
                "Upper_Bound": "7403.99",
            },
            "29/08/2020": {
                "Forecast_Price": "4898.99",
                "Lower_Bound": "2395.11",
                "Upper_Bound": "7402.87",
            },
            "05/09/2020": {
                "Forecast_Price": "4896.25",
                "Lower_Bound": "2394.80",
                "Upper_Bound": "7397.70",
            },
            "12/09/2020": {
                "Forecast_Price": "4891.95",
                "Lower_Bound": "2393.12",
                "Upper_Bound": "7390.78",
            },
            "19/09/2020": {
                "Forecast_Price": "4895.30",
                "Lower_Bound": "2393.58",
                "Upper_Bound": "7397.02",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4892.67",
                "Lower_Bound": "2402.15",
                "Upper_Bound": "7383.19",
            },
            "30/09/2020": {
                "Forecast_Price": "4877.16",
                "Lower_Bound": "2399.96",
                "Upper_Bound": "7354.36",
            },
            "30/10/2020": {
                "Forecast_Price": "4855.10",
                "Lower_Bound": "2386.81",
                "Upper_Bound": "7323.38",
            },
            "29/11/2020": {
                "Forecast_Price": "4832.37",
                "Lower_Bound": "2372.55",
                "Upper_Bound": "7292.18",
            },
            "29/12/2020": {
                "Forecast_Price": "4819.75",
                "Lower_Bound": "2375.19",
                "Upper_Bound": "7264.30",
            },
            "28/01/2021": {
                "Forecast_Price": "4888.75",
                "Lower_Bound": "2421.72",
                "Upper_Bound": "7355.78",
            },
            "27/02/2021": {
                "Forecast_Price": "4687.60",
                "Lower_Bound": "2348.00",
                "Upper_Bound": "7027.20",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5415.08",
                "Lower_Bound": "4518.86",
                "Upper_Bound": "6311.30",
            },
            "02/08/2020": {
                "Forecast_Price": "5437.46",
                "Lower_Bound": "4237.52",
                "Upper_Bound": "6637.39",
            },
            "03/08/2020": {
                "Forecast_Price": "5442.66",
                "Lower_Bound": "4269.74",
                "Upper_Bound": "6615.57",
            },
            "04/08/2020": {
                "Forecast_Price": "5467.35",
                "Lower_Bound": "4581.78",
                "Upper_Bound": "6352.92",
            },
            "05/08/2020": {
                "Forecast_Price": "5407.86",
                "Lower_Bound": "4644.03",
                "Upper_Bound": "6171.68",
            },
            "06/08/2020": {
                "Forecast_Price": "5422.57",
                "Lower_Bound": "4218.18",
                "Upper_Bound": "6626.96",
            },
            "07/08/2020": {
                "Forecast_Price": "5439.63",
                "Lower_Bound": "4274.57",
                "Upper_Bound": "6604.69",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5181.60",
                "Lower_Bound": "2529.07",
                "Upper_Bound": "7834.12",
            },
            "15/08/2020": {
                "Forecast_Price": "5177.80",
                "Lower_Bound": "2527.90",
                "Upper_Bound": "7827.70",
            },
            "22/08/2020": {
                "Forecast_Price": "5176.12",
                "Lower_Bound": "2526.38",
                "Upper_Bound": "7825.86",
            },
            "29/08/2020": {
                "Forecast_Price": "5175.84",
                "Lower_Bound": "2526.01",
                "Upper_Bound": "7825.67",
            },
            "05/09/2020": {
                "Forecast_Price": "5171.06",
                "Lower_Bound": "2521.65",
                "Upper_Bound": "7820.46",
            },
            "12/09/2020": {
                "Forecast_Price": "5167.35",
                "Lower_Bound": "2520.51",
                "Upper_Bound": "7814.19",
            },
            "19/09/2020": {
                "Forecast_Price": "5165.66",
                "Lower_Bound": "2518.98",
                "Upper_Bound": "7812.33",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5250.29",
                "Lower_Bound": "2555.60",
                "Upper_Bound": "7944.97",
            },
            "30/09/2020": {
                "Forecast_Price": "5329.36",
                "Lower_Bound": "2582.19",
                "Upper_Bound": "8076.53",
            },
            "30/10/2020": {
                "Forecast_Price": "5311.08",
                "Lower_Bound": "2586.16",
                "Upper_Bound": "8036.00",
            },
            "29/11/2020": {
                "Forecast_Price": "5294.49",
                "Lower_Bound": "2585.10",
                "Upper_Bound": "8003.88",
            },
            "29/12/2020": {
                "Forecast_Price": "5405.42",
                "Lower_Bound": "2618.38",
                "Upper_Bound": "8192.46",
            },
            "28/01/2021": {
                "Forecast_Price": "5471.93",
                "Lower_Bound": "2649.93",
                "Upper_Bound": "8293.93",
            },
            "27/02/2021": {
                "Forecast_Price": "5339.28",
                "Lower_Bound": "2589.05",
                "Upper_Bound": "8089.50",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5401.95",
                "Lower_Bound": "4367.44",
                "Upper_Bound": "6436.45",
            },
            "02/08/2020": {
                "Forecast_Price": "5398.31",
                "Lower_Bound": "4413.02",
                "Upper_Bound": "6383.60",
            },
            "03/08/2020": {
                "Forecast_Price": "5407.43",
                "Lower_Bound": "4292.14",
                "Upper_Bound": "6522.71",
            },
            "04/08/2020": {
                "Forecast_Price": "5418.67",
                "Lower_Bound": "3828.60",
                "Upper_Bound": "7008.75",
            },
            "05/08/2020": {
                "Forecast_Price": "5390.63",
                "Lower_Bound": "4420.94",
                "Upper_Bound": "6360.32",
            },
            "06/08/2020": {
                "Forecast_Price": "5367.75",
                "Lower_Bound": "4490.64",
                "Upper_Bound": "6244.87",
            },
            "07/08/2020": {
                "Forecast_Price": "5415.65",
                "Lower_Bound": "4491.22",
                "Upper_Bound": "6340.09",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5454.90",
                "Lower_Bound": "2655.76",
                "Upper_Bound": "8254.04",
            },
            "15/08/2020": {
                "Forecast_Price": "5401.25",
                "Lower_Bound": "2637.74",
                "Upper_Bound": "8164.76",
            },
            "22/08/2020": {
                "Forecast_Price": "5349.30",
                "Lower_Bound": "2620.28",
                "Upper_Bound": "8078.33",
            },
            "29/08/2020": {
                "Forecast_Price": "5426.09",
                "Lower_Bound": "2645.07",
                "Upper_Bound": "8207.11",
            },
            "05/09/2020": {
                "Forecast_Price": "5432.10",
                "Lower_Bound": "2646.60",
                "Upper_Bound": "8217.61",
            },
            "12/09/2020": {
                "Forecast_Price": "5378.43",
                "Lower_Bound": "2628.54",
                "Upper_Bound": "8128.32",
            },
            "19/09/2020": {
                "Forecast_Price": "5326.45",
                "Lower_Bound": "2611.03",
                "Upper_Bound": "8041.88",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5396.57",
                "Lower_Bound": "2641.11",
                "Upper_Bound": "8152.03",
            },
            "30/09/2020": {
                "Forecast_Price": "5415.75",
                "Lower_Bound": "2688.47",
                "Upper_Bound": "8143.02",
            },
            "30/10/2020": {
                "Forecast_Price": "5435.13",
                "Lower_Bound": "2736.09",
                "Upper_Bound": "8134.18",
            },
            "29/11/2020": {
                "Forecast_Price": "5462.10",
                "Lower_Bound": "2796.27",
                "Upper_Bound": "8127.93",
            },
            "29/12/2020": {
                "Forecast_Price": "5495.37",
                "Lower_Bound": "2866.89",
                "Upper_Bound": "8123.85",
            },
            "28/01/2021": {
                "Forecast_Price": "5528.69",
                "Lower_Bound": "2935.42",
                "Upper_Bound": "8121.96",
            },
            "27/02/2021": {
                "Forecast_Price": "5525.13",
                "Lower_Bound": "2949.79",
                "Upper_Bound": "8100.48",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4420.87",
                "Lower_Bound": "3755.26",
                "Upper_Bound": "5086.48",
            },
            "02/08/2020": {
                "Forecast_Price": "4387.34",
                "Lower_Bound": "3640.33",
                "Upper_Bound": "5134.35",
            },
            "03/08/2020": {
                "Forecast_Price": "4432.80",
                "Lower_Bound": "3869.91",
                "Upper_Bound": "4995.69",
            },
            "04/08/2020": {
                "Forecast_Price": "4535.12",
                "Lower_Bound": "3793.59",
                "Upper_Bound": "5276.64",
            },
            "05/08/2020": {
                "Forecast_Price": "4445.48",
                "Lower_Bound": "3526.07",
                "Upper_Bound": "5364.89",
            },
            "06/08/2020": {
                "Forecast_Price": "4413.48",
                "Lower_Bound": "3765.67",
                "Upper_Bound": "5061.28",
            },
            "07/08/2020": {
                "Forecast_Price": "4475.23",
                "Lower_Bound": "3904.42",
                "Upper_Bound": "5046.03",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4584.15",
                "Lower_Bound": "2232.62",
                "Upper_Bound": "6935.67",
            },
            "15/08/2020": {
                "Forecast_Price": "4594.41",
                "Lower_Bound": "2235.48",
                "Upper_Bound": "6953.35",
            },
            "22/08/2020": {
                "Forecast_Price": "4609.08",
                "Lower_Bound": "2239.93",
                "Upper_Bound": "6978.23",
            },
            "29/08/2020": {
                "Forecast_Price": "4648.15",
                "Lower_Bound": "2252.60",
                "Upper_Bound": "7043.70",
            },
            "05/09/2020": {
                "Forecast_Price": "4680.94",
                "Lower_Bound": "2263.84",
                "Upper_Bound": "7098.05",
            },
            "12/09/2020": {
                "Forecast_Price": "4691.21",
                "Lower_Bound": "2266.70",
                "Upper_Bound": "7115.73",
            },
            "19/09/2020": {
                "Forecast_Price": "4705.88",
                "Lower_Bound": "2271.15",
                "Upper_Bound": "7140.61",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4504.42",
                "Lower_Bound": "2161.66",
                "Upper_Bound": "6847.19",
            },
            "30/09/2020": {
                "Forecast_Price": "4483.39",
                "Lower_Bound": "2132.35",
                "Upper_Bound": "6834.42",
            },
            "30/10/2020": {
                "Forecast_Price": "4459.76",
                "Lower_Bound": "2099.82",
                "Upper_Bound": "6819.70",
            },
            "29/11/2020": {
                "Forecast_Price": "4443.64",
                "Lower_Bound": "2077.84",
                "Upper_Bound": "6809.43",
            },
            "29/12/2020": {
                "Forecast_Price": "4433.17",
                "Lower_Bound": "2068.34",
                "Upper_Bound": "6797.99",
            },
            "28/01/2021": {
                "Forecast_Price": "4435.06",
                "Lower_Bound": "2072.67",
                "Upper_Bound": "6797.45",
            },
            "27/02/2021": {
                "Forecast_Price": "4414.92",
                "Lower_Bound": "2048.12",
                "Upper_Bound": "6781.72",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4647.69",
                "Lower_Bound": "4024.53",
                "Upper_Bound": "5270.84",
            },
            "02/08/2020": {
                "Forecast_Price": "4651.43",
                "Lower_Bound": "3868.36",
                "Upper_Bound": "5434.51",
            },
            "03/08/2020": {
                "Forecast_Price": "4646.85",
                "Lower_Bound": "3550.39",
                "Upper_Bound": "5743.32",
            },
            "04/08/2020": {
                "Forecast_Price": "4642.35",
                "Lower_Bound": "3648.90",
                "Upper_Bound": "5635.79",
            },
            "05/08/2020": {
                "Forecast_Price": "4630.03",
                "Lower_Bound": "3918.29",
                "Upper_Bound": "5341.77",
            },
            "06/08/2020": {
                "Forecast_Price": "4622.82",
                "Lower_Bound": "4080.58",
                "Upper_Bound": "5165.06",
            },
            "07/08/2020": {
                "Forecast_Price": "4624.19",
                "Lower_Bound": "3951.97",
                "Upper_Bound": "5296.41",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4583.35",
                "Lower_Bound": "2246.14",
                "Upper_Bound": "6920.56",
            },
            "15/08/2020": {
                "Forecast_Price": "4568.52",
                "Lower_Bound": "2237.39",
                "Upper_Bound": "6899.64",
            },
            "22/08/2020": {
                "Forecast_Price": "4527.76",
                "Lower_Bound": "2214.40",
                "Upper_Bound": "6841.12",
            },
            "29/08/2020": {
                "Forecast_Price": "4557.70",
                "Lower_Bound": "2234.69",
                "Upper_Bound": "6880.71",
            },
            "05/09/2020": {
                "Forecast_Price": "4538.26",
                "Lower_Bound": "2227.03",
                "Upper_Bound": "6849.48",
            },
            "12/09/2020": {
                "Forecast_Price": "4524.28",
                "Lower_Bound": "2218.56",
                "Upper_Bound": "6830.00",
            },
            "19/09/2020": {
                "Forecast_Price": "4493.52",
                "Lower_Bound": "2198.86",
                "Upper_Bound": "6788.19",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4562.00",
                "Lower_Bound": "2256.27",
                "Upper_Bound": "6867.73",
            },
            "30/09/2020": {
                "Forecast_Price": "4509.33",
                "Lower_Bound": "2247.15",
                "Upper_Bound": "6771.50",
            },
            "30/10/2020": {
                "Forecast_Price": "4453.17",
                "Lower_Bound": "2225.64",
                "Upper_Bound": "6680.69",
            },
            "29/11/2020": {
                "Forecast_Price": "4392.53",
                "Lower_Bound": "2193.11",
                "Upper_Bound": "6591.96",
            },
            "29/12/2020": {
                "Forecast_Price": "4347.31",
                "Lower_Bound": "2189.38",
                "Upper_Bound": "6505.24",
            },
            "28/01/2021": {
                "Forecast_Price": "4322.17",
                "Lower_Bound": "2206.88",
                "Upper_Bound": "6437.46",
            },
            "27/02/2021": {
                "Forecast_Price": "4307.20",
                "Lower_Bound": "2248.85",
                "Upper_Bound": "6365.55",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4446.41",
                "Lower_Bound": "3803.71",
                "Upper_Bound": "5089.11",
            },
            "02/08/2020": {
                "Forecast_Price": "4441.09",
                "Lower_Bound": "3755.54",
                "Upper_Bound": "5126.65",
            },
            "03/08/2020": {
                "Forecast_Price": "4432.48",
                "Lower_Bound": "3838.41",
                "Upper_Bound": "5026.55",
            },
            "04/08/2020": {
                "Forecast_Price": "4432.31",
                "Lower_Bound": "3832.77",
                "Upper_Bound": "5031.84",
            },
            "05/08/2020": {
                "Forecast_Price": "4423.88",
                "Lower_Bound": "3759.04",
                "Upper_Bound": "5088.71",
            },
            "06/08/2020": {
                "Forecast_Price": "4418.42",
                "Lower_Bound": "3768.70",
                "Upper_Bound": "5068.15",
            },
            "07/08/2020": {
                "Forecast_Price": "4412.89",
                "Lower_Bound": "3706.17",
                "Upper_Bound": "5119.62",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4465.58",
                "Lower_Bound": "2187.58",
                "Upper_Bound": "6743.58",
            },
            "15/08/2020": {
                "Forecast_Price": "4460.94",
                "Lower_Bound": "2183.77",
                "Upper_Bound": "6738.11",
            },
            "22/08/2020": {
                "Forecast_Price": "4449.92",
                "Lower_Bound": "2169.29",
                "Upper_Bound": "6730.55",
            },
            "29/08/2020": {
                "Forecast_Price": "4450.91",
                "Lower_Bound": "2174.90",
                "Upper_Bound": "6726.93",
            },
            "05/09/2020": {
                "Forecast_Price": "4475.62",
                "Lower_Bound": "2192.53",
                "Upper_Bound": "6758.71",
            },
            "12/09/2020": {
                "Forecast_Price": "4470.98",
                "Lower_Bound": "2188.72",
                "Upper_Bound": "6753.24",
            },
            "19/09/2020": {
                "Forecast_Price": "4459.96",
                "Lower_Bound": "2174.24",
                "Upper_Bound": "6745.68",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4675.01",
                "Lower_Bound": "2236.50",
                "Upper_Bound": "7113.53",
            },
            "30/09/2020": {
                "Forecast_Price": "4724.97",
                "Lower_Bound": "2251.09",
                "Upper_Bound": "7198.85",
            },
            "30/10/2020": {
                "Forecast_Price": "4702.13",
                "Lower_Bound": "2234.81",
                "Upper_Bound": "7169.45",
            },
            "29/11/2020": {
                "Forecast_Price": "4658.88",
                "Lower_Bound": "2221.99",
                "Upper_Bound": "7095.76",
            },
            "29/12/2020": {
                "Forecast_Price": "4632.66",
                "Lower_Bound": "2231.11",
                "Upper_Bound": "7034.21",
            },
            "28/01/2021": {
                "Forecast_Price": "4568.05",
                "Lower_Bound": "2212.27",
                "Upper_Bound": "6923.84",
            },
            "27/02/2021": {
                "Forecast_Price": "4638.23",
                "Lower_Bound": "2239.45",
                "Upper_Bound": "7037.01",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5145.16",
                "Lower_Bound": "4150.63",
                "Upper_Bound": "6139.69",
            },
            "02/08/2020": {
                "Forecast_Price": "5141.27",
                "Lower_Bound": "4286.21",
                "Upper_Bound": "5996.33",
            },
            "03/08/2020": {
                "Forecast_Price": "5143.03",
                "Lower_Bound": "4432.12",
                "Upper_Bound": "5853.95",
            },
            "04/08/2020": {
                "Forecast_Price": "5137.59",
                "Lower_Bound": "4376.43",
                "Upper_Bound": "5898.75",
            },
            "05/08/2020": {
                "Forecast_Price": "5132.03",
                "Lower_Bound": "3979.64",
                "Upper_Bound": "6284.43",
            },
            "06/08/2020": {
                "Forecast_Price": "5139.29",
                "Lower_Bound": "4328.17",
                "Upper_Bound": "5950.40",
            },
            "07/08/2020": {
                "Forecast_Price": "5135.53",
                "Lower_Bound": "4305.93",
                "Upper_Bound": "5965.13",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4908.20",
                "Lower_Bound": "2396.62",
                "Upper_Bound": "7419.77",
            },
            "15/08/2020": {
                "Forecast_Price": "4894.23",
                "Lower_Bound": "2393.21",
                "Upper_Bound": "7395.26",
            },
            "22/08/2020": {
                "Forecast_Price": "4900.89",
                "Lower_Bound": "2396.56",
                "Upper_Bound": "7405.22",
            },
            "29/08/2020": {
                "Forecast_Price": "4928.60",
                "Lower_Bound": "2406.82",
                "Upper_Bound": "7450.38",
            },
            "05/09/2020": {
                "Forecast_Price": "4929.18",
                "Lower_Bound": "2408.18",
                "Upper_Bound": "7450.19",
            },
            "12/09/2020": {
                "Forecast_Price": "4915.22",
                "Lower_Bound": "2404.76",
                "Upper_Bound": "7425.68",
            },
            "19/09/2020": {
                "Forecast_Price": "4921.87",
                "Lower_Bound": "2408.11",
                "Upper_Bound": "7435.63",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4872.86",
                "Lower_Bound": "2383.43",
                "Upper_Bound": "7362.29",
            },
            "30/09/2020": {
                "Forecast_Price": "4931.72",
                "Lower_Bound": "2402.33",
                "Upper_Bound": "7461.10",
            },
            "30/10/2020": {
                "Forecast_Price": "5091.81",
                "Lower_Bound": "2454.47",
                "Upper_Bound": "7729.16",
            },
            "29/11/2020": {
                "Forecast_Price": "5170.35",
                "Lower_Bound": "2479.83",
                "Upper_Bound": "7860.86",
            },
            "29/12/2020": {
                "Forecast_Price": "5218.93",
                "Lower_Bound": "2495.37",
                "Upper_Bound": "7942.49",
            },
            "28/01/2021": {
                "Forecast_Price": "5218.83",
                "Lower_Bound": "2494.93",
                "Upper_Bound": "7942.73",
            },
            "27/02/2021": {
                "Forecast_Price": "5171.00",
                "Lower_Bound": "2480.43",
                "Upper_Bound": "7861.58",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4350.44",
                "Lower_Bound": "3734.72",
                "Upper_Bound": "4966.15",
            },
            "02/08/2020": {
                "Forecast_Price": "4345.55",
                "Lower_Bound": "3731.30",
                "Upper_Bound": "4959.80",
            },
            "03/08/2020": {
                "Forecast_Price": "4338.83",
                "Lower_Bound": "3775.91",
                "Upper_Bound": "4901.75",
            },
            "04/08/2020": {
                "Forecast_Price": "4332.80",
                "Lower_Bound": "3653.72",
                "Upper_Bound": "5011.87",
            },
            "05/08/2020": {
                "Forecast_Price": "4327.41",
                "Lower_Bound": "3485.15",
                "Upper_Bound": "5169.66",
            },
            "06/08/2020": {
                "Forecast_Price": "4332.56",
                "Lower_Bound": "3689.06",
                "Upper_Bound": "4976.05",
            },
            "07/08/2020": {
                "Forecast_Price": "4285.24",
                "Lower_Bound": "3633.14",
                "Upper_Bound": "4937.33",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3639.94",
                "Lower_Bound": "1777.12",
                "Upper_Bound": "5502.77",
            },
            "15/08/2020": {
                "Forecast_Price": "3671.14",
                "Lower_Bound": "1788.43",
                "Upper_Bound": "5553.86",
            },
            "22/08/2020": {
                "Forecast_Price": "3691.25",
                "Lower_Bound": "1795.66",
                "Upper_Bound": "5586.84",
            },
            "29/08/2020": {
                "Forecast_Price": "3688.17",
                "Lower_Bound": "1793.88",
                "Upper_Bound": "5582.47",
            },
            "05/09/2020": {
                "Forecast_Price": "3710.39",
                "Lower_Bound": "1801.55",
                "Upper_Bound": "5619.23",
            },
            "12/09/2020": {
                "Forecast_Price": "3741.59",
                "Lower_Bound": "1812.86",
                "Upper_Bound": "5670.32",
            },
            "19/09/2020": {
                "Forecast_Price": "3761.69",
                "Lower_Bound": "1820.09",
                "Upper_Bound": "5703.30",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3555.40",
                "Lower_Bound": "1653.91",
                "Upper_Bound": "5456.89",
            },
            "30/09/2020": {
                "Forecast_Price": "3487.77",
                "Lower_Bound": "1572.38",
                "Upper_Bound": "5403.16",
            },
            "30/10/2020": {
                "Forecast_Price": "3404.52",
                "Lower_Bound": "1485.70",
                "Upper_Bound": "5323.35",
            },
            "29/11/2020": {
                "Forecast_Price": "3423.00",
                "Lower_Bound": "1444.01",
                "Upper_Bound": "5401.99",
            },
            "29/12/2020": {
                "Forecast_Price": "3522.16",
                "Lower_Bound": "1453.40",
                "Upper_Bound": "5590.93",
            },
            "28/01/2021": {
                "Forecast_Price": "3569.31",
                "Lower_Bound": "1463.51",
                "Upper_Bound": "5675.12",
            },
            "27/02/2021": {
                "Forecast_Price": "3542.44",
                "Lower_Bound": "1417.45",
                "Upper_Bound": "5667.43",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "5148.35",
                "Lower_Bound": "4441.29",
                "Upper_Bound": "5855.42",
            },
            "02/08/2020": {
                "Forecast_Price": "5146.80",
                "Lower_Bound": "4536.01",
                "Upper_Bound": "5757.59",
            },
            "03/08/2020": {
                "Forecast_Price": "5147.89",
                "Lower_Bound": "4443.83",
                "Upper_Bound": "5851.95",
            },
            "04/08/2020": {
                "Forecast_Price": "5145.82",
                "Lower_Bound": "4260.03",
                "Upper_Bound": "6031.62",
            },
            "05/08/2020": {
                "Forecast_Price": "5142.75",
                "Lower_Bound": "4506.04",
                "Upper_Bound": "5779.46",
            },
            "06/08/2020": {
                "Forecast_Price": "5142.00",
                "Lower_Bound": "4533.48",
                "Upper_Bound": "5750.51",
            },
            "07/08/2020": {
                "Forecast_Price": "5138.81",
                "Lower_Bound": "4603.64",
                "Upper_Bound": "5673.98",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "5095.70",
                "Lower_Bound": "2487.71",
                "Upper_Bound": "7703.70",
            },
            "15/08/2020": {
                "Forecast_Price": "5083.79",
                "Lower_Bound": "2483.90",
                "Upper_Bound": "7683.67",
            },
            "22/08/2020": {
                "Forecast_Price": "5101.26",
                "Lower_Bound": "2491.89",
                "Upper_Bound": "7710.62",
            },
            "29/08/2020": {
                "Forecast_Price": "5092.23",
                "Lower_Bound": "2487.31",
                "Upper_Bound": "7697.14",
            },
            "05/09/2020": {
                "Forecast_Price": "5093.89",
                "Lower_Bound": "2487.96",
                "Upper_Bound": "7699.81",
            },
            "12/09/2020": {
                "Forecast_Price": "5088.95",
                "Lower_Bound": "2486.44",
                "Upper_Bound": "7691.45",
            },
            "19/09/2020": {
                "Forecast_Price": "5099.22",
                "Lower_Bound": "2492.08",
                "Upper_Bound": "7706.36",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "5147.44",
                "Lower_Bound": "2592.57",
                "Upper_Bound": "7702.32",
            },
            "30/09/2020": {
                "Forecast_Price": "5180.02",
                "Lower_Bound": "2633.62",
                "Upper_Bound": "7726.43",
            },
            "30/10/2020": {
                "Forecast_Price": "5190.16",
                "Lower_Bound": "2657.12",
                "Upper_Bound": "7723.20",
            },
            "29/11/2020": {
                "Forecast_Price": "5253.37",
                "Lower_Bound": "2691.39",
                "Upper_Bound": "7815.35",
            },
            "29/12/2020": {
                "Forecast_Price": "5349.78",
                "Lower_Bound": "2734.44",
                "Upper_Bound": "7965.12",
            },
            "28/01/2021": {
                "Forecast_Price": "5370.58",
                "Lower_Bound": "2751.97",
                "Upper_Bound": "7989.20",
            },
            "27/02/2021": {
                "Forecast_Price": "5604.33",
                "Lower_Bound": "2908.48",
                "Upper_Bound": "8300.18",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4898.01",
                "Lower_Bound": "4052.63",
                "Upper_Bound": "5743.39",
            },
            "02/08/2020": {
                "Forecast_Price": "4895.79",
                "Lower_Bound": "4291.42",
                "Upper_Bound": "5500.15",
            },
            "03/08/2020": {
                "Forecast_Price": "4898.28",
                "Lower_Bound": "4202.34",
                "Upper_Bound": "5594.22",
            },
            "04/08/2020": {
                "Forecast_Price": "4897.36",
                "Lower_Bound": "4208.50",
                "Upper_Bound": "5586.21",
            },
            "05/08/2020": {
                "Forecast_Price": "4897.61",
                "Lower_Bound": "4277.47",
                "Upper_Bound": "5517.74",
            },
            "06/08/2020": {
                "Forecast_Price": "4896.45",
                "Lower_Bound": "4294.24",
                "Upper_Bound": "5498.66",
            },
            "07/08/2020": {
                "Forecast_Price": "4895.06",
                "Lower_Bound": "4284.74",
                "Upper_Bound": "5505.37",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4890.02",
                "Lower_Bound": "2380.64",
                "Upper_Bound": "7399.39",
            },
            "15/08/2020": {
                "Forecast_Price": "4908.87",
                "Lower_Bound": "2388.91",
                "Upper_Bound": "7428.82",
            },
            "22/08/2020": {
                "Forecast_Price": "4914.85",
                "Lower_Bound": "2393.15",
                "Upper_Bound": "7436.54",
            },
            "29/08/2020": {
                "Forecast_Price": "4905.07",
                "Lower_Bound": "2386.31",
                "Upper_Bound": "7423.83",
            },
            "05/09/2020": {
                "Forecast_Price": "4922.50",
                "Lower_Bound": "2392.34",
                "Upper_Bound": "7452.67",
            },
            "12/09/2020": {
                "Forecast_Price": "4933.74",
                "Lower_Bound": "2398.11",
                "Upper_Bound": "7469.36",
            },
            "19/09/2020": {
                "Forecast_Price": "4938.70",
                "Lower_Bound": "2402.02",
                "Upper_Bound": "7475.38",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4442.52",
                "Lower_Bound": "2307.63",
                "Upper_Bound": "6577.40",
            },
            "30/09/2020": {
                "Forecast_Price": "4122.41",
                "Lower_Bound": "2234.29",
                "Upper_Bound": "6010.52",
            },
            "30/10/2020": {
                "Forecast_Price": "4104.00",
                "Lower_Bound": "2256.06",
                "Upper_Bound": "5951.95",
            },
            "29/11/2020": {
                "Forecast_Price": "4082.37",
                "Lower_Bound": "2272.07",
                "Upper_Bound": "5892.66",
            },
            "29/12/2020": {
                "Forecast_Price": "4071.09",
                "Lower_Bound": "2293.29",
                "Upper_Bound": "5848.89",
            },
            "28/01/2021": {
                "Forecast_Price": "4059.75",
                "Lower_Bound": "2312.74",
                "Upper_Bound": "5806.77",
            },
            "27/02/2021": {
                "Forecast_Price": "4344.84",
                "Lower_Bound": "2479.63",
                "Upper_Bound": "6210.05",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4600.07",
                "Lower_Bound": "3939.33",
                "Upper_Bound": "5260.81",
            },
            "02/08/2020": {
                "Forecast_Price": "4594.41",
                "Lower_Bound": "3893.36",
                "Upper_Bound": "5295.46",
            },
            "03/08/2020": {
                "Forecast_Price": "4592.85",
                "Lower_Bound": "3980.39",
                "Upper_Bound": "5205.31",
            },
            "04/08/2020": {
                "Forecast_Price": "4586.56",
                "Lower_Bound": "3816.35",
                "Upper_Bound": "5356.77",
            },
            "05/08/2020": {
                "Forecast_Price": "4588.72",
                "Lower_Bound": "3711.37",
                "Upper_Bound": "5466.07",
            },
            "06/08/2020": {
                "Forecast_Price": "4586.07",
                "Lower_Bound": "3966.74",
                "Upper_Bound": "5205.40",
            },
            "07/08/2020": {
                "Forecast_Price": "4591.75",
                "Lower_Bound": "3941.46",
                "Upper_Bound": "5242.04",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4884.90",
                "Lower_Bound": "2310.00",
                "Upper_Bound": "7459.81",
            },
            "15/08/2020": {
                "Forecast_Price": "4915.01",
                "Lower_Bound": "2368.12",
                "Upper_Bound": "7461.89",
            },
            "22/08/2020": {
                "Forecast_Price": "4908.57",
                "Lower_Bound": "2393.09",
                "Upper_Bound": "7424.05",
            },
            "29/08/2020": {
                "Forecast_Price": "4668.58",
                "Lower_Bound": "2255.66",
                "Upper_Bound": "7081.51",
            },
            "05/09/2020": {
                "Forecast_Price": "4815.12",
                "Lower_Bound": "2295.80",
                "Upper_Bound": "7334.45",
            },
            "12/09/2020": {
                "Forecast_Price": "4849.65",
                "Lower_Bound": "2355.37",
                "Upper_Bound": "7343.93",
            },
            "19/09/2020": {
                "Forecast_Price": "4832.97",
                "Lower_Bound": "2376.98",
                "Upper_Bound": "7288.97",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4671.70",
                "Lower_Bound": "2325.07",
                "Upper_Bound": "7018.32",
            },
            "30/09/2020": {
                "Forecast_Price": "4683.26",
                "Lower_Bound": "2342.33",
                "Upper_Bound": "7024.20",
            },
            "30/10/2020": {
                "Forecast_Price": "4691.39",
                "Lower_Bound": "2353.44",
                "Upper_Bound": "7029.33",
            },
            "29/11/2020": {
                "Forecast_Price": "4707.23",
                "Lower_Bound": "2377.10",
                "Upper_Bound": "7037.37",
            },
            "29/12/2020": {
                "Forecast_Price": "4728.08",
                "Lower_Bound": "2408.74",
                "Upper_Bound": "7047.43",
            },
            "28/01/2021": {
                "Forecast_Price": "4732.00",
                "Lower_Bound": "2411.71",
                "Upper_Bound": "7052.29",
            },
            "27/02/2021": {
                "Forecast_Price": "4723.01",
                "Lower_Bound": "2400.60",
                "Upper_Bound": "7045.41",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3895.43",
                "Lower_Bound": "3354.45",
                "Upper_Bound": "4436.40",
            },
            "02/08/2020": {
                "Forecast_Price": "3890.79",
                "Lower_Bound": "3350.51",
                "Upper_Bound": "4431.06",
            },
            "03/08/2020": {
                "Forecast_Price": "3895.09",
                "Lower_Bound": "3420.93",
                "Upper_Bound": "4369.24",
            },
            "04/08/2020": {
                "Forecast_Price": "3882.52",
                "Lower_Bound": "3338.25",
                "Upper_Bound": "4426.78",
            },
            "05/08/2020": {
                "Forecast_Price": "3880.30",
                "Lower_Bound": "3259.13",
                "Upper_Bound": "4501.47",
            },
            "06/08/2020": {
                "Forecast_Price": "3873.86",
                "Lower_Bound": "3256.59",
                "Upper_Bound": "4491.14",
            },
            "07/08/2020": {
                "Forecast_Price": "3883.57",
                "Lower_Bound": "3186.88",
                "Upper_Bound": "4580.27",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3816.40",
                "Lower_Bound": "1877.04",
                "Upper_Bound": "5755.75",
            },
            "15/08/2020": {
                "Forecast_Price": "3822.64",
                "Lower_Bound": "1880.62",
                "Upper_Bound": "5764.67",
            },
            "22/08/2020": {
                "Forecast_Price": "3826.06",
                "Lower_Bound": "1880.02",
                "Upper_Bound": "5772.09",
            },
            "29/08/2020": {
                "Forecast_Price": "3834.10",
                "Lower_Bound": "1887.42",
                "Upper_Bound": "5780.78",
            },
            "05/09/2020": {
                "Forecast_Price": "3849.73",
                "Lower_Bound": "1907.59",
                "Upper_Bound": "5791.87",
            },
            "12/09/2020": {
                "Forecast_Price": "3855.66",
                "Lower_Bound": "1911.06",
                "Upper_Bound": "5800.25",
            },
            "19/09/2020": {
                "Forecast_Price": "3858.80",
                "Lower_Bound": "1910.38",
                "Upper_Bound": "5807.22",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3782.41",
                "Lower_Bound": "1777.54",
                "Upper_Bound": "5787.29",
            },
            "30/09/2020": {
                "Forecast_Price": "3844.32",
                "Lower_Bound": "1796.08",
                "Upper_Bound": "5892.56",
            },
            "30/10/2020": {
                "Forecast_Price": "3851.65",
                "Lower_Bound": "1809.04",
                "Upper_Bound": "5894.26",
            },
            "29/11/2020": {
                "Forecast_Price": "3855.29",
                "Lower_Bound": "1792.65",
                "Upper_Bound": "5917.93",
            },
            "29/12/2020": {
                "Forecast_Price": "3979.85",
                "Lower_Bound": "1830.78",
                "Upper_Bound": "6128.93",
            },
            "28/01/2021": {
                "Forecast_Price": "3981.37",
                "Lower_Bound": "1824.51",
                "Upper_Bound": "6138.23",
            },
            "27/02/2021": {
                "Forecast_Price": "3939.81",
                "Lower_Bound": "1792.90",
                "Upper_Bound": "6086.72",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "2827.77",
                "Lower_Bound": "2322.24",
                "Upper_Bound": "3333.29",
            },
            "02/08/2020": {
                "Forecast_Price": "2641.36",
                "Lower_Bound": "2168.93",
                "Upper_Bound": "3113.79",
            },
            "03/08/2020": {
                "Forecast_Price": "2564.02",
                "Lower_Bound": "1924.80",
                "Upper_Bound": "3203.24",
            },
            "04/08/2020": {
                "Forecast_Price": "2502.54",
                "Lower_Bound": "2035.63",
                "Upper_Bound": "2969.45",
            },
            "05/08/2020": {
                "Forecast_Price": "2645.14",
                "Lower_Bound": "2264.79",
                "Upper_Bound": "3025.50",
            },
            "06/08/2020": {
                "Forecast_Price": "2604.67",
                "Lower_Bound": "1901.51",
                "Upper_Bound": "3307.83",
            },
            "07/08/2020": {
                "Forecast_Price": "2808.48",
                "Lower_Bound": "2188.42",
                "Upper_Bound": "3428.54",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "2971.54",
                "Lower_Bound": "1552.02",
                "Upper_Bound": "4391.05",
            },
            "15/08/2020": {
                "Forecast_Price": "3256.31",
                "Lower_Bound": "1638.19",
                "Upper_Bound": "4874.43",
            },
            "22/08/2020": {
                "Forecast_Price": "3404.84",
                "Lower_Bound": "1684.38",
                "Upper_Bound": "5125.31",
            },
            "29/08/2020": {
                "Forecast_Price": "3279.55",
                "Lower_Bound": "1645.30",
                "Upper_Bound": "4913.81",
            },
            "05/09/2020": {
                "Forecast_Price": "2823.06",
                "Lower_Bound": "1499.25",
                "Upper_Bound": "4146.88",
            },
            "12/09/2020": {
                "Forecast_Price": "3110.29",
                "Lower_Bound": "1589.52",
                "Upper_Bound": "4631.06",
            },
            "19/09/2020": {
                "Forecast_Price": "3260.39",
                "Lower_Bound": "1638.32",
                "Upper_Bound": "4882.45",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3414.90",
                "Lower_Bound": "1692.04",
                "Upper_Bound": "5137.76",
            },
            "30/09/2020": {
                "Forecast_Price": "3353.06",
                "Lower_Bound": "1621.92",
                "Upper_Bound": "5084.20",
            },
            "30/10/2020": {
                "Forecast_Price": "3292.70",
                "Lower_Bound": "1527.63",
                "Upper_Bound": "5057.77",
            },
            "29/11/2020": {
                "Forecast_Price": "3295.90",
                "Lower_Bound": "1480.78",
                "Upper_Bound": "5111.02",
            },
            "29/12/2020": {
                "Forecast_Price": "3315.51",
                "Lower_Bound": "1486.26",
                "Upper_Bound": "5144.76",
            },
            "28/01/2021": {
                "Forecast_Price": "3644.47",
                "Lower_Bound": "1736.46",
                "Upper_Bound": "5552.48",
            },
            "27/02/2021": {
                "Forecast_Price": "3586.70",
                "Lower_Bound": "1721.89",
                "Upper_Bound": "5451.51",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3977.58",
                "Lower_Bound": "3419.88",
                "Upper_Bound": "4535.27",
            },
            "02/08/2020": {
                "Forecast_Price": "3950.19",
                "Lower_Bound": "3227.19",
                "Upper_Bound": "4673.19",
            },
            "03/08/2020": {
                "Forecast_Price": "3933.48",
                "Lower_Bound": "3336.01",
                "Upper_Bound": "4530.96",
            },
            "04/08/2020": {
                "Forecast_Price": "3970.13",
                "Lower_Bound": "3373.14",
                "Upper_Bound": "4567.12",
            },
            "05/08/2020": {
                "Forecast_Price": "3927.84",
                "Lower_Bound": "3344.41",
                "Upper_Bound": "4511.27",
            },
            "06/08/2020": {
                "Forecast_Price": "3949.35",
                "Lower_Bound": "3332.92",
                "Upper_Bound": "4565.77",
            },
            "07/08/2020": {
                "Forecast_Price": "4009.22",
                "Lower_Bound": "3297.69",
                "Upper_Bound": "4720.75",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4166.06",
                "Lower_Bound": "2053.73",
                "Upper_Bound": "6278.40",
            },
            "15/08/2020": {
                "Forecast_Price": "4203.71",
                "Lower_Bound": "2070.17",
                "Upper_Bound": "6337.24",
            },
            "22/08/2020": {
                "Forecast_Price": "4218.51",
                "Lower_Bound": "2067.06",
                "Upper_Bound": "6369.97",
            },
            "29/08/2020": {
                "Forecast_Price": "4204.68",
                "Lower_Bound": "2045.07",
                "Upper_Bound": "6364.28",
            },
            "05/09/2020": {
                "Forecast_Price": "4204.76",
                "Lower_Bound": "2067.25",
                "Upper_Bound": "6342.28",
            },
            "12/09/2020": {
                "Forecast_Price": "4228.24",
                "Lower_Bound": "2079.04",
                "Upper_Bound": "6377.44",
            },
            "19/09/2020": {
                "Forecast_Price": "4220.36",
                "Lower_Bound": "2068.49",
                "Upper_Bound": "6372.23",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4310.25",
                "Lower_Bound": "2059.50",
                "Upper_Bound": "6561.00",
            },
            "30/09/2020": {
                "Forecast_Price": "4247.79",
                "Lower_Bound": "1937.41",
                "Upper_Bound": "6558.18",
            },
            "30/10/2020": {
                "Forecast_Price": "4107.42",
                "Lower_Bound": "1747.98",
                "Upper_Bound": "6466.85",
            },
            "29/11/2020": {
                "Forecast_Price": "4122.21",
                "Lower_Bound": "1646.99",
                "Upper_Bound": "6597.44",
            },
            "29/12/2020": {
                "Forecast_Price": "4124.31",
                "Lower_Bound": "1542.49",
                "Upper_Bound": "6706.13",
            },
            "28/01/2021": {
                "Forecast_Price": "4176.21",
                "Lower_Bound": "1489.90",
                "Upper_Bound": "6862.53",
            },
            "27/02/2021": {
                "Forecast_Price": "4131.91",
                "Lower_Bound": "1389.01",
                "Upper_Bound": "6874.82",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4207.47",
                "Lower_Bound": "3632.22",
                "Upper_Bound": "4782.72",
            },
            "02/08/2020": {
                "Forecast_Price": "4161.94",
                "Lower_Bound": "3531.62",
                "Upper_Bound": "4792.27",
            },
            "03/08/2020": {
                "Forecast_Price": "4177.18",
                "Lower_Bound": "3380.20",
                "Upper_Bound": "4974.16",
            },
            "04/08/2020": {
                "Forecast_Price": "4143.22",
                "Lower_Bound": "3446.03",
                "Upper_Bound": "4840.40",
            },
            "05/08/2020": {
                "Forecast_Price": "4207.79",
                "Lower_Bound": "3161.89",
                "Upper_Bound": "5253.68",
            },
            "06/08/2020": {
                "Forecast_Price": "4185.62",
                "Lower_Bound": "3483.40",
                "Upper_Bound": "4887.85",
            },
            "07/08/2020": {
                "Forecast_Price": "4203.06",
                "Lower_Bound": "3602.46",
                "Upper_Bound": "4803.67",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "3854.48",
                "Lower_Bound": "1880.10",
                "Upper_Bound": "5828.87",
            },
            "15/08/2020": {
                "Forecast_Price": "3862.18",
                "Lower_Bound": "1882.38",
                "Upper_Bound": "5841.99",
            },
            "22/08/2020": {
                "Forecast_Price": "3870.17",
                "Lower_Bound": "1887.31",
                "Upper_Bound": "5853.03",
            },
            "29/08/2020": {
                "Forecast_Price": "3878.57",
                "Lower_Bound": "1888.71",
                "Upper_Bound": "5868.43",
            },
            "05/09/2020": {
                "Forecast_Price": "3886.56",
                "Lower_Bound": "1891.11",
                "Upper_Bound": "5882.00",
            },
            "12/09/2020": {
                "Forecast_Price": "3894.17",
                "Lower_Bound": "1893.36",
                "Upper_Bound": "5894.97",
            },
            "19/09/2020": {
                "Forecast_Price": "3901.66",
                "Lower_Bound": "1898.13",
                "Upper_Bound": "5905.19",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "3895.00",
                "Lower_Bound": "1903.27",
                "Upper_Bound": "5886.74",
            },
            "30/09/2020": {
                "Forecast_Price": "3920.51",
                "Lower_Bound": "1889.02",
                "Upper_Bound": "5952.01",
            },
            "30/10/2020": {
                "Forecast_Price": "3981.34",
                "Lower_Bound": "1918.84",
                "Upper_Bound": "6043.85",
            },
            "29/11/2020": {
                "Forecast_Price": "3996.55",
                "Lower_Bound": "1903.54",
                "Upper_Bound": "6089.57",
            },
            "29/12/2020": {
                "Forecast_Price": "4008.97",
                "Lower_Bound": "1889.68",
                "Upper_Bound": "6128.26",
            },
            "28/01/2021": {
                "Forecast_Price": "4014.81",
                "Lower_Bound": "1870.71",
                "Upper_Bound": "6158.92",
            },
            "27/02/2021": {
                "Forecast_Price": "3969.59",
                "Lower_Bound": "1802.92",
                "Upper_Bound": "6136.26",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "3347.79",
                "Lower_Bound": "2815.11",
                "Upper_Bound": "3880.47",
            },
            "02/08/2020": {
                "Forecast_Price": "3320.02",
                "Lower_Bound": "2741.72",
                "Upper_Bound": "3898.33",
            },
            "03/08/2020": {
                "Forecast_Price": "3335.85",
                "Lower_Bound": "2817.00",
                "Upper_Bound": "3854.71",
            },
            "04/08/2020": {
                "Forecast_Price": "3316.89",
                "Lower_Bound": "2918.20",
                "Upper_Bound": "3715.59",
            },
            "05/08/2020": {
                "Forecast_Price": "3353.92",
                "Lower_Bound": "2857.41",
                "Upper_Bound": "3850.43",
            },
            "06/08/2020": {
                "Forecast_Price": "3373.96",
                "Lower_Bound": "2717.35",
                "Upper_Bound": "4030.56",
            },
            "07/08/2020": {
                "Forecast_Price": "3412.38",
                "Lower_Bound": "2849.70",
                "Upper_Bound": "3975.06",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4151.64",
                "Lower_Bound": "2036.21",
                "Upper_Bound": "6267.06",
            },
            "15/08/2020": {
                "Forecast_Price": "3843.84",
                "Lower_Bound": "1898.85",
                "Upper_Bound": "5788.83",
            },
            "22/08/2020": {
                "Forecast_Price": "3797.11",
                "Lower_Bound": "1874.01",
                "Upper_Bound": "5720.22",
            },
            "29/08/2020": {
                "Forecast_Price": "3587.16",
                "Lower_Bound": "1797.78",
                "Upper_Bound": "5376.54",
            },
            "05/09/2020": {
                "Forecast_Price": "4225.17",
                "Lower_Bound": "2066.06",
                "Upper_Bound": "6384.29",
            },
            "12/09/2020": {
                "Forecast_Price": "3967.07",
                "Lower_Bound": "1945.00",
                "Upper_Bound": "5989.15",
            },
            "19/09/2020": {
                "Forecast_Price": "3851.54",
                "Lower_Bound": "1897.58",
                "Upper_Bound": "5805.51",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4024.39",
                "Lower_Bound": "1932.81",
                "Upper_Bound": "6115.97",
            },
            "30/09/2020": {
                "Forecast_Price": "4098.75",
                "Lower_Bound": "2004.54",
                "Upper_Bound": "6192.97",
            },
            "30/10/2020": {
                "Forecast_Price": "4141.81",
                "Lower_Bound": "2049.29",
                "Upper_Bound": "6234.33",
            },
            "29/11/2020": {
                "Forecast_Price": "4157.59",
                "Lower_Bound": "2072.80",
                "Upper_Bound": "6242.38",
            },
            "29/12/2020": {
                "Forecast_Price": "4171.62",
                "Lower_Bound": "2098.89",
                "Upper_Bound": "6244.36",
            },
            "28/01/2021": {
                "Forecast_Price": "4186.89",
                "Lower_Bound": "2125.26",
                "Upper_Bound": "6248.51",
            },
            "27/02/2021": {
                "Forecast_Price": "4135.70",
                "Lower_Bound": "2106.63",
                "Upper_Bound": "6164.78",
            },
        },
    },
    {
        "Daily": {
            "01/08/2020": {
                "Forecast_Price": "4777.65",
                "Lower_Bound": "3913.29",
                "Upper_Bound": "5642.01",
            },
            "02/08/2020": {
                "Forecast_Price": "4775.64",
                "Lower_Bound": "3958.08",
                "Upper_Bound": "5593.21",
            },
            "03/08/2020": {
                "Forecast_Price": "4774.54",
                "Lower_Bound": "3775.87",
                "Upper_Bound": "5773.20",
            },
            "04/08/2020": {
                "Forecast_Price": "4771.38",
                "Lower_Bound": "4019.46",
                "Upper_Bound": "5523.29",
            },
            "05/08/2020": {
                "Forecast_Price": "4770.84",
                "Lower_Bound": "4154.82",
                "Upper_Bound": "5386.86",
            },
            "06/08/2020": {
                "Forecast_Price": "4774.72",
                "Lower_Bound": "4131.19",
                "Upper_Bound": "5418.25",
            },
            "07/08/2020": {
                "Forecast_Price": "4777.76",
                "Lower_Bound": "3816.33",
                "Upper_Bound": "5739.20",
            },
        },
        "Weekly": {
            "08/08/2020": {
                "Forecast_Price": "4658.85",
                "Lower_Bound": "2274.29",
                "Upper_Bound": "7043.42",
            },
            "15/08/2020": {
                "Forecast_Price": "4677.29",
                "Lower_Bound": "2284.30",
                "Upper_Bound": "7070.27",
            },
            "22/08/2020": {
                "Forecast_Price": "4693.14",
                "Lower_Bound": "2291.32",
                "Upper_Bound": "7094.96",
            },
            "29/08/2020": {
                "Forecast_Price": "4714.64",
                "Lower_Bound": "2298.12",
                "Upper_Bound": "7131.15",
            },
            "05/09/2020": {
                "Forecast_Price": "4733.36",
                "Lower_Bound": "2308.85",
                "Upper_Bound": "7157.87",
            },
            "12/09/2020": {
                "Forecast_Price": "4750.54",
                "Lower_Bound": "2318.45",
                "Upper_Bound": "7182.62",
            },
            "19/09/2020": {
                "Forecast_Price": "4765.10",
                "Lower_Bound": "2325.04",
                "Upper_Bound": "7205.17",
            },
        },
        "Monthly": {
            "31/08/2020": {
                "Forecast_Price": "4629.56",
                "Lower_Bound": "2267.60",
                "Upper_Bound": "6991.52",
            },
            "30/09/2020": {
                "Forecast_Price": "4576.19",
                "Lower_Bound": "2198.02",
                "Upper_Bound": "6954.37",
            },
            "30/10/2020": {
                "Forecast_Price": "4516.96",
                "Lower_Bound": "2118.21",
                "Upper_Bound": "6915.72",
            },
            "29/11/2020": {
                "Forecast_Price": "4468.97",
                "Lower_Bound": "2056.77",
                "Upper_Bound": "6881.17",
            },
            "29/12/2020": {
                "Forecast_Price": "4432.13",
                "Lower_Bound": "2013.58",
                "Upper_Bound": "6850.69",
            },
            "28/01/2021": {
                "Forecast_Price": "4394.14",
                "Lower_Bound": "1968.06",
                "Upper_Bound": "6820.23",
            },
            "27/02/2021": {
                "Forecast_Price": "4331.66",
                "Lower_Bound": "1900.60",
                "Upper_Bound": "6762.72",
            },
        },
    },
]

Market_Types = [
    ["Adilabad", "Cotton"],
    ["Amreli", "Other"],
    ["Annigeri", "GCH"],
    ["Anoopgarh", "American"],
    ["Arvi", "H"],
    ["Asifabad", "Cotton"],
    ["Babra", "Shanker"],
    ["Bagasara", "Other"],
    ["Balwadi", "H"],
    ["Bhattu Kalan", "American"],
    ["Bhavnagar", "Other"],
    ["Bhiloda", "Other"],
    ["Bhokar", "Other"],
    ["Bijapur", "LH"],
    ["Bilara", "Other"],
    ["Bodeli", "Shanker"],
    ["Bodeli(Hadod)", "Shanker"],
    ["Bodeli(Kalediya)", "Shanker"],
    ["Bodeli(Modasar)", "Shanker"],
    ["Botad(Haddad)", "Shanker"],
    ["Choppadandi", "Cotton"],
    ["Chotila", "Shanker"],
    ["Davangere", "MCU"],
    ["Dhandhuka", "Shanker"],
    ["Dhoraji", "H.B"],
    ["Dhrol", "Other"],
    ["Ding", "American"],
    ["Enkoor", "Cotton"],
    ["Gajsinghpur", "American"],
    ["Gharsana", "American"],
    ["Goluwala", "American"],
    ["Goluwala", "Desi"],
    ["Gondal", "H.B"],
    ["Halvad", "Other"],
    ["Hanumangarh", "Desi"],
    ["Haveri", "GCH"],
    ["Hubli (Amaragol)", "GCH"],
    ["Indravelly(Utnoor)", "Cotton"],
    ["Jaitsar", "American"],
    ["Jamnagar", "Other"],
    ["Jangaon", "Cotton"],
    ["Jetpur(Dist.Rajkot)", "Cotton"],
    ["Jhabua", "DCH"],
    ["Jobat", "Other"],
    ["Kalmeshwar", "Other"],
    ["Kapadvanj", "Other"],
    ["Karimnagar", "Cotton"],
    ["Karjan", "Shanker"],
    ["Kekri", "Other"],
    ["Khairthal", "Other"],
    ["Khammam", "Cotton"],
    ["Khetia", "H"],
    ["Kille Dharur", "Other"],
    ["Kolathur", "Other"],
    ["Konganapuram", "Other"],
    ["Kothagudem", "Cotton"],
    ["Kuber", "Cotton"],
    ["Limdi", "Shanker"],
    ["Mahuva(Station Road)", "Shanker"],
    ["Malout", "Other"],
    ["Manavdar", "Shanker"],
    ["Narkhed", "Other"],
    ["Narsampet", "Cotton"],
    ["Padampur_Rajasthan", "American"],
    ["Pandhurna", "Other"],
    ["Parbhani", "Other"],
    ["Parkal", "Cotton"],
    ["Patan", "Other"],
    ["Pilli Banga", "American"],
    ["Pilli Banga", "Desi"],
    ["Pulgaon", "Other"],
    ["Raichur", "F"],
    ["Raisingh Nagar", "American"],
    ["Rajura", "Other"],
    ["Ranebennur", "GCH"],
    ["Rawatsar", "American"],
    ["Rawla", "American"],
    ["Sadulshahar", "American"],
    ["Sangriya", "Other"],
    ["Saunsar", "H"],
    ["Savanur", "GCH"],
    ["Sendhwa", "H"],
    ["Sirsa_Haryana", "American"],
    ["Sri Karanpur", "American"],
    ["Sri Vijayanagar", "American"],
    ["Sri Vijayanagar", "Desi"],
    ["Sriganganagar", "American"],
    ["Suratgarh", "American"],
    ["Thirumangalam", "MCU"],
    ["Thirumangalam", "Other"],
    ["Uchana", "American"],
    ["Unava", "Other"],
    ["Usilampatty", "LRA"],
    ["Usilampatty", "MCU"],
    ["Usilampatty", "Other"],
    ["Vankaner", "Other"],
    ["Vikkiravandi", "Other"],
    ["Villupuram", "Other"],
    ["Visavadar", "Other"],
    ["Visnagar", "Other"],
    ["Warangal", "Cotton"],
]

print(len(PREDICTIONS))

for i in range(len(Market_Types)):
    predictions = PREDICTIONS[i]
    market = Market_Types[i][0]
    cotton_type = Market_Types[i][1]
    for period in predictions:
        for date in predictions[period]:
            Analysis.objects.create(
                cotton_type=CottonType.objects.filter(name=cotton_type)[0],
                market=Market.objects.filter(name=market)[0],
                period=period,
                date=datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d"),
                prediction=predictions[period][date]["Forecast_Price"],
                confidence_lower=predictions[period][date]["Lower_Bound"],
                confidence_upper=predictions[period][date]["Upper_Bound"],
            )
