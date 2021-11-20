import plotly.express as px

def generate_stacked_line_plot(data):
    df = data
    df = df.groupby(['year', 'site']).agg({'yield': 'median'})
    df.columns = ['Median of yield']
    df = df.reset_index()
    fig = px.line(df, x="year", y="Median of yield", color="site", 
        title="Median of Site Yields vs. Year",
        width=300, height=600,
        labels={ # replaces default labels by column name
            "year": "<b>year</b>",  "Median of yield": "<b>Median of yield</b>", "site": "<b>site</b>"
        },
        category_orders={ # replaces default order by column name
            "site": sorted(df['site'].unique().tolist(), reverse=False)
        },
        color_discrete_map={ # replaces default color mapping by value
            "Crookston": "#5578A4", "Duluth": "#E78A39", "Grand Rapids": "#D4605B", "Morris": "#81B5B2", "University Farm": "#689F55", "Waseca": "#E9CA58"
        },
        template="simple_white"
        )
    fig.update_yaxes( # the y-axis is in dollars
        #tickprefix="$",
        tickmode = 'linear',
        range = [0, 55],
        tick0 = 0,
        dtick = 5,
        showgrid=True
    )
    fig.update_xaxes( # the y-axis is in dollars
        #tickprefix="$",
        tickmode = 'linear',
        range=[1930.5, 1932.5],
        dtick = 1,
        showgrid=False,
        tickangle=-90
    )
    # fig.update_layout(
    #     margin=dict(l=0, r=10, b=0, pad=0)
    #     )
    return fig

def generate_stacked_bar_plot(data):
    df = data
    df = df.groupby(['variety', 'site']).agg({'yield': 'sum'})
    df.columns = ['Sum of yield']
    df['Sum of yield'] = df['Sum of yield'].apply(lambda x: round(x,2))
    df.sort_values('variety', ascending=False, inplace=True)
    df.sort_values('site', ascending=False, inplace=True)
    df = df.reset_index()
    fig = px.bar(df, x="variety", y="Sum of yield", color="site",
            title="Sum of Yield vs. Variety with Site breakdown",
            width=500, height=600,
            labels={ # replaces default labels by column name
                "variety": "<b>variety</b>",  "Sum of yield": "<b>Sum of yield</b>", "site": "<b>site</b>"
            },
            category_orders={ # replaces default order by column name
                "variety": sorted(df['variety'].unique().tolist()),
                "site": sorted(df['site'].unique().tolist(), reverse=True)
            },
            color_discrete_map={ # replaces default color mapping by value
                "Crookston": "#5578A4", "Duluth": "#E78A39", "Grand Rapids": "#D4605B", "Morris": "#81B5B2", "University Farm": "#689F55", "Waseca": "#E9CA58"
            },
            template="simple_white"
            )
    fig.update_yaxes(
        tickmode = 'linear',
        linewidth=0,
        range = [0, 500],
        tick0 = 0,
        dtick = 50,
        showgrid=True
    )
    fig.update_xaxes(
        showgrid=False,
        tickangle=-90
    )
    fig.update_layout(
        legend={'traceorder': 'reversed'},
        barmode='relative',
        bargap=0.0,
        bargroupgap=0.2,
        boxmode='group',
        boxgap=0.0,
        boxgroupgap=0.0,
        # margin=dict(l=0, r=10, b=0, pad=0)
        )
    return fig
