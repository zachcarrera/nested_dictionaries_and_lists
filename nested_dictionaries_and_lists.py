# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


# 1.1 change value in x
x[1][0] = 15

# 1.2 change last_name of first student
students[0]["last_name"] = "Bryant"

# 1.3 change "Messi" to "Andres"
sports_directory["soccer"][0] = "Andres"

# 1.4 change value 20 in z to 30
z[0]["y"] = 30


# 2. Iterate Through a List of Dictionaries
def iterateDictionary(my_list):
    """ Loop through each Dictionary in a list and print every key value pair """
    for i in my_list:
        for key, val in i.items():
            print(key, "-", val)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    """ Prints every value associated with a given key """
    for i in some_list:
        print(i[key_name])


iterateDictionary2("first_name", students)


# 4. Iterate Through a Dictionary with List Values
def printInfo(my_dict):
    """ Function that prints each key along with the size of its
        value list and prints every value in that list """
    for key in my_dict.keys():
        print(len(my_dict[key]), key.upper())
        for i in my_dict[key]:
            print(i)
        print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
