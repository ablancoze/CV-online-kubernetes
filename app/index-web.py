#import de las librerias
from datetime import datetime
import postgres
from flask import Blueprint, render_template, request, flash, redirect, url_for

#variable app para inidicar a flask las rutas de los comandos back
app = Flask(__name__)

#    
@app.route('/')
def index():

    return render_template("cv-alvaro.html")