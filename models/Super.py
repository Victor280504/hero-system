# responsavel por manipular os dados da tabela super do banco de dados
from config.Database import Database
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError
from utils.response import Response


class Super:
    def __init__(self, id, nome, descricao, status, rank, fraqueza, arqui_inimigo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.rank = rank
        self.fraqueza = fraqueza
        self.arqui_inimigo = arqui_inimigo

    # Listar os atributos da classe
    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    # Listar as chaves dos atributos da classe
    @staticmethod
    def get_attributes_list() -> list:
        return [
            "id",
            "nome",
            "descricao",
            "status",
            "rank",
            "fraqueza",
            "arqui_inimigo",
        ]

    # RETORNA UM Super Por iD
    @staticmethod
    @exception_handler
    def get_by_id(id: str) -> Response:
        res = Database("super").findBy("id_super", id, "*")

        if not res:
            raise NotFoundError("Identificador Inexistente")

        return Response(success=True, message="Super encontrado", data=Super(*res))

    # RETORNA TODOS OS SUPER
    @staticmethod
    @exception_handler
    def get_all() -> Response:
        res = Database("super").findAll("*")
        supers = [Super(*res) for res in res]
        return Response(success=True, message="Todos os Super", data=supers)

    @staticmethod
    @exception_handler
    def insert(data) -> Response:
        res = Database("super")
        item = res.insert(data, "id_super")
        if not item:
            raise DatabaseError("Super não foi criado")
        
        return Response(success=True, message="Super inserido com sucesso", data=item)

    @exception_handler
    def update(self, data) -> Response:
        super_db = Database("super")

        if not data:
            return Response(success=True, message="Nenhum dado foi atualizado", data=None)

        for key, value in data.items():
            self.__setattr__(key, value)

        res = super_db.update(data, "id_super", self.id)
        
        return Response(success=True, message="Super atualizado com sucesso", data=res)

    @exception_handler
    def delete(self) -> Response:
        res = Database("super")
        item = res.delete("id_super", self.id)
        if not item:
            raise DatabaseError("Super não foi deletado")
        return Response(success=True, message="Vilão deletado com sucesso", data=item)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nDescrição: {self.descricao}\nStatus: {self.status}\nRank: {self.rank}\nFraqueza: {self.fraqueza}\nArqui Inimigo: {self.arqui_inimigo}"
