import requests
from flask import request, Flask, jsonify, render_template, redirect, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from flask_restful import Resource, Api
from flask import Blueprint
from project import db
from flask_login import login_required, current_user
# app = Flask(__name__)
app = Blueprint('app', __name__)
api = Api(app)


@app.route("/")
def index():
    return render_template('index.html', name=current_user.name, welcome=f'Hello, {current_user.name}')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email)





@app.route('/fruit')
def fruit():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City',
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   return render_template('graph.html', graphJSON=graphJSON, heading=f"Fruit data")


@app.route('/weather/<city>', methods=["GET", "POST"])
def weather(city):

   url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key=4be57259674a48259b9dbb74f75da13d&days=3&lat&lon'
   response = requests.get(url)
   data = response.json()
   data.keys()
   df = pd.DataFrame({'Date': [data['data'][0]['datetime'], data['data'][1]['datetime'], data['data'][2]['datetime']],
                      'Temperature': [data['data'][0]['temp'], data['data'][1]['temp'], data['data'][2]['temp']],
                      'High Temp': [data['data'][0]['max_temp'], data['data'][1]['max_temp'], data['data'][2]['max_temp']]
                      })
   fig = px.bar(df, x='Date', y='Temperature', color='High Temp', barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   if request.method == "POST":
      weather_city = request.form.get("weather_city")
      return redirect(url_for('app.weather', city=weather_city))

   return render_template('graph.html', graphJSON=graphJSON, city_name=city, heading=f"Weather for {city}")


