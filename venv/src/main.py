import random


class Yahtzee:

    def __init__(self):
        self.nums = [0, 0, 0, 0, 0]
        self.score = 0
        self.nums_count = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }
        self.is_start = False
        self.player_command = ''

    def roll(self):
        for i in range(0, 5):
            self.nums[i] = random.randint(1, 6)

    def check_same_num(self):
        for i in self.nums:
            if i == 1:
                self.nums_count['1'] += 1
            elif i == 2:
                self.nums_count['2'] += 1
            elif i == 3:
                self.nums_count['3'] += 1
            elif i == 4:
                self.nums_count['4'] += 1
            elif i == 5:
                self.nums_count['5'] += 1
            elif i == 6:
                self.nums_count['6'] += 1

    def print_dices(self):
        print("dice:", self.nums, '\n')

    def show_upper_section(self):
        print("-------------upper section-------------\n")
        for i in range(1, 7):
            print(f"{i} score:", self.nums_count[str(i)] * i)

    def start_game(self):
        self.is_start = True
        while self.is_start:
            self.start_turn()
            self.player_command = input("")

    def start_turn(self):
        self.roll()
        self.print_dices()
        self.check_same_num()
        self.show_upper_section()


ya = Yahtzee()
ya.start_turn()
print(ya.nums_count)
