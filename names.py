import random


def get_names(filename):
    try:
        f = open(filename, 'r')
        _ = f.readline()        # Reads M for Masc names
        masc_names = f.readline().split(', ')
        _ = f.readline()        # Reads F for Femme names
        femme_names = f.readline().split(', ')
        _ = f.readline()        # Reads N for Neutral names
        neutral_names = f.readline().split(', ')
        _ = f.readline()        # Reads L for Last names
        last_names = f.readline().split(', ')
        return masc_names, femme_names, neutral_names, last_names
    finally:
        f.close()


def make_full_name(first_list, last_list):
    return "{0} {1}".format(random.choice(first_list), random.choice(last_list))


class NameFile:
    """A class for unpacking and using a name file"""
    def __init__(self, filename):
        self.masc_names, self.femme_names, self.neutral_names, self.last_names = get_names(filename)

    def rand_name(self, gender='a'):
        """A method to return a random name. Genders of names are (M)asculine, (F)eminine, or (N)eutral.
        Anything else chooses from all three categories"""
        if gender.capitalize() == 'M':
            return random.choice(self.masc_names)
        elif gender.capitalize() == 'F':
            return random.choice(self.femme_names)
        elif gender.capitalize() == 'N':
            return random.choice(self.neutral_names)
        else:
            return random.choice(self.masc_names + self.femme_names + self.neutral_names)

    def rand_full_name(self, gender='a'):
        if gender.capitalize() == 'M':
            return make_full_name(self.masc_names, self.last_names)
        elif gender.capitalize() == 'F':
            return make_full_name(self.femme_names, self.last_names)
        elif gender.capitalize() == 'N':
            return make_full_name(self.neutral_names, self.last_names)
        else:
            return make_full_name(self.masc_names + self.femme_names + self.neutral_names, self.last_names)


if __name__ == "__main__":
    western_names = NameFile("westernnames.txt")
    print(western_names.rand_full_name())
    print()
    print(western_names.rand_full_name('m'))
