from flask import Flask, render_template, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
# Note you need to create a config.py file 
from config import db_username, db_password


# Create app instance
app = Flask(__name__)
# Database Setup using SQLAlchmy ORM
engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost:5432/covid_modality_db")
conn = engine.connect()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/plotly')
def plotly():
    return render_template('index.html')

@app.route('/plotly_dash')
def map_leaf():
    return render_template('plotly_dash.html') 
 

@app.route("/state_list")
def income():

    df1 = pd.read_sql("""SELECT DISTINCT state 
        FROM covid
		Group BY state
		ORDER BY state;""",conn)

    income_results = df1.to_json()
    return income_results
    
@app.route("/year-list")
def state():

    df2 = pd.read_sql("""SELECT DISTINCT year
          FROM covid;     
        """,conn)

    census_results = df2.to_json()
    return census_results


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)