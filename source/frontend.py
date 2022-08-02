import random
import re
import sys
import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main():
    displaytext= ""
    response = requests.get("http://10.0.3.10:8989/checkout")
    if response.status_code == 200:
        displaytext= displaytext + "\n" +response.text
    else:
        displaytext= displaytext + "\n" +"Checkout endpoint is not responding!!"

    response = requests.get("http://10.0.3.11:8990/ad")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "ad endpoint is not responding!!"

    response = requests.get("http://10.0.3.12:8991/recommend")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "recommend endpoint is not responding!!"

    response = requests.get("http://10.0.3.13:8992/payment")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "payment endpoint is not responding!!"

    response = requests.get("http://10.0.3.14:8993/emails")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "emails endpoint is not responding!!"

    response = requests.get("http://10.0.3.15:8994/productcatalog")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "productcatalog endpoint is not responding!!"

    response = requests.get("http://10.0.3.16:8995/shipping")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "shipping endpoint is not responding!!"

    response = requests.get("http://10.0.3.17:8996/currency")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "currency endpoint is not responding!!"

    response = requests.get("http://10.0.3.18:8997/carts")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "cart endpoint is not responding!!"

    response = requests.get("http://10.0.5.10:8998/redis")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "redis endpoint is not responding!!"

    return displaytext

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
