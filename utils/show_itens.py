# responsável por mostrar os itens de uma lista

def print_items(func):
    def wrapper(items):
        for item in items:
            print(item, '\n')
        return func(items)

    return wrapper

@print_items
def process_items(items):
    # Faça algo com os itens
    return
