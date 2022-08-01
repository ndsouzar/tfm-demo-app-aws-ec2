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

    response = requests.get("http://10.0.3.10:8990/ad")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "ad endpoint is not responding!!"

    response = requests.get("http://10.0.3.10:8989/recommendation")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "recommendation endpoint is not responding!!"

    response = requests.get("http://10.0.3.10:8989/payment")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "payment endpoint is not responding!!"

    response = requests.get("http://10.0.3.10:8989/emails")
    if response.status_code == 200:
        displaytext= displaytext + "\n" + response.text
    else:
        displaytext= displaytext + "\n" + "emails endpoint is not responding!!"

    return displaytext

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
