import enum


class CategoryEnum(enum.Enum):
    GROUP = 0
    USER = 1
    OFFICE = 2
    TASK = 3
    SUB_TASK = 4
    FIXTURE = 5
    PROJECT = 6


class TimeFactorEnum(enum.Enum):
    EFFECTIVE = 0
    CUMULATIVE = 1
