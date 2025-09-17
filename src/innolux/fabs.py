from innolux import *

fabs = {
    "T1": {
        "q-time":{
            "PIPB": [
                "1CPIL1A1",
                "1CPIL1A2",
                "1CPIL1A3",
                "1CPIL1A4",
                "1CPIL2A1",
                "1CPIL2A2",
                "1CPIL2A3",
                "1CPIL2A4",
            ],
            "PAUV": [
                "1CPHA110",
                "1CPHA210",
            ],
            "PAPB": [
                "1CPAO121",
                "1CPAO122",
                "1CPAO123",
                "1CPAO124",
                "1CPAO221",
                "1CPAO222",
            ],
            "BOOX": [
                "1CASM120",
                "1CASM130",
                "1CASM220",
                "1CASM230",
                "1CASM320",
                "1CASM330",
            ],
            "LCDP": [
                "1CASM191",
                "1CASM192",
                "1CASM193",
                "1CASM194",
                "1CASM291",
                "1CASM292",
                "1CASM293",
                "1CASM294",
                "1CASM391",
                "1CASM392",
                "1CASM393",
            ],
            "ODFX": [
                "1CASM1H3",
                "1CASM1H4",
                "1CASM1H7",
                "1CASM1H8",
                "1CASM2H3",
                "1CASM2H4",
                "1CASM2H7",
                "1CASM2H8",
                "1CASM3H3",
                "1CASM3H4",
            ],
            "SEUV": [
                "1CASM1J2",
                "1CASM1J3",
                "1CASM1J5",
                "1CASM1J6",
                "1CASM2J2",
                "1CASM2J3",
                "1CASM2J5",
                "1CASM2J6",
                "1CASM3J2",
                "1CASM3J5",
                "1CASM3J6",
            ]
        },
        "edc": {
            "PIPR TEMP": {"step": ("1CPIL", "PreCur[1-4]_temp"), "filter": None},
            "PIPR TIME": {"step": ("1CPIL", "Heater_Time"),      "filter": None},
            "PIPB TEMP": {"step": ("1CPIL", "Oven[A-D]_Temp"),   "filter": None},
            "PIPB TIME": {"step": ("1CPIL", "Heating_Time"),     "filter": None},
            "PAUV"     : {"step": ("1CPHA", "S[1-2]_EXP_MON"),   "filter": [pl.col("AVG_VALUE") > 100]},
            "PAPB TEMP": {"step": ("1CPAO", "Heating_Temp"),     "filter": None},
            "PAPB TIME": {"step": ("1CPAO", "Heating_Time"),     "filter": None},
            "BOOX TEMP": {"step": ("1CASM", "Current_Temp"),     "filter": None},
            "BOOX TIME": {"step": ("1CASM", "HEAT_TIME"),        "filter": None},
            "ODFX Q2"  : {"step": ("1CASM", "ASMQ2_TIME"),       "filter": None}, # ODFX in -> SEUV out
            "SEUV"     : {"step": ("1CASM", "(?i)uv_energy_2"),  "filter": None},
            "SEPB TEMP": {"step": ("1CASM", "Oven_temp"),        "filter": None},
            "SEPB TIME": {"step": ("1CASM", "HeatingTime"),      "filter": None},
        }
    }
}