from enum import Enum
from pydantic import BaseModel
from typing import Optional


class CulturasPlantadas(str, Enum):
    soja = "Soja"
    milho = "Milho"
    algodao = "Algodao"
    cafe = "Cafe"
    cana_acucar = "Cana de açucar"

class ProdutorRural(BaseModel):
    id: int
    nome: str
    cpf: str
    nome_fazenda: str
    cidade: str
    estado: str
    area_total_hec: int
    area_total_agricutavel: int
    area_total_vegetacao: int
    culturas_plantadas: CulturasPlantadas


