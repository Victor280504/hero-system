
def factory(Object) -> object:
    new_data = []

    for value in Object.get_attributes_list():
        new_value = input(f"Digite o {value}: ")
        if new_value:
            new_data.append(new_value)

    return Object(*new_data)
