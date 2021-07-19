# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom 
from model import getBeyonceImage
import os


# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
# add route for your gif results 
@app.route('/yourgif', methods = ["GET", "POST"])
def yourgif():
    # get the gif for giphy and puts the link on webpage
    user_response = "dog"
    #gif_link =getImageUrlFrom(user_response)
    gif_link = getBeyonceImage(user_response)
    print(gif_link)
    # pass url to render template and have that url appear as an image in yourgift.html
    return render_template("yourgif.html", time=datetime.now(), gif_link = gif_link)
    #add datetime.now() browser to trick our browser into updating the css if we make any changes
   
