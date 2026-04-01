from IPython.display import display as ipython_display
import base64


def display(yaml_recipe:str):
    """
    Converts YAML recipe as a string to a format that can be visualized as a code snippet.
    """
    
    # Create the output dictionary
    ipython_display({
        "application/vnd.moderne.yamlrecipe": {
            "code": base64.b64encode(yaml_recipe)
        }
    }, raw=True)
