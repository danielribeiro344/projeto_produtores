from fastapi import APIRouter, Depends
from app.shemas.produtor_rural import ProdutorRural, ProdutorRuralCreate
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.services.produtor_rural_service import ProdutorRuralService

router = APIRouter()
 
@router.post("/criar-produtor", response_model=ProdutorRural)
def create_item(item: ProdutorRuralCreate, db: Session = Depends(get_db)):
    return ProdutorRuralService(db).criar_produtor(item)

@router.get("/listar-produtores", response_model=List[ProdutorRural])
def get_items(db: Session = Depends(get_db)):
    return ProdutorRuralService(db).listar_produtores()

@router.put("/atualizar-produtor{item_id}", response_model=ProdutorRural)
def update_item(item_id: int, item: ProdutorRuralCreate, db: Session = Depends(get_db)):
    return ProdutorRuralService(db).atualizar_produtor(item_id, item)

@router.delete("/deletar-produtor{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return ProdutorRuralService(db).deletar_produtor(item_id)

# @router.get("/total-fazendas")
# def get_total_fazendas(db: Session = Depends(get_db)):
#     return ProdutorRuraIndicadoreslService(db).listar_total_fazendas()

# @router.get("/total-fazendas-hectares")
# def get_total_fazendas_hectares(db: Session = Depends(get_db)):
#     return ProdutorRuraIndicadoreslService(db).listar_total_fazendas_hectares()

# @router.get("/total-culturas-estado")
# def get_total_culturas_estado(db: Session = Depends(get_db)):
#     return ProdutorRuraIndicadoreslService(db).listar_total_culturas_estado()
