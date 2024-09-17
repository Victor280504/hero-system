# Responsável por diferenciar os tipos de exceções

class NotFoundError(Exception):
    def __init__(self, message="Item não encontrado"):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    def __init__(self, message="Erro de validação"):
        self.message = message
        super().__init__(self.message)

class DatabaseError(Exception):
    def __init__(self, message="Erro no banco de dados"):
        self.message = message
        super().__init__(self.message)