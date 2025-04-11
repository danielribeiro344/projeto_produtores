# from collections import defaultdict
# from fastapi import HTTPException

# from app.repositories.produtor_rural_repository import ProdutorRuralRepository

# class ProdutorRuraIndicadoreslService:
#     def __init__(self):
#         self.repository = ProdutorRuralRepository()


#     def listar_total_fazendas(self):
#         produtores = self.repository.get_items()
#         total_fazendas = len(produtores)
#         return {"message": f"Total de fazendas: {total_fazendas}"}
    
#     def listar_total_fazendas_hectares(self):
#         produtores = self.repository.get_items()
#         total_hectares = sum(produtor.area_total_hec for produtor in produtores)
#         return {"message": f"Soma total das áreas das fazendas: {total_hectares} hectares"}
    
#     def listar_total_culturas_estado(self):
#         produtores = self.repository.get_items()
#         culturas_por_estado = defaultdict(lambda: defaultdict(int))

#         for produtor in produtores:
#             estado = produtor.estado
#             cultura = produtor.culturas_plantadas
#             culturas_por_estado[estado][cultura] += 1

#         return {"culturas_por_estado": culturas_por_estado}