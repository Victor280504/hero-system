def make_dict(pessoa_itens: list) -> dict:
    new_res = {}
    for value in pessoa_itens:
        new_value = input(f"Digite o {value}: ")

        while not new_value:
            new_value = input(f"Digite o {value}: ")

        if new_value:
            new_res[value] = new_value

    return new_res