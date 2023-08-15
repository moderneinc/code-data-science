from typing import TypeAlias

"""
This file contains type aliases to use for notebook parameters (via papermill).
Papermill allows parameters to be any type but these type aliases are intended
to be used to make the experience of running visualizations consistent.
"""
String: TypeAlias = str
Boolean: TypeAlias = bool
StringList: TypeAlias = list[str]
