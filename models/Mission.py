from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update
from models.Equipment import Equipment
from models.Hero import Hero
from models.Villain import Villain
from utils.show_itens import print_items


class Mission:
    def __init__(self, id, descricao, data, status, local, rank, id_adm):
        self.id = id
        self.descricao = descricao
        self.data = data
        self.status = status
        self.local = local
        self.rank = rank
        self.id_adm = id_adm

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

    # equipamentos -- Pensar em implementar com o group by
    def get_equipments_by_mission(self) -> list:
        res = Database("missao_equipamento").find(["id_missao"], [self.id], "*")
        return [(Equipment.get_by_id(equip[1]), equip[2]) for equip in res]

    def add_equipments(self, id_equipamento: str, qtd: int = 0) -> int:
        res = Database("missao_equipamento")
        equip = Equipment.get_by_id(id_equipamento)
        data_dict = {
            "id_missao": self.id,
            "id_equipamento": id_equipamento,
            "quantidade": qtd,
        }

        if equip.qtd_estoque < qtd:
            return "Quantidade insuficiente no estoque"

        search = res.find(
            ["id_equipamento", "id_missao"], [id_equipamento, self.id], "*", ["=", "="]
        
        )
        equip.qtd_estoque -= qtd
        equip.update_qtd()
        if search:
            return res.update_field(
                {"quantidade": search[0][2] + qtd},
                ["id_missao", "id_equipamento"],
                [self.id, id_equipamento],
            )

        return res.insert(data_dict, "id_equipamento")

    def remove_equipments(self, id_equipamento: str, qtd: int = 0) -> int:
        res = Database("missao_equipamento")
        equip = Equipment.get_by_id(id_equipamento)

        search = res.find(
            ["id_equipamento", "id_missao"], [id_equipamento, self.id], "*", ["=", "="]
        )
        if search:
            equip.qtd_estoque += qtd
            equip.update_qtd()
            return res.update_field(
                {"quantidade": search[0][2] - qtd},
                ["id_missao", "id_equipamento"],
                [self.id, id_equipamento],
            )

    # missao_heroi
    def get_heroes_by_mission(self) -> list:
        res = Database("missao_heroi").find(["id_missao"], [self.id], "*")
        return [Hero.get_by_id(str(hero[0])) for hero in res]

    def add_heroes(self, id_heroi: str) -> int:
        res = Database("missao_heroi")
        data_dict = {
            "id_missao": self.id,
            "id_super_heroi": id_heroi,
        }
        return res.insert(data_dict, "id_super_heroi")

    def remove_heroes(self, id_heroi: str) -> int:
        res = Database("missao_heroi")
        return res.delete("id_super_heroi", id_heroi)

    # missao_vilao
    def get_villain_by_mission(self) -> list:
        res = Database("missao_vilao").findBy("id_missao", self.id, "*")
        return [Villain.get_by_id(villain[1]) for villain in res]

    def add_villain(self, id_vilao: str) -> int:
        res = Database("missao_vilao")
        data_dict = {
            "id_missao": self.id,
            "id_super_vilao": id_vilao,
        }
        return res.insert(data_dict, "id_super_vilao")

    def remove_villain(self, id_vilao: str) -> int:
        res = Database("missao_vilao")
        return res.delete("id_super_vilao", id_vilao)

    # self methods
    @staticmethod
    def get_by_id(id: str) -> "Mission":
        res = Database("missao").findBy("id_missao", id, "*")

        if not res:
            return None

        return Mission(*res)

    @staticmethod
    def get_all() -> list:
        res = Database("missao").findAll("*")
        return [Mission(*res) for res in res]

    @staticmethod
    def insert(id_adm) -> int:
        res = Database("missao")
        data_dict: dict = make_dict(Mission.get_attributes_list()[1:6])
        data_dict["id_adm"] = id_adm
        return res.insert(data_dict, "id_missao")

    def update(self, id_adm) -> int:
        missao_db = Database("missao")
        data_dict = make_dict_for_update(Mission.get_attributes_list()[1:6])

        if not data_dict:
            return "Nenhuma atualização foi feita"

        data_dict["id_adm"] = id_adm

        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return missao_db.update(data_dict, "id_missao", self.id)

    def delete(self) -> int:
        res = Database("missao")

        if input(f"Você deseja deletar a missao {self.id} (s/n)? ").lower() == "s":
            return res.delete("id_missao", self.id)

        return "Nenhuma ação foi realizada"

    def __str__(self):
        return f"ID: {self.id}\nDescrição: {self.descricao}\nData: {self.data}\nStatus: {self.status}\nLocal: {self.local}\nRank: {self.rank}\nAdministrador: {self.id_adm}"
