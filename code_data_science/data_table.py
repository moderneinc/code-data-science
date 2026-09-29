import os
import csv
import gzip

from typing import Union

import pandas as pd
from pandas import DataFrame

FilePath = Union[str, "PathLike[str]"]


def _count_leading_comments(filepath: FilePath) -> int:
    # Data table metadata (`# @name ...`) only precedes the header. Skipping just those lines lets
    # pandas read the file directly; a `#` line further down is inside a quoted multi-line cell.
    # pandas infers compression from the file name, so this pre-read has to decompress the same way.
    opener = gzip.open if str(filepath).endswith('.gz') else open
    n = 0
    with opener(filepath, 'rt') as f:
        for line in f:
            if not line.lstrip().startswith('#'):
                break
            n += 1
    return n


def read_table(filepath: FilePath, *args, **kwargs) -> DataFrame:
    """Read the data table at `filepath`, which may be gzipped, skipping its metadata preamble.

    Unlike `read_csv`, `NB_DATA_TABLE` does not override the path, so this reads the additional
    data tables a notebook receives as parameters.
    """
    return pd.read_csv(filepath, skiprows=_count_leading_comments(filepath), on_bad_lines='skip',
                       skip_blank_lines=True, quoting=csv.QUOTE_ALL, *args, **kwargs)


def read_csv(sample: FilePath, *args, **kwargs) -> DataFrame:
    return read_table(os.environ.get('NB_DATA_TABLE', sample), *args, **kwargs)
