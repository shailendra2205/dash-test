"""This module contains functions that use plotly express to visualize the
two graphs using the provided data and returns the figures to the dash app.
"""

import plotly.express as px


def generate_stacked_line_plot(data):

    """This function generates the stacked line chart"""

    data_df = data
    data_df = data_df.groupby(["year", "site"]).agg({"yield": "median"})
    data_df.columns = ["Median of yield"]
    data_df = data_df.reset_index()

    fig = px.line(
        data_df,
        x="year",
        y="Median of yield",
        color="site",
        title="Median of Site Yields vs. Year",
        width=300,
        height=600,
        labels={  # replaces default labels by column name
            "year": "<b>year</b>",
            "Median of yield": "<b>Median of yield</b>",
            "site": "<b>site</b>",
        },
        category_orders={  # replaces default order by column name
            "site": sorted(data_df["site"].unique().tolist(), reverse=False)
        },
        color_discrete_map={  # replaces default color mapping by value
            "Crookston": "#5578A4",
            "Duluth": "#E78A39",
            "Grand Rapids": "#D4605B",
            "Morris": "#81B5B2",
            "University Farm": "#689F55",
            "Waseca": "#E9CA58",
        },
        template="simple_white",
    )

    fig.update_yaxes(
        tickmode="linear",
        range=[0, 55],
        tick0=0,
        dtick=5,
        showgrid=True,
    )

    fig.update_xaxes(
        tickmode="linear",
        range=[1930.5, 1932.5],
        dtick=1,
        showgrid=False,
        tickangle=-90,
    )

    return fig


def generate_stacked_bar_plot(data):

    """This function generates the stacked bar chart"""

    data_df = data
    data_df = data_df.groupby(["variety", "site"]).agg({"yield": "sum"})
    data_df.columns = ["Sum of yield"]
    data_df["Sum of yield"] = data_df["Sum of yield"].apply(lambda x: round(x, 2))
    data_df.sort_values("variety", ascending=False, inplace=True)
    data_df.sort_values("site", ascending=False, inplace=True)
    data_df = data_df.reset_index()

    fig = px.bar(
        data_df,
        x="variety",
        y="Sum of yield",
        color="site",
        title="Sum of Yield vs. Variety with Site breakdown",
        width=500,
        height=600,
        labels={  # replaces default labels by column name
            "variety": "<b>variety</b>",
            "Sum of yield": "<b>Sum of yield</b>",
            "site": "<b>site</b>",
        },
        category_orders={  # replaces default order by column name
            "variety": sorted(data_df["variety"].unique().tolist()),
            "site": sorted(data_df["site"].unique().tolist(), reverse=True),
        },
        color_discrete_map={  # replaces default color mapping by value
            "Crookston": "#5578A4",
            "Duluth": "#E78A39",
            "Grand Rapids": "#D4605B",
            "Morris": "#81B5B2",
            "University Farm": "#689F55",
            "Waseca": "#E9CA58",
        },
        template="simple_white",
    )

    fig.update_yaxes(
        tickmode="linear", linewidth=0, range=[0, 500], tick0=0, dtick=50, showgrid=True
    )

    fig.update_xaxes(showgrid=False, tickangle=-90)

    fig.update_layout(
        legend={"traceorder": "reversed"},
        barmode="relative",
        bargap=0.0,
        bargroupgap=0.2,
        boxmode="group",
        boxgap=0.0,
        boxgroupgap=0.0,
    )

    return fig
