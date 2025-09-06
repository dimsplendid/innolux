# Innolux

Summarize and reconstruct the function I used in Innolux.

## Project Layout

```
.
├── data/                       # For all job-related data, maybe using pgsql or just excel files
├── docs/                       # Documentation, reports, or a README for each project
├── notebooks/                  # Jupyter notebooks
│   ├── project_A/
│   │   ├── analysis_1.ipynb
│   │   └── analysis_2.ipynb
│   └── project_B/
│       ├── exploratory_data_analysis.ipynb
│       └── final_report.ipynb
├── src/                     
│   └── innolux/                # All reusable Python code
│       ├── __init__.py         # Makes 'src' a package
│       ├── data_processing.py
│       ├── visualization.py
│       └── utils.py
├── tests/                      # Unit tests for the code in 'src/'
├── pyproject.toml              # Project metadata and dependencies
└── README.md                   # A main project description
```

## Install

```bash
uv sync
overlay use .venv/Scripts/activate.nu # change by your shell
uv pip install -e .                   # install package in editable mode.
```

## Usage

```python
# jupyter notebooks
%load_ext autoreload
%autoreload 2
from innolux.utils import (...)
from innolux.data_processing import (...)
from innolux.visualization import (...)

...
```

