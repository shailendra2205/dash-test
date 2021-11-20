from vega_datasets import data

def fetch_data_source():
    try:
        source = data.barley()
        return source
    except:
        return None