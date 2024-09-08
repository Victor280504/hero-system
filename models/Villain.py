from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update
from models.Super import Super


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
    def insert() -> int:
        res_super = Super.insert()
        res_villain = Database("vilao")
        data_dict = {"id_super_vilao": res_super}
        data_dict.update(make_dict(Villain.get_attributes_list()[7:]))

        return res_villain.insert(data_dict, "id_super_vilao")

    def update(self) -> int:
        res_villain = Database("vilao")
        super_obj = Super.get_by_id(self.id)
        super_obj.update()
        data_dict = make_dict_for_update(Villain.get_attributes_list()[7:])

        if not data_dict:
            return "Nenhuma atualização foi feita"

        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return res_villain.update(data_dict, "id_super_vilao", self.id)

    @staticmethod
    def get_all() -> list:
        res = Database("super_vilao").findAll("*")
        return [Villain(*res) for res in res]
    
    def get_all_id_list() -> list:
        res = Database("vilao").findAll("id_vilao")
        return [item[0] for item in res]

    @staticmethod
    def get_by_id(id: str) -> "Villain":
        res = Database("super_vilao").findBy("id_super", id, "*")
        
        if not res:
            return None
        
        return Villain(*res)

    def delete(self) -> int:
        res = Database("vilao")
        super_obj = Super.get_by_id(self.id)

        if input(f"Você deseja deletar o vilão {self.nome} (s/n)? ").lower() == "s":
            res.delete("id_super_vilao", self.id)
            return super_obj.delete()

        return "Nenhuma ação foi realizada"

    def __str__(self):
        return f"{super().__str__()},\nSituação: {self.situacao}"
