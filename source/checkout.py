import random
import re
import sys
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/checkout')
def checkout():
    return render_template('checkout.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8989,debug=True)
