import os
import csv

from typing import Union

import pandas as pd
from pandas import DataFrame

FilePath = Union[str, "PathLike[str]"]


def read_csv(sample: FilePath, *args, **kwargs) -> DataFrame:
    return pd.read_csv(os.environ.get('NB_DATA_TABLE', sample), on_bad_lines='skip', skip_blank_lines=True, quoting=csv.QUOTE_ALL, *args, **kwargs)
