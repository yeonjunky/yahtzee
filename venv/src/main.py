import random
import sys


def quit_game():
    sys.exit()


def remove_same_element(dict_val):
    return_list = []
    for i in range(0, len(list(dict_val))):
        if list(dict_val)[i] not in return_list:
            return_list.append(list(dict_val)[i])
    return return_list


class Yahtzee:

    def __init__(self):
        self.nums = [0, 0, 0, 0, 0]
        self.score = 0
        self.sum = 0
        self.nums_count = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }
        self.upper_section = [0, 0, 0, 0, 0, 0]
        self.upper_score = 0
        self.lower_section = [0, 0, 0, 0, 0, 0, 0]
        self.lower_section_score = [0, 0, 0, 0, 0, 0, 0]
        self.roll_count = 0
        self.round_count = 0
        self.is_start = True
        self.player_command = ''
        self.commands = ['1', '2', '3', '4', '5', '6', 'three', 'four', 'full', 'small', 'large', 'chance', 'yahtzee',
                         'reroll', 'exit']

    def roll(self):
        for i in range(0, 5):
            self.nums[i] = random.randint(1, 6)

    def init_sum(self):
        self.sum = 0

    def init_count(self):
        self.nums_count = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }

    def dice_sum(self):
        self.init_sum()
        for i in self.nums:
            self.sum += i

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

    def check_lower_section(self):
        if 3 in self.nums_count:
            self.lower_section_score[0] = 25
            pass

    def print_dices(self):
        print("dice:", self.nums, '\n')

    def show_upper_section(self):
        print("-------------upper section-------------\n")
        for i in range(1, 7):
            print(f"{i} score:", self.nums_count[str(i)] * i)

    def show_lower_section(self):
        print("-------------lower section-------------\n")
        print("Three of a kind:", self.lower_section_score[0], '\n' +
              "Four of a kind:", self.lower_section_score[1], '\n' +
              "Full house:", self.lower_section_score[2], '\n' +
              "Small straight:", self.lower_section_score[3], '\n' +
              "Large straight:", self.lower_section_score[4], '\n' +
              "Chance:", self.lower_section_score[5], '\n' +
              "Yahtzee:", self.lower_section_score[6], '\n'
              )

    def show_score(self):
        print("current score: ", self.score)

    def get_player_command(self):
        self.player_command = input("")

    def get_score(self):
        if self.player_command in self.commands:
            if self.player_command == '1':
                if self.upper_section[0]:
                    print("already got ace score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["1"]
                    self.upper_score += self.nums_count["1"]
                    self.upper_section[0] = 1

            elif self.player_command == '2':
                if self.upper_section[1]:
                    print("already got twos score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["2"] * 2
                    self.upper_score += self.nums_count["2"] * 2
                    self.upper_section[1] = 1

            elif self.player_command == '3':
                if self.upper_section[2]:
                    print("already got threes score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["3"] * 3
                    self.upper_score += self.nums_count["3"] * 3
                    self.upper_section[2] = 1

            elif self.player_command == '4':
                if self.upper_section[3]:
                    print("already got fours score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["4"] * 4
                    self.upper_score += self.nums_count["4"] * 4
                    self.upper_section[3] = 1

            elif self.player_command == '5':
                if self.upper_section[4]:
                    print("already got fives score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["5"] * 5
                    self.upper_score += self.nums_count["5"] * 5
                    self.upper_section[4] = 1

            elif self.player_command == '6':
                if self.upper_section[5]:
                    print("already get sixes score")
                    self.show_dice()
                else:
                    self.score += self.nums_count["6"] * 6
                    self.upper_score += self.nums_count["6"] * 6
                    self.upper_section[5] = 1

            elif self.player_command == 'three':
                if self.lower_section[0]:
                    print("already get three of a kind score")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[0]
                    self.lower_section[0] = 1

            elif self.player_command == 'four':
                if self.lower_section[1]:
                    print("already get four of a kind")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[1]
                    self.lower_section[1] = 1

            elif self.player_command == 'full':
                if self.lower_section[2]:
                    print("already get four of a kind")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[2]
                    self.lower_section[2] = 1

            elif self.player_command == 'small':
                if self.lower_section[3]:
                    print("already get small straight score")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[3]
                    self.lower_section[3] = 1

            elif self.player_command == 'large':
                if self.lower_section[4]:
                    print("already get large straight score")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[4]
                    self.lower_section[4] = 1

            elif self.player_command == 'chance':
                if self.lower_section[5]:
                    print("already get chance score")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[5]
                    self.lower_section[5] = 1

            elif self.player_command == 'yahtzee':
                if self.lower_section[6]:
                    print("already get yahtzee score")
                    self.show_dice()
                else:
                    self.score += self.lower_section_score[6]
                    self.lower_section[6] = 1

            elif self.player_command == 'reroll':
                self.reroll()

            elif self.player_command == 'exit':
                quit_game()

        else:
            print('wrong command! type again')
            self.show_dice()

    def check_bonus_score(self):
        if self.upper_score > 63:
            print("bonus score!")
            self.score += 35
        else:
            pass

    def check_lower_score(self):
        if 3 in self.nums_count.values():
            self.lower_section_score[0] = self.sum

        if 4 in self.nums_count.values():
            self.lower_section_score[1] = self.sum

        if 2 in self.nums_count.values() and 3 in self.nums_count.values():
            self.lower_section_score[2] = 25

        if len(remove_same_element(self.nums_count.values())) == 4 or len(remove_same_element(self.nums_count.values())) == 5:
            self.lower_section_score[3] = 30

        if len(remove_same_element(self.nums_count.values())) == 5:
            self.lower_section_score[4] = 40

        self.lower_section_score[5] = self.sum

        if 5 in self.nums_count.values():
            self.lower_section_score[6] = 50

    def reroll(self):
        if self.roll_count < 2:
            self.roll_count += 1
            self.init_count()
            self.roll()

            self.print_dices()
            self.check_same_num()
            self.show_upper_section()
            self.get_player_command()
            self.get_score()
        else:
            print("already rolled three times")
            self.get_player_command()
            self.get_score()

    def new_turn(self):
        self.roll_count = 0
        self.round_count += 1

        print("Round:", self.round_count)
        self.check_bonus_score()
        self.init_count()
        self.roll()
        self.dice_sum()
        print('sum:', self.sum)
        self.print_dices()
        self.check_same_num()
        self.check_lower_score()
        self.show_upper_section()
        self.show_lower_section()
        self.get_player_command()
        self.get_score()
        self.show_score()

    def show_dice(self):
        self.print_dices()
        self.show_upper_section()
        self.show_lower_section()
        self.get_player_command()
        self.get_score()
        self.show_score()


ya = Yahtzee()
while True:
    if ya.round_count == 13:
        print("game end")
        break
    ya.new_turn()
