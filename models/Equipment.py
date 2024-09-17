# Responsável por realizar a manipulação dos dados referentes aos Equipamentos
from config.Database import Database
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response

class Equipment:
    def __init__(self, id, nome, qtd_estoque, tipo):
        self.id = id
        self.nome = nome
        self.qtd_estoque = qtd_estoque
        self.tipo = tipo

    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    @staticmethod
    def get_attributes_list() -> list:
        return [
            "id",
            "nome",
            "qtd_estoque",
            "tipo",
        ]

    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("equipamento").findBy("id_equipamento", id, "*")
        
        if not res:
            raise NotFoundError("Identificador inexistente")
        
        return Response(success=True, message="Equipamento encontrado", data=Equipment(*res))

    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("equipamento").findAll("*")
        items = [Equipment(*res) for res in res]
        return Response(success=True, message="Equipamentos encontrados", data=items)

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res = Database("equipamento")
        new_equipment = res.insert(data, "id_equipamento")
        
        if not new_equipment:
            raise DatabaseError("Equipamento não foi criado, tente adicionar uma quantidade válida")
        
        return Response(success=True, message="Equipamento inserido com sucesso", data=new_equipment)

    @exception_handler
    def update(self, data) -> Response:
        equipamento_db = Database("equipamento")

        if not data:
            return Response(success=True, message="Nenhum dado foi atualizado", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)

        res = equipamento_db.update(data, "id_equipamento", self.id)

        if not res:
            raise DatabaseError("Equipamento não foi atualizado")
        
        return Response(success=True, message="Equipamento atualizado com sucesso", data=res)
    
    @exception_handler
    def update_qtd(self) -> int:
        equipamento_db = Database("equipamento")

        data_dict = {"qtd_estoque": self.qtd_estoque}

        res = equipamento_db.update(data_dict, "id_equipamento", self.id)
         
        if not res:
            raise DatabaseError("Quantidade de equipamento não foi atualizada")
        return Response(success=True, message="Quantidade de equipamento atualizada com sucesso", data=res)

    @staticmethod
    def get_available() -> list:
        res = Database("equipamento").findAll("*")
        return [Equipment(*item) for item in res if item[2] > 0]

    @exception_handler
    def delete(self) -> Response:
        res = Database("equipamento")

        delete_res = res.delete("id_equipamento", self.id)
        
        if not delete_res:
            raise DatabaseError("Equipamento não foi deletado")
        
        return Response(success=True, message="Equipamento deletado com sucesso", data=delete_res)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nQuantidade: {self.qtd_estoque}\nTipo: {self.tipo}\n"
