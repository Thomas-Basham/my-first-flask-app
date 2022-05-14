import random

import requests
from flask import Flask

app = Flask(__name__)

url = "https://fakestoreapi.com/products/"


@app.route("/")
def index():
    return "Hello Mothefuckin world"


# @app.route("/api/<num>")
# def get_product(num):
#     # if responses[num]:
#     #     return responses[num]
#     # else:
#     if num:
#         data = requests.get(url + num)
#         parsed_data = data.json()
#     responses[num] = parsed_data
#     return responses

# responses = {}
# print(responses)
# labels = [row[0] for row in responses]
# values = [row[1] for row in responses]
#
#
# @app.route()
# def show_chart()




# # url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
# url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=1MIN&time_start=2022-01-01T00:00:00&time_end=2022-05-10T00:00:00'
# headers = {'X-CoinAPI-Key': '545A4363-65FD-4F81-A022-E910AE739497'}
# response = requests.get(url, headers=headers)
# print(response)
# data = response.json()
# print(data)


