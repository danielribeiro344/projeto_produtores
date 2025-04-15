
from fastapi.encoders import jsonable_encoder
from fastapi import status, Query
from fastapi.responses import JSONResponse
from app.models.produtor_rural import ProdutorRuralModel
from app.shemas.produtor_rural import ProdutorRuralCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ProdutorRuralService:
    def __init__(self, db: Session):
        self.db = db

    def criar_produtor(self, produtor_rural: ProdutorRuralCreate):
        #Valida CPF
        if len(produtor_rural.cpf) != 11:
            raise HTTPException(status_code=400, detail="CPF inválido!")

        #Valida soma das áreas totais
        soma = produtor_rural.area_total_agricutavel + produtor_rural.area_total_vegetacao
        if soma > produtor_rural.area_total_hec:
            raise HTTPException(status_code=400, detail="A soma da area total agricutavel + area total de vegetação não pode ser maior que a área total agricultavel!")

        #Valida se produtor já existe na base
        produtor_existente = self.db.query(ProdutorRuralModel).filter_by(cpf=produtor_rural.cpf).first()
        if produtor_existente:
            raise HTTPException(status_code=400, detail="ID desse produtor já existe!")
        

        #Cria uma instancia de ProdutorRuralModel e atribui os valores recebidos a ela
        #Forma simplificada
        novo_produtor = ProdutorRuralModel(**produtor_rural.dict())

        #Forma verbosa
        # novo_produtor = ProdutorRuralModel(
        #     nome=produtor_rural.nome,
        #     cpf=produtor_rural.cpf,
        #     nome_fazenda=produtor_rural.nome_fazenda,
        #     cidade=produtor_rural.cidade,
        #     estado=produtor_rural.estado,
        #     area_total_hec=produtor_rural.area_total_hec,
        #     area_total_agricutavel=produtor_rural.area_total_agricutavel,
        #     area_total_vegetacao=produtor_rural.area_total_vegetacao,
        #     culturas_plantadas=produtor_rural.culturas_plantadas,
        # )

        self.db.add(novo_produtor)# Adiciona na lista para ser executado no banco
        self.db.commit()# Executa no banco
        self.db.refresh(novo_produtor)# Atualiza o retorno com dados reais do banco (como o ID gerado)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Produtor criado com sucesso!",
                "data": jsonable_encoder(novo_produtor),
                "status_code": status.HTTP_201_CREATED
            }
        )

    def listar_produtores(self):
        produtores = self.db.query(ProdutorRuralModel).all()
        if len(produtores) > 0:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "Produtores listados com sucesso!",
                    "data": jsonable_encoder(produtores),
                    "status_code": status.HTTP_200_OK
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_204_NO_CONTENT,
                content={
                    "message": "Nenhum produtor encontrado!",
                    "data": jsonable_encoder(produtores),
                    "status_code": status.HTTP_204_NO_CONTENT
                }
            )

    def atualizar_produtor( self, id: int, nome: str = Query(None), cpf: str = Query(None), idade: int = Query(None) ):
        produtor = self.db.query(ProdutorRuralModel).filter_by(id=id).first()
        if not produtor:
            raise HTTPException(status_code=404, detail="Produtor não encontrado.")

        if nome is not None:
            produtor.nome = nome
        if cpf is not None:
            produtor.cpf = cpf
        if idade is not None:
            produtor.idade = idade


        self.db.commit()
        self.db.refresh(produtor)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Produtores atualizado com sucesso!",
                "data": jsonable_encoder(produtor),
                "status_code": status.HTTP_201_CREATED
            }
        )

    def deletar_produtor(self, item_id: int):
        produtor = self.db.query(ProdutorRuralModel).filter_by(id=item_id).first()
        if not produtor:
            raise HTTPException(status_code=404, detail="Produtor não encontrado.")
        self.db.delete(produtor)
        self.db.commit()
        return {"message": "Item deletado com sucesso"}
