import csv
from enum import Enum
from pandas import DataFrame
from IPython.display import display as ipython_display


class ColumnType(str, Enum):
    """
    Enum for the column types supported by the moderne data grid
    """
    LINK = "link"


def display(df: DataFrame, column_types=None):
    """
    Converts the dataframe to a format that can be consumed by the moderne data grid.
    Calling this will result in the data frame passed being rendered as a moderne data grid on the dashboard

    You can also pass a dictionary where the keys are the column names and the values are the column types.
    To have greater control of how the data grid is rendered.
    """
    line_terminator = "|^~^|"
    csv_data = df.to_csv(index=False,quoting=csv.QUOTE_MINIMAL, lineterminator=line_terminator).split(line_terminator)

    # Remove empty lines (likely to always be one at the end)
    csv_data = list(filter(None, csv_data))

    # Create the output dictionary
    ipython_display({
        "application/vnd.moderne.datagrid+json": {
            "rows": csv_data,
            "columnTypes": column_types
        }
    }, raw=True)
