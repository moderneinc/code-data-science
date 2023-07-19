from pandas import DataFrame
from IPython.display import display

def moderne_data_grid(df: DataFrame):
    """
    Converts the dataframe to a format that can be consumed by the Moderne data grid.
    Calling this will result in the data frame passed being rendered as a Moderne data grid
    """
    csv_data = df.to_csv(index=False).split('\n')

    # Remove empty lines (likely to always be one at the end)
    csv_data = list(filter(None, csv_data))

    # Create the output dictionary
    output_data = {
        "application/vnd.moderne.datagrid+json": csv_data
    }

    display(output_data, raw=True)