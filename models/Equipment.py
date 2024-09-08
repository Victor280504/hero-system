from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update


class Equipment:
    def __init__(self, id, nome, qtd_estoque, tipo):
        self.id = id
        self.nome = nome
        self.qtd_estoque = qtd_estoque
        self.tipo = tipo

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
            "qtd_estoque",
            "tipo",
        ]

    @staticmethod
    def get_by_id(id: str) -> "Equipment":
        res = Database("equipamento").findBy("id_equipamento", id, "*")
        
        if not res:
            return None
        
        return Equipment(*res)

    # RETORNA TODOS OS SUPER
    @staticmethod
    def get_all() -> list:
        res = Database("equipamento").findAll("*")
        return [Equipment(*res) for res in res]

    @staticmethod
    def insert() -> int:
        res = Database("equipamento")
        data_dict: dict = make_dict(Equipment.get_attributes_list()[1:])
        return res.insert(data_dict, "id_equipamento")

    def update(self) -> int:
        equipamento_db = Database("equipamento")
        data_dict = make_dict_for_update(Equipment.get_attributes_list()[1:])

        if not data_dict:
            return "Nenhuma atualização foi feita"

        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return equipamento_db.update(data_dict, "id_equipamento", self.id)

    def update_qtd(self) -> int:
        equipamento_db = Database("equipamento")

        data_dict = {"qtd_estoque": self.qtd_estoque}

        return equipamento_db.update(data_dict, "id_equipamento", self.id)

    def delete(self) -> int:
        res = Database("equipamento")

        if (
            input(f"Você deseja deletar o equipamento {self.nome} (s/n)? ").lower()
            == "s"
        ):
            return res.delete("id_equipamento", self.id)

        return "Nenhuma ação foi realizada"

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nQuantidade: {self.qtd_estoque}\nTipo: {self.tipo}\n"
