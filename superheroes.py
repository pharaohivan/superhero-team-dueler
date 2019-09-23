import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = 100

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        damage = 0

        for ability in self.abilities:
            damage = ability.attack() + damage
        return damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage):
        total_block = 0
        for i in self.armors:
            total_block += i.block()
        return total_block

    def take_damage(self, damage):
        self.current_health -= (damage - self.defend(damage))















if __name__ == "__main__":


    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
