from flask import Flask, url_for, render_template, request
 #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

from markupsafe import Markup

import os
import json

app = Flask(__name__)


@app.route("/")
def render_main():
    return render_template('about.html')
    
@app.route("/causes")
def render_causes():
    return render_template('causes.html')
    
@app.route("/health")
def render_health():
    return render_template('healthImpacts.html')
    
@app.route("/attacks")
def render_attacks():
    return render_template('attacks.html')
    
@app.route("/gov")
def render_gov():
    return render_template('government.html')
    
@app.route("/solutions")
def render_solutions():
    return render_template('solutions.html')
    
        
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
    

if __name__=="__main__":
    app.run(debug=False)