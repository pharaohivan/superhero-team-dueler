import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)

if __name__ == "__main__":

    ability = Ability("freeze", 10)
    print(ability.name)
    print(ability.attack())
