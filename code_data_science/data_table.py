import os
import csv
from io import StringIO

from typing import Union

import pandas as pd
from pandas import DataFrame

FilePath = Union[str, "PathLike[str]"]


def _strip_comments(filepath: FilePath) -> StringIO:
    # pandas comment="#" strips both whole lines and inline occurrences, even inside quoted cells,
    # so it would break cells containing code with #
    with open(filepath, 'r') as f:
        lines = [line for line in f if not line.lstrip().startswith('#')]
    return StringIO(''.join(lines))


def read_csv(sample: FilePath, *args, **kwargs) -> DataFrame:
    source = _strip_comments(os.environ.get('NB_DATA_TABLE', sample))
    return pd.read_csv(source, on_bad_lines='skip', skip_blank_lines=True, quoting=csv.QUOTE_ALL, *args, **kwargs)
