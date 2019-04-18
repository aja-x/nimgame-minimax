from anytree import Node, RenderTree, findall


class Tree(object):
    def __init__(self, root_value, first_player):
        self.root_value = root_value
        self.first_player = first_player  # first_player: True = Human, False = Computer
        # Tree disimpan dalam list bertipe Node,
        # Tiap list punya 2 property:
        # is_final buat menandai node itu terakhir, udah gak bisa dipecah lagi, lawan milih node final, auto kalah
        # evaluator_value buat memberi nilai evaluator tiap node
        # node root / utama ada di self.tree[0]
        self.tree = [Node(0, node_value=[self.root_value], is_final=False, evaluator_value=None)]
        self.render_tree()

    # Fungsi induk untuk membuat tree
    def render_tree(self):
        current_state = 0
        check_state = True
        while check_state:
            count_final = 0
            # looping node di state yang sama
            # findall doc: https://anytree.readthedocs.io/en/2.6.0/api/anytree.search.html
            for i in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                if not i.is_final:
                    for j in self.count_child(i):
                        # buat node baru
                        self.tree.append(Node(len(self.tree), parent=self.tree[i.name],
                                              node_value=j[0], is_final=j[1], evaluator_value=None))
                else:
                    count_final += 1
                if count_final == self.count_siblings(current_state):
                    check_state = False
            current_state += 1
        self.set_evaluator_value()

    # Fungsi untuk menghitung ada berapa kemungkinan child di setiap nodenya, sekaligus menghitung node_value nya
    # return list 3 dimensi. Ex: [[[7, 1, 1], True], [[6, 2, 1], False]].
    # [7, 1, 1] untuk node_value, True/False untuk is_final
    # banyaknya child node dihitung dari banyaknya list dimensi pertama
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

    # Fungsi untuk menghitung node_value
    # return list 1 dimensi. Ex: [7, 1, 1]
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

    # Fungsi untuk memberi nilai evaluator pada tree yang sudah dibuat
    def set_evaluator_value(self):
        # current state dimulai dari node terbawah / yang height nya paling rendah
        current_state = self.get_tree_height()
        current_player = self.first_player
        while current_state >= 0:
            # looping node di state yang sama
            for i in findall(self.tree[0], filter_=lambda n: n.depth == current_state):
                i.evaluator_value = 1 if current_player else -1
            current_player = not current_player
            current_state -= 1

    # menghitung banyaknya node di state yang sama
    # findall doc: https://anytree.readthedocs.io/en/2.6.0/api/anytree.search.html
    def count_siblings(self, current_state):
        return len(findall(self.tree[0], filter_=lambda n: n.depth == current_state))

    # melihat tampilan tree
    # doc: https://anytree.readthedocs.io/en/latest/api/anytree.render.html
    def get_tree(self):
        # return RenderTree(self.tree[0]).by_attr(lambda n: "-".join(map(str, n.node_value)))
        return RenderTree(self.tree[0])

    # melihat ketinggian tree
    # doc: https://anytree.readthedocs.io/en/2.6.0/api/anytree.node.html
    def get_tree_height(self):
        return self.tree[0].height


# Contoh implementasi, ini ada di luar class
number_of_sticks = 9
is_play_first = True  # Play first, True: Human, False: Computer
tree = Tree(number_of_sticks, is_play_first)
print(tree.get_tree())
print(tree.get_tree_height())
