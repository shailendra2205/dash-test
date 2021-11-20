import dash
from dash import html
from vega_datasets import data
import pandas as pd

source = data.barley()

df = pd.read_csv(source)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello, World!'+str(len(df)))
])

if __name__ == '__main__':
    app.run_server(debug=True)