from anytree import Node, RenderTree, findall


class Tree:
    def __init__(self, root_value, player_turn):
        self.root_value = root_value
        self.player_turn = player_turn  # player_turn: True = Human, False = Computer
        self.current_state = 0
        self.check_state = True
        if self.player_turn:
            self.tree = [Node(self.current_state, node_value=[self.root_value], is_final=False, state_value=None)]
        else:
            self.tree = [Node(self.current_state, node_value=[self.root_value], is_final=False, state_value=None)]
        self.render_tree()

    def render_tree(self):
        while self.check_state:
            count_final = 0
            for i in findall(self.tree[0], filter_=lambda n: n.depth == self.current_state):
                if not i.is_final:
                    for j in self.count_child(i):
                        self.tree.append(Node(len(self.tree), parent=self.tree[i.name],
                                              node_value=j[0], is_final=j[1], state_value=None))
                else:
                    count_final += 1
                if count_final == self.count_siblings():
                    self.check_state = False

            self.current_state += 1

    def count_child(self, node):
        value = []
        for k in node.node_value:
            j = 0
            temp = k
            while temp - 1 >= j + 1:
                value.append([self.set_child_value(node.node_value, k, j + 1), True if temp - 1 == j + 1 else False])
                temp -= 1
                j += 1
        return value

    def set_child_value(self, node, k, j):
        value = []
        for i in node:
            if i == k:
                value.append(k - j)
                value.append(j)
            else:
                value.append(i)
        value.sort(reverse=True)
        return value

    def count_siblings(self):
        return len(findall(self.tree[0], filter_=lambda n: n.depth == self.current_state))

    def get_tree(self):
        return RenderTree(self.tree[0]).by_attr(lambda n: "-".join(map(str, n.node_value)))
        # return RenderTree(self.tree[0])

    def get_tree_height(self):
        return self.tree[0].height


tree = Tree(5, True)
print(tree.get_tree())
print(tree.get_tree_height())
