from anytree import Node, RenderTree, findall


class Tree:
    def __init__(self, root_value, player):
        self.tree = None
        self.root_value = root_value
        self.player = player  # player 0 = Human, 1 = Computer
        self.current_state = 0
        self.check_state = True
        self.render_tree()

    def render_tree(self):
        if self.player == 0:
            self.tree = [Node(self.current_state, node_value=[0, [self.root_value]])]
        else:
            self.tree = [Node(self.current_state, node_value=[1, [self.root_value]])]
        self.current_state += 1

        # current_node = RenderTree(self.tree).by_attr("node_value")
        while self.check_state:
            for i in findall(self.tree[0], filter_=lambda n: n.depth == 1):
                for j in self.count_child(i):
                    pass  # mentok, lanjut besok

    def count_child(self, node):
        deduction = 1
        value = []
        for i in node.node_value[1]:
            while i > deduction:
                value.append(i - 1)
                deduction += 1
                i -= 1
            deduction = 1
        value.sort(reverse=True)
        return value

    # def make_node(self, value, parent):
    #     self.tree.append(Node(self.calculate_value(value), parent=parent))
    #
