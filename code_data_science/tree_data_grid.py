from IPython.display import display as ipython_display


def display(tree_data, header_name: str, columns):
    """
    Used for populating the notebook cell outputs with the Moderne tree data 
    grid mime type and data used for rendering a tree data grid in the Moderne 
    platform.

    tree_data   - a list of dictionaries where each dictionary must have a path
                  key which is a string presenting the path to the node from the 
                  root. Other keys are optional and will be used as column values.

    header_name - the header name rendered above the tree column.

    columns     - a list of dictionaries where each dictionary is a column 
                  definition. The key field is required and must match a key
                  in the tree_data dictionaries. Other keys are optional and
                  are based around MUI DataGrid column definitions.

    """
    ipython_display({
        "application/vnd.moderne.treedatagrid+json": {
            "headerName": header_name,
            "columns": columns,
            "rows": tree_data
        }
    }, raw=True)
