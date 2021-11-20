"""This is a simple dash app that visualizes two graphs using plotly.
The dataset used is the Barley dataset which is imported using the
 vega-datasets python package from the altair library.
"""

import logging

import dash
from dash import html
import dash_core_components as dcc

import pandas as pd

from utilities.graph import generate_stacked_line_plot, generate_stacked_bar_plot
from utilities.data import fetch_data_source


logging.basicConfig(filename="logs.log", level=logging.INFO)

app = dash.Dash(__name__)

# fetch the data source from the vega-datasets
source = fetch_data_source()

# if data is fetched successfully, render the two graphs
if isinstance(source, pd.DataFrame):
    app.logger.info("Data imported successfully")

    # generate the graphs from the data source
    fig_median_of_yield_vs_year = generate_stacked_line_plot(data=source)
    fig_sum_of_yield_vs_variety = generate_stacked_bar_plot(data=source)

    app.layout = html.Div(
        [
            dcc.Graph(figure=fig_median_of_yield_vs_year),
            dcc.Graph(figure=fig_sum_of_yield_vs_variety),
        ]
    )

# else render an error message
else:
    app.logger.error("Failed to import data")
    app.layout = html.Div([html.H1("Failed to load Data")])


if __name__ == "__main__":
    app.run_server(debug=True)
