from anytree import Node, RenderTree, findall


def set_child(node, k, j):
    value = []
    for i in node:
        if i == k:
            value.append(k-j)
            value.append(j)
        else:
            value.append(i)
    value.sort(reverse=True)
    return value


def count_child(node):
    value = []
    for k in node.node_value[0]:
        j = 0
        temp = k
        while temp - 1 >= j + 1:
            value.append(set_child(node.node_value[0], k, j + 1))
            temp -= 1
            j += 1
    print(value)


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


def count_child3(node):
    value = []
    for j in node.node_value[0]:
        # deduction = 1
        # node.node_value[1].pop(j)
        # print(node.node_value[1])
        # print("hubla\n")
        temp = node.node_value[0]
        for k in temp:
            deduction = 1
            l = k
            while (l > deduction + 1) and (l != 1):
                value.append(node.node_value[0])
                value[len(value) - 1].remove(l)
                for h in value[len(value)-1]:
                    print(str(k)+str(h))
                    break
                # print("+"+str(l)+"+"+str(k)+"\n")
                # value[len(value) - 1].remove(k)
                # value[len(value) - 1].append(l-1)
                # value[len(value) - 1].append(deduction)
                deduction += 1
                l -= 1

        # while j > deduction:
        #     value.append(node.node_value[0])
        #     value[deduction - 1].remove(j)
        #     value[deduction - 1].append(j - 1)
        #     value[deduction - 1].append(deduction)
        #     value[deduction - 1].sort(reverse=True)
        #     deduction += 1
        #     j -= 1
    print(value)


def set_child_value(node_value):
    pass


root_value = 9
current_state = 0
tree = [Node(current_state, node_value=[[root_value]])]
current_state += 1
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[8, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[7, 2]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[6, 3]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[5, 4]]))

current_state += 1
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[7, 1, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[6, 2, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[5, 3, 1]]))
tree.append(Node(len(tree), parent=tree[current_state - 1], node_value=[[4, 4, 1]]))

# print(RenderTree(tree[0]).by_attr())
# print(RenderTree(tree[0]).by_attr(lambda n: n.name if n.depth == 1 else None))
# print(RenderTree(tree[0]).by_attr(lambda n: n.depth == 1))

tree.append(Node(len(tree), parent=tree[current_state], node_value=[[6, 3]]))

for i in findall(tree[0], filter_=lambda n: n.depth == 1):
    # print(i)
    # print(i.name)
    print(i.node_value[0])
    count_child(i)
    print("\n")
    # for j in i.node_value[1]:
    #     print(j)
    # print("\n")
