from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update
from models.Super import Super


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
    def insert() -> int:
        res_super = Super.insert()
        res_hero = Database("heroi")
        data_dict = {"id_super_heroi": res_super}
        data_dict.update(make_dict(Hero.get_attributes_list()[6:]))

        return res_hero.insert(data_dict, "id_super_heroi")

    def update(self) -> int:
        hero_db = Database("heroi")
        super_obj = Super.get_by_id(self.id)
        super_obj.update()
        data_dict = make_dict_for_update(Hero.get_attributes_list()[7:])

        if not data_dict:
            return
        
        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return hero_db.update(data_dict, "id_super_heroi", self.id)

    @staticmethod
    def get_all() -> list:
        res = Database("super_heroi").findAll("*")
        return [
            Hero(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
            for res in res
        ]

    @staticmethod
    def get_by_id(id: str) -> "Hero":
        res = Database("super_heroi").findBy("id_super", id, "*")
        return Hero(
            res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8]
        )

    def delete(self) -> int:
        res = Database("heroi")
        super_obj = Super.get_by_id(self.id)

        if input(f"Você deseja deletar o herói {self.nome} (s/n)? ").lower() == "s":
            res.delete("id_super_heroi", self.id)
            return super_obj.delete()

        return "Nenhuma ação foi realizada"

    def __str__(self):
        return f"{super().__str__()}, Contato: {self.contato}, Disponibilidade: {self.disponibilidade}"
