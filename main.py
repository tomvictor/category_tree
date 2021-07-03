import datetime

from _map import CATEGORY_BACKEND_MAP
from enums import CategoryEnum, TimeFactorEnum


class CategoryFilter(object):
    def __init__(
        self,
        category_order,
        start_date,
        end_date,
        filter_params,
        time_factor=TimeFactorEnum.EFFECTIVE,
    ):
        self.category_order = category_order
        self.start_date = start_date
        self.end_date = end_date
        self.filter_params = filter_params
        self.raw_queryset = self.get_raw_queryset()
        self.queryset = self.get_queryset(
            self.start_date, self.end_date, **filter_params
        )

        self.queue = [CATEGORY_BACKEND_MAP[key] for key in self.category_order]
        self.depth = len(category_order)
        self.n = 0
        self.nodes = list()

    def get_queryset(self, start_date, end_date, *args, **kwargs):
        queryset = []
        # prefetch the full data
        # Apply filter logic here
        return queryset

    def get_raw_queryset(self):
        # TODO : return full queryset without filtering
        # TODO : prefetch
        return []

    def perform_grouping(self):
        if self.depth == 0:
            raise Exception("No Groups selected")
        if self.depth < self.n:
            return self.nodes
        else:
            backend_cls = self.queue[self.n]
            backend = backend_cls(
                self.queryset, self.raw_queryset, self.nodes, self.queue
            )
            backend.generate_nodes()
            return self.nodes

    def generate_data(self):
        data = [node.to_dict() for node in self.nodes]
        return data


def main(category_order, start_date, end_date, filter_params):
    filter = CategoryFilter(category_order, start_date, end_date, filter_params)
    filter.perform_grouping()
    data = filter.generate_data()
    return data


if __name__ == "__main__":

    category_order = [
        CategoryEnum.GROUP,
        # CategoryEnum.USER,
        # CategoryEnum.OFFICE,
        # CategoryEnum.TASK,
        # CategoryEnum.SUB_TASK,
        # CategoryEnum.FIXTURE,
        # CategoryEnum.PROJECT,
    ]
    start_date, end_date = datetime.datetime.now(), datetime.datetime.now()

    filter_params = {
        "group": [1, 2, 3],
        "user": [1, 2, 3],
    }

    result = main(category_order, start_date, end_date, filter_params)
    print(result)
