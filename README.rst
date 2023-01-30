Code Data Science Tools for Python
==================================

Installation:

    pip install code_data_science

Usage

    from code_data_science.sort_versions import sort_versions

    >>>sort_versions(['1.1.0','1.2.0','1.3.0.RELEASE'])
    -----input

    from code_data_science.index_versions import index_versions

    >>>index_versions(['1.1.0','1.2.0','1.3.0.RELEASE'])
    -----input

This package uses doctest for testing, run :code:`doctest sort_versions.py` to run the tests.