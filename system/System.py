# Responsável por controlar o fluxo do sistema, chamando as interfaces e processando as opções do usuário

from models.Administrator import Administrator
from models.Hero import Hero
from utils.show_itens import process_items
from system.interfaces.Interface import Interface
from utils.input import Input

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
        Input.print_slash()
        print("Bem vind@ ao sistema de gerenciamento de super-heróis")
        Input.print_slash()
        print("Por favor, selecione uma opção:")
        print("1. Logar como Administrador")
        print("2. Novo Administrador")
        print("3. Ver lista de heróis")
        print("4. Exit")
        Input.print_slash()
        option = Input.get_option("Digite a opção desejada: ", ["1", "2", "3", "4"])
        return self.process_first_menu(option)
           
    def process_first_menu(self, option):
        if option == "1":
            return self.authenticate_admin()
        elif option == "2":
            data = Input.make_dict(Administrator.get_attributes_list()[1:])
            adm_id = Administrator.insert(data)
            adm = Administrator.get_by_id(str(adm_id.data))
            
            if not adm.success:
                print(adm.message)
                return 0
            
            self.admin = adm.data
            self.admin_authenticated = True
            self.interface = Interface(self.admin)
            return 1
        elif option == "3":
            print("Esses são os nossos heróis cadastrados")
            heroes = Hero.get_all()
            
            if not heroes.success:
                print(heroes.message)
                return 0
            
            process_items(heroes.data)
            return 0
        elif option == "4":
            print("Até mais! Obrigado por utilizar o nosso sistema =)")
            exit()
        else:
            return 0

    def authenticate_admin(self):
        adm = Administrator.sign_in(Input.make_dict(["login", "senha"]))
        if adm.success:
            self.admin_authenticated = True
            self.admin = adm.data
            self.interface = Interface(self.admin)
        else:
            Input.print_slash()
            print(adm.message)
            self.admin_authenticated = False
            return 0
        return 1
