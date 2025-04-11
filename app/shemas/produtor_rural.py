from pydantic import BaseModel
from enum import Enum

class CulturasPlantadas(str, Enum):
    Soja = "Soja"
    Milho = "Milho"
    Algodao = "Algodao"
    Cafe = "Cafe"
    cana_acucar = "Cana de açucar"

class ProdutorRuralBase(BaseModel):
    nome: str
    cpf: str
    nome_fazenda: str
    cidade: str
    estado: str
    area_total_hec: int
    area_total_agricutavel: int
    area_total_vegetacao: int
    culturas_plantadas: CulturasPlantadas

class ProdutorRuralCreate(ProdutorRuralBase):
    pass

class ProdutorRural(ProdutorRuralBase):
    id: int

    class Config:
        orm_mode = True
