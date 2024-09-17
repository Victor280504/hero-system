# Responsável por gerenciar as interfaces do sistema

from models.Administrator import Administrator
from models.Hero import Hero
from models.Villain import Villain
from models.Equipment import Equipment
from system.interfaces.InterfaceCRUD import InterfaceCRUD
from system.interfaces.InterfaceMission import InterfaceMission

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
