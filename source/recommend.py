import random
import re
import sys
from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/recommend')
def recommend():
    return render_template('recommended.json')

if __name__ == '__main__':
    app.run(host='localhost',port=8991,debug=True)
