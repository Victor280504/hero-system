# Responsável por gerenciar as informações dos administradores
from config.Database import Database
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response

class Administrator:
    def __init__(self, id, nome, contato, login, senha, endereco, data_inicio_adm):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.data_inicio_adm = data_inicio_adm

    # Listar os atributos da classe
    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    @staticmethod
    @exception_handler
    def sign_in(data) -> Response:
        adm = Database("administrador")

        res = adm.findBy("login", "'" + data["login"] + "'", "*")
        
        if not res:
            return Response(success=False, message="Administrador não encontrado", data=None)

        if not res[4] == data["senha"]:
            return Response(success=False, message="Administrador ou senha incorretos", data=None)
        
        admin = Administrator.get_by_id(str(res[0]))
        
        if not admin.success:
            return DatabaseError(admin.message)
        
        return Response(success=True, message="Administrador autenticado", data=admin.data)

    @staticmethod
    def get_attributes_list() -> list:
        return [
            "id",
            "nome",
            "contato",
            "login",
            "senha",
            "endereco",
            "data_inicio_adm",
        ]

    # self methods
    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("administrador").findBy("id_adm", id, "*")

        if not res:
            raise NotFoundError("Identificador Inexistente")

        return Response(success=True, message="Administrador encontrado", data=Administrator(*res))

    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("administrador").findAll("*")
        items = [Administrator(*res) for res in res]
        return Response(success=True, message="Administradores encontrados", data=items)

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res = Database("administrador")
        
        new_adm = res.insert(data, "id_adm")
        
        if not new_adm:
            raise DatabaseError("Administrador não foi criado")
        
        return Response(success=True, message="Administrador inserido com sucesso", data=new_adm)

    @exception_handler
    def update(self, data) -> Response:
        adm = Database("administrador")

        if not data:
            return Response(success=True, message="Nenhum dado foi atualizado", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)
            
        res = adm.update(data, "id_adm", self.id)
        return Response(success=True, message="Administrador atualizado com sucesso", data=res)

    @exception_handler
    def delete(self) -> Response:
        res = Database("administrador")
        deleted = res.delete("id_adm", self.id)
        if not deleted:
            raise DatabaseError("Administrador não foi deletado")
            
        return Response(success=True, message="Administrador deletado com sucesso", data=deleted)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nContato: {self.contato}\nLogin: {self.login}\nSenha: {self.senha}\nEndereço: {self.endereco}\nData de Início: {self.data_inicio_adm}"
