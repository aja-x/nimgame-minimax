from Tree import Tree


class Game:
    def __init__(self):
        self.number_of_sticks = None
        self.is_play_first = None
        self.tree = None
        self.current_player = None
        self.play()

    def play(self):
        self.show_title()
        self.show_insert_number_of_stick()
        self.show_turn_choice()
        self.creating_tree()
        current_node = self.tree.tree[0]
        while not current_node.is_leaf:
            if not self.available_moving_point(current_node):
                break
            if self.current_player:
                current_node = self.get_human_moving_choice(current_node)
            else:
                current_node = self.get_comp_moving_choice(current_node)
            self.current_player = not self.current_player
            print("---------------------------------------------------\n\n")
        print("\n---------------------------------------------------\n\n")
        self.show_winner()
        self.show_rendered_tree()

    def available_moving_point(self, current_node):
        print("---------------------------------------------------")
        print(("\t\t(^_^)/ YOUR" if self.current_player else "\t     ['-']/ COMPUTER'S") + " TURN")
        print("---------------------------------------------------")
        print("Available Moving Point")
        count_child = 0
        for child in current_node.children:
            if child.is_leaf:
                print("\nThere are no available moving point T____T", end="")
                return False
            else:
                print(str(count_child + 1) + ". [" + ("-".join(map(str, child.node_value)))+"]")
            count_child += 1
        print("")
        return True

    def get_comp_moving_choice(self, current_node):
        choice_child = self.check_comp_moving_choice(current_node)
        current_child = 0
        for child in current_node.children:
            if current_child == choice_child:
                print("Computer move\t: [" + ("-".join(map(str, child.node_value)))+"]")
                return child
            current_child += 1
        print("---------------------------------------------------")

    def check_comp_moving_choice(self, current_node):
        child_choice = 0
        for child in current_node.children:
            if child.evaluator_value == 1:
                return child_choice
            child_choice += 1
        return child_choice / child_choice - 1

    def get_human_moving_choice(self, current_node):
        while True:
            count_child = 0
            moving_choice = int(input("Choose your move\t: "))
            for child in current_node.children:
                if moving_choice - 1 == count_child:
                    print("Your move\t\t: [" + ("-".join(map(str, child.node_value))) + "]")
                    return child
                count_child += 1
            print("Invalid move\n")

    def show_title(self):
        print("\t -------------------------------")
        print("\t|                               |")
        print("\t|           NIM GAME            |")
        print("\t|    Develop using python 3     |")
        print("\t|                               |")
        print("\t -------------------------------\n\n")

    def show_insert_number_of_stick(self):
        print("---------------------------------------------------")
        while True:
            self.number_of_sticks = int(input("Insert number of sticks\t: "))
            if self.number_of_sticks % 2 != 0 and self.number_of_sticks != 1:
                break
            print("Must be odd and not 1.\n")
        print("---------------------------------------------------\n\n")

    def show_turn_choice(self):
        print("---------------------------------------------------")
        print("\t\t  FIRST PLAYER")
        print("---------------------------------------------------")
        self.is_play_first = int(input("1. You\n2. Computer\n\nInsert your choice\t: "))
        self.is_play_first = True if self.is_play_first == 1 else False
        print("---------------------------------------------------\n\n")

    def creating_tree(self):
        print("---------------------------------------------------")
        print("Creating tree....")
        self.tree = Tree(self.number_of_sticks, self.is_play_first)
        print("Tree created.")
        self.current_player = self.tree.first_player
        print("---------------------------------------------------\n\n")

    def show_rendered_tree(self):
        print("---------------------------------------------------")
        is_show_tree = input("View rendered tree [y/n]? ")
        print("---------------------------------------------------")
        if is_show_tree == "y" or is_show_tree == "Y":
            print(self.tree.get_tree())
        print("---------------------------------------------------\n\n")

    def show_winner(self):
        print("---------------------------------------------------")
        print(("\t    Y O U   " if not self.current_player else "\tC O M P U T E R   ") + "W I N !")
        self.current_player = not self.current_player
        print(("\t    Y O U   " if not self.current_player else "\tC O M P U T E R   ") + "L O S E !")
        print("---------------------------------------------------\n\n")


Game()
