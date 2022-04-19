from __future__ import division, print_function
# coding=utf-8

# Flask utils
from flask import Flask, redirect, request, render_template, jsonify, make_response
from werkzeug.utils import secure_filename
import json

# Define a flask app
app = Flask(__name__)
# app.config['SERVER_NAME'] = 'localhost:5000'

@app.route('/', methods=['GET'])
def Home():
    return render_template('homepage.html')

@app.route('/templates', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=5000)