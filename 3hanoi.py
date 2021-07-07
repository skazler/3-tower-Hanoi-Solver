##############################
#  3 Towers of Hanoi Solver
##############################

# variables
SUM_T = 6 # sum of towers 1+2+3

# print instructions
def inst_print(orig, dest): print(orig, '->', dest)

# get inputs
def get_disks():
    disks = input("How many disks do you have? Type here: ")
    if (int(disks) > 0):
        print(disks, "disks.")
        return int(disks)
    else: 
        print("Invalid number of disks :( Must be greater than 0.")
        get_disks()

def get_start():
    start = input("Which tower are you starting at? Type here: ")
    if ((int(start) > 0) and (int(start) < 4)):
        print("Starting at tower", start, ".")
        return int(start)
    else: 
        print("Invalid tower number :( Must be 1, 2, or 3.")
        get_start()

def get_end():
    end = input("What is your destination tower? Type here: ")
    if ((int(end) > 0) and (int(end) < 4)):
        print("Going to tower", end, ".")
        return int(end)
    else: 
        print("Invalid tower number :( Must be 1, 2, or 3.")
        get_end()

# the recursion
def hanoi(disks, start, end):

    # base case
    if (disks == 1):
        inst_print(start, end)
        return

    # recursive case
    else:
        other = SUM_T - start - end
        hanoi(disks - 1, start, other)
        inst_print(start, end)
        hanoi(disks - 1, other, end)


if __name__ == "__main__":

    disks = get_disks()
    start = get_start()
    end = get_end()

    print("\nHere are your instructions:")

    hanoi(disks, start, end)

    print("Done!\n")
