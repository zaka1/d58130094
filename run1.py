# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, redirect, url_for, flash,request

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1> this is a test! </h1>"
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)