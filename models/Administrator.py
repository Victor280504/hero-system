from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update

class Administrator:
    def __init__(self, id, nome, contato, login, senha, endereco, data_inicio_adm):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.data_inicio_adm = data_inicio_adm

    # Listar os atributos da classe
    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes
    
    @staticmethod
    def sign_in(login: str, senha: str) -> bool:
        adm = Database("administrador")

        res = adm.findBy("login", "'" + login + "'", "*")
        if res and res[4] == senha:
            return res[0]
        return False

     # Listar os valores dos atributos da classe por chaves
    def get_values_by_keys(self, keys: list) -> dict:
        values = {}
        for key in keys:
            if key in self.__dict__:
                values[key] = self.__dict__[key]
        return values

    @staticmethod
    def get_attributes_list() -> list:
        return [
            "id",
            "nome",
            "contato",
            "login",
            "senha",
            "endereco",
            "data_inicio_adm",
        ]
   
    @staticmethod
    def get_by_id(id: str) -> "Administrator":
        res = Database("administrador").findBy("id_adm", id, "*")
        return Administrator(res[0], res[1], res[2], res[3], res[4], res[5], res[6])

    @staticmethod
    def get_all() -> list:
        res = Database("administrador").findAll("*")
        return [
            Administrator(res[0], res[1], res[2], res[3], res[4], res[5], res[6])
            for res in res
        ]

    @staticmethod
    def insert() -> int:
        res = Database("administrador")
        data_dict: dict = make_dict(Administrator.get_attributes_list()[1:])
        return res.insert(data_dict, "id_adm")

    def update(self) -> int:
        adm = Database("administrador")
        data_dict = make_dict_for_update(Administrator.get_attributes_list()[1:])

        if not data_dict:
            return
        
        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return adm.update(data_dict, "id_adm", self.id)

    def delete(self) -> int:
        res = Database("administrador")
        return res.delete("id_adm", self.id)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nContato: {self.contato}\nLogin: {self.login}\nSenha: {self.senha}\nEndereço: {self.endereco}\nData de Início: {self.data_inicio_adm}"