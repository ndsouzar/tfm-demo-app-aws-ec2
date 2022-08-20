import random
import re
import sys
import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/checkout')
def checkout():
    displaytext = ""
    response = requests.get("http://10.0.3.11:8990/ad")
    if response.status_code == 200:
        with open('./app/templates/checkout.json', 'r') as myfile:
            data = myfile.read()
            displaytext= "Checkout > Ad: " + data +response.text
        return render_template('web.html', title="page", jsonfile=jsonify(displaytext))
    else:
        displaytext= displaytext + "\n" +"ad endpoint is not responding!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8989,debug=True)
