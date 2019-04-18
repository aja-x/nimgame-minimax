from anytree import Node, RenderTree, findall


class Tree:
    def __init__(self, root_value, player_turn):
        self.root_value = root_value
        self.player_turn = player_turn  # player_turn: True = Human, False = Computer
        self.current_state = 0
        self.check_state = True
        if self.player_turn:
            self.tree = [Node(self.current_state, node_value=[self.root_value], is_final=False, state_value=1)]
        else:
            self.tree = [Node(self.current_state, node_value=[self.root_value], is_final=False, state_value=-1)]
        # self.render_tree()

    def render_tree(self):
        while self.check_state:
            self.player_turn = not self.player_turn
            for i in findall(self.tree[0], filter_=lambda n: n.depth == self.current_state):
                print(i)
                for j in self.count_child(i):
                    self.tree.append(Node(len(self.tree)+1, parent=self.tree[i.name], node_value=j, state_value=None))
            self.current_state += 1
            # print(RenderTree(self.tree[0]))

    def count_child(self, node):
        value = []
        for k in node.node_value:
            j = 0
            temp = k
            while temp - 1 >= j + 1:
                value.append(self.set_child_value(node.node_value, k, j + 1))
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

    def set_node(self, parent_node, ):
        pass


tree = Tree(9, True)
tree.render_tree()