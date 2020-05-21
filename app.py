import json
import random
from flask import render_template
from flask import request
from flask import Flask
from flask import redirect


app = Flask(__name__)


@app.route('/')
def get():
    '''
    Returns items
    '''
    with open('db.txt') as f:
        items = json.load(f)
    return render_template(
        'index.html',
        items=items
    )


@app.route('/post', methods=['POST'])
def post():
    '''
    Updates items
    '''
    item = request.form['item']
    quantity = request.form['quantity']
    with open('db.txt') as f:
        items = json.load(f)
    items.update({item: quantity})
    with open('db.txt', 'w') as f:
        json.dump(items, f)
    return redirect('/')


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
        return render_template('post.html', items=items)


@app.route('/remove_items', methods=['GET', 'POST'])
def remove_items():
    '''
    Delete items and Quantity from db.txt
    '''
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            del items[item]
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('remove_items.html', items=items)


@app.route('/surprise')
def surprise():
    with open('db.txt') as f:
        items = json.load(f)
        rand = random.choice(list(items))
    return render_template('surprise.html', rand=rand)


# @app.route('/lottery', methods=["POST"])
# def lottery():
#     item = request.form['item']
#     quantity = request.form['quantity']
#     with open('db2.txt', 'r') as f:
#         items = json.load(f)
#         rand = random.choice(list(items))
#     items.update({item: quantity})
#     with open('db2.txt', 'w') as f:
#         json.dump(items, f)
#     return render_template('lottery.html', items=items, rand=rand)

@app.route('/lottery', methods=['GET', 'POST'])
def lottery():
    with open('db2.txt') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            items.update({item: quantity})
        with open('db2.txt', 'w') as f:
            json.dump(items, f)
        winner = None
        if len(items) > 5:
            winner = random.choice(list(items))
        return render_template('lottery.html', items=items, winner=winner)
