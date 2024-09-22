# Responsável por realizar a manipulação dos dados referentes aos Heróis
from config.Database import Database
from models.Super import Super
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response
from utils.slices import get_subset, get_subset_by_key_list


class Hero(Super):
    def __init__(
        self,
        id,
        nome,
        descricao,
        status,
        rank,
        fraqueza,
        arqui_inimigo,
        contato,
        disponibilidade,
    ):
        super().__init__(id, nome, descricao, status, rank, fraqueza, arqui_inimigo)
        self.contato = contato
        self.disponibilidade = disponibilidade

    @staticmethod
    def get_attributes_list() -> list:
        return Super.get_attributes_list() + ["contato", "disponibilidade"]

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res_super = Super.insert(get_subset(data, 0, 6))

        if not res_super.success:
            raise DatabaseError(res_super.message)

        hero = Database("heroi")
        data_dict = get_subset(data, 6, 8)
        data_dict["id_super_heroi"] = res_super.data

        res = hero.insert(data_dict, "id_super_heroi")

        if not res:
            raise DatabaseError("Herói não foi criado")

        return Response(success=True, message="Herói inserido com sucesso", data=res)

    @exception_handler
    def update(self, data) -> Response:
        hero_db = Database("heroi")
        super_obj = Super.get_by_id(self.id)

        if not super_obj.success:
            raise DatabaseError(super_obj.message)

        if not data:
            return Response(
                success=True, message="Nenhum dado foi atualizado", data=None
            )
            
        h_res = super_obj.data.update(
            get_subset_by_key_list(data, Super.get_attributes_list()[:7])
        )

        if not h_res:
            raise DatabaseError(h_res.message)

        data_dict = get_subset_by_key_list(data, Hero.get_attributes_list()[7:])

        if not data_dict:
            return Response(success=True, message="Herói atualizado com sucesso", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)
        
        res = hero_db.update(data_dict, "id_super_heroi", self.id)
        
        return Response(success=True, message="Herói atualizado com sucesso", data=res)

    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("super_heroi").findAll("*")
        heroes = [Hero(*res) for res in res]
        return Response(success=True, message="Todos os Heróis", data=heroes)

    @staticmethod    
    def get_available() -> list:
        res = Database("super_heroi").findAll("*")
        return [Hero(*item) for item in res if item[8] == "Disponível"]
    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("super_heroi").findBy("id_super", id, "*")

        if not res:
            raise NotFoundError("Identificador Inexistente")

        return Response(success=True, message="Herói encontrado", data=Hero(*res))
    
    @exception_handler
    def delete(self) -> Response:
        super_obj = Super.get_by_id(self.id)
        if not super_obj.success:
            raise DatabaseError(super_obj.message)
        
        res = super_obj.data.delete()
        return Response(
            success=True, message="Vilão deletado com sucesso", data=res
        )
    
    def __str__(self):
        return f"{super().__str__()},\nContato: {self.contato},\nDisponibilidade: {self.disponibilidade}"
