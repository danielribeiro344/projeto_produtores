from sqlalchemy import Column, Integer, String, Enum
from app.config.database import Base
import enum

class CulturasPlantadas(str, enum.Enum):
    Soja = "Soja"
    Milho = "Milho"
    Algodao = "Algodao"
    Cafe = "Cafe"
    cana_acucar = "Cana de açucar"

class ProdutorRuralModel(Base):
    __tablename__ = "produtores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    nome_fazenda = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    area_total_hec = Column(Integer, nullable=False)
    area_total_agricutavel = Column(Integer, nullable=False)
    area_total_vegetacao = Column(Integer, nullable=False)
    culturas_plantadas = Column(Enum(CulturasPlantadas), nullable=False)
