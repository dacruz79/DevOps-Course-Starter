from flask import Flask, render_template, session, request, redirect, url_for, json

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item

from todo_app.data.trello_items import get_to_do_items, add_item_to_list, change_list_of_item, get_board_list

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')


def index():
    get_board_list()
    data = get_to_do_items()
    return render_template('index.html', data=data )

@app.route('/add_new_item', methods=['post'])
def add_new_item():

    list_name = request.form['list_name']
    item_title = request.form['item_title']
    item_description = request.form['item_desc']

    if list_name == '':
        list_name = 'To Do'
    if item_title == '':
        error_text = 'No title provided!'
        return (error_text)
    
    add_item_to_list(item_title, item_description,list_name)
    return redirect(url_for('index'))

@app.route('/complete', methods=['post'])
def complete():
    card_id = request.form.get("Complete")
    
    change_list_of_item(card_id,'Done')
    
    return redirect(url_for('index'))