# A Sample Dash Application that plots two graphs

## Structure of the Dash App

dash_app_example/
├── app.py
├── logs.log
├── README.md
├── requirements.txt
└── utilities
    ├── data.py
    ├── graph.py
    ├── __init__.py

## Running the Dash App

### Step 1. Create a new folder for your project:

$ mkdir dash_app_example
$ cd dash_app_example

### Step 2. Initialize the folder with git and a virtualenv

$ git init        # initializes an empty git repo
$ virtualenv venv # creates a virtualenv called "venv"
$ source venv/bin/activate # uses the virtualenv

virtualenv creates a fresh Python instance. You will need to reinstall the app's dependencies with this virtualenv:

$ pip install dash
$ pip install plotly
$ pip install -r requirements.txt

The app.py is the main dash application which can be run using ```python3 app.py``` .


### Data Source

The data source for the visualizations is the Barley dataset which is imported using the vega-datasets python package from the altair library.


### Screenshots

![Alt text](https://github.com/shailendra2205/dash-test/tree/main/screenshots/plot_1.png?raw=true "Graph 1")

![Alt text](https://github.com/shailendra2205/dash-test/tree/main/screenshots/plot_2.png?raw=true "Graph 1")


