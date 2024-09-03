from config.Database import Database
from utils import make_dict

class Pessoa:
    def __init__(self, id, nome, endereco, email, login, senha):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.login = login
        self.senha = senha

    # Listar os atributos da classe
    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    # Listar as chaves dos atributos da classe
    @staticmethod
    def get_attributes_list() -> list:
        return ["nome", "endereco", "email", "login", "senha"]

    # Listar os valores dos atributos da classe por chaves
    def get_values_by_keys(self, keys: list) -> dict:
        values = {}
        for key in keys:
            if key in self.__dict__:
                values[key] = self.__dict__[key]
        return values

    # Retornar a representação da classe
    def __str__(self):
        return f"ID:{self.id} ,Nome: {self.nome}, Endereço: {self.endereco}, Email: {self.email}, Login: {self.login}, Senha: {self.senha}"

    # Factory Method
    @staticmethod
    def factory() -> "Pessoa":
        # TESTE
        pessoa_itens = [
            "id",
            "nome",
            "endereço",
            "email",
            "login",
            "senha",
        ]
        new_person_data = []

        for value in pessoa_itens:
            new_value = input(f"Digite o {value}: ")
            if new_value:
                new_person_data.append(new_value)

        return Pessoa(
            new_person_data[0],
            new_person_data[1],
            new_person_data[2],
            new_person_data[3],
            new_person_data[4],
            new_person_data[5],
        )

    # RETORNA UMA PESSOA PELO ID
    @staticmethod
    def get_by_id(id: str) -> "Pessoa":
        usuario = Database("usuario").findBy("id", id, "*")
        return Pessoa(
            usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]
        )

    # RETORNA TODAS AS PESSOAS
    @staticmethod
    def get_all() -> list:
        usuarios = Database("usuario").findAll("*")
        return [
            Pessoa(
                usuario[0],
                usuario[1],
                usuario[2],
                usuario[3],
                usuario[4],
                usuario[5],
            )
            for usuario in usuarios
        ]

    @staticmethod
    def insert():
        user = Database("usuario")
        pessoa_dict = make_dict(Pessoa.get_attributes_list())
        return user.insert(pessoa_dict)
    
    def update(self):
        user = Database("usuario")
        pessoa_dict = self.get_attributes_dict()
        update_keys = []

        # Ask for the new values
        for key, value in pessoa_dict.items():
            if key != "id":
                new_value = input(
                    f"Digite o novo {key} (deixe em branco para não atualizar): "
                )
                if new_value:
                    update_keys.append(key)
                    self.__setattr__(key, new_value)

        data = self.get_values_by_keys(update_keys)

        # Call the update function only if there are fields to update
        if pessoa_dict:
            return user.update(data, "id", self.id)
        else:
            return "Nenhum campo preenchido para atualização"

    def delete(self):
        user = Database("usuario")
        return user.delete("id", self.id)
