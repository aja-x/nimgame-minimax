from Tree import Tree


class Game2(Tree):
    def __init__(self):
        self.number_of_sticks = None
        self.is_play_first = None
        self.menu()
        super().__init__(self.number_of_sticks, self.is_play_first)


    def __run(self):
        self.menu()

    def

    def menu(self):
        self.number_of_sticks = input("Insert number of sticks: ")
        self.is_play_first = input("\nSelect Turn\n1. You play first\n2. Computer play first\nInsert your choice: ")
