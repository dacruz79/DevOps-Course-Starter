from todo_app.data.view_model import ViewModel
from todo_app.Item import Item

def test_view_model_done_items():
    # Arrange
    items = [
        Item("1","New ToDo", "To Do"),
        Item("2","Completed task", "Done")
    ]
    view_model = ViewModel(items)

    # Act
    returned_items = view_model.done_items

    # Assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == "Done"

def test_view_model_to_do_items():
    # Arrange
    items = [
        Item("1","New ToDo", "To Do"),
        Item("2","Completed task", "Done")
    ]
    view_model = ViewModel(items)

    # Act
    returned_items = view_model.to_do_items

    # Assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == "To Do"