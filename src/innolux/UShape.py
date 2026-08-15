import os
from pathlib import Path
import polars as pl
from datetime import timedelta

from .data_processing import strptime_timedelta

def hello():
    print("hello from UShape")

def parser(
        file_path: Path,
        file_name_parser=None,
    ):
    if file_name_parser is None:
        def file_name_parser(file_name):
            _, gamma, panel_id, cond, *_ = file_name.split("_")
            return {
                "Gamma Code": gamma,
                "Condition": cond,
                "Panel ID": panel_id,
            }

    df = pl.read_csv(file_path, ignore_errors=True)
    meta = file_name_parser(file_path.name)
    return df.select(
        *[pl.lit(v).alias(k) for k, v in meta.items()], # meta data from file name parsing
        pl.col("烙印時間").map_elements(
            lambda t: strptime_timedelta(t, '%HHr%MMin%SSec') / timedelta(hours=1),
            return_dtype=float
        ).alias("Stress Time(hr)"),
        "Region",
        "Remark",
        pl.col("灰階").map_elements(lambda g: int(g[:-4]), return_dtype=int),
        pl.col("系Vcom").alias("系統 Vcom"),
        pl.col("白Vcom").alias("白格 Vcom"),
        pl.col("黑Vcom").alias("黑格 Vcom"),
        pl.col("白Fitting Vcom").alias("白格 Vcom(Fitting)"),
        pl.col("黑Fitting Vcom").alias("黑格 Vcom(Fitting)"),
        pl.col("白U最低Lum(%)").alias("白格最佳 Vcom 亮度(%)"),
        pl.col("黑U最低Lum(%)").alias("黑格最佳 Vcom 亮度(%)"),
        pl.col("白U Lum@系Vcom(%)").alias("W(%)"),
        pl.col("黑U Lum@系Vcom(%)").alias("B(%)"),
        pl.col("Total亮度差(W-B)@系Vcom(%)").alias("Total亮度差(%)"),
        pl.col("AC IS亮度差(W-B)(%)").alias("AC IS亮度差(%)"),
        pl.col("DC IS亮度差(W-B)(%)").alias("DC IS亮度差(%)"),
        '白U擬合R^2',
        '黑U擬合R^2',
        '高阻抗PI黑階補值',
        '高阻抗PI灰階補值',
        '高阻抗PI只補黑階補值',
        '中低阻抗PI白階補值',
        '中低阻抗PI灰階補值',
    )

def batch_parser(
    folder: Path, 
    file_parser=parser,
):
    _, _, files = next(os.walk(folder))
    
    ushape_logs = [ file_parser(folder / file) for file in files ]
    
    return pl.concat(ushape_logs)

def w_drift_gen(df: pl.DataFrame):
    diff_expr = (
        pl.col("白格 Vcom(Fitting)")
        .filter(
            pl.col("Stress Time(hr)") == 6,
            pl.col("灰階") == 128,
        ).first()
        .sub(
            pl.col("白格 Vcom(Fitting)")
            .filter(
                pl.col("Stress Time(hr)") == 0,
                pl.col("灰階") == 128,
            ).first()
        ).mul(10)
        .alias("W drift")
    )

    return (
        df
        .group_by([
            'Gamma Code',
            'Condition',
            "VGLO",
            "Vw",
            'Panel ID',
            "Region",
        ], maintain_order=True)
        .agg(diff_expr)
    )
    

