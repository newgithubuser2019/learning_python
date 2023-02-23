from random import randint


# ---------------------------------------------------------------------------------------------------
# Create a class
class Die():
    """docstring here"""
    # A class representing a single die

    def __init__(self, num_sides=6):
        # Assume a six-sided die
        self.num_sides = num_sides

    def roll(self):
        """docstring here"""
        # Return a random value between 1 and number of sides
        return randint(1, self.num_sides)


# ---------------------------------------------------------------------------------------------------
# import class
# from die import Die

# Create a D6(a die with six sides)
# die = Die()
die_1 = Die()
# die_2 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = []
for roll_num in range(100):
    # result = die.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)
print("--------------------------------------------------------------------------------------------------------------------------------")
# print(results)
# print("\n")

# Analyze the results.
frequencies = []
frequencies_dict = {}
max_result = die_1.num_sides + die_2.num_sides
# for value in range(1, die.num_sides+1):
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    frequencies_dict.setdefault(value, frequency)

for k, v in frequencies_dict.items():
    print(str(k) + " was rolled " + str(v) + " times")
    # print("\n")

# ---------------------------------------------------------------------------------------------------
# Visualize the results
