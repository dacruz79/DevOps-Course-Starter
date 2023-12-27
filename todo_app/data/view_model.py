class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        items = []
        for item in self._items:
            status = item.status
            if status == 'Done':
                items.append(item)
    
        return items
    
    @property
    def doing_items(self):
        return []
    
    @property
    def to_do_items(self):
        items = []
        for item in self._items:
            status = item.status
            if status == 'To Do':
                items.append(item)
    
        return items
    

