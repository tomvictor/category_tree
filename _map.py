from _group_category import GroupCategorytBackend
from _user_category import UserCategorytBackend
from enums import CategoryEnum

CATEGORY_BACKEND_MAP = {
    CategoryEnum.GROUP: GroupCategorytBackend,
    CategoryEnum.USER: UserCategorytBackend,
    # TODO : Complete
}
