from anytree import Node, RenderTree, findall


class Tree(object):
    def __init__(self, root_value, first_player):
        self.root_value = root_value
        self.first_player = first_player  # first_player: True = Human, False = Computer
        self.tree = [Node(0, node_value=[self.root_value], is_final=False, evaluator_value=None)]
        self.render_tree()

    def render_tree(self):
        current_state, check_state = 0, True
        while check_state:
            count_final = 0
            for node in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                if not node.is_final:
                    for list_ in self.set_all_child(node):
                        self.tree.append(Node(len(self.tree), parent=self.tree[node.name],
                                              node_value=list_[0], is_final=True if list_[1] == 1 else False,
                                              evaluator_value=None))
                else:
                    count_final += 1
                if count_final == self.count_siblings(current_state):
                    check_state = False
            current_state += 1
        self.set_evaluator_value()

    def set_all_child(self, node):
        result_list = []
        if max(node.node_value) == 2:
            result_list.append([self.set_child_value(node.node_value, 2, 1), 1])
        else:
            for value in node.node_value:
                number_of_children = self.count_children(value)
                if value > 2:
                    for i in range(number_of_children):
                        result_list.append([self.set_child_value(node.node_value, value, i + 1), 0])
        return self.check_duplicate(result_list)

    def count_children(self, current_value):
        return (int(current_value / 2) - 1) if current_value % 2 == 0 else int(current_value / 2)

    def check_duplicate(self, list_):
        result_list = []
        for value in list_:
            if value not in result_list:
                result_list.append(value)
        return result_list

    def set_child_value(self, list_, current_value, deduction):
        result_list = []
        is_already_split = True
        for value in list_:
            if value == current_value and is_already_split:
                result_list.append(current_value - deduction)
                result_list.append(deduction)
                is_already_split = False
            else:
                result_list.append(value)
        # result_list.sort(reverse=True)  # Uncomment for sorted list
        return result_list

    def set_evaluator_value(self):
        current_state, current_player = self.get_tree_height(), self.first_player
        while current_state >= 0:
            for node in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                node.evaluator_value = self.calculate_evaluator_value(node, current_player, current_state)
            current_player = not current_player
            current_state -= 1

    def calculate_evaluator_value(self, node, current_player, current_state):
        if node.is_final and current_state % 2 == 0:
            return -1 if current_player else 1
        elif node.is_final and current_state % 2 != 0:
            return 1 if not current_player else -1
        else:
            value = []
            for child in node.children:
                value.append(child.evaluator_value)
            if current_state % 2 == 0:
                return min(value) if current_player else max(value)
            else:
                return max(value) if not current_player else min(value)

    def count_siblings(self, current_state):
        return len(findall(self.tree[0], filter_=lambda n: n.depth == current_state))

    def get_tree(self):
        print("Total node: " + str(len(self.tree)), end="\n\n")
        # Choose between 2 type of return, simple or details
        return RenderTree(self.tree[0]).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
                                                           "  [" + str(n.evaluator_value) + "]"))
        # return RenderTree(self.tree[0])

    def get_tree_height(self):
        return self.tree[0].height
