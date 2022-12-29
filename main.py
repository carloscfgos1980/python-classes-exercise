# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
import operator
# PART 1


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if speed >= 0 and speed <= 1:
            self.speed = speed
        else:
            raise ValueError
        if endurance >= 0 and endurance <= 1:
            self.endurance = endurance
        else:
            raise ValueError
        if accuracy >= 0 and accuracy <= 1:
            self.accuracy = accuracy
        else:
            raise ValueError

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
        skill_max = max(skills.items(), key=operator.itemgetter(1))[0]
        print(skill_max)
        return ((skill_max), skills[skill_max])


alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)

print(alice)
print(bob)
print('Alice', alice.strength())
print('Bob', bob.strength())
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
