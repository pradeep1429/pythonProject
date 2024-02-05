class sport:
    def __init__(self):
        self.wins = 0
        self.loses = 0

    def wons(self):
        self.wins += 1

    def losses(self):
        self.loses -= 1

    @property
    def scores(self):
        return self.wins - self.loses


s = sport()
s.wons()
scr = int(s.scores)
print(scr)