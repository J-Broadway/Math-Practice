import pickle
from os import path


# Check for ranges.pickle. If not available create it.
def main():
    ranges = {'a': [[1, 100], [1, 100]], 's': [[1, 100], [1, 100]], 'm': [[1, 12], [1, 12]], 'd': [[1, 12], [1, 12]]}
    if path.exists("ranges.pickle") == True:
        pass
    else:
        with open("ranges.pickle", "wb") as f:
            pickle.dump(ranges, f)
            print("Default ranges created")


if __name__ == "__main__":
    main()