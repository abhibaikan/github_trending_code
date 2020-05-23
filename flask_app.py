# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:25:49 2020

@author: ab
"""

from flask import Flask, render_template
app=Flask(__name__)


@app.route("/")
def display():
    with open('output.txt', 'r') as f:
      return render_template('index.html', text=f.read())

if __name__=="__main__":
    app.run(debug=True)
