#!/usr/bin/env python3

from person import Person
from dog import Dog


class DogOwner(Person):
    
    def __init__(self, name, email, phone, club_id):    
        self.club_id = club_id
        super().__init__(name, email, phone)
        
        self.dogs = []

    def add_dog(self, dog):   
        self.dogs.append(dog)
        
    def print_dogs(self):
        print(f'Dogs owned by {self.name}:')
        
        for dog in self.dogs:
            print(dog)

    def avg_score(self):
        return sum(dog.avg_score() for dog in self.dogs) / len(self.dogs) if self.dogs else 0.0
    
    def __repr__(self):
        return f'DogOwner({self.name}, {self.email}, {self.phone}, {self.club_id})'
    
    def __str__(self):
        return f'{self.name} is a dog owner with club ID {self.club_id}.'
    
    
if __name__ == '__main__':
    owner = DogOwner('Alice', 'alice@email.com', '555-1234', '1234')

    dog1 = Dog('Fido', 'Labrador')
    dog1.add_score(90)
    dog1.add_score(85)
    owner.add_dog(dog1)

    owner.print_dogs()

