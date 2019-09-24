import random
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
      '''
        return random.randint(0, self.max_damage)

class Weapon(Ability):

    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Returns a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):

        """Adds abilities to abilities list in the hero class"""

        self.abilities.append(ability)

    def attack(self):
        """adds up damage from abilites list"""

        damage = 0

        for ability in self.abilities:
            return ability.attack()

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

        self.current_health -= damage

    def is_alive(self):
        """Returns True or False depending on whether the hero is alive or not."""

        if self.current_health > 0:
            # print("dead")
            return True
        else:
            # print("alive")
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
        if self.is_alive() == False:
            print(f'{opponent.name} won')
        elif opponent.is_alive() == False:
            print(f'{self.name} won')
        elif self.is_alive() == False and opponent_attack == False:
            print('Draw')

class Team:

    def __init__(self, team_name):
        self.teamname = team_name
        self.heroes = []

    def addhero(self, hero):
        self.addhero = hero

    def removehero(self, name):
        self.removehero = name

    def viewallheroes(self):






if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.

    hero1 = Hero("Wonder Woman", 1000)
    hero2 = Hero("Dumbledore", 1000)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
