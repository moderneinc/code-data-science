import os
import csv

from typing import Union

import pandas as pd
from pandas import DataFrame

FilePath = Union[str, "PathLike[str]"]


def _count_leading_comments(filepath: FilePath) -> int:
    # Data table metadata (`# @name ...`) only precedes the header. Skipping just those lines lets
    # pandas read the file directly; a `#` line further down is inside a quoted multi-line cell.
    n = 0
    with open(filepath, 'r') as f:
        for line in f:
            if not line.lstrip().startswith('#'):
                break
            n += 1
    return n


def read_csv(sample: FilePath, *args, **kwargs) -> DataFrame:
    filepath = os.environ.get('NB_DATA_TABLE', sample)
    return pd.read_csv(filepath, skiprows=_count_leading_comments(filepath), on_bad_lines='skip',
                       skip_blank_lines=True, quoting=csv.QUOTE_ALL, *args, **kwargs)
