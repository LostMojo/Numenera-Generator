import random

def getnames(filename):
    try:
        f = open(filename, 'r')
        _ = f.readline()        #Reads M for Masc names
        mNames = f.readline().split(', ')
        _ = f.readline()        #reads F for Femme names
        fNames = f.readline().split(', ')
        _ = f.readline()        #reads N for Neutral names
        nNames = f.readline().split(', ')
        _ = f.readline()        #reads L for Last names
        lNames = f.readline().split(', ')
        return (mNames, fNames, nNames, lNames)
    finally:
        f.close()

def makefullname(first_list, last_list):
    return "{0} {1}".format(random.choice(first_list), random.choice(last_list))

class NameFile:
    """A class for unpacking and using a name file"""
    def __init__(self, filename):
        self.mNames, self.fNames, self.nNames, self.lNames = getnames(filename)

    def rand_name(self, gender='a'):
        if gender.capitalize() == 'M':
            return random.choice(self.mNames)
        elif gender.capitalize() == 'F':
            return random.choice(self.fNames)
        elif gender.capitalize() == 'N':
            return random.choice(self.nNames)
        else:
            return random.choice(self.mNames+self.fNames+self.nNames)


    def rand_full_name(self, gender='a'):
        if (gender.capitalize() == 'M'):
            return makefullname(self.mNames, self.lNames)
        elif (gender.capitalize() == 'F'):
            return makefullname(self.fNames, self.lNames)
        elif (gender.capitalize() == 'N'):
            return makefullname(self.nNames, self.lNames)
        else:
            return makefullname(self.mNames+self.fNames+self.nNames, self.lNames)

if __name__ == "__main__":
    western_names = NameFile("westernnames")
    print(western_names.rand_full_name())
    print()
    print(western_names.rand_full_name('m'))