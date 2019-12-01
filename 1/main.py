
def op(mass):
    return int(mass / 3) - 2

def read_file():
    with open("data.txt", "r") as f:
        contents = f.read().split("\n")
        contents = [int(x) for x in contents if x]
        return contents

def recursive_add(mass, sum):
    if mass <= 0:
        return sum

    this_fuel = op(mass)
    new_sum = sum + this_fuel if this_fuel >= 0 else sum
    return recursive_add(this_fuel, new_sum)

def main():
    sum = 0
    masses = read_file()
    for i in masses:
        sum += recursive_add(i, 0)

    print(sum)

if __name__ == "__main__":
    main()
