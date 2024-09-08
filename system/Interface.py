from models.Administrator import Administrator
from models.Hero import Hero
from models.Mission import Mission
from models.Villain import Villain
from models.Equipment import Equipment
from utils.show_itens import process_items


class InterfaceCRUD:
    def __init__(self, Object, name, pronoun, plural, adm_id, menu=1):
        self.Object = Object
        self.name = name
        self.pronoun = pronoun
        self.plural = plural
        self.adm_id = adm_id
        self.menu = menu

    def show_menu(self):
        print(
            "============================================================================\n"
        )
        print(f"O que você deseja fazer com {self.name}?")
        print(f"1. Inserir {self.name}")
        print(f"2. Listar {self.plural}")
        print(f"3. Buscar {self.name} por id")
        print(f"4. Atualizar {self.name}")
        print(f"5. Deletar {self.name}")
        print(f"6. Voltar")
        print(
            "============================================================================\n"
        )

    def processar_opcao(self, opcao):
        if opcao == "1":
            res = self.Object.insert()

            if type(res) == int:
                print(
                    "============================================================================\n"
                )
                print(f"{self.name} de id {res} inserid{self.pronoun} com sucesso.")
            else:
                print(
                    "============================================================================\n"
                )
                print(f"\nErro ao inserir {self.name}.")

        elif opcao == "2":
            print(
                "============================================================================\n"
            )
            print(f"Listando Todos {self.pronoun}s {self.plural}:")
            process_items(self.Object.get_all())
        elif opcao == "3":

            res = self.Object.get_by_id(
                input(f"Digite o id d{self.pronoun} {self.name}: ")
            )
            if res == None:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} não encontrad{self.pronoun}.")
            else:
                print(
                    "============================================================================\n"
                )
                print(res)

        elif opcao == "4":

            new_obj = self.Object.get_by_id(
                input(f"Digite o id d{self.pronoun} {self.name}: ")
            )

            if new_obj == None:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} não encontrad{self.pronoun}.")
                return self.menu

            res = new_obj.update()

            if res == 1:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} atualizad{self.pronoun} com sucesso.")
            else:
                print(
                    "============================================================================\n"
                )
                print(res)
        elif opcao == "5":
            new_obj = self.Object.get_by_id(
                input(f"Digite o id d{self.pronoun} {self.name}: ")
            )

            if new_obj == None:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} não encontrad{self.pronoun}.")
                return self.menu

            res = new_obj.delete()
            if res == 1:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} deletad{self.pronoun} com sucesso.")
            elif res == None:
                print(
                    "============================================================================\n"
                )
                print(f"\n{self.name} não encontrad{self.pronoun} ou erro do servidor")
            else:
                print(res)
        elif opcao == "6":
            return 1

        return self.menu

    def executar(self):
        self.show_menu()
        while True:
            option = input("Digite a opção desejada: ")
            if option in ["1", "2", "3", "4", "5", "6"]:
                return self.processar_opcao(option)
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")


