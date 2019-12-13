"""
A module that holds The Numenera NPC class.
"""
import roll_cypher


class CypherNPC:
    """A Cypher System NPC"""

    def __init__(self, name="Alex", level=1, skills={}, summary="", notes=""):
        """Initializes Npc

        Args
            name: the npc's name
            level: should be an Int between 1 and 11, signifying overall
            Numenera Level
            skills: Dictionary of the NPC's skills and level in those skills
            summary: summary of the NPC
            notes: DM notes on NPC
        """
        if isinstance(name, str):       # check if name is a string
            self._name = name
        else:
            raise ValueError("NPC Name Error: Not a valid string")

        if level in range(1,12):        # check if it is an Int between 1 and 12
            self._level = level
        else:
            raise ValueError("NPC Lv Error: {} is not valid int for an NPC level".format(level))

        for key in skills:
            if not skills[key] in range(1,11):       # Check if skill is an int between 1 and 11
                raise ValueError("NPC Skill Error: Skills must have a int level between 1 and 11")

        self._skills = skills

        if isinstance(summary, str):        # check if notes is string, if not, raise exception
            self._summary = summary
        else:
            raise ValueError("NPC Summary Error: Summary not a valid string")

        if isinstance(notes, str):
            self._notes = notes
        else:
            raise ValueError("NPC Notes Error: Notes not a valid string")

    def skill(self, skill):
        if skill in self._skills:
            return self._skills[skill]
        else:
            return self.level();

    def level(self):
        return self._level

    def name(self):
        return self._name

    def rename(self, new_name):
        self._name = new_name

    def add_skill(self, new_skill, level):
        self._skills[new_skill] = level

    def change_level(self, new_level):
        self._level = new_level

    def check(self, skill="", mod=0, add=0):
        """
        rolls a check against an NPC level or specific skill
        :param skill: the skill being compared
        :param mod: player's mod from their skills & assets
        :param add: the player's addition to their roll
        :return: returns whether the roll succeeded and the roll itself
        """
        level = self._level
        if skill in self._skills:
            level = self._skills[skill]
        return roll_cypher.check_roll(level, mod, add)

    def show_stats(self):
        print("Name:    {}".format(self._name))
        print("Level:   {}".format(self._level))
        print("Skills:  {}".format(self._skills))
        print("Summary: {}".format(self._summary))

