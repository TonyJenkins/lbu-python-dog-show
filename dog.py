#!/usr/bin/env python3

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def avg_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

    def reset_scores(self):
        self.scores = []

    @staticmethod
    def bark():
        return 'Woof!'

    def __lt__(self, other):
        return self.avg_score() < other.avg_score()

    def __eq__(self, other):
        return self.avg_score() == other.avg_score()

    def __repr__(self):
        return f'Dog({self.name}, {self.breed})'

    def __str__(self):
        return f'{self.name} is a {self.breed} with an average score of {self.avg_score():.2f}.'


if __name__ == '__main__':
    d1 = Dog('Fido', 'Labrador')
    d1.add_score(90)
    d1.add_score(85)
    d1.add_score(88)
    print(d1)
    print(d1.bark())

    d2 = Dog('Spot', 'Dalmatian')
    d2.add_score(90)
    d2.add_score(75)
    d2.add_score(80)
    print(d2)

    print(d1 < d2)
    print(d1 == d2)
    print(d1 > d2)
