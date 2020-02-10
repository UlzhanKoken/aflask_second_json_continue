import json
from flask import render_template
from flask import request
from flask import Flask
from flask import redirect


app = Flask(__name__)


@app.route('/')
def get():
    with open('db.txt') as f:
        items = json.load(f)
    return render_template(
        'index.html',
        items=items
    )


@app.route('/post', methods=['POST'])
def post():
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












# app = Flask(__name__)


# @app.route('/')
# def get():
#     with open('db.txt') as f:
#         tasks = json.load(f)
#     return render_template(
#         'index.html',
#         tasks=tasks
#     )


# @app.route('/post', methods=['POST'])
# def post():
#     task = request.form['task']
#     with open('db.txt') as f:
#         tasks = json.load(f)
#     tasks.append(task)
#     with open('db.txt', 'w') as f:
#         json.dump(tasks, f)
#     return 'Success'



# app = Flask(__name__)


# @app.route('/')
# def index():
#     '''
#     Return index page of the app
#     '''
#     return render_template('index.html')


# @app.route('/items', methods=['GET', 'POST'])
# def items():
#     '''
#     Returns items page
#     Loads data from db.txt as json
#     '''
#     with open('db.txt', 'r') as f:
#         items = json.load(f)
#         if request.method == 'POST':
#             item = request.form['item']
#             quantity = request.form['quantity']
#             items.update({item: quantity})
#             with open('db.txt', 'w') as f2:
#                 json.dump(items, f2)
#         return render_template('post.html', items=items)


# @app.route('/remove_items', methods=['GET', 'POST'])
# def remove_items():
#     '''
#     Delete items and Quantity from db.txt
#     '''
#     with open('db.txt', 'r') as f:
#         items = json.load(f)
#         if request.method == 'POST':
#             item = request.form['item']
#             del items[item]
#             with open('db.txt', 'w') as f2:
#                 json.dump(items, f2)
#         return render_template('remove_items.html', items=items)

#-----------------------------------------------------------------











# @app.route('/post', methods=['GET', 'POST'])
# def post():
#     task = ''
#     with open('db.txt', 'r') as f:
#         tasks = json.load(f)
#     if request.method == 'POST':
#         task = request.form['data']
#         with open('db.txt', 'w') as f2:
#             json.dump(tasks, f2)
#         tasks.append(task)
#     return render_template('post.html', tasks=tasks)

# @app.route('/post', methods=['POST'])
# def post():
#     with open('db.txt', 'r') as f:
#         tasks = json.load(f)
#         if request.method == 'POST':
#             task = request.form['task']
#             with open('db.txt', 'w') as f2:
#                 json.dump(tasks, f2)
#             tasks.append(task)
#         return render_template('post.html', tasks=tasks)


