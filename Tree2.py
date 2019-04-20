from anytree import Node, RenderTree, findall


class Tree2(object):
    def __init__(self, root_value, first_player):
        self.root_value = root_value
        self.first_player = first_player  # first_player: True = Human, False = Computer
        self.tree = [Node(0, node_value=[self.root_value], is_final=False, evaluator_value=None)]
        self.render_tree()

    def render_tree(self):
        current_state = 0
        check_state = True
        while check_state:
            count_final = 0
            for node in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                if not node.is_final:
                    for list_ in self.count_child(node):
                        self.tree.append(Node(len(self.tree), parent=self.tree[node.name],
                                              node_value=list_[0], is_final=list_[1], evaluator_value=None))
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
                break
            deduction = 1
            temp_value = node.node_value[i] - 1
            while temp_value >= deduction:
                if temp_value / deduction == 1 and temp_value != 1:
                    break
                else:
                    result_list.append([self.set_child_value(node.node_value, node.node_value[i], deduction),
                                        True if temp_value == deduction else False])
                    # print(result_list[len(result_list)-1])
                temp_value -= 1
                deduction += 1
        return self.check_duplicate(result_list)

    def check_duplicate(self, list_):
        temp_list1 = []  # Ex: [[7, 1, 1], ...]
        temp_list2 = []  # Ex: [True, ...]
        for i in range(len(list_)):
            if list_[i][0] not in temp_list1:
                temp_list1.append(list_[i][0])
                temp_list2.append(list_[i][1])
        list_.clear()
        for i in range(len(temp_list1)):
            list_.append([temp_list1[i], temp_list2[i]])
        return list_

    def set_child_value(self, list_, current_value, deduction):
        result_list = []
        for value in list_:
            if value == current_value:
                result_list.append(current_value - deduction)
                result_list.append(deduction)
                current_value += 1
            else:
                result_list.append(value)
        # result_list.sort(reverse=True)
        return result_list

    def set_evaluator_value(self):
        current_state = self.get_tree_height()
        current_player = self.first_player
        while current_state >= 0:
            for node in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                node.evaluator_value = 1 if (current_player and not node.is_final) else -1
            current_player = not current_player
            current_state -= 1

    def count_siblings(self, current_state):
        return len(findall(self.tree[0], filter_=lambda n: n.depth == current_state))

    def get_tree(self):
        return RenderTree(self.tree[0]).by_attr(lambda n: "-".join(map(str, n.node_value), ))
        # return RenderTree(self.tree[0])

    def get_tree_height(self):
        return self.tree[0].height
