from anytree import Node, RenderTree, findall


def count_child(node):
    for k in node.node_value[1]:
        print(k)


def count_child2(node):
    deduction = 1
    value = []
    for i in node.node_value[1]:
        while i > deduction:
            value.append(i - 1)
            deduction += 1
            i -= 1
        deduction = 1
    value.sort(reverse=True)
    print(value)


root_value = 9
current_state = 0
tree = [Node(current_state, node_value=[0, [root_value]])]
current_state += 1
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[1, [8, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[1, [7, 2]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[1, [6, 3]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[1, [5, 4]]))

current_state += 1
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[0, [7, 1, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[0, [6, 2, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[0, [5, 3, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[0, [4, 4, 1]]))

# print(RenderTree(tree[0]).by_attr())
# print(RenderTree(tree[0]).by_attr(lambda n: n.name if n.depth == 1 else None))
# print(RenderTree(tree[0]).by_attr(lambda n: n.depth == 1))

tree.append(Node(len(tree), parent=tree[current_state], node_value=[2, [6, 3]]))

for i in findall(tree[0], filter_=lambda n: n.depth == 2):
    print(i.name)
    print(i.node_value[1])
    count_child2(i)
    # for j in i.node_value[1]:
    #     print(j)
    # print("\n")
