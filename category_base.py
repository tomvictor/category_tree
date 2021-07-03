class CategorytBackendBase(object):
    name = "category_base"

    def __init__(self, queryset, raw_queryset, nodes, depth, n, queue):
        self.raw_queryset = raw_queryset
        self.queryset = queryset
        self.nodes = nodes
        self.depth = depth
        self.queue = queue
        self.n = n

    def prepare_nodes(self):
        pass

    def generate_nodes(self):
        self.prepare_nodes()
        return self.nodes

    def add_children(self, node):
        if self.depth > self.n:
            return
        else:
            backend_cls = self.queue[self.n + 1]
            backend = backend_cls(
                self.queryset,
                self.raw_queryset,
                node,
                self.depth,
                self.n + 1,
                self.queue,
            )
            backend.generate_nodes()
            # node.add_child()

            return self.nodes
