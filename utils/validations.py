# Responsável por lidar com as validações específicas de entrada de dados
import re

patterns = {
    "date": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$",
    "disponibilidade": ["Disponível", "Indisponível"],
}

def validate_update(data, validation_type):
    pattern = re.compile(patterns[validation_type])
    if data:
        return pattern.fullmatch(data) is not None
    else:
        return True

def validate_create(data, validation_type):
    pattern = re.compile(patterns[validation_type])
    return pattern.fullmatch(data) is not None

def validate_avalialble_c(data, validation_type):
    return data in patterns[validation_type]
    
def validate_avalialble_u(data, validation_type):
    if data:
        return data in patterns[validation_type]
    else:
        return True