from cypher_pcs import CypherPC
import numenera_data as data
import random


def get_type(noun): return data.types[noun]


def get_descriptor(adjective): return data.types[adjective]


def get_focus(verb): return data.types[verb]


def type_list(): return list(data.types.keys())


def descriptor_list(): return list(data.descriptors.keys())


def focus_list(): return list(data.foci.keys())


class NumeneraPC(CypherPC):
    _type_stat_base = data.type_template["Base Stats"]
    _assignable_points = data.assignable_stat_points

    _weapons = []
    _community_bonus = ""

    _oddities = []
    _shins = 0

    _attacks = {}
    # edge base?

    def shins(self): return self._shins

    def _configure_character(self):
        self.new_type(self.type())
        self.new_descriptor(self.descriptor())
        self.new_descriptor(self.focus())

    def new_type(self, char_type="Noun"):
        if char_type in data.types:
            self._type = char_type
            d = data.types[char_type]
            self._type_stat_base = d["Base Stats"]
            self._max_pools = [self._type_stat_base[p]+self._other_pool_bonuses[p]+self._assigned_points[p] for p in
                               range(0, len(self._max_pools))]
            self._edge_list = d["Starting Edge"]
            self._weapons = d["Weapon Proficiencies"]
            for skill in d["Class Skills"]:
                self.overwrite_skill(skill)
            self._intrusion_options.update(d["Class Intrusions"])
            self._cypher_limit = d["Cypher Limit"]
            self._items += d["Starting Equipment"]
            # optional default cyphers & oddity?
            self._community_bonus = d["Community Bonus"]
            # pick a connection? self._connections.update(d["Connections"])
            for num in range(1, self._tier+1):
                if num <= 6:
                    if str(num) in self._abilities:
                        self._abilities[str(num)].update(d["Tiers"][str(num)])
                    else:
                        self._abilities[str(num)] = d["Tiers"][str(num)]
                    # no support for overlevelling
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
            self._abilities.update(d["Features"])
            self._items.append(d["Additional Equipment"])
            # Link to starting adventure?
        else:
            self._reset_character()
            self._descriptor = descriptor

    def new_focus(self, focus="verbs"):
        if focus in data.foci:
            d = data.foci[focus]
            self._connections.append(d["Connection"])
            self._items
        else:
            self._reset_character()
            self._focus = focus

    def _reset_character(self):
        pass


if __name__ == "__main__":
    teddy = NumeneraPC("Theodore", char_type="Glaive", descriptor="Charming", focus="Bears a Halo of Fire")
    print(teddy.describe())
