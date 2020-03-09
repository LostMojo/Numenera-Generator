"""Contains the PC class, used to make Cypher system (Numenera) player characters"""

import roll_cypher as r
import random
import copy


class CypherPC:

    _advancement_choices = ["Pool", "Edge", "Skills", "Effort"]
    _advancement_choices_taken = []
    _recovery_rolls = ["1 Action", "10 minutes", "1 hour", "10 hours"]
    _recovery_rolls_used = []

    _stat_map = {"might": 0, "speed": 1, "int": 2, "intellect": 2, '0': 0, '1': 1, '2': 2}

    _type_stat_base = [5, 5, 5]
    _assignable_points = 6
    _assigned_points = [0, 0, 0]
    _other_pool_bonuses = [0, 0, 0]
    _assignable_edge_points = 0

    _weapons = []

    _cypher_limit = 1
    _cyphers = {}
    _artifacts = {}
    _items = dict()

    _connections = []
    _core_features = {}
    _abilities = {
        '1': {},
    }

    _minor_effect_suggestions = []
    _major_effect_suggestions = []
    _intrusion_options = {}

    _link_to_starting_adventure = []

    _damage_track = ["Hale", "Impaired", "Debilitated", "Dead"]

    def __init__(self, name, tier=1, descriptor="adjective", char_type="noun", focus="verbs", skills={},
                 max_might=10, max_speed=10, max_int=10, might_edge=0, speed_edge=0, int_edge=0, armor=0,
                 exp=0, max_effort=1, damage_track_position=0):
        """
        Initializes PC class
        Arguments:
        name: the name of the character. String
        tier: the tier ("Level") of the character. Int between 1 and 10
        descriptor: the descriptor (Adjective) of the character. String
        type: the type ("Class" or Noun) of the character. String
        focus: the focus (or verb) of a character. String
        skills: A dictionary of Skills and amount that a task is eased (positive) or hindered (negative) by. Int
        max_might: Might Pool Maximum. Int
        max_speed: Speed Pool Maximum. Int
        max_int: Intellect Pool Maximum. Int
        might_edge: Might Edge. Int
        speed_edge: Speed Edge. Int
        int_edge: Intellect Edge. Int
        armor: Armor value
        exp: Exp. Int, maximum 10
        """

        if isinstance(name, str):       # ensure name is a string
            self._name = name
        else:
            raise ValueError("PC name must be a string")

        if tier in range(1, 10):        # ensure tier  is an int between 1 and 10
            self._tier = tier
        else:
            raise ValueError("PC level must be an int between 1 and 10")

        for key in skills:          # ensures skills are within -2 to 3
            if not skills[key] in range(-2,3):       # Check if skill is an int between -2 and 3
                raise ValueError("PC Skill Error: Skills must have a int level between -2 and 3")

        self._skills = skills

        if isinstance(descriptor, str):     # ensure descriptor is string
            self._descriptor = descriptor
        else: raise ValueError("PC descriptor must be a string")

        if isinstance(char_type, str):       # ensure char_type is string
            self._type = char_type
        else: raise ValueError("PC Type must be a string")

        if isinstance(focus, str):      # ensure focus is string
            self._focus = focus
        else: raise ValueError("PC focus must be string")

        if max_might not in range (1, 100):      # ensure max might is positive int
            raise ValueError("PC max might must be positive integer")

        if max_speed not in range(1, 100):  # ensure max speed is positive int
            raise ValueError("PC max speed must be positive integer")

        if max_int not in range(1, 100):      # ensure max intellect is positive int
            raise ValueError("PC max intellect must be positive integer")

        # a list of max pools
        self._max_pools = [max_might, max_speed, max_int]

        # A list of current stat pools, going Might, Speed, Intelligence
        self._current_pools = [max_might, max_speed, max_int]

        if might_edge not in range(-3, 20):      # ensure might edge is an int between -3 and 20
            raise ValueError("PC might edge must be an int between -3 and 20")

        if speed_edge not in range(-3, 20):  # ensure edge is an int between -3 and 20
            raise ValueError("PC speed edge must be an int between -3 and 20")

        if int_edge not in range(-3, 20):  # ensure edge is an int between -3 and 20
            raise ValueError("PC int edge must be an int between -3 and 20")

        self._edge_list = [might_edge, speed_edge, int_edge]

        if armor in range(0, 30):        # ensure armor is within 0 and 30
            self._armor = armor
        else: raise ValueError("PC armor must be an int between 0 and 30")

        if exp in range(0, 10):      # ensure exp is an int between 0 and 10
            self._exp = exp
        else: raise ValueError("PC exp must be an int between 0 and 10")

        self._max_effort = max_effort
        self._damage_track_position = damage_track_position

        self._configure_character()

    def name(self): return self._name
    def tier(self): return self._tier
    def descriptor(self): return self._descriptor
    def type(self): return self._type
    def focus(self): return self._focus
    def skills(self): return self._skills
    def max_pools(self): return self._max_pools
    def max_might(self): return self.max_pools()[self.which_stat("might")]
    def max_speed(self): return self.max_pools()[self.which_stat("speed")]
    def max_int(self): return self.max_pools()[self.which_stat("int")]
    def assignable_points(self): return self._assignable_points
    def assigned_points(self): return self._assigned_points
    def current_might(self): return self._current_pools[self.which_stat("might")]
    def current_speed(self): return self._current_pools[self.which_stat("speed")]
    def current_int(self): return self._current_pools[self.which_stat("int")]
    def current_pools(self): return self._current_pools
    def edge_list(self): return self._edge_list
    def might_edge(self): return self.edge_list()[self.which_stat("might")]
    def speed_edge(self): return self.edge_list()[self.which_stat("speed")]
    def int_edge(self): return self.edge_list()[self.which_stat("int")]
    def damage_track_position(self): return self._damage_track_position
    def armor(self): return self._armor
    def exp(self): return self._exp
    def abilities(self): return self._abilities
    def link_to_starting_adventure(self): return self._link_to_starting_adventure
    def connections(self): return self._connections

    def damage_status(self):
        try:
            return self._damage_track[self.damage_track_position()]
        except IndexError:
            return "Dead"

    def which_stat(self, stat):
        """A method that takes common names for might/speed/int or an index and returns the index of the right stat"""
        return self._stat_map[str(stat)]

    def _configure_character(self):
        self.heal_full()

    def describe(self):
        return ("{name} is a {adjective} {noun} who {verbs}.".format(name=self._name, adjective=self._descriptor,
                                                                     noun=self._type, verbs=self._focus))

    def assign_stat_point(self, pool):
        i = self.which_stat(pool)
        print(self.max_pools())
        self.max_pools()[i] = self.max_pools()[i]+1
        self._assigned_points[i] += 1
        self._assignable_points -= 1

    def print_pools(self):
        left = 3
        right = 3
        print("MIGHT".center(left + right + 1))
        print(str(self.current_might()).ljust(left) + '/' + str(self.max_might()).rjust(right))
        print("SPEED".center(left + right + 1))
        print(str(self.current_speed()).ljust(left) + '/' + str(self.max_speed()).rjust(right))
        print("INT".center(left + right + 1))
        print(str(self.current_int()).ljust(left) + '/' + str(self.max_int()).rjust(right))

    def rename(self, name): self._name = name
    def change_descriptor(self, descriptor): self._descriptor = descriptor
    def change_type(self, char_type): self._type = char_type
    def change_focus(self, focus): self._focus = focus

    def add_skill(self, skill="Unnamed", training=1):
        if skill in self._skills:
            self._skills[skill] += training
        else:
            self._skills[skill] = training

    def overwrite_skill(self, skill="Unnamed", training=1):
        self._skills[skill] = training

    def add_hindrance(self, skill="Unnamed", hinder_level=1):
        self.add_skill(skill, -1*hinder_level)

    def remove_skill(self, skill="Unnamed"):
        if skill in self._skills:
            del self._skills[skill]
        else:
            raise ValueError("Cannot delete skill {0} because {1} doesn't know it".format(skill, self._name))

    def print_skills(self):
        for skill in self._skills:
            print(str(skill) + ": " + str(self._skills[skill]))

    def _add_dict_inventory(self, d, item_pouch):        # item_pouch used to find which dictionary to look in
        """A method that takes a dictionary of items sorted into their categories, and adds them to their right
        "compartment", recursive, dictionaries inside dictionaries can be sorted"""
        for group in d:
            if group in item_pouch:
                if item_pouch[group] is None:
                    item_pouch[group] = d[group]
                elif isinstance(item_pouch[group], list):
                    item_pouch[group].extend(d[group])
                elif isinstance(item_pouch[group], dict):
                    self._add_dict_inventory(d[group], item_pouch[group])
                elif isinstance(item_pouch[group], int):
                    item_pouch[group] = item_pouch.setdefault(group, 0)+d[group]
            else:
                item_pouch[group] = d[group]

    def print_items(self):
        for key in self._items:
            print(str(key) + ": " + str(self._items[key]))

    def skill_check(self, difficulty, skill="", effort=0):
        if skill in self._skills:
            difficulty -= self._skills[skill]
        if difficulty-effort < 0:
            return True, -1
        else:
            r.check_roll(difficulty, effort)

    def spend_pool(self, amount, pool="int"):
        stats = self.current_pools()
        offset = self.which_stat(pool)
        edge = self.edge_list()[offset]
        stats[offset] -= (amount-edge)

    def take_damage(self, damage=1, ignore_armor=False, targeted_pool="might"):
        """
        Deals damage, starting at might, trickling down to speed and then int if the pools are empty
        Args:
        damage: how much damage dealt
        ignore_armor: whether the attack ignores armor
        targeted_pool: which pool the damage is targeting, all lowercase
        :return: True if the attack does damage, False if it does not
        """
        if not ignore_armor:
            damage -= self.armor()
            if damage <= 0:
                return False
        starting_pool = self.which_stat(targeted_pool)
        stats = self.current_pools()
        new_damage_track = 0
        for i in range(len(stats)):
            pool = (starting_pool+i)%len(stats)
            stats[pool] -= damage
            if stats[pool] >= 0:
                damage = 0
            else:
                damage = -1 * stats[pool]  # removes negative
                stats[pool] = 0
                new_damage_track += 1
        if new_damage_track > self.damage_track_position():
            self._damage_track_position = new_damage_track
        return True

    def recovery_roll(self, targeted_pool="int", beyond_max=False, addition=0, set_roll=-1):
        stats = self.current_pools()
        offset = self.which_stat(targeted_pool)
        if set_roll < 0:
            recover = random.randint(1, 6) + self._tier + addition
        else:
            recover = set_roll + self._tier + addition
        if beyond_max or (stats[offset] + recover) < self._max_might:
            stats[offset] += recover
        else:
            stats[offset] = self.max_pools()[offset]

    def heal(self, amount, targeted_pool="int", beyond_max=False):
        """
        Heals an amount to a targeted pool
        :param amount: the amount healed. Int
        :param targeted_pool: The pool targeted, all lowercase, or the index. Str or Int
        :param beyond_max: true if the healing can go beyond max pool. Bool
        :return:
        """
        stats = self.current_pools()
        offset = self.which_stat(targeted_pool)
        if beyond_max or (stats[offset] + amount) < self.max_pools()[offset]:
            stats[offset] += amount
        else:
            stats[offset] = self.max_pools()[offset]

    def heal_full(self):
        self._current_pools = copy.deepcopy(self.max_pools())

    def print_connections(self):
        for g in self.connections():
            if not isinstance(g, str):
                print("Choice: " + str(g))
            else:
                print(g)

    def gain_exp(self, amount=1):
        self._exp += amount

    def spend_exp(self, amount=1):
        self._exp -= amount

    def level_up(self, choice):
        """
        Spends 4 exp to level up, and chooses 1 from the lvl up choices. After 4 choices, the tier goes up.
        Incomplete.
        :param choice: The level up choice chosen
        :return:
        """
        self.spend_exp(4)
        if choice in range(0,3):
            self._advancement_choices_taken += self._advancement_choices[choice]
            # add skill add choice?
        elif choice not in self._advancement_choices_taken:
            self._advancement_choices_taken += choice
        if len(self._advancement_choices_taken) >= 4:
            self.advance_tier()
            self._advancement_choices_taken = []

    def advance_tier(self):
        """
        Advances Tier, unlocking new abilities
        Incomplete.
        """
        self._tier += 1

    def _reset_character(self):
        pass

    def print_character(self):
        print("NAME: \t" + str(self.name()))
        print("STATUS:\t" + str(self.damage_status()))
        self.print_pools()
        print("ASSIGNABLE POOL POINTS:\t" + str(self.assignable_points()))
        print("SKILLS: ")
        self.print_skills()
        print("ITEMS: ")
        self.print_items()
        print("EXP: \t" + str(self.exp()))
        print("CONNECTIONS: ")
        self.print_connections()


def record_pc(self, pc, filename):
    # fuck how should I format this
    with open(filename, "w") as f:
        f.write(pc.name())


def read_pcs(filename):
    with open(filename, "r") as f:
        pass


if __name__ == "__main__":
    mojo = CypherPC("Mojo")
    mojo.assign_stat_point("might")
    print(mojo.max_pools())
