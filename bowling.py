import random

class Frame:
    def __init__(self): #probably neet to add a class attribute tracking if it's the 10th frame
        self._rolls = []
        self._pins = 10
    
    @property
    def get_rolls(self):
        return self._rolls
    
    def roll(self): #10th frame attribute would factor in here to calculate an extra roll
        roll_score = random.randint(0, 10)
        if roll_score < self._pins:
            self._rolls.append(roll_score)
            self._pins -= roll_score
        elif roll_score > self._pins:
            self._rolls.append(self._pins)
            self._pins =- self._pins
        else:
            self._rolls.append(roll_score)
        if self._rolls[0] != 10 and len(self._rolls) < 2: #or last_frame == True and len(self.rolls) < 3
            self.roll()

class Player:
    def __init__(self) -> None:
       self._frames = [Frame() for x in range(0, 10)]
       self._score = 0

    def calculate_score(self):
        i = 0
        frame_score = 0
        for frame in self._frames:
            for roll in frame._rolls:
                if roll == 10:
                    try:
                        frame_score = 10 + sum(self._frames[i + 1]._rolls) #try except for index errors here when we have a strike but no next frame
                    except IndexError:
                        frame_score = 10
                    break
                else:
                    frame_score += roll
            i += 1
            self._score += frame_score
        return self._score
    
    @property
    def get_frames(self):
        for frame in self._frames:
            print(f"{frame.get_rolls}")
            
class Game:
    def __init__(self) -> None:
        self.players = []

    def play(self, bowl_to):
        for frame in range(0, bowl_to):
            for player in self.players:
                player._frames[frame].roll()
        return f"{self.players[0]} bowled a {self.players[0].calculate_score()}\n{self.players[1]} bowled a {self.players[1].calculate_score()}"

player1 = Player()
player2 = Player()

game = Game()

game.players.append(player1)
game.players.append(player2)

print(game.play(10))

print(player1.get_frames)