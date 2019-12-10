from pcs import Pc
from names import NameFile

def ask_name():
    pass

def random_pc(name_file = NameFile("westernnames.txt")):
    rpc =  Pc(name = name_file.rand_full_name())
    rpc.randomize_details()
    return rpc


if __name__ == "__main__":
    western_names = NameFile("westernnames.txt")
    western_boi = random_pc(western_names)
    print(western_boi.describe())
