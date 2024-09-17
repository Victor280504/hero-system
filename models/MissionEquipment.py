# Responsável por gerenciar a relação entre as missões e os equipamentos

from config.Database import Database
from models.Equipment import Equipment
from utils.decorators import exception_handler
from utils.exceptions import NotFoundError, DatabaseError, ValidationError
from utils.response import Response

class MissionEquipment:
    def __init__(self, mission_id, equipment_id, quantity):
        self.id_missao = mission_id
        self.id_equipamento = equipment_id
        self.quantidade = quantity

    @staticmethod
    def get_equipments_by_mission(id) -> list:
        res = Database("missao_equipamento").find(["id_missao"], [id], "*")
        return [(Equipment.get_by_id(equip[1]).data, equip[2]) for equip in res]

    def get_attributes_dict(self) -> dict:
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes

    @staticmethod
    def get(id_missao, id_equipamento):
        res = Database("missao_equipamento").find(["id_missao", "id_equipamento"], [id_missao, id_equipamento], "*", ["=", "="])
        return MissionEquipment(*res[0]) if res else None

    @exception_handler
    def insert(self) -> Response:
        res = Database("missao_equipamento")
        equip = Equipment.get_by_id(self.id_equipamento)
        
        if not equip.success:
            raise NotFoundError(equip.message)

        if equip.data.qtd_estoque < self.quantidade:
            raise ValidationError(f"Quantidade de equipamentos insuficiente no estoque, disponível: {equip.data.qtd_estoque}")

        search = res.find(
            ["id_equipamento", "id_missao"], [self.id_equipamento, self.id_missao], "*", ["=", "="]
        )
        
        equipamento = equip.data
        equipamento.qtd_estoque -= self.quantidade
        equip_res = equipamento.update_qtd()
        
        if not equip_res.success:
            raise DatabaseError(equip_res.message)
        
        if search:
            update_qtd = res.update_field(
                {"quantidade": search[0][2] + self.quantidade},
                ["id_missao", "id_equipamento"],
                [self.id_missao, self.id_equipamento],
            )
            
            if not update_qtd:
                raise DatabaseError("Quantidade de equipamentos não foi atualizada")
            return Response(success=True, message="Quantidade de equipamentos atualizada com sucesso", data=update_qtd)
            
        iserted_item = res.insert(self.get_attributes_dict(), "id_equipamento")
        
        if not iserted_item:
            raise DatabaseError('Equipamento não foi adicionado')
        
        return Response(success=True, message="Equipamento adicionado com sucesso", data=iserted_item)
    
    @exception_handler
    def remove_equipments(self, qtd) -> Response:
        res = Database("missao_equipamento")
        equip = Equipment.get_by_id(self.id_equipamento)
        
        if not equip.success:
            raise NotFoundError(equip.message)
        
        if qtd > self.quantidade:
            raise ValidationError(f"Quantidade de equipamentos insuficiente na missão, disponível: {self.quantidade}")
        
        equipamento = equip.data
        equipamento.qtd_estoque += qtd
        equip_res = equipamento.update_qtd()
        
        if not equip_res.success:
            raise DatabaseError(equip_res.message)
        
        removed = res.update_field(
            {"quantidade": self.quantidade - qtd},
            ["id_missao", "id_equipamento"],
            [self.id_missao, self.id_equipamento],
        )
        
        return Response(success=True, message=f"Removeu {qtd} equipamento(s) {equip.data.nome} com sucesso", data=removed)
