from loguru import logger
from functools import wraps
from typing import Callable, Any, TypeVar, ParamSpec, get_type_hints


def default_return_for_type(typ: Any) -> Any:
    origin = getattr(typ, '__origin__', typ)
    if typ is None or typ is type(None): return None
    if origin is bool: return False
    if origin is list: return []
    if origin is dict: return {}
    if origin is str: return ''
    if origin is int: return 0
    if origin is float: return 0.0
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
