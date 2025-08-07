from enum import Enum


class ControlStatus(int, Enum):
    NEED_META_LOGIN = 0
    NEED_FIRST_LOGIN = 1
    OKAY = 2


class UserStatus(int, Enum):
    ACTIVE = 0
    INACTIVE = 1
    BLOCKED = 2
    DELETED = 3


class UserPermissions(int, Enum):
    ADMIN = 0
    EMPLOYEE = 1
    ZIA = 2


class ClientStatus(int, Enum):
    ON_BOT = 0
    ON_QUEUE = 1
    WITH_SECTOR = 2
    TAKEN = 3
    ON_HOLD = 4


class SectorStatus(int, Enum):
    IDLE = 0
    WITH_CLIENT = 1
    ON_BOT = 2


class EmpresaPlan(int, Enum):
    DELETED = -10
    ASA_EXPIRED = -3
    SCHEDULE_EXPIRED = -2
    BASIC_EXPIRED = -1

    BASIC = 0
    SCHEDULE = 1
    ASA = 2


VALID_EMPRESA_PLAN_VALUES = {item.value for item in EmpresaPlan}


class EmpresaTipo(str, Enum):
    PADRAO = "padrao"
    CLINICA = "clinica"
    SALAO = "salao"
    CORRETORA = "corretora"
    GARAGEM = "garagem"


VALID_EMPRESA_TIPO_VALUES = {item.value for item in EmpresaTipo}


class MessageTemplateHeaderType(str, Enum):
    NONE = "none"
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    DOCUMENT = "DOCUMENT"


VALID_MESSAGE_TEMPLATE_HEADER_TYPE_VALUES = {
    item.value for item in MessageTemplateHeaderType
}
