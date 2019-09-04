
class Walking:

    def __init__(self):
        self.walk_speed = 0
        self.legs = 0

    def run(self):
        print("The animal walks")

class Swimming:

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print("The animal swims")

class Flying:

    def __init__(self):
        self.fly_speed = 0
        self.maximum_speed = 0

    def fly(self):
        print("The animal flies")

class Digging:

    def __init__(self):
        self.dig_rate = 0
        self.maximum_dig = 0

    def dig(self):
        print("The animal digs")