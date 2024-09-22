# Responsável por lidar com a entrada de dados do usuário
from utils.validations import (
    validate_update,
    validate_create,
    validate_avalialble_c,
    validate_avalialble_u,
)
from utils.exceptions import ValidationError


class Input:
    @staticmethod
    def get_string(prompt, min_length=1, max_length=255):
        while True:
            user_input = input(prompt)

            try:
                if not user_input:
                    raise ValidationError(
                        "Entrada inválida. Por favor, digite um texto."
                    )

                if len(user_input) < min_length:
                    raise ValidationError(
                        f"Entrada muito curta. Deve ter pelo menos {min_length} caracteres."
                    )
                elif len(user_input) > max_length:
                    raise ValidationError(
                        f"Entrada muito longa. Deve ter no máximo {max_length} caracteres."
                    )

                return user_input
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_int(prompt, min_value=None, max_value=None):
        while True:
            try:
                user_input = int(input(prompt))
                if min_value is not None and user_input < min_value:
                    print(f"Valor muito baixo. Deve ser pelo menos {min_value}.")
                elif max_value is not None and user_input > max_value:
                    print(f"Valor muito alto. Deve ser no máximo {max_value}.")
                else:
                    return user_input
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    @staticmethod
    def get_option(prompt, valid_options):
        while True:
            user_input = input(prompt)
            try:
                if user_input not in valid_options:
                    raise ValidationError(
                        f"Opção inválida. Por favor, selecione uma das seguintes opções: {', '.join(valid_options)}."
                    )
                return user_input
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_text(prompt):
        while True:
            text_input = input(prompt)
            try:
                if not text_input:
                    raise ValidationError(
                        "Entrada inválida. Por favor, digite um texto."
                    )
                return text_input
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_text_update(prompt):
        while True:
            text_input = input(prompt)
            try:
                return text_input
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_date(prompt, validation):
        while True:
            date_input = input(prompt)
            try:
                if validation(date_input, "date"):
                    return date_input
                else:
                    raise ValidationError(
                        "Data inválida. Por favor, digite a data no seguinte formato DD/MM/YYYY."
                    )
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_available(prompt, validation):
        while True:
            date_input = input(prompt)
            try:
                if validation(date_input, "disponibilidade"):
                    return date_input
                else:
                    raise ValidationError(
                        "Disponibilidade inválida. Por favor, digite a disponibilidade como 'Disponível' ou 'Indisponível'."
                    )
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_confirmation(prompt):
        while True:
            user_input = input(prompt).lower()
            try:
                if user_input not in ["s", "n"]:
                    raise ValidationError(
                        "Opção inválida. Por favor, selecione 's' para sim ou 'n' para não: "
                    )
                return user_input
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def make_dict(itens: list) -> dict:
        new_res = {}
        for value in itens:
            if value in ["data", "data_inicio_adm"]:
                new_res[value] = Input.get_date(
                    f"Digite a {value} no seguinte formato DD/MM/YYYY: ",
                    validate_create,
                )
            elif value in ["disponibilidade"]:
                new_res[value] = Input.get_available(
                    f"Digite a {value} como 'Disponível' ou 'Indisponível': ",
                    validate_avalialble_c,
                )
            else:
                new_res[value] = Input.get_text(f"Digite o {value}: ")
        return new_res

    @staticmethod
    def make_dict_for_update(itens: list) -> dict:
        new_res = {}
        for value in itens:
            if value in ["data", "data_inicio_adm"]:
                res = Input.get_date(
                    f"Digite a {value} no seguinte formato DD/MM/YYYY (deixe em branco para não atualizar): ",
                    validate_update,
                )
                if res != "":
                    new_res[value] = res
            elif value in ["disponibilidade"]:
                res = Input.get_available(
                    f"Digite a {value} como 'Disponível' ou 'Indisponível' (deixe em branco para não atualizar): ",
                    validate_avalialble_u,
                )
                if res != "":
                    new_res[value] = res
            else:
                res = Input.get_text_update(
                    f"Digite o novo {value} (deixe em branco para não atualizar): "
                )
                if res != "":
                    new_res[value] = res
        return new_res

    @staticmethod
    def get_list(prompt):
        while True:
            user_input = input(prompt).replace(" ", "")
            try:
                if not user_input:
                    raise ValidationError(
                        "Entrada inválida. Por favor, digite uma lista de valores separados por vírgula."
                    )
                    
                new_res = user_input.split(",")
                
                for value in new_res:
                    if value == " ":
                        new_res.remove(value)

                if len(new_res) == 1:
                    return [user_input]
                    
                    
                return new_res
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def get_list_with_validation(prompt, validation):
        while True:
            user_input = input(prompt).replace(" ", "")
            try:
                if not user_input:
                    raise ValidationError(
                        "Entrada inválida. Por favor, digite uma lista de valores separados por vírgula."
                    )

                new_res = user_input.split(",")
                
                for value in new_res:
                    if value == " ":
                        new_res.remove(value)

                for value in new_res:
                    if value not in validation:
                        raise ValidationError(
                        "Valor indisponível. Por favor, digite uma lista de valores separados por vírgula."
                    )

                if len(new_res) == 1:
                    return [user_input]

                return new_res
            except ValidationError as e:
                print(e.message)

    @staticmethod
    def print_slash():
        print(
            "============================================================================\n"
        )
