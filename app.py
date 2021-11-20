import dash
from dash import html
from vega_datasets import data
import pandas as pd

source = data.barley()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello, World!'+str(len(source)))
])

if __name__ == '__main__':
    app.run_server(debug=True)