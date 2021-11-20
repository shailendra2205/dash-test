import dash
from dash import html
import dash_core_components as dcc

import pandas as pd

from utilities.graph import generate_stacked_line_plot, generate_stacked_bar_plot
from utilities.data import fetch_data_source

import logging

logging.basicConfig(filename='logs.log',level=logging.INFO)

app = dash.Dash(__name__)

source = fetch_data_source()
if isinstance(source, pd.DataFrame):
    app.logger.info("Data imported successfully")
    fig_median_of_yield_vs_year = generate_stacked_line_plot(data=source)
    fig_sum_of_yield_vs_variety = generate_stacked_bar_plot(data=source)
    app.layout = html.Div([
        dcc.Graph(figure=fig_median_of_yield_vs_year),
        dcc.Graph(figure=fig_sum_of_yield_vs_variety)
    ])
else:
    app.logger.error("Failed to import data")
    app.layout = html.Div([
        html.H1("Failed to load Data")
    ])


if __name__ == '__main__':
    app.run_server(debug=True)