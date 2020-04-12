# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = (
    "elephant",
    "giraffe",
    "hippopotamus",
    "monkey",
    "otter",
    "peacock",
    "panther",
    "rhino",
    "alligator",
    "lama"
)

# Find one of your animals using the tuple.index(value) syntax on the tuple.

print(zoo.index("hippopotamus"))

# Determine if an animal is in your tuple by using value in tuple syntax.

animal_to_find = "hippopotamus"
if animal_to_find in zoo:
    print(f"We found the {animal_to_find}")

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
"""
children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"
"""
# Create a variable for the animals in your zoo tuple, and print them to the console.

(
    first_animal,
    second_animal,
    third_animal,
    fourth_animal,
    fifth_animal,
    sixth_animal,
    seventh_animal,
    eighth_animal,
    ninth_animal,
    tenth_animal
) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)

# Convert your tuple into a list.

zooList = list(zoo)
print(zooList)

# Use extend() to add three more animals to your zoo.

three_animals = ["zebra", "jellyfish", "antelope"]
zooList.extend(three_animals)
print(zooList)

# Convert the list back into a tuple.

zooListToTuple = tuple(zooList)
print(zooListToTuple)