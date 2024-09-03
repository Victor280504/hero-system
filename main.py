from config.Database import Database


def menu_listar_todas_pessoas():

    usuario = Database("usuario")
    print("Listando Todas as Pessoas...")

    encontrou = False
    if pessoas:
        encontrou = True
        for pessoa in pessoas:
            print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Endereço: {pessoa[2]}")
    if not encontrou:
        print("Nenhum registro encontrado")


def listar_pessoa():
    usuario = Database("usuario")
    pessoa = usuario.findBy("id", 1, "*")
    print(pessoa[0])
    # print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Endereço: {pessoa[2]}")


def inserir_pessoa():
    pessoa = dict()

    user = Database("usuario")
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["endereco"] = input("Digite o endereço: ")
    pessoa["email"] = input("Digite o email: ")
    pessoa["login"] = input("Digite o login: ")
    pessoa["senha"] = input("Digite a senha: ")

    return user.insert(pessoa)


class Pessoa:
    def __init__(self, id, nome, endereco, email, login, senha):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.login = login
        self.senha = senha

    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    def get_values_by_keys(self, keys: list) -> dict:
        values = {}
        for key in keys:
            if key in self.__dict__:
                values[key] = self.__dict__[key]
        return values

    def __str__(self):
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Email: {self.email}, Login: {self.login}, Senha: {self.senha}"

    @staticmethod
    def preencher_dados_pessoa():
        nome = input("Digite o nome: ")
        endereco = input("Digite o endereço: ")
        email = input("Digite o email: ")
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")

        pessoa = Pessoa(nome, endereco, email, login, senha)
        return pessoa

    @staticmethod
    def get_pessoa(id: str):
        usuario = Database("usuario").findBy("id", id, "*")[0]
        return Pessoa(
            usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]
        )

    @staticmethod
    def get_all_people():
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


def update_pessoa():

    user = Database("usuario")

    pessoa = Pessoa.preencher_dados_pessoa()

    print(pessoa.get_attributes_dict())

    update_keys = []

    for key, value in pessoa.get_attributes_dict().items():
        new_value = input(f"Digite o novo {key} (deixe em branco para não atualizar): ")
        if new_value:
            update_keys.append(key)
            pessoa.__setattr__(key, new_value)

    return print(pessoa.get_values_by_keys(update_keys))

    # Call the update function only if there are fields to update
    if pessoa_dict:
        return user.update(pessoa_dict)
    else:
        return "Nenhum campo preenchido para atualização"

    # Remove empty fields from the pessoa dictionary
    pessoa = {k: v for k, v in pessoa.items() if v}

    # Call the update function only if there are fields to update
    if pessoa:
        return user.update(pessoa)
    else:
        return "Nenhum campo preenchido para atualização"


if __name__ == "__main__":
    # menu_listar_todas_pessoas()
    # listar_pessoa()
    # inserir_pessoa()
    # update_pessoa()
    people = Pessoa.get_pessoa("1")
    # print(people.get_attributes_dict())
    for t in Pessoa.get_all_people():
        print(t.get_attributes_dict())
