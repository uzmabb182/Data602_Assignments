from flask import Flask, render_template, request, jsonify
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
 

@app.route("/state_list")
def state_name():

    df1 = pd.read_sql("""SELECT DISTINCT state 
        FROM covid_df
		Group BY state
		ORDER BY state;""",conn)

    state_results = df1.to_json()
    return state_results
    
@app.route("/year_list")
def year__choose():

    df2 = pd.read_sql("""SELECT DISTINCT year
          FROM covid_df
          Order By year;""",conn)

    year_results = df2.to_json()
    return year_results

@app.route("/search_state/<state>/<year>")
def state_search(state, year):

    df3 = pd.read_sql(f"""SELECT * 
          FROM covid_df 
          WHERE year = '{year}'
          AND state = '{state}';
          """,conn)

    search_state_results = df3.to_json()
    return search_state_results


@app.route("/covid_data/<year>")
def covid_results(year):

    df4 = pd.read_sql(f"""SELECT state, SUM(cases_count) AS total_cases, 
          SUM(deaths_count) AS total_deaths
          FROM covid_df
          WHERE year = '{year}'
          GROUP By state
          ORDER BY state;
          """,conn)

    covid_data_results = df4.to_json()
    return covid_data_results



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)