# Responsável por gerenciar a relação entre as missões e os vilões

from config.Database import Database
from models.Villain import Villain
from utils.decorators import exception_handler
from utils.exceptions import DatabaseError
from utils.response import Response

class MissionVillain:
    def __init__(self, vilao_id, mission_id):
        self.id_super_vilao = vilao_id
        self.id_missao = mission_id

    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes
    
    @staticmethod
    def get_villain_by_mission(id) -> list:
        res = Database("missao_vilao").find(["id_missao"], [id], "*")
        return [Villain.get_by_id(str(villain[1])).data for villain in res]
    
    @exception_handler
    def insert(self) -> Response:
        res = Database("missao_vilao").insert(self.get_attributes_dict(), "id_super_vilao")
        if not res:
            raise DatabaseError("Erro ao inserir o vilão na missão")
        return Response(success=True, message="Vilão inserido na missão com sucesso", data=res)
    
    @exception_handler
    def delete(self) -> Response:
        res = Database("missao_vilao").delete_fields(["id_super_vilao", "id_missao"], [self.id_super_vilao, self.id_missao])
        
        if not res:
            raise DatabaseError("Erro ao remover o vilão da missão")
        
        return Response(success=True, message="Vilão removido da missão com sucesso", data=res)
