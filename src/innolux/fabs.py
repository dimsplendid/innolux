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
    },
    "T2": {
        "q-time": {
            "PIPB": {"step": ("6110_PI2_PIC",""),   "filter": None},
            "PAUV": {"step": ("6220_PH3_PA_UV",""), "filter": None},
            "PAPB": {"step": ("6220_PH3_OVEN",""),  "filter": None},
            "BOOX": {"step": ("6310_AS1_ARO",""),   "filter": None},
            "ODFX": {"step": ("6310_AS1_LCD",""),   "filter": None},
            "SEUV": {"step": ("6310_AS1_UV_MA",""), "filter": None},
        },
        "edc": {
            "PIPR TEMP"  : {"step": (r"2CPIL\d+" , r"PreCur\d+_temp"),     "filter": None},
            "PIPR TIME"  : {"step": (r"2CPIL\d+" , r"PreCur\d+_Time"),     "filter": None},
            "PIPB TEMP"  : {"step": (r"2CPIL\d+" , r"Oven_Temp_\d+"),      "filter": None},
            "PIPB TIME"  : {"step": (r"2CPIL\d+" , r"Heating_Time"),       "filter": None},
            "PAUV"       : {"step": (r"2CPHA\d+" , r"\d-\d exposure"),     "filter": None},
            "PAPB TEMP"  : {"step": (r"2CPHA\d+" , r"Baking temp zone\d+"),"filter": None},
            "PAPB TIME"  : {"step": (r"2CPHA\d+" , r"Heating_Time"),       "filter": None},
            "BOOX TEMP"  : {"step": (r"2CASM\d+" , r"Oven_Temp_\d+"),      "filter": None},
            "BOOX TIME"  : {"step": (r"2CASM\d30", r"Heating_Time"),       "filter": None},
            "SEUV"       : {"step": (r"2CASM\dC0", r"UV_Energy"),          "filter": None},
            "SEPB TEMP"  : {"step": (r"2CASM\dD0", r"Temp"),               "filter": None},
            "SEPB TIME"  : {"step": (r"2CASM\dD0", r"Heating_Time"),       "filter": None},
            "BOOX to ODF": {"step": (r"2CASM\dB0", r"ARO_ODF_QTime"),      "filter": None},
            "ODF to SEUV": {"step": (r"2CASM\dC0", r"ODF_UV_QTime"),       "filter": None},
        },
    }
}

def edc_get(
    edc_raw: pl.DataFrame, 
    step: tuple[str, str], 
    filter: list[pl.Expr] | None = None,
) -> pl.DataFrame:
    result = (
        edc_raw.filter(
            pl.col("SUB_EQUIP_ID").str.contains(step[0]),
            pl.col("PARAM_NAME").str.contains(step[1])
        )
        # .select(
        #     "GLASS_ID", "SUB_EQUIP_ID", "PARAM_NAME", "AVG_VALUE"
        # )
        .select(
            "GLASS_ID", "AVG_VALUE"
        )
    )
    
    if filter is not None:
        result = result.filter(*filter)
    
    return result.group_by(['GLASS_ID']).mean()

def qtime_get(
    qtime_raw: pl.DataFrame, 
    step: tuple[str, str], 
    filter: list[pl.Expr] | None = None,
) -> pl.DataFrame:
    result = (
        qtime_raw.filter(
            pl.col("STEP_ID").str.contains(step[0]),
        )
        .select(
            pl.col("GLASS_ID").alias("ID"), 
            pl.col("TRACK_IN_TIME"),
            pl.col("TRACK_OUT_TIME"),
        )
    )
    
    if filter is not None:
        return result.filter(*filter)
    
    return result