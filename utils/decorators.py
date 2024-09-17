# Responsável por tratar exceções de forma genérica

from functools import wraps
from utils.response import Response
from utils.exceptions import NotFoundError, ValidationError, DatabaseError

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError as e:
            return Response(success=False, message=e.message)
        except ValidationError as e:
            return Response(success=False, message=e.message)
        except DatabaseError as e:
            return Response(success=False, message=e.message)
        except Exception as e:
            return Response(success=False, message=f"Error: {e}")
    return wrapper