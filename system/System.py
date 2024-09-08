from models.Administrator import Administrator
from models.Hero import Hero
from utils.show_itens import process_items
from system.Interface import Interface


class System:
    def __init__(self):
        self.admin_authenticated = False
        self.admin = None
        self.interface = None
        self.menu = 0

    def run(self):
        while True:
            if self.menu == 0:
                self.menu = self.first_menu()
            elif self.menu == 1:
                self.menu = self.interface.executar()
            elif self.menu == 2:
                self.menu = self.interface.administrador()
            elif self.menu == 3:
                self.menu = self.interface.heroi()
            elif self.menu == 4:
                self.menu = self.interface.vilao()
            elif self.menu == 5:
                self.menu = self.interface.missao_f()
            elif self.menu == 6:
                self.menu = self.interface.missao_s()
            elif self.menu == 7:
                self.menu = self.interface.equipamento()

    def first_menu(self):
        print(
            "============================================================================"
        )
        print("Bem vind@ ao sistema de gerenciamento de super-heróis")
        print(
            "============================================================================"
        )
        print("Por favor, selecione uma opção:")
        print("1. Logar como Administrador")
        print("2. Novo Administrador")
        print("3. Ver lista de heróis")
        print("4. Exit")
        print(
            "============================================================================"
        )
        while True:
            option = input("Digite a opção desejada: ")
            if option in ["1", "2", "3", "4"]:
                return self.process_first_menu(option)
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

    def process_first_menu(self, option):
        if option == "1":
            return self.authenticate_admin()
        elif option == "2":
            adm_id = Administrator.insert()
            self.admin = Administrator.get_by_id(str(adm_id))
            self.admin_authenticated = True
            self.interface = Interface(self.admin)
            return 1
        elif option == "3":
            print("Esses são os nossos heróis cadastrados")
            process_items(Hero.get_all())
            return 0
        elif option == "4":
            print("Até mais!")
            exit()
        else:
            return 0

    def authenticate_admin(self):
        self.admin = Administrator.sign_in()
        if self.admin:
            self.admin_authenticated = True
            self.interface = Interface(self.admin)
        else:
            print(
                "============================================================================"
            )
            print("Invalid credentials. Please try again.")
            self.admin_authenticated = False
            return 0
        return 1
