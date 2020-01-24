from cypher_pcs import CypherPC
import numenera_data as data
import random


def get_type(noun): return data.types[noun]


def get_descriptor(adjective): return data.types[adjective]


def get_focus(verb): return data.types[verb]


def type_list(): return list(data.types.keys())


def descriptor_list(): return list(data.descriptors.keys())


def focus_list(): return list(data.discovery_foci.keys())       # temporary change to limit to discovery


class NumeneraPC(CypherPC):
    _type_stat_base = data.type_template["Base Stats"]
    _assignable_points = data.assignable_stat_points
    _assignable_edge_points = 0
    _damage_track = ["Hale", "Impaired", "Debilitated", "Dead"]

    _weapons = []
    _community_bonus = ""

    _items = {
        "Shins": 0,
        "Equipment": [],
        "Cyphers": [],
        "Oddities": [],
        "Iotum": {},
        "Parts": 0,
        "Artifacts": []
    }

    _attacks = {}
    # edge base?

    def shins(self): return self._items["Shins"]
    def set_shins(self, amount=0): self._items["Shins"] = amount
    def add_shins(self, amount=1): self._items["Shins"] = self._items["Shins"] + amount
    def lose_shins(self, amount=1): self._items["Shins"] = self._items["Shins"] - amount

    def artifacts(self): return self._items["Artifacts"]

    def _configure_character(self):
        self.new_type(self.type())
        self.new_descriptor(self.descriptor())
        self.new_focus(self.focus())

    def new_type(self, char_type="Noun"):
        if char_type in data.types:
            self._type = char_type
            d = data.types[char_type]
            self._type_stat_base = d["Base Stats"]
            self._max_pools = [self._type_stat_base[p]+self._other_pool_bonuses[p]+self._assigned_points[p] for p in
                               range(0, len(self._max_pools))]
            if d["Starting Edge"] == "CHOICE":
                self._edge_list = [0, 0, 0]
                self._assignable_edge_points = 1
            else:
                self._edge_list = d["Starting Edge"]
            self._weapons = d["Weapon Proficiencies"]
            for skill in d["Class Skills"]:
                self.overwrite_skill(skill)
            self._intrusion_options.update(d["Class Intrusions"])
            self._cypher_limit = d["Cypher Limit"]
            self._add_dict_inventory(d["Starting Equipment"])   # items
            # optional default cyphers & oddity?
            self._community_bonus = d["Community Bonus"]
            # pick a connection? self._connections.update(d["Connections"])
            self._update_tier_abilities(d["Tiers"])
        else:
            self._type = char_type
            self._reset_character()

    def new_descriptor(self, descriptor="adjective"):
        if descriptor in data.descriptors:
            d = data.descriptors[descriptor]
            self._other_pool_bonuses = [self._other_pool_bonuses[p]+d["Stat Bonuses"][p] for p in
                                        range(0, len(self._other_pool_bonuses))]
            self._max_pools = [self._type_stat_base[p]+self._other_pool_bonuses[p]+self._assigned_points[p] for p in
                               range(0, len(self._max_pools))]
            for skill in d["Skills"]:
                self.add_skill(skill)
            for skill in d["Inabilities"]:
                self.add_hindrance(skill)
            self._abilities['1'].update(d["Features"])        # separate variable for descriptor abilities?
            self._add_dict_inventory(d["Additional Equipment"])
            # Link to starting adventure?
        else:
            self._reset_character()
            self._descriptor = descriptor

    def new_focus(self, focus="verbs"):
        if focus in data.foci:
            d = data.foci[focus]
            self._connections.append(d["Connection"])       # appends a choice of connections
            self._add_dict_inventory(d["Additional Equipment"])
            self._major_effect_suggestions.extend(d["Major Effect Suggestions"])
            self._minor_effect_suggestions.extend(d["Minor Effect Suggestions"])
            self._update_tier_abilities(d["Tiers"])
        else:
            self._reset_character()
            self._focus = focus

    def _update_tier_abilities(self, tier_dictionary):
        for t in range(1, self._tier+1):
            if t <= 6:
                if str(t) in self.abilities():
                    self._abilities[str(t)].update(tier_dictionary[str(t)])
                else:
                    self._abilities[str(t)] = tier_dictionary[str(t)]
            # no support for over-levelling

    def _add_dict_inventory(self, d, item_pouch=_items):        # item_pouch used to find which dictionary to look in
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

    def _print_items(self):
        for key in self._items:
            print(str(key) + ": " + str(self._items[key]))

    def randomize_character(self):
        self._descriptor = random.choice(descriptor_list())
        self._type = random.choice(type_list())
        self._focus = random.choice(focus_list())
        # self._configure_character()

    def _reset_character(self):
        pass


if __name__ == "__main__":
    teddy = NumeneraPC("Theodore", tier=6, char_type=random.choice(type_list()),
                       descriptor=random.choice(descriptor_list()), focus=random.choice(descriptor_list()))
    print(teddy.describe())
    print(teddy.max_pools())
    teddy._print_items()
"""    for tier in teddy.abilities():
        print(str(tier))
        for key in teddy.abilities()[tier]:
            print(key)
"""
