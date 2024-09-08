from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update


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
        
    # RETORNA UM Super Por iD
    @staticmethod
    def get_by_id(id: str) -> "Super":
        res = Database("super").findBy("id_super", id, "*")
        
        if not res:
            return None
        
        return Super(*res)

    # RETORNA TODOS OS SUPER
    @staticmethod
    def get_all() -> list:
        res = Database("super").findAll("*")
        return [
            Super(*res) for res in res
        ]

    @staticmethod
    def insert() -> int:
        res = Database("super")
        data_dict: dict = make_dict(Super.get_attributes_list()[1:])
        return res.insert(data_dict, "id_super")

    def update(self) -> int:
        super_db = Database("super")
        data_dict = make_dict_for_update(Super.get_attributes_list()[1:])

        if not data_dict:
            return "Nenhuma atualização foi feita"

        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return super_db.update(data_dict, "id_super", self.id)

    def delete(self) -> int:
        res = Database("super")
        return res.delete("id_super", self.id)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nDescrição: {self.descricao}\nStatus: {self.status}\nRank: {self.rank}\nFraqueza: {self.fraqueza}\nArqui Inimigo: {self.arqui_inimigo}"
