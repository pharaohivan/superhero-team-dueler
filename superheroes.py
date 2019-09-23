import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = 100

    def add_ability(self, ability):

        """Adds abilities to abilities list in the hero class"""

        self.abilities.append(ability)

    def attack(self):
        """adds up damage from abilites list"""

        damage = 0

        for ability in self.abilities:
            damage = ability.attack() + damage
        return damage

    def add_armor(self, armor):

        """Adds armor to armor list in the hero class"""

        self.armors.append(armor)

    def defend(self, damage):

        """runs block function on each armor item and returns as total block"""

        total_block = 0
        for i in self.armors:
            total_block += i.block()
        return total_block

    def take_damage(self, damage):

        """ Updates self.current_health to reflect the damage minus the defense."""

        self.current_health -= (damage - self.defend(damage))

    def is_alive(self):
        """Returns True or False depending on whether the hero is alive or not."""

        if self.current_health > 0:
            return True
        else:
            return False


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
      '''
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Returns a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)






if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
