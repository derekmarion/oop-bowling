class Frame:
    def __init__(self, frame_score=0, strike=False):
        self._frame_score = frame_score
        self._strike = strike

    @property
    def get_frame_score(self):
        return self._frame_score
    
    @get_frame_score.setter
    def set_frame_score(self, score):
        self._frame_score = score
    
    @property
    def get_strike(self):
        return self._strike
    
    @get_strike.setter
    def set_strike(self, strike: bool):
        self._strike = strike

class Game:


