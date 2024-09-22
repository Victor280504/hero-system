# Responsável por gerenciar as informações dos vilões
from config.Database import Database
from models.Super import Super
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response
from utils.slices import get_subset, get_subset_by_key_list


class Villain(Super):
    def __init__(
        self,
        id,
        nome,
        descricao,
        status,
        rank,
        fraqueza,
        arqui_inimigo,
        situacao,
    ):
        super().__init__(id, nome, descricao, status, rank, fraqueza, arqui_inimigo)
        self.situacao = situacao

    @staticmethod
    def get_attributes_list() -> list:
        return Super.get_attributes_list() + ["situacao"]

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res_super = Super.insert(get_subset(data, 0, 6))

        if not res_super.success:
            raise DatabaseError(res_super.message)

        villain = Database("vilao")
        data_dict = get_subset(data, 6, 8)
        data_dict["id_super_vilao"] = res_super.data

        res = villain.insert(data_dict, "id_super_vilao")

        if not res:
            raise DatabaseError("Vilão não foi criado")

        return Response(success=True, message="Vilão inserido com sucesso", data=res)

    @exception_handler
    def update(self, data) -> Response:
        res_villain = Database("vilao")
        super_obj = Super.get_by_id(self.id)

        if not super_obj.success:
            raise DatabaseError(super_obj.message)
        
        if not data:
            return Response(
                success=True, message="Nenhum dado foi atualizado", data=None
            )

        v_res = super_obj.data.update(get_subset_by_key_list(data, Super.get_attributes_list()[:7]))

        if not v_res:
            raise DatabaseError(v_res.message)

        data_dict = get_subset_by_key_list(data, Villain.get_attributes_list()[7:])
        
        if not data_dict:
            return Response(success=True, message="Vilão atualizado com sucesso", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)

        res = res_villain.update(data_dict, "id_super_vilao", self.id)

        return Response(success=True, message="Vilão atualizado com sucesso", data=res)

    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("super_vilao").findAll("*")
        villains = [Villain(*res) for res in res]
        return Response(success=True, message="Todos os Vilões", data=villains)

    @staticmethod
    def get_available() -> list:
        res = Database("super_vilao").findAll("*")
        return [Villain(*res) for res in res]
    
    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("super_vilao").findBy("id_super", id, "*")

        if not res:
            raise NotFoundError("Identificador Inexistente")

        return Response(success=True, message="Vilão encontrado", data=Villain(*res))

    def delete(self) -> Response:
        super_obj = Super.get_by_id(self.id)

        if not super_obj.success:
            raise DatabaseError(super_obj.message)
        
        res = super_obj.data.delete()
        return Response(
            success=True, message="Vilão deletado com sucesso", data=res
        )

    def __str__(self):
        return f"{super().__str__()},\nSituação: {self.situacao}"
