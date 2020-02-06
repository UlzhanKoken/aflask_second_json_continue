import json
from flask import render_template
from flask import request
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    '''
    Return index page of the app
    '''
    return render_template('index.html')


@app.route('/items', methods=['GET', 'POST'])
def items():
    '''
    Returns items page
    Loads data from db.txt as json
    '''
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            items.update({item: quantity})
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('items.html', items=items)


@app.route('/remove_items', methods=['GET', 'POST'])
def remove_items():
    '''
    Delete items and Quantity from db.txt
    '''
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            del items[item]
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('remove_items.html', items=items)
