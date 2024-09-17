# Classe responsável por retornar uma resposta padrão

class Response:
    def __init__(self, success, message, data=None):
        self.success = success
        self.message = message
        self.data = data

    def __repr__(self):
        return f"Response(success={self.success}, message='{self.message}', data={self.data})"