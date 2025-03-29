
from app.models.produtor_rural import ProdutorRural


class ProdutorRuralRepository:
    def __init__(self):
        self.items = []  # Lista em memória para armazenar os itens

    def add_item(self, item: ProdutorRural):
        self.items.append(item)
        return item

    def get_items(self):
        return self.items

    def get_item_by_id(self, item_id: int):
        return next((item for item in self.items if item.id == item_id), None)

    def update_item(self, item_id: int, new_item: ProdutorRural):
        for index, item in enumerate(self.items):
            if item.id == item_id:
                self.items[index] = new_item
                return new_item
        return None

    def delete_item(self, item_id: int):
        for index, item in enumerate(self.items):
            if item.id == item_id:
                del self.items[index]
                return True
        return False
