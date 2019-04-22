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
                    for list_ in self.count_child(node):
                        self.tree.append(Node(len(self.tree), parent=self.tree[node.name],
                                              node_value=list_[0], is_final=True if list_[1] == 1 else False,
                                              evaluator_value=None))
                else:
                    count_final += 1
                if count_final == self.count_siblings(current_state):
                    check_state = False
            current_state += 1
        self.set_evaluator_value()

    def count_child(self, node):
        result_list = []
        for i in range(len(node.node_value)):
            if i != 0 and node.node_value[i] == 2:
                continue
            deduction, temp_value = 1, node.node_value[i] - 1
            while temp_value >= deduction:
                if temp_value == deduction and temp_value != 1:
                    break
                result_list.append([self.set_child_value(node.node_value, node.node_value[i], deduction),
                                    1 if temp_value == deduction else 0])
                temp_value -= 1
                deduction += 1
        return self.check_duplicate(result_list)

    def check_duplicate(self, list_):
        result_list = []
        for value in list_:
            if value not in result_list:
                result_list.append(value)
        return result_list

    def set_child_value(self, list_, current_value, deduction):
        result_list = []
        for value in list_:
            if value == current_value:
                result_list.append(current_value - deduction)
                result_list.append(deduction)
                current_value += 1
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
        elif node.is_final:
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
        # Choose between 2 type of return, simple or details
        return RenderTree(self.tree[0]).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
                                                           "  [" + str(n.evaluator_value) + "]"))
        # return RenderTree(self.tree[0])

    def get_tree_height(self):
        return self.tree[0].height
