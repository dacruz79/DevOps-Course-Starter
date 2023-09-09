import requests
import dotenv
import os

dotenv.load_dotenv()

trello_key = os.getenv("API_KEY")
trello_api_token = os.getenv("API_TOKEN")

def get_to_do_items():
    """
    Fetches all saved items from trello

    Returns:
        list: The list of saved items.
    """

    open_list_id = "64f9997df2894da1f3f1c05d"

    # DevOps BOW board, look to pass this in to make more dynamic
    board_id = "64f9997df2894da1f3f1c056"

    # reqUrl = f"https://api.trello.com/1/lists/{open_list_id}/cards"
    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "cards": "open",
        "card_fields": "id,closed,name"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)
    return cards

def add_to_do_item(title, description):
    """
    Adds a new item with the specified title to trello board.

    Args:
        title: The title of the item.
        description: The description of the item.
    Returns:
        item: The saved item.
    """

    # DevOps BOW board, look to pass this in to make more dynamic
    to_do_board_id = "64f9997df2894da1f3f1c05d"

    reqUrl = f"https://api.trello.com/1/cards"
    
    query_params = {
        "key": trello_key,
        "token": trello_api_token,
        "idList": to_do_board_id,
        "name": title,
        "desc": description,
        "pos": "bottom"
    }

    response = requests.post(reqUrl, params=query_params)

    response_json = response.json()
    print(response_json)
    return response_json
