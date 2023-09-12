import requests
import dotenv
import os

from todo_app.Item import Item

dotenv.load_dotenv()

trello_key = os.getenv("API_KEY")
trello_api_token = os.getenv("API_TOKEN")
list_name = {}

def get_board_list():
    """
    Fetches id for the name from trello

    Returns:
        id: The id of the items.
    """

    # DevOps BOW board, look to pass this in to make more dynamic
    board_id = "64f9997df2894da1f3f1c056"

    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "fields": "name,id"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    for trello_list in response_json:
        list_name.update({trello_list['name']:trello_list['id']})
    
    return list_name


def get_to_do_items():
    """
    Fetches all saved items from trello

    Returns:
        list: The list of saved items.
    """

    # DevOps BOW board, look to pass this in to make more dynamic
    board_id = "64f9997df2894da1f3f1c056"

    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "cards": "open"
        #"card_fields": "id,closed,name"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    ##l = 1
    obj_list = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            ##globals()[f'item"_{l}'] = Item.from_trello_card(card, trello_list)
            ##i_1 = Item.from_trello_card(card, trello_list)
            ##print(i_1.name + ' ' + i_1.id + ' ' + i_1.status)
            ##l += 1
            #obj_list.append(globals()[f'item_{l}'])
            obj_list.append(Item.from_trello_card(card, trello_list))

    return obj_list 


def add_item_to_list(title, description, add_to_list_name = 'To Do'):
    """
    Adds a new item with the specified title to trello board.

    Args:
        title: The title of the item.
        description: The description of the item.
        add_to_list_name: List to add item to.
    Returns:
        item: The saved item.
    """

    list_id = list_name[add_to_list_name]

    reqUrl = f"https://api.trello.com/1/cards"
    
    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "idList": list_id,
        "name": title,
        "desc": description,
        "pos": "bottom"
    }

    response = requests.post(reqUrl, params=query_params)

    response_json = response.json()
    return response_json

def change_list_of_item(card_id, changed_list_name):
    """
    Change the list the item should fall under on the trello board.

    Args:
        card_id: The id of the item.
        changed_list_name: The name of the list to go to.
    Returns:
        item: The saved item.
    """

    new_list_id = list_name[changed_list_name]
    reqUrl = f"https://api.trello.com/1/cards/{card_id}"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "idList": new_list_id
    }

    response = requests.put(reqUrl, params=query_params)

    response_json = response.json()
    return response_json
