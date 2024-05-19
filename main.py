import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = 'ab22c749a02b458288392120240605'
BASE_URL = 'http://api.weatherapi.com/v1'

@app.route('/')
def index():
    return 'hello!'

# @app.route('/about')
# def api():
#     return jsonify({'data': 'It is now working!'})

# Weather prediction for today
@app.route('/weather/today/<location>')
def weather_today(location):
    url = f'{BASE_URL}/forecast.json?key={API_KEY}&q={location}&days=1&aqi=no&alerts=no'
    response = requests.get(url)
    return jsonify(response.json())

# Weather prediction for the current week
@app.route('/weather/week/<location>')
def weather_week(location):
    url = f'{BASE_URL}/forecast.json?key={API_KEY}&q={location}&days=7&aqi=yes&alerts=yes'
    response = requests.get(url)
    return jsonify(response.json())


# Weather prediction for specified date
@app.route('/weather/future/<location>/<date>')
def weather_future(location, date):
    url = f'{BASE_URL}/future.json?key={API_KEY}&q={location}&dt={date}'
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)

