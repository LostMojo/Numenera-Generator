"""Contains the PC class, used to make Numenera/Cypher system player characters"""

import roll_numenera as r
import random
import copy

class Pc:

    descriptors = ["Charming", "Clever", "Graceful", "Intelligent", "Learned", "Mystical", "Mechanical", "Rugged",
                   "Stealthy", "Strong", "Strong-willed", "Swift", "Tough", "Adaptable", "Articulate", "Beneficient",
                   "Cheerful", "Civic", "Committed", "Confident", "Cultured", "Curious", "Earnest", "Empirical",
                   "Exacting", "Foreward-Thinking", "Gregarious", "Heroic", "Imaginitive", "Industrious",
                   "Intimidating", "Intuitive", "Irrepressable", "Lawful", "Loyal", "Meddlesome", "Nurturing",
                   "Obsessive", "Optimistic", "Organized", "Passionate", "Perservering", "Prepared", "Protective",
                   "Relentless", "Risk-taking", "Serene", "Vicious"]
    types = ["Glaive", "Jack", "Nano", "Delve", "Arkus", "Wright"]
    foci = ["Bears a Halo of Fire", "Commands Mental Powers", "Controls Beasts", "Controls Gravity", "Crafts Illusions",
            "Employs Magnetism", "Entertains", "Exists Partially Out of Phase", "Explores Dark Places",
            "Fights with Panache", "Fuses Flesh and Steel", "Howls at the Moon", "Hunts", "Lives in the Wilderness",
            "Masters Defense", "Masters Weaponry", "Murders", "Rages", "Rides the Lightning",
            "Speaks With a Silver Tongue", "Talks to Machines", "Wears a Sheen of Ice", "Weilds Power with Precision",
            "Wields Two Weapons at Once", "Works the Back Alleys", "Works Miracles", "Absorbs Energy",
            "Acts Without Consequence", "Adjures the Leviathan", "Augments Flesh with Grafts", "Battles Automatons",
            "Brandishes an Exotic Shield", "Breaks Down Walls", "Builds Tomorrow", "Dances with Dark Matter",
            "Defends the Gate", "Defends the Weak", "Descends From Nobility", "Emerged From The Obelisk",
            "Explores Yesterday", "Fights with a Hoarde", "Fuses Mind and Machine", "Hunts Abhumans", "Imparts Wisdom",
            "Leads", "Learns From Adversity", "Metes Out Justice", "Moves Like A Cat", "Needs No Weapons",
            "Never Says Die", "Posesses a Shard of the Sun", "Radiates Vitality", "Sees Beyond",
            "Sheperds the Community", "Shreds the Walls of the World", "Thunders", "Touches the Sky",
            "Wields Words Like Weapons"]
    #nested dictionaries with skills and benefits?

    _advancement_choices = ["Pool", "Edge", "Skills", "Effort"]
    _advancement_choices_taken = []
    _recovery_rolls = ["1 Action", "10 minutes", "1 hour", "10 hours"]
    _recovery_rolls_used = []


    def __init__(self, name, tier = 1, descriptor = "adjective", type = "noun", focus = "verbs", skills = {},
                 max_might = 10, max_speed = 10, max_int = 10, might_edge = 0, speed_edge = 0, int_edge = 0, armor = 0,
                 exp=0):
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

        if isinstance(name, str):       #ensure name is a string
            self._name = name
        else:
            raise ValueError("PC name must be a string")

        if tier in range(1,10):        #ensure tier  is an int between 1 and 10
            self._tier = tier
        else:
            raise ValueError("PC level must be an int between 1 and 10")

        for key in skills:          #ensures skills are within -2 to 3
            if not skills[key] in range(-2,3):       #Check if skill is an int between -2 and 3
                raise ValueError("PC Skill Error: Skills must have a int level between -2 and 3")

        self._skills = skills
        #add Inabilities for Salvaging, Understanding, and Crafting Numenera?

        if isinstance(descriptor, str):     #ensure descriptor is string
            self._descriptor = descriptor
        else: raise ValueError("PC descriptor must be a string")

        if isinstance(type, str):       #ensure type is string
            self._type = type
        else: raise ValueError("PC Type must be a string")

        if isinstance(focus, str):      #ensure focus is string
            self._focus = focus
        else: raise ValueError("PC focus must be string")

        if max_might in range (1,100):      #ensure max might is positive int
            self._max_might = max_might
        else: raise ValueError("PC max might must be positive integer")

        if max_speed in range(1, 100):  # ensure max speed is positive int
            self._max_speed = max_speed
        else: raise ValueError("PC max speed must be positive integer")

        if max_int in range(1,100):      #ensure max intellect is positive int
            self._max_int = max_int
        else: raise ValueError("PC max intellect must be positive integer")

        #A list of current stat pools, going Might, Speed, Intelligence
        self._current_pools = [self._max_might, self._max_speed, self._max_int]

        if might_edge in range(-3,20):      #ensure might edge is an int between -3 and 20
            self._might_edge = might_edge
        else: raise ValueError("PC might edge must be an int between -3 and 20")

        if speed_edge in range(-3, 20):  # ensure edge is an int between -3 and 20
            self._speed_edge = speed_edge
        else: raise ValueError("PC speed edge must be an int between -3 and 20")

        if speed_edge in range(-3, 20):  # ensure edge is an int between -3 and 20
            self._int_edge = speed_edge
        else: raise ValueError("PC speed edge must be an int between -3 and 20")

        if armor in range(0,30):        #ensure armor is within 0 and 30
            self._armor = armor
        else: raise ValueError("PC armor must be an int between 0 and 30")

        if exp in range(0,10):      #ensure exp is an int between 0 and 10
            self._exp = exp
        else: raise ValueError("PC exp must be an int between 0 and 10")

        _damage_track = 0

    def name(self): return self._name
    def tier(self): return self._tier
    def descriptor(self): return self._descriptor
    def type(self): return self._type
    def focus(self): return self._focus
    def skills(self): return self._skills
    def max_might(self): return self._max_might
    def max_speed(self): return self._max_speed
    def max_int(self): return self._max_int
    def max_pools(self): return [self._max_might, self._max_speed, self._max_int]
    def current_might(self): return self._current_pools[0]
    def current_speed(self): return self._current_pools[1]
    def current_int(self): return self._current_pools[2]
    def current_pools(self): return self._current_pools
    def might_edge(self): return self._might_edge
    def speed_edge(self): return self._speed_edge
    def int_edge(self): return self._int_edge
    def armor(self): return self._armor
    def exp(self): return self._exp

    def describe(self):
        return ("{name} is a {adjective} {noun} who {verbs}.".format(name = self._name, adjective = self._descriptor,
                                                                    noun = self._type, verbs = self._focus))

    def rename(self, name): self._name = name
    def change_descriptor(self, descriptor): self._descriptor = descriptor
    def change_type(self, type): self._type = type
    def change_focus(self, focus): self._focus = focus

    def add_skill(self, skill="Unnamed", training = 1):
        if skill in self._skills:
            self._skills[skill] += training
        else:
            self._skills[skill] = training

    def overwrite_skill(self, skill="Unnamed", training = 1):
        self._skills[skill] = training

    def add_hinderance(self, skill="Unnamed", hinder_level = 1):
        self.add_skill(skill, -1*hinder_level)

    def remove_skill(self, skill="Unnamed"):
        if skill in self._skills:
            del self._skills[skill]
        else:
            raise ValueError("Cannot delete skill {0} because {1} doesn't know it".format(skill, self._name))

    def skill_check(self, difficulty, skill="", effort=0):
        if skill in self._skills:
            difficulty -= self._skills[skill]
        if difficulty-effort < 0:
            return (True, -1)
        else:
            r.check_roll(difficulty, effort)

    def spend_pool(self, amount, pool="int"):
        stats = self.current_pools()
        if pool == "might" or pool == 0:
            offset = 0
            edge = self.might_edge()
        elif pool == "speed" or pool == 1:
            offset = 1
            edge = self.speed_edge()
        else:
            offset = 2
            edge = self.int_edge()
        stats[offset] -= (amount-edge)

    def take_damage(self, damage=1, ignore_armor=False, targeted_pool="might"):
        """
        Deals damage, starting at might, trickling down to speed and then int if the pools are empty
        Args:
        damage: how much damage dealt
        armor: whether the attack is blocked by armor
        targeted_pool: which pool the damage is targeting, all lowercase
        :return: True if the attack does damage, false if it does not
        """
        if not ignore_armor:
            damage -= self.armor()
            if damage <= 0:
                return False
        if targeted_pool == "speed" or targeted_pool == 1: starting_pool = 1
        elif targeted_pool == "int" or targeted_pool == 2: starting_pool = 2
        else: starting_pool = 0
        stats = self.current_pools()
        for i in range(len(stats)):
            pool = (starting_pool+i)%len(stats)
            stats[pool] -= damage
            if stats[pool] >= 0:
                damage = 0
            else:
                damage = -1 * stats[pool]  # removes negative
                stats[pool] = 0
        return True

    def recovery_roll(self, targeted_pool = "int", beyond_max = False, addition = 0, set_roll = -1):
        stats = self.current_pools()
        if targeted_pool == "might" or targeted_pool == 0: offset = 0
        elif targeted_pool == "speed" or targeted_pool == 1: offset = 1
        else: offset = 2
        if set_roll < 0:
            recover = random.randint(1,6) + self._tier + addition
        else:
            recover = set_roll + self._tier + addition
        if beyond_max or (stats[offset] + recover) < self._max_might:
             stats[offset] += recover
        else:
            stats[offset] = self.max_pools()[offset]

    def gain_exp(self, amount=1):
        self._exp += amount

    def spend_exp(self, amount=1):
        self._exp -= amount

    def level_up(self, choice):
        self.spend_exp(4)
        if choice in range(0,3):
            self._advancement_choices_taken += self._advancement_choices[choice]
            #add skill add choice?
        elif choice not in self._advancement_choices_taken:
            self._advancement_choices_taken += choice
        if len(self._advancement_choices_taken) >= 4:
            self.advance_tier()
            self._advancement_choices_taken = []

    def advance_tier(self):
        self._tier += 1

    def gain_skill(self, skill_name):
        self._skills += skill_name

    def randomize_details(self):
        self._descriptor = random.choice(self.descriptors)
        self._type = random.choice(self.types)
        self._focus = random.choice(self.foci)

    def record_pc(self, filename):
        #fuck how should I do this
        with open(filename, "w") as f:
            f.write(self._name)
            f.write(str(self._tier))
            f.write("{0}-{1}-{2}".format(self._descriptor, self._type, self._focus))
            for key in self._skills:
                f.write("{skill}:{lv};".format(skill=key, lv=self._skills[key]))
            f.write(str(self._max_might))


def read_pcs(filename):
    with open(filename, "r") as f:
        pass

    #method for rolling against an NPC?

if __name__ == "__main__":
    Zirconia = Pc(name="Zirconia", tier=1, skills={"Salvaging Numenera":1})
    Zirconia.gain_exp(4)
    Zirconia.level_up(0)
    Zirconia.randomize_details()
    Zirconia.spend_pool(10)
    Zirconia.recovery_roll(targeted_pool="int", beyond_max=True)
    print(str(Zirconia.current_pools()))
    Zirconia.record_pc("pclist.txt")
    print(Zirconia.describe())