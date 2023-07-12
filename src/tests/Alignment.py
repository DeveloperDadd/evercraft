# As a user I want to have an alignment so that it is an excuse for my mental health issues.
from Character import Character
# three alignments: Good, Neutral, and Evil
class Morals:
    def __init__(self):
        self.alignment = 'Good'

    def set_alignment(self, alignment):
        self.alignment = alignment