from sqlalchemy.orm import Session
from app.models.produtor_rural import ProdutorRural

class ProdutorRuralRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_item(self, item: ProdutorRural):
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_items(self):
        return self.db.query(ProdutorRural).all()

    def get_item_by_id(self, item_id: int):
        return self.db.query(ProdutorRural).filter(ProdutorRural.id == item_id).first()

    def update_item(self, item_id: int, new_data: ProdutorRural):
        item = self.get_item_by_id(item_id)
        if not item:
            return None
        for key, value in vars(new_data).items():
            if key != "_sa_instance_state":
                setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete_item(self, item_id: int):
        item = self.get_item_by_id(item_id)
        if not item:
            return False
        self.db.delete(item)
        self.db.commit()
        return True
