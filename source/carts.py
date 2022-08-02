import random
import re
import sys
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/carts')
def carts():
    return render_template('carts.json')

if __name__ == '__main__':
    app.run(host='localhost',port=8997,debug=True)
