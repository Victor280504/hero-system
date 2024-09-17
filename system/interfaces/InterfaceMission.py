# Responsável por lidar com a entrada de dados da missão, e seus componentes associativos

from models.Hero import Hero
from models.Mission import Mission
from models.Villain import Villain
from models.Equipment import Equipment
from utils.show_itens import process_items
from utils.input import Input
from utils.response import Response
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, ValidationError
from models.MissionEquipment import MissionEquipment
from models.MissionHero import MissionHero
from models.MissionVillain import MissionVillain


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
            all_missions = Mission.get_all()

            Input.print_slash()
            if all_missions.success:
                process_items(all_missions.data)
            else:
                print(f"\nErro ao listar Missões: {all_missions.message}")
                return self.menu_f
        elif opcao == "2":
            return self.menu_s
        elif opcao == "3":
            mission_id = self.set_mission()

            Input.print_slash()
            if not mission_id.success:
                print(f"Ocorreu um erro: {mission_id.message}")
                return self.menu_f

            print(f"Missão de id {mission_id.data} criada com sucesso")

            if Input.get_confirmation("Deseja adicionar equipamentos (s/n)? ") == "s":
                eqp_res = self.set_equipments(mission_id.data)
                if eqp_res.success:
                    print(eqp_res.message)
                else:
                    print(f"Ocorreu um erro: {eqp_res.message}")

            if Input.get_confirmation("Deseja adicionar heróis (s/n)? ") == "s":
                hero_res = self.set_heroes(mission_id.data)
                if hero_res.success:
                    print(hero_res.message)
                else:
                    print(f"Ocorreu um erro: {hero_res.message}")

            if Input.get_confirmation("Existe algum vilão associado (s/n)? ") == "s":
                villain_res = self.set_villains(mission_id.data)
                if villain_res.success:
                    print(villain_res.message)
                else:
                    print(f"Ocorreu um erro: {villain_res.message}")
        elif opcao == "4":
            print("Gerando relatório de Missão")
            missao_id = Input.get_text("Digite o id da Missão: ")
            mission = Mission.get_by_id(missao_id)
            if not mission.success:
                print(f"Missão não encontrada: {mission.message}")
                return self.menu_f
            self.get_report(missao_id)
        elif opcao == "5":
            return 1

        return self.menu_f

    def exec_firt(self):
        self.show_menu()
        option = Input.get_option("Digite a opção desejada:", ["1", "2", "3", "4", "5"])
        return self.process_options(option)

    def crud_menu(self):
        print(
            "============================================================================\n"
        )
        print("O que você deseja fazer com a Missão?")
        print("1. Adicionar Heróis")
        print("2. Remover Heróis")
        print("3. Adicionar Equipamentos")
        print("4. Remover Equipamentos")
        print("5. Adicionar Vilões")
        print("6. Remover Vilões")
        print("7. Atualizar dados Missão")
        print("8. Deletar Missão")
        print("9. Voltar")

    def process_crud_menu(self, option, mission_id):
        Input.print_slash()
        if option == "1":
            res = self.set_heroes(mission_id)
            print(res.message)
        elif option == "2":
            res = self.remove_heroes(mission_id)
            print(res.message)
        elif option == "3":
            res = self.set_equipments(mission_id)
            if res.success:
                print(res.message)
            else:
                print(res.message)
                print(res.data)
        elif option == "4":
            res = self.remove_equipments(mission_id)
            if res.success:
                print(res.message)
            else:
                print(res.message)
                print(res.data)
        elif option == "5":
            res = self.set_villains(mission_id)
            print(res.message)
        elif option == "6":
            res = self.remove_villains(mission_id)
            print(res.message)
        elif option == "7":
            mission = Mission.get_by_id(mission_id)
            if not mission.success:
                print(mission.message)
                return self.menu_s
            data = Input.make_dict_for_update(Mission.get_attributes_list()[1:6])
            res = mission.data.update(data)

            if res.success:
                print(f"Missão de id {mission_id} atualizada com sucesso.")
            else:
                print(f"Erro ao atualizar Missão: {res.message}")
        elif option == "8":
            mission = Mission.get_by_id(mission_id)

            if not mission.success:
                print(mission.message)
                return self.menu_s

            res = mission.data.delete()

            if res.success:
                print(f"Missão de id {mission_id} deletada com sucesso.")
                return self.menu_f
            else:
                print(f"Erro ao deletar Missão: {res.message}")
        elif option == "9":
            return self.menu_f

        return self.menu_s

    def exec_second(self):
        mission_id = Input.get_text("Digite o id da Missão: ")
        Input.print_slash()

        mission = Mission.get_by_id(mission_id)

        if not mission.success:
            print(f"Missão não encontrada: {mission.message}")
            return self.menu_f

        while True:
            res = self.exec_second_option(mission_id)
            if res == self.menu_f:
                return res

    def exec_second_option(self, mission_id):
        self.get_report(mission_id)
        self.crud_menu()
        option = Input.get_option(
            "Digite a opção desejada: ", ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        )
        return self.process_crud_menu(option, mission_id)

    def get_report(self, mission_id):
        res = Mission.get_by_id(mission_id)
        mission = res.data

        mission_report = f"Relatório da Missão {mission.id}:\n"
        mission_report += f"Descrição: {mission.descricao}\n"
        mission_report += f"Status: {mission.status}\n"
        mission_report += f"Data: {mission.data}\n"
        mission_report += "Equipamentos Utilizados:\n"

        equipments = mission.equipments
        if equipments:
            for equip in equipments:
                mission_report += f"- {equip[0].nome} (Quantidade: {equip[1]})\n"
        else:
            mission_report += "- Nenhum equipamento utilizado\n"

        mission_report += "Heróis Envolvidos:\n"
        heroes = mission.heroes
        if heroes:
            for hero in heroes:
                mission_report += f"- {hero.nome}\n"
        else:
            mission_report += "- Nenhum herói envolvido\n"

        mission_report += "Vilões Envolvidos:\n"
        viloes = mission.villains
        if viloes:
            for vilao in viloes:
                mission_report += f"- {vilao.nome}\n"
        else:
            mission_report += "- Nenhum vilão envolvido\n"

        Input.print_slash()
        print(mission_report)

    def set_mission(self) -> Response:
        data = Input.make_dict(Mission.get_attributes_list()[1:6])
        data["id_adm"] = self.adm.id
        res = Mission.insert(data)
        return res

    @exception_handler
    def get_available_items(self, Object, item_type) -> Response:
        avaliable = Object.get_available()

        if not avaliable:
            raise NotFoundError(f"Não há {item_type} disponíveis")

        print(f"{item_type} disponíveis:")
        process_items(avaliable)

        return Response(
            success=True,
            message=f"{item_type} disponíveis",
            data=[str(item.id) for item in avaliable],
        )

    @exception_handler
    def set_equipments(self, mission_id) -> Response:

        avaliable_ids = self.get_available_items(Equipment, "Equipamentos")

        if not avaliable_ids.success:
            raise NotFoundError(avaliable_ids.message)

        eqp_data = Input.get_list_with_validation(
            "Digite os IDs dos equipamentos que deseja adicionar separados por vírgula: ",
            avaliable_ids.data,
        )
        eqp_qtd = Input.get_list(
            "Digite a quantidade de cada equipamento separados por vírgula: "
        )

        if len(eqp_data) != len(eqp_qtd):
            raise ValidationError(
                "O número de equipamentos e quantidades de equipamentos não são iguais"
            )

        equipments = [(eqp_data[i], eqp_qtd[i]) for i in range(len(eqp_data))]

        response = []

        for equip in equipments:
            mission_equipment = MissionEquipment(mission_id, equip[0], int(equip[1]))
            result = mission_equipment.insert()
            if not result.success:
                response.append(
                    str(result.message) + " para o equipamento de id " + equip[0]
                )
        
        if len(response) > 0:
            return Response(
                success=False,
                message="Alguns equipamentos não foram adicionados, verifique no menu individual da missão.",
                data=response,
            )

        return Response(
            success=True, message="Equipamentos adicionados com sucesso", data=response
        )

    @exception_handler
    def remove_equipments(self, mission_id) -> Response:
        mission = Mission.get_by_id(mission_id)
        equipments = mission.data.equipments
        available_ids = [str(equip[0].id) for equip in equipments]

        if not equipments:
            raise NotFoundError("A missão não possui equipamentos")

        print("Equipamentos:")
        for equip in equipments:
            print(f"ID: {equip[0].id}- {equip[0].nome} (Quantidade: {equip[1]})\n")

        eqp_data = Input.get_list_with_validation(
            "Digite os IDs dos equipamentos que deseja remover separados por vírgula: ",
            available_ids,
        )
        eqp_qtd = Input.get_list(
            "Digite a quantidade de cada equipamento separados por vírgula: "
        )

        if len(eqp_data) != len(eqp_qtd):
            raise ValidationError(
                "O número de equipamentos e quantidades de equipamentos não são iguais"
            )

        data = [(eqp_data[i], eqp_qtd[i]) for i in range(len(eqp_data))]

        response = []

        for equip in data:
            mission_eqp = MissionEquipment.get(mission_id, equip[0])
            result = mission_eqp.remove_equipments(int(equip[1]))
            if not result.success:
                response.append(
                    str(result.message) + " para o equipamento de id " + equip[0]
                )
                
        if len(response) > 0:
            return Response(
                success=False,
                message="Alguns equipamentos não foram removidos, verifique no menu individual da missão.",
                data=response,
            )

        return Response(
            success=True, message="Equipamentos removidos com sucesso", data=response
        )

    @exception_handler
    def set_heroes(self, mission_id) -> Response:
        all_heroes = self.get_available_items(Hero, "Heróis")

        if not all_heroes.success:
            raise NotFoundError(all_heroes.message)

        herois = Input.get_list_with_validation(
            "Digite os IDs dos heróis que deseja adicionar separados por vírgula: ",
            all_heroes.data
        )

        for hero in herois:
            mission_hero = MissionHero(hero, mission_id)
            teste = mission_hero.insert()
            if not teste.success:
                raise NotFoundError(teste.message)

        return Response(
            success=True, message="Heróis adicionados com sucesso", data=herois
        )

    @exception_handler
    def remove_heroes(self, mission_id) -> Response:
        mission = Mission.get_by_id(mission_id)

        if not mission.success:
            raise NotFoundError(mission.message)

        avaliable_heroes = mission.data.heroes

        if not avaliable_heroes:
            raise NotFoundError("Não há heróis disponíveis")

        print("Heróis da missão:")
        process_items(avaliable_heroes)

        herois = Input.get_list_with_validation(
            "Digite os IDs dos heróis que deseja remover separados por vírgula: ",
            [str(hero.id) for hero in avaliable_heroes],
        )

        print(herois)
        for hero in herois:
            mission_hero = MissionHero(hero, mission_id)
            teste = mission_hero.delete()
            if not teste.success:
                raise NotFoundError(teste.message)

        return Response(
            success=True, message="Heróis removidos com sucesso", data=herois
        )

    @exception_handler
    def set_villains(self, mission_id) -> Response:
        all_villains = self.get_available_items(Villain, "Vilões")

        if not all_villains.success:
            raise NotFoundError(all_villains.message)

        viloes = Input.get_list_with_validation(
            "Digite os IDs dos vilões que deseja adicionar separados por vírgula: ",
            all_villains.data,
        )

        for vilao in viloes:
            mission_villain = MissionVillain(vilao, mission_id)
            teste = mission_villain.insert()
            if not teste.success:
                raise NotFoundError(teste.message)

        return Response(
            success=True, message="Vilões adicionados com sucesso", data=viloes
        )

    @exception_handler
    def remove_villains(self, mission_id) -> Response:
        mission = Mission.get_by_id(mission_id)

        if not mission.success:
            raise NotFoundError(mission.message)

        avaliable_villains = mission.data.villains

        if not avaliable_villains:
            raise NotFoundError("Não há vilões para remover")

        print("Vilões associados:")
        process_items(avaliable_villains)

        villains = Input.get_list_with_validation(
            "Digite os IDs dos vilões que deseja remover separados por vírgula: ",
            [str(villain.id) for villain in avaliable_villains],
        )

        for villain in villains:
            mission_villain = MissionVillain(villain, mission_id)
            teste = mission_villain.delete()
            if not teste.success:
                raise NotFoundError(teste.message)

        return Response(
            success=True, message="Vilões removidos com sucesso", data=villains
        )
