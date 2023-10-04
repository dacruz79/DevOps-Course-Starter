from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config

from todo_app.data.trello_items import get_to_do_items, add_item_to_list, change_list_of_item, get_board_list, list_name

from todo_app.data.view_model import ViewModel
from todo_app.Item import Item

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config())
    
    # All the routes and setup code etc
    # e.g.
    # @app.route('/')
    # def index():
    #     ...
    

    @app.route('/')

    def index():
        get_board_list()
        items = get_to_do_items()

        item_list: list[Item] = []

        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/add_new_item', methods=['post'])
    def add_new_item():

        list_status = request.form['list_name']
        item_name = request.form['item_title']
        item_description = request.form['item_desc']

        found = 0
        for name in list_name.keys():
            if list_status == name:
                found = 1

        if not found:
            error_text  = 'List \'' + list_status + '\' not supported.'
            return (error_text)

        if item_name == '':
            error_text = 'No title provided!'
            return (error_text)
        
        add_item_to_list(item_name, item_description,list_status)
        return redirect(url_for('index'))

    @app.route('/complete', methods=['post'])
    def complete():
        card_id = request.form.get("Complete")
        
        change_list_of_item(card_id,'Done')
        
        return redirect(url_for('index'))
    return app