class InterfaceMission:
    def __init__(self, adm, menu_f, menu_s):
        self.adm = adm
        self.menu_f = menu_f
        self.menu_s = menu_s

    def show_menu(self):
        print(
            "============================================================================"
        )
        print("O que você deseja gerenciar hoje?\n")
        print("1. Listar Missões")
        print("2. Missão Existente")
        print("3. Nova Missão")
        print("4. Gerar relatório de Missão")
        print("5. Voltar")
        print(
            "============================================================================"
        )

    def process_options(self, opcao):
        if opcao == "1":
            print(f"Listando Todas as Missões:")
            process_items(Mission.get_all())
        elif opcao == "2":
            return 6
        elif opcao == "3":
            res = self.adm.set_mission()
            print(res)
        elif opcao == "4":
            print("Gerando relatório de Missão")
            missao_id = input("Digite o id da Missão: ")

            if not Mission.get_by_id(missao_id):
                print(
                    "============================================================================\n"
                )
                print("Missão não encontrada.")
                return 5

            self.get_report(missao_id)
        elif opcao == "5":
            return 1

        return 5

    def get_report(self, mission_id):
        mission = Mission.get_by_id(mission_id)

        mission_report = f"Relatório da Missão {mission.id}:\n"
        mission_report += f"Descrição: {mission.descricao}\n"
        mission_report += f"Status: {mission.status}\n"
        mission_report += f"Data: {mission.data}\n"
        mission_report += "Equipamentos Utilizados:\n"

        equipments = mission.get_equipments_by_mission()
        if equipments:
            for equip in equipments:
                mission_report += f"- {equip[0].nome} (Quantidade: {equip[1]})\n"
        else:
            mission_report += "- Nenhum equipamento utilizado\n"

        mission_report += "Heróis Envolvidos:\n"
        heroes = mission.get_heroes_by_mission()
        if heroes:
            for hero in heroes:
                mission_report += f"- {hero.nome}\n"
        else:
            mission_report += "- Nenhum herói envolvido\n"

        # mission_report += "Vilões Envolvidos:\n"
        # viloes = mission.get_villain_by_mission()
        # if viloes:
        #     for vilao in viloes:
        #         mission_report += f"- {vilao.nome}\n"
        # else:
        #     mission_report += "- Nenhum vilão envolvido\n"

        print(
            "============================================================================\n"
        )
        print(mission_report)

    def crud_menu(self):
        print(
            "============================================================================\n"
        )
        print("O que você deseja fazer com a Missão?")
        print("1. Adicionar Heróis")
        print("2. Remover Heróis")
        print("3. Adicionar Equipamentos")
        print("4. Remover Equipamentos")
        print("5. Atualizar dados Missão")
        print("6. Deletar Missão")
        print("7. Voltar")

    def process_crud_menu(self, option, mission_id):
        if option == "1":
            print(self.adm.heroes(mission_id))
        elif option == "2":
            print(self.adm.heroes_remove(mission_id))
        elif option == "3":
            print(self.adm.equipments(mission_id))
        elif option == "4":
            print(self.adm.equipments_remove(mission_id))
        elif option == "5":
            mission = Mission.get_by_id(mission_id)

            if mission == None:
                print(
                    "============================================================================\n"
                )
                print("Missão não encontrada.")
                return 6

            mission.update(self.adm.id)
        elif option == "6":
            mission = Mission.get_by_id(mission_id)

            if mission == None:
                print(
                    "============================================================================\n"
                )
                print("Missão não encontrada.")
                return 6

            res = mission.delete()
            if res == 1:
                print(
                    "============================================================================\n"
                )
                print("Missão deletada com sucesso.")
            elif res == None:
                print(
                    "============================================================================\n"
                )
                print("Missão não encontrada ou erro do servidor")
            else:
                print(res)
        elif option == "7":
            return 5

        return 6

    def exec_firt(self):
        self.show_menu()
        while True:
            option = input("Digite a opção desejada: ")
            if option in ["1", "2", "3", "4", "5"]:
                return self.process_options(option)
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

    def exec_second(self):
        mission_id = input("Digite o id da Missão: ")

        if not mission_id:
            print(
                "============================================================================\n"
            )
            print("Missão não encontrada.")
            return 5

        if mission_id:
            if not Mission.get_by_id(mission_id):
                print(
                    "============================================================================\n"
                )
                print("Missão não encontrada.")
                return 5

        self.get_report(mission_id)
        self.crud_menu()

        while True:
            option = input("Digite a opção desejada: ")
            if option in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                return self.process_crud_menu(option, mission_id)
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")


class Interface:
    def __init__(self, adm):
        self.adm = adm
        self.administrator = InterfaceCRUD(
            Administrator, "Administrador", "o", "Administradores", self.adm.id, 2
        )
        self.hero = InterfaceCRUD(Hero, "Herói", "o", "Heróis", self.adm.id, 3)
        self.villain = InterfaceCRUD(Villain, "Vilão", "o", "Vilões", self.adm.id, 4)
        self.mission = InterfaceMission(self.adm, 5, 6)
        self.equipment = InterfaceCRUD(
            Equipment, "Equipamento", "o", "Equipamentos", self.adm.id, 7
        )

    def show_menu(self):
        print(
            "============================================================================"
        )
        print(
            f"Bem-vindo ao sistema de gerenciamento de super-heróis e vilões {self.adm.nome}.\n"
        )
        print("O que você deseja gerenciar hoje?\n")
        print("1. Administrador")
        print("2. Herói")
        print("3. Vilão")
        print("4. Missão")
        print("5. Equipamento")
        print("6. Logout")
        print(
            "============================================================================"
        )

    def administrador(self):
        return self.administrator.executar()

    def heroi(self):
        return self.hero.executar()

    def vilao(self):
        return self.villain.executar()

    def missao_f(self):
        return self.mission.exec_firt()

    def missao_s(self):
        return self.mission.exec_second()

    def equipamento(self):
        return self.equipment.executar()

    def processar_opcao(self, opcao):
        if opcao == "1":
            return 2
        elif opcao == "2":
            return 3
        elif opcao == "3":
            return 4
        elif opcao == "4":
            return 5
        elif opcao == "5":
            return 7
        elif opcao == "6":
            return 0
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

    def executar(self):
        self.show_menu()
        while True:
            option = input("Digite a opção desejada: ")
            if option in ["1", "2", "3", "4", "5", "6"]:
                return self.processar_opcao(option)
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
