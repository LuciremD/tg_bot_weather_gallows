import helpfull_stuff
import random


class Game():
    def __init__(self):
        self.at = ""
        self.amount_letters = ""

    def create(self):
        self.word = random.choice(helpfull_stuff.words)
        print(self.word, self.amount_letters)
        self.pat = ["*" for _ in range(len(self.word))]
        self.already_open = []
        self.exist = list(set(self.word))
        self.number_letters = 0
        self.shoud_be_open = []
        while len(self.shoud_be_open) != self.amount_letters:
            let = random.choice(self.exist)
            if let not in self.shoud_be_open:
                self.shoud_be_open.append(let)
                self.already_open.append(let)
        for i in self.shoud_be_open:
            for j in range(len(self.word)):
                if i == self.word[j]:
                    self.pat[j] = i
                    self.number_letters += 1

    def out(self):
        separator = ""
        result_string = separator.join(self.pat)
        return result_string
