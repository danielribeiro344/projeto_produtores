from fastapi import APIRouter

from app.models.produtor_rural import ProdutorRural
from app.services.produtor_rural_indicaores_service import ProdutorRuraIndicadoreslService
from app.services.produtor_rural_service import ProdutorRuralService

router = APIRouter()
service_produtor = ProdutorRuralService()
service_indicadores = ProdutorRuraIndicadoreslService()

@router.post("/criar-produtor", response_model=ProdutorRural)
def create_item(item: ProdutorRural):
    return service_produtor.criar_produtor(item)

@router.get("/listar-produtores", response_model=list[ProdutorRural])
def get_items():
    return service_produtor.listar_produtores()

@router.put("/atualizar-produtor{item_id}", response_model=ProdutorRural)
def update_item(item_id: int, item: ProdutorRural):
    return service_produtor.atualizar_produtor(item_id, item)

@router.delete("/deletar-produtor{item_id}")
def delete_item(item_id: int):
    return service_produtor.deletar_produtor(item_id)

@router.get("/total-fazendas")
def get_total_fazendas():
    return service_indicadores.listar_total_fazendas()

@router.get("/total-fazendas-hectares")
def get_total_fazendas_hectares():
    return service_indicadores.listar_total_fazendas_hectares()

@router.get("/total-culturas-estado")
def get_total_culturas_estado():
    return service_indicadores.listar_total_culturas_estado()