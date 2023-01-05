import random


class ProduceRanNum:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def ran_num(self):
        return random.randrange(self.start, self.end+1)

        #print(random.randrange(self.start, self.end+1))

