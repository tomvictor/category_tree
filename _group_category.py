from category_base import CategorytBackendBase
from node import Node


class GroupCategorytBackend(CategorytBackendBase):
    name = "group_category"

    def prepare_nodes(self):
        groups = self.get_groups()
        for group in groups:
            node = Node(self.name, depth=self.depth, instance=group)
            self.add_children(node)
            self.nodes.append(node)

        # # handle none groups
        # none_group = Node(self.name, depth=self.depth, instance=group)

    def get_groups(self):
        # TODO
        # groups = Group.objects.filter(members__id__in = self.queryset.valuelist("user_id",flat=True))
        groups = [1, 3]
        return groups
