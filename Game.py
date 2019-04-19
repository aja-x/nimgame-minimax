from Tree import Tree


class Game:
    def __init__(self):
        self.number_of_sticks = None
        self.is_play_first = None
        self.tree = None
        self.current_player = None
        self.play()

    def play(self):
        self.menu()
        current_node = self.tree.tree[0]
        while not current_node.is_leaf:
            if self.current_player:
                self.available_moving_point(current_node)
                current_node = self.get_human_moving_choice(current_node)
            else:
                self.available_moving_point(current_node)
                current_node = self.get_comp_moving_choice(current_node)
            self.current_player = not self.current_player
        print("\n" + ("You" if self.current_player else "Computer") + " win!")

    def available_moving_point(self, current_node):
        print("\n-->" + ("Your" if self.current_player else "Computer") + " Turn\nAvailable moving point:")
        count_child = 0
        temp = ""
        for i in current_node.children:
            if temp != ("-".join(map(str, i.node_value))):
                print(str(count_child + 1) + ". [" + ("-".join(map(str, i.node_value)))+"]")
            temp = ("-".join(map(str, i.node_value)))
            count_child += 1

    def get_comp_moving_choice(self, current_node):
        choice_child = self.check_comp_moving_choice(current_node)
        current_child = 0
        for i in current_node.children:
            if current_child == choice_child:
                print("Computer move: [" + ("-".join(map(str, i.node_value)))+"]")
                return i
            current_child += 1
        for i in current_node.children:
            print("Computer move: [" + ("-".join(map(str, i.node_value)))+"]")
            return i

    def check_comp_moving_choice(self, current_node):
        child_choice = 0
        for i in current_node.children:
            if i.evaluator_value == 1:
                return child_choice
            child_choice += 1
        return child_choice / child_choice - 1

    def get_human_moving_choice(self, current_node):
        count_child = 0
        while True:
            moving_choice = int(input("Choose your move: "))
            for i in current_node.children:
                if moving_choice - 1 == count_child:
                    return i
                count_child += 1
            print("Invalid move\n\n")

    def menu(self):
        self.number_of_sticks = int(input("Insert number of sticks: "))
        self.is_play_first = int(input("\nSelect Turn\n1. You play first\n2. Computer play first\n"
                                       "Choose your turn: "))
        self.is_play_first = True if self.is_play_first == 1 else False
        print("\nCreating tree....")
        self.tree = Tree(self.number_of_sticks, self.is_play_first)
        print("Tree created.\n")
        is_show_tree = input("View rendered tree [y/n]? ")
        if is_show_tree == "y" or is_show_tree == "Y":
            print(self.tree.get_tree())
            print("\n")
        self.current_player = self.tree.first_player


Game()
