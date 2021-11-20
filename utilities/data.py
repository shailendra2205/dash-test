"""This is a module that just fetches and returns the dataset used by the dash app
"""

from vega_datasets import data


def fetch_data_source():

    """This function tries to fetch the dataset from the vega-datasets package
    and returns None in case of any error/exception
    """

    try:
        source = data.barley()
        return source
    except Exception as error:
        return str(error)
