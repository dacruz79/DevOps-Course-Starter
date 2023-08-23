from flask import Flask, render_template, session, request, redirect, url_for

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
# def index():
#     return render_template('index.html')

def index():
    data = get_items()
    return render_template('index.html', len = len(data), data=data )

@app.route('/add_new_item', methods=['post'])
def add_new_item():

    item_status = request.form['item_status']
    item_title = request.form['item_title']
    data = get_items()
    last_item = len(data) - 1
    item_id = data[last_item]["id"] + 1

    if item_status == '':
        item_status = 'Not Started'
    if item_title == '':
        error_text = 'No title provided!'
        return (error_text)
    
    add_item(item_title)
    return redirect(url_for('index'))
