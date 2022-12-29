# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# PART 1


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        if speed < 0 or speed > 1:
            return 'ValueError'
        if endurance < 0 or endurance > 1:
            return 'ValueError'
        if accuracy < 0 or accuracy > 1:
            return 'ValueError'
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def __str__(self):
        return f"Hello everyone, my name is {self.name}."

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        skills = {
            'speed': self.speed,
            'endurance': self.endurance,
            'accuracy': self.accuracy
        }
        return (max(skills), skills[max(skills)])


alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)

print(alice)
print(bob)
print(alice.strength())
# PART 2

'''
class Commentator(Player):
    def __init__(self, name):
        self.name = name

    def sum_player(Player):

        return Player.speed + Player.endurance + Player.accuracy

    def compare_players(player_1, player_2, )


ray = Commentator('Ray Hudson')
print(ray.name)
'''
