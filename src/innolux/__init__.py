# prelude packages

import os
from pathlib import Path

import numpy as np
import polars as pl

# matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data_path = Path(os.path.abspath("../../data"))