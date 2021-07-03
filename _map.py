from _group_category import GroupCategorytBackend
from _user_category import UserCategorytBackend
from enums import CategoryEnum

CATEGORY_BACKEND_MAP = {
    CategoryEnum.GROUP: GroupCategorytBackend,
    CategoryEnum.USER: UserCategorytBackend,
    CategoryEnum.OFFICE: UserCategorytBackend,
    CategoryEnum.TASK: UserCategorytBackend,
    CategoryEnum.SUB_TASK: UserCategorytBackend,
    CategoryEnum.FIXTURE: UserCategorytBackend,
    CategoryEnum.PROJECT: UserCategorytBackend,
}
