#!/usr/bin/env python3

class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def update_email(self, new_email):
        self.email = new_email

    def update_phone(self, new_phone):
        self.phone = new_phone
        
    def __repr__(self):
        return f'Person({self.name}, {self.email}, {self.phone})'

    def __str__(self):
        return f'{self.name} can be reached at {self.email} or {self.phone}.'
