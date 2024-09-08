from config.Database import Database
from utils.make_dict import make_dict, make_dict_for_update
from utils.show_itens import process_items
from models.Mission import Mission
from models.Equipment import Equipment
from models.Hero import Hero


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
    def sign_in() -> bool | int:
        adm = Database("administrador")
        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")

        res = adm.findBy("login", "'" + login + "'", "*")

        if res and res[4] == senha:
            admin = Administrator.get_by_id(str(res[0]))
            return admin
        return False

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

    # missions
    def set_mission(self) -> int:

        mission_id = Mission.insert(self.id)

        if not mission_id:
            return "Missão não foi criada"

        self.equipments(mission_id)
        self.heroes(mission_id)

        return f"A missão {mission_id} foi cadastrada com sucesso"

    def equipments(self, mission_id) -> list:
        if (
            input(f"Você deseja adicionar equipamentos? {self.nome} (s/n)? ").lower()
            == "s"
        ):
            mission = Mission.get_by_id(mission_id)

            print("Equipamentos disponíveis:")
            availaible_equipments = [
                equip for equip in Equipment.get_all() if equip.qtd_estoque > 0
            ]
            process_items(availaible_equipments)

            if not availaible_equipments:
                return "Não há equipamentos disponíveis"

            equipamentos = input(
                "Digite os IDs dos equipamentos que deseja adicionar separados por vírgula: "
            ).split(",")

            process_items(equipamentos)

            quantidade = input(
                "Digite a quantidade de cada equipamento separados por vírgula: "
            ).split(",")

            if len(equipamentos) != len(quantidade):
                return "O número de equipamentos e quantidades de equipamentos não são iguais"

            response = []

            for equip in equipamentos:
                result = mission.add_equipments(
                    equip, int(quantidade[equipamentos.index(equip)])
                )
                if result == "Quantidade insuficiente no estoque":
                    response.append(str(result) + " para o equipamento de id " + equip)

            return response if response else "Equipamentos adicionados com sucesso"
        return "Nenhum equipamento foi adicionado"

    def equipments_remove(self, mission_id) -> list:
        if (
            input(f"Você deseja remover equipamentos? {self.nome} (s/n)? ").lower()
            == "s"
        ):
            mission = Mission.get_by_id(mission_id)

            print("Equipamentos:")
            equipments = mission.get_equipments_by_mission()
            if equipments:
                for equip in equipments:
                    print(f"ID: {equip[0].id}- {equip[0].nome} (Quantidade: {equip[1]})\n")

            if not equipments:
                return "Não há equipamentos nessa missão"

            equipamentos = input(
                "Digite os IDs dos equipamentos que deseja remover separados por vírgula: "
            ).split(",")

            process_items(equipamentos)

            quantidade = input(
                "Digite a quantidade de cada equipamento separados por vírgula: "
            ).split(",")

            if len(equipamentos) != len(quantidade):
                return "O número de equipamentos e quantidades de equipamentos não são iguais"

            for equip in equipamentos:
                mission.remove_equipments(
                    equip, int(quantidade[equipamentos.index(equip)])
                )

            return "Equipamentos removidos com sucesso"
        return "Nenhum equipamento foi removido"

    def heroes(self, mission_id) -> list:
        if input(f"Você deseja adicionar heróis? {self.nome} (s/n)? ").lower() == "s":
            mission = Mission.get_by_id(mission_id)
            print("Heróis disponíveis:")

            availaible_heroes = [
                hero for hero in Hero.get_all() if hero.disponibilidade == "Disponível"
            ]

            process_items(availaible_heroes)

            if not availaible_heroes:
                return "Não há Heróis disponíveis"

            herois = input(
                "Digite os IDs dos heróis que deseja adicionar separados por vírgula: "
            ).split(",")

            process_items(herois)

            for hero in herois:
                mission.add_heroes(hero)

            return "Heróis adicionados com sucesso"
        return "Nenhum herói foi adicionado"

    def heroes_remove(self, mission_id) -> list:
        if input(f"Você deseja remover heróis? {self.nome} (s/n)? ").lower() == "s":
            mission = Mission.get_by_id(mission_id)

            avaliable_heroes = mission.get_heroes_by_mission()

            process_items(avaliable_heroes)

            if not avaliable_heroes:
                return "A missão não possui heróis"

            herois = input(
                "Digite os IDs dos heróis que deseja remover separados por vírgula: "
            ).split(",")

            process_items(herois)

            for hero in herois:
                mission.remove_heroes(hero)

            return "Heróis removidos com sucesso"

        return "Nenhum herói foi removido"

    # self methods
    @staticmethod
    def get_by_id(id: str) -> "Administrator":
        res = Database("administrador").findBy("id_adm", id, "*")

        if not res:
            return None

        return Administrator(*res)

    @staticmethod
    def get_all() -> list:
        res = Database("administrador").findAll("*")
        return [Administrator(*res) for res in res]

    @staticmethod
    def insert() -> int:
        res = Database("administrador")
        data_dict: dict = make_dict(Administrator.get_attributes_list()[1:])
        return res.insert(data_dict, "id_adm")

    def update(self) -> int:
        adm = Database("administrador")
        data_dict = make_dict_for_update(Administrator.get_attributes_list()[1:])

        if not data_dict:
            return "Nenhuma atualização foi feita"

        for key, value in data_dict.items():
            self.__setattr__(key, value)

        return adm.update(data_dict, "id_adm", self.id)

    def delete(self) -> int:
        res = Database("administrador")
        # Delete cascade ou default? Como implementar?
        if (
            input(f"Você deseja deletar o administrador {self.nome} (s/n)? ").lower()
            == "s"
        ):
            return res.delete("id_adm", self.id)

        return "Nenhuma ação foi realizada"

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nContato: {self.contato}\nLogin: {self.login}\nSenha: {self.senha}\nEndereço: {self.endereco}\nData de Início: {self.data_inicio_adm}"
