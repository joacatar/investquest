from flask import render_template, request, redirect, url_for
from flask import flash, abort, session, jsonify, Blueprint
import yfinance as yf

import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('investquest', __name__)


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/login', methods=['GET','POST'])
def login():
    # error = None
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        if user != 'admin' or password != 'admin':
            flash('Invalid Credentials. Please Try Again.')
        else:
            return redirect(url_for('investquest.your_account'))

    return render_template('login.html')


@bp.route('/your_account')
def your_account():
    return render_template('your-account.html')


@bp.route('/stock/<symbol>')
def get_stock_page(symbol):
    try:
        stock = yf.Ticker(symbol)
        for key, value in stock.info.items():
            print(key, ":", value)
        stock_info = {
            "regularMarketPrice": stock.info.get('previousClose', 'N/A'),
            "previousClose": stock.info.get('previousClose', 'N/A'),
            "marketCap": stock.info.get('previousClose', 'N/A')
        }
        print(stock_info)
        return render_template('stock.html', symbol=symbol, stock_info=stock_info)
    except Exception as e:
        return jsonify({"error": str(e)})



