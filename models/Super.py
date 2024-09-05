from config.Database import Database
from utils.make_dict import make_dict

class Super:
    def __init__(self, id, nome, descricao, status, rank, fraqueza, arqui_inimigo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.rank = rank
        self.fraqueza = fraqueza
        self.arqui_inimigo = arqui_inimigo

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
            "nome",
            "descricao",
            "status",
            "rank",
            "fraqueza",
            "arqui_inimigo",
        ]

    # Listar os valores dos atributos da classe por chaves
    def get_values_by_keys(self, keys: list) -> dict:
        values = {}
        for key in keys:
            if key in self.__dict__:
                values[key] = self.__dict__[key]
        return values


    # Factory Method
    @staticmethod
    def factory(itens: list) -> "Super":
        new_data = []
        
        for value in itens:
            new_value = input(f"Digite o {value}: ")
            if new_value:
                new_data.append(new_value)

        return Super(
            new_data[0],
            new_data[1],
            new_data[2],
            new_data[3],
            new_data[4],
            new_data[5],
            new_data[6],
        )

    # RETORNA UM Super Por iD
    @staticmethod
    def get_by_id(id: str) -> "Super":
        res = Database("super").findBy("id_super", id, "*")
        return Super(res[0], res[1], res[2], res[3], res[4], res[5], res[6])

    # RETORNA TODOS OS SUPER
    @staticmethod
    def get_all() -> list:
        res = Database("super").findAll("*")
        return [
            Super(res[0], res[1], res[2], res[3], res[4], res[5], res[6])
            for res in res
        ]

    @staticmethod
    def insert() -> int:
        res = Database("super")
        data_dict: dict = make_dict(Super.get_attributes_list()[1:])
        return res.insert(data_dict, "id_super")

    def update(self) -> int:
        res = Database("super")
        data_dict = self.get_attributes_dict()
        update_keys = []

        for key, value in data_dict.items():
            if key != "id":
                new_value = input(
                    f"Digite o novo {key} (deixe em branco para não atualizar): "
                )
                if new_value:
                    update_keys.append(key)
                    self.__setattr__(key, new_value)

        data = self.get_values_by_keys(update_keys)

        if not data:
            return

        return res.update(data, "id_super", self.id)

    def delete(self) -> int:
        res = Database("super")
        return res.delete("id_super", self.id)

    def __str__(self):
        return f"ID: {self.id} , Nome: {self.nome}, Descrição: {self.descricao}, Status: {self.status}, Rank: {self.rank}, Fraqueza: {self.fraqueza}, Arqui Inimigo: {self.arqui_inimigo}"