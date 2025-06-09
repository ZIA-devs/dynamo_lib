from loguru import logger
from functools import wraps
from typing import Callable, Any, TypeVar, ParamSpec, get_type_hints


def default_return_for_type(typ: Any) -> Any:
    if typ is None or typ is type(None):
        return None

    origin = get_origin(typ)
    args = get_args(typ)

    # Se for Union, retorna o default do primeiro tipo que não seja None
    if origin is Union:
        non_none_args = [t for t in args if t is not type(None)]
        if non_none_args:
            return default_return_for_type(non_none_args[0])
        return None

    if typ is bool or origin is bool: return False
    if typ is list or origin is list: return []
    if typ is dict or origin is dict: return {}
    if typ is str or origin is str: return ''
    if typ is int or origin is int: return 0
    if typ is float or origin is float: return 0.0

    try:
        return typ()
    except Exception:
        return None


P = ParamSpec("P"); R = TypeVar("R")
def log_exceptions(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except Exception:
            logger.exception(f"Erro na função {func.__name__}")
            return_type = get_type_hints(func).get("return", None)
            return default_return_for_type(return_type)
    return wrapper
