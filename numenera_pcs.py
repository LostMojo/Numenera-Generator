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

    # weapons
    # edge base?

    def _configure_character(self):
        # function that makes sure things are where they're supposed to be?
        pass

    def new_type(self, char_type="Noun"):
        if char_type in data.types:
            self._type = char_type
            self._type_stat_base = data.types["Base Stats"]
            for skill in data.types["Class Skills"]:
                self.overwrite_skill(skill)
        else:
            self._type = char_type
            self._type_stat_base = data.type_template["Base Stats"]
            self._reset_character()


if __name__ == "__main__":
    print(random.choice(list(data.types.keys())))
