class Main:
    def main():
        print('Masukkan total stik\t: ')
        stick = input()

        print('\tMAIN\n1. Pertama\n2. Kedua\nMasukkan pilihan anda\t: ')
        choice = input()

        state = State(stick)
        tree = Tree(state)
        tree.build()

        game = Game(state, choice)
        game.start()