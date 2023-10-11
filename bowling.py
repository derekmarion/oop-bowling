import random

class Frame:
    def __init__(self):
        self._rolls = []
        self._pins = 10
    
    @property
    def get_rolls(self):
        return self._rolls
    
    def roll(self):
        roll_score = random.randint(0, 10)
        if roll_score < self._pins:
            self._rolls.append(roll_score)
            self._pins -= roll_score
        elif roll_score > self._pins:
            self._rolls.append(self._pins)
            self._pins =- self._pins
        else:
            self._rolls.append(roll_score)
        if self._rolls[0] != 10 and len(self._rolls) < 2:
            self.roll()

new_frame = Frame()
new_frame.roll()
print(new_frame.get_rolls)