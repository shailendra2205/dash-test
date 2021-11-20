# A Sample Dash Application that plots two graphs

## Structure of the Dash App

![Structure](https://github.com/shailendra2205/dash-test/blob/main/screenshots/structure.png?raw=true "Structure")

## Running the Dash App

### Step 1. Create a new folder for your project:

```mkdir dash_app_example```

```cd dash_app_example```

### Step 2. Clone the repository and Use a virtualenv to run the application

```virtualenv venv # creates a virtualenv called "venv"```

```source venv/bin/activate # uses the virtualenv```

virtualenv creates a fresh Python instance. You will need to reinstall the app's dependencies with this virtualenv:

```pip install dash```

```pip install plotly```

```pip install -r requirements.txt```


The app.py is the main dash application which can be run using ```python3 app.py``` .


### Data Source

The data source for the visualizations is the Barley dataset which is imported using the vega-datasets python package from the altair library.


### Graph Visualization Examples

![Graph 1](https://github.com/shailendra2205/dash-test/blob/main/screenshots/plot_1.png?raw=true "Graph 1")

![Graph 2](https://github.com/shailendra2205/dash-test/blob/main/screenshots/plot_2.png?raw=true "Graph 2")


