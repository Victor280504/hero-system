# Responsável por gerenciar a relação entre as missões e os heróis

from config.Database import Database
from models.Hero import Hero
from utils.decorators import exception_handler
from utils.exceptions import DatabaseError
from utils.response import Response

class MissionHero:
    def __init__(self, hero_id, mission_id):
        self.id_super_heroi = hero_id
        self.id_missao = mission_id

    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes
    
    @staticmethod
    def get_heroes_by_mission(id) -> list:
        res = Database("missao_heroi").find(["id_missao"], [id], "*")
        return [Hero.get_by_id(str(hero[0])).data for hero in res]
    
    @exception_handler
    def insert(self) -> Response:
        res = Database("missao_heroi").insert(self.get_attributes_dict(), "id_super_heroi")
        
        if not res:
            raise DatabaseError("Erro ao inserir o herói na missão")
        
        return Response(success=True, message="Herói inserido na missão com sucesso", data=res)
    
    @exception_handler
    def delete(self) -> Response:
        res = Database("missao_heroi").delete_fields(["id_super_heroi", "id_missao"], [self.id_super_heroi, self.id_missao])
        
        if not res:
            raise DatabaseError("Erro ao remover o herói da missão")
        
        return Response(success=True, message="Herói removido da missão com sucesso", data=res)
