from flask import Flask, url_for, render_template, request
 #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

from markupsafe import Markup

import os
import json

app = Flask(__name__)


@app.route("/")
def render_main():
    return render_template('home.html')
    
    