import random
from random import choice

def divide():
    print("----------------------------------------")


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
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):

        """Adds abilities to abilities list in the hero class"""

        self.abilities.append(ability)

    def attack(self):
        """adds up damage from abilites list"""

        damage = 0

        for ability in self.abilities:
            damage += ability.attack()

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
            self.add_deaths(1)
            opponent.add_kill(1)

        elif opponent.is_alive() == False:
            print(f'{self.name} won')
            self.add_kill(1)
            opponent.add_deaths(1)

        elif self.is_alive() == False and opponent_attack == False:
            print('Draw')



    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        findhero = False
        for hero in self.heroes:
            if name == hero.name:
                findhero = True
                self.heroes.remove(hero)

        if findhero == False:
            return 0

    def view_all_heroes(self):
        all_heroes = []
        for hero in self.heroes:
            all_heroes.append(hero.name)
        print(all_heroes)
        return all_heroes

    def attack(self, other_team):
        fighting = True
        team_one = []
        team_two = []

        while fighting:
            team_one.clear()
            team_two.clear()
            for hero in self.heroes:
                if hero.is_alive():
                    team_one.append(hero)
            for hero in other_team.heroes:
                if hero.is_alive():
                    team_two.append(hero)
            if len(team_one) <= 0 or len(team_two) <= 0:
                fighting = False
            else:
                hero_one = choice(team_one)
                hero_two = choice(team_two)
                hero_one.fight(hero_two)

    def stats(self):
        print("Statistics: ")
        ratios = list()
        for hero in self.heroes:
            if not hero.deaths == 0:
                ratio = hero.kills/hero.deaths
                ratios.append(ratio)
                print(f"{hero.name}: {ratio}")
        else:
            print(f"{hero.name}: No deaths")

        sum = 0
        for ratio in ratios:
            sum += ratio
        if not len(ratios) == 0:
            avg = sum/len(ratios)
            print(f"Avg. kill/death ratio: {avg}")
        else:
            print("Avg. kill/death ratio: N/A")

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter name of hero's ability")
        strength = int(input("Enter the attack strength: "))
        return Ability(name, strength)

    def create_weapon(self):
        name = input("Enter name of hero's weapon: ")
        strength = input("Enter weapon strength: ")
        return Weapon(name, int(strength))

    def create_armor(self):
        name = input("Enter the name of your new armor: ")
        block = int(input("Enter armor blocking power: "))
        return Armor(name, block)

    def prompt(self, hero, attribute):
        choice = ""
        while not (choice == "N" or choice == "n"):
            choice = input(f"Do you want to add a new {attribute} (Y/N)?")
            if (choice == "Y" or choice == "y") and attribute == "ability":
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif (choice == "Y" or choice == "y") and attribute == "weapon":
                new_weapon = self.create_weapon()
                hero.add_ability(new_weapon)
            elif (choice == "Y" or choice == "y") and attribute == "armor":
                new_armor = self.create_armor()
                hero.add_armor(new_armor)

    def create_hero(self):
        name = input("Enter a name for your new hero: ")
        new_hero = Hero(name)

        self.prompt(new_hero, "ability")
        self.prompt(new_hero, "weapon")
        self.prompt(new_hero, "armor")

        return new_hero

    def build_team_one(self):
        team_one_name = input("Enter Team One name: ")
        self.team_one = Team(team_one_name)
        team_size = input("Enter size of Team One: ")

        heroes_added = 0
        while heroes_added < int(team_size):
            new_team_player = self.create_hero()
            self.team_one.add_hero(new_team_player)
            heroes_added += 1

    def build_team_two(self):
        team_two_name = input("Enter Team Two name: ")
        self.team_two = Team(team_two_name)
        team_size = input("Enter size of Team Two: ")

        heroes_added = 0
        while heroes_added < int(team_size):
            new_team_player = self.create_hero()
            self.team_two.add_hero(new_team_player)
            heroes_added += 1

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        alive_team_one_heroes_names = list()
        alive_team_two_heroes_names = list()

        alive_team_one_heroes = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                alive_team_one_heroes += 1
                alive_team_one_heroes_names.append(hero.name)

        alive_team_two_heroes = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                alive_team_two_heroes += 1
                alive_team_two_heroes_names.append(hero.name)

        if alive_team_one_heroes > alive_team_two_heroes:
            print("Team One wins!")
            divide()
        elif alive_team_two_heroes > alive_team_one_heroes:
            divide()
            print("Team Two wins!")
            divide()

        else:
            print("Draw!")
            divide()

        print("Team One Stats:")
        self.team_one.stats()
        print("Surviving Heroes from Team One:")
        for name in alive_team_one_heroes_names:
            print(name)
        divide()

        print("Team Two Stats: ")
        self.team_two.stats()
        print("Surviving Heroes from Team Two")
        divide()
        for name in alive_team_two_heroes_names:
            print(name)





if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.

    # hero1 = Hero("Wonder Woman", 1000)
    # hero2 = Hero("Dumbledore", 1000)
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    # team = Team('TEam')
    # team.add_hero(hero1)
    # team.add_hero(hero2)
    # team.view_all_heroes()
    # test = []
    # test.append(hero1.name)
    # test.append(hero2.name)
    # print(test)

    if __name__ == "__main__":
        arena = Arena()
        arena.build_team_one()
        arena.build_team_two()
        arena.team_battle()
        arena.show_stats()
