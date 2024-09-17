# Responsável por gerenciar as missões

from config.Database import Database
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response
from models.MissionHero import MissionHero
from models.MissionVillain import MissionVillain
from models.MissionEquipment import MissionEquipment

class Mission:
    def __init__(self, id, descricao, data, status, local, rank, id_adm):
        self.id = id
        self.descricao = descricao
        self.data = data
        self.status = status
        self.local = local
        self.rank = rank
        self.id_adm = id_adm

    @property
    def heroes(self) -> list:
        return MissionHero.get_heroes_by_mission(self.id)
    
    @property
    def villains(self) -> list:
        return MissionVillain.get_villain_by_mission(self.id)
    
    @property
    def equipments(self) -> list:
        return MissionEquipment.get_equipments_by_mission(self.id)
    
    # Listar os atributos da classe
    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    # Listar as chaves dos atributos da classe
    @staticmethod
    def get_attributes_list() -> list:
        return [
            "id",
            "descricao",
            "data",
            "status",
            "local",
            "rank",
            "id_adm",
        ]

    # self methods
    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("missao").findBy("id_missao", id, "*")

        if not res:
            raise NotFoundError("Identificador inexistente")

        return Response(success=True, message="Missão encontrada", data=Mission(*res))

    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("missao").findAll("*")
        items = [Mission(*res) for res in res]
        return Response(success=True, message="Todas as Missões", data=items)

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res = Database("missao")
        new_mission = res.insert(data, "id_missao")
        if not new_mission:
            raise DatabaseError("Missão não foi criada")
        return Response(success=True, message="Missão inserida com sucesso", data=new_mission)

    @exception_handler
    def update(self, data) -> Response:
        missao_db = Database("missao")
        
        if not data:
           return Response(success=True, message="Nenhum dado foi atualizado", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)

        res = missao_db.update(data, "id_missao", self.id)
        
        return Response(success=True, message="Missão atualizada com sucesso", data=res)

    @exception_handler
    def delete(self) -> Response:
        res = Database("missao")
        
        deleted_item = res.delete("id_missao", self.id)
        
        if not deleted_item:
            raise DatabaseError("Missão não foi deletada")

        return Response(success=True, message="Missão deletada com sucesso", data=deleted_item)

    def __str__(self):
        return f"ID: {self.id}\nDescrição: {self.descricao}\nData: {self.data}\nStatus: {self.status}\nLocal: {self.local}\nRank: {self.rank}\nAdministrador: {self.id_adm}"
