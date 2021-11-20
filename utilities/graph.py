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
            "year": "Year",  "Median of yield": "Median of yield", "site": "Site"
        },
        category_orders={ # replaces default order by column name
            #"day": ["Thur", "Fri", "Sat", "Sun"], "sex": ["Male", "Female"]
        },
        color_discrete_map={ # replaces default color mapping by value
            #"Male": "RebeccaPurple", "Female": "MediumPurple"
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
        dtick = 1,
        showgrid=False
    )
    fig.update_layout(margin_pad=10)
    return fig

def generate_stacked_bar_plot(data):
    df = data
    df = df.groupby(['variety', 'site']).agg({'yield': 'sum'})
    df.columns = ['Sum of yield']
    df = df.reset_index()
    fig = px.bar(df, x="variety", y="Sum of yield", color="site",
            title="Sum of Yield vs. Variety with Site breakdown",
            width=600, height=600,
            labels={ # replaces default labels by column name
                "variety": "Variety",  "Sum of yield": "Sum of yield", "site": "Site"
            },
            category_orders={ # replaces default order by column name
                #"day": ["Thur", "Fri", "Sat", "Sun"], "sex": ["Male", "Female"]
            },
            color_discrete_map={ # replaces default color mapping by value
                #"Male": "RebeccaPurple", "Female": "MediumPurple"
            },
            template="simple_white"
            )
    fig.update_yaxes( # the y-axis is in dollars
        #tickprefix="$",
        tickmode = 'linear',
        range = [0, 500],
        tick0 = 0,
        dtick = 50,
        showgrid=True
    )
    fig.update_xaxes( # the y-axis is in dollars
        #tickprefix="$",
        showgrid=False
    )
    return fig
