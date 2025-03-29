from app.models.produtor_rural import ProdutorRural
from fastapi import HTTPException

from app.repositories.produtor_rural_repository import ProdutorRuralRepository

class ProdutorRuralService:
    def __init__(self):
        self.repository = ProdutorRuralRepository()

    def criar_produtor(self, produtor_rural: ProdutorRural):
        if self.repository.get_item_by_id(produtor_rural.id):
            raise HTTPException(status_code=400, detail="ID desse produtor já existe!")
        
        if len(produtor_rural.cpf) != 11:
            raise HTTPException(status_code=400, detail="CPF inválido!")
        
        valida_area_total = produtor_rural.area_total_agricutavel + produtor_rural.area_total_vegetacao
        if valida_area_total > produtor_rural.area_total_hec:
            raise HTTPException(status_code=400, detail="A soma da area total agricutavel + area total de vegetação não pode ser maior que a área total agricultavel!")
        
        self.repository.add_item(produtor_rural)
        return produtor_rural

    def listar_produtores(self):
        produtores = self.repository.get_items()
        return produtores

    def atualizar_produtor(self, item_id: int, atualiza_produtor: ProdutorRural):
        atualizar_produtor = self.repository.update_item(item_id, atualiza_produtor)
        if not atualizar_produtor:
            raise HTTPException(status_code=404, detail="Produtor não encontrado!")
        return atualizar_produtor

    def deletar_produtor(self, item_id: int):
        if not self.repository.delete_item(item_id):
            raise HTTPException(status_code=404, detail="Produtor não encontrado!")
        return {"message": "Item deletado com sucesso"}
