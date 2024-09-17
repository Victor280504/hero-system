# Responável por realizar a manipulação dos dados referentes a entrada de dados

from utils.show_itens import process_items
from utils.input import Input
from utils.response import Response

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
            data = Input.make_dict(self.Object.get_attributes_list()[1:])
            res = self.Object.insert(data)
            Input.print_slash()
            if res.success:
                print(
                    f"{self.name} de id {res.data} inserid{self.pronoun} com sucesso."
                )
            else:
                print(f"\nErro ao inserir {self.name}: {res.message}")

        elif opcao == "2":
            print(f"Listando Todos {self.pronoun}s {self.plural}:")
            res = self.Object.get_all()
            Input.print_slash()
            if res.success:
                process_items(res.data)
            else:
                print(f"\nErro ao listar {self.plural}: {res.message}")

        elif opcao == "3":
            res = self.Object.get_by_id(
                Input.get_string(f"Digite o id d{self.pronoun} {self.name}: ")
            )
            Input.print_slash()
            if res.success:
                print(res.data)
            else:
                print(f"\n{self.name} não encontrad{self.pronoun}: {res.message}")

        elif opcao == "4":
            new_obj = self.Object.get_by_id(
                Input.get_string(f"Digite o id d{self.pronoun} {self.name}: ")
            )
            Input.print_slash()
            if not new_obj.success:
                print(f"\n{self.name} não encontrad{self.pronoun}: {new_obj.message}")
                return self.menu

            data = Input.make_dict_for_update(self.Object.get_attributes_list()[1:])
            res = new_obj.data.update(data)
            if res.success:
                print(f"\n{self.name} atualizad{self.pronoun} com sucesso.")
            else:
                print(f"\nErro ao atualizar {self.name}: {res.message}")

        elif opcao == "5":
            new_obj = self.Object.get_by_id(
                Input.get_string(f"Digite o id d{self.pronoun} {self.name}: ")
            )
            Input.print_slash()
            if not new_obj.success:
                print(f"\n{self.name} não encontrad{self.pronoun}: {new_obj.message}")
                return self.menu

            if (
                Input.get_confirmation(
                    f"Você deseja deletar o {self.name} (s/n)? Todas os elementos relacionadas ao id do {self.name} serão deletados: "
                )
                == "s"
            ):
                res = new_obj.data.delete()
            else:
                res = Response(success=False, message="Operação cancelada")

            if res.success:
                print(f"\n{self.name} deletad{self.pronoun} com sucesso.")
            else:
                print(f"\nErro ao deletar {self.name}: {res.message}")

        elif opcao == "6":
            return 1

        return self.menu

    def executar(self):
        self.show_menu()
        option = Input.get_option("Sua escolha: ", ["1", "2", "3", "4", "5", "6"])
        return self.processar_opcao(option)