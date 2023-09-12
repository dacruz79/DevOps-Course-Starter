import requests, dotenv, os

from todo_app.Item import Item

dotenv.load_dotenv()

trello_key = os.getenv("API_KEY")
trello_api_token = os.getenv("API_TOKEN")
board_id = os.getenv("BOARD_ID")
list_name = {}

def get_board_list():
    """
    Fetches details from trello for a board

    Returns:
        name: The name of the item.
        id:   The id of the items.
    """

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
    Fetches all items from trello board.

    Returns:
        list: The list of items.
    """

    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "cards": "open"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    obj_list = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            obj_list.append(Item.from_trello_card(card, trello_list))

    return obj_list 


def add_item_to_list(title, description, list_status = 'To Do'):
    """
    Adds a new item with the specified title to trello board.

    Args:
        title:        The title of the item.
        description:  The description of the item.
        list_status:  List to add item to, defaulted to To Do
    Returns:
        item: The saved item.
    """

    list_id = list_name[list_status]

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

def change_list_of_item(card_id, list_status):
    """
    Change the list the item should fall under on the trello board.

    Args:
        card_id:     The id of the item.
        list_status: The name of the list to go to.
    Returns:
        item: The saved item.
    """

    list_id = list_name[list_status]
    reqUrl = f"https://api.trello.com/1/cards/{card_id}"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "idList": list_id
    }

    response = requests.put(reqUrl, params=query_params)

    response_json = response.json()
    return response_json
