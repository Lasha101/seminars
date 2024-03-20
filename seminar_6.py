

# login_db = [
#     {"user_name":"tako_99", "password" :"Green$1999", "foreign_key": "0"},
#     {"user_name":"guga_11", "password" :"Yellow$2011", "foreign_key": "1"},
#     {"user_name":"nani_77", "password" :"Black$1977", "foreign_key": "2"},
#     {"user_name":"luka_13", "password" :"Orange$2013", "foreign_key": "3"},
# ]

# tasks_db = {
#     "0":[{"saturday":[{"morning":"walk the dog"}, {"noon": "restaurant"}, {"evening":"cinema"}]},
#          {"sunday":[{"morning":"walk the dog"}, {"noon": "planning week-end"}, {"evening":"nothong to do"}]}],

#     "1":[{"saturday":[{"morning":"by the fruits"}, {"noon": "nothing to do"}, {"evening":"with family"}]},
#          {"sunday":[{"morning": "math, physics"}, {"noon": "walk in the park"}, {"evening":"english, chemistry"}]}],

#     "2":[{"saturday":[{"morning":"sleeping good"}, {"noon": "jogging, yoga"}, {"evening":"wash the car"}]},
#          {"sunday":[{"morning":"go to church"}, {"noon": "reading the book"}, {"evening":"nothing to do"}]}],

#     "3":[{"saturday":[{"morning":"go to pool"}, {"noon": "call to James"}, {"evening":"nothing to do"}]},
#          {"sunday":[{"morning":"go to pool"}, {"noon": "programming"}, {"evening":"nothing to do"}]}],
# }

# print(tasks_db["0"])
# print()
# print(tasks_db["0"][1])

# print()
# print(tasks_db["0"][1]["sunday"])

# print()
# print(tasks_db["0"][1]["sunday"][2]["evening"])



# print(login_db)
# print(type(login_db))
# print(len(login_db))
# print(login_db[2])
# print(login_db[2].items())
# print(login_db[2].keys())
# print(login_db[2]["password"])

# for i in login_db[2].items():
#     print(*i)

# for i in login_db:
#     print(i)


# my_list = []

# for i in login_db[2].items():
#     my_list.append(i)

# print("my_list:", my_list)

# for i in my_list:
#      if my_list.index(i) == 1:
#           print(*i)


# new_list = [element for element in login_db[2].items()]

# print("new_list", new_list)





# Regular expressions: re.search(pattern, text), re.match(pattern, text), re.fullmatch(pattern, text)
#                      re.sub(pattern, replace, text), re.split(pattern, text), re.findall(pattern, text)

# import re

# pattern = r"\d+" #"[0-9]" 

# replace = "number"

# text = "I apples have 3 apples and 5 bannas"

# match = re.findall(pattern, text)


# print(match)



# password = ["lasha", "dachi", "andro", "natia"]

# my_list = []

# for i in range(len(password)):
#     my_list.append(password[i - 1])


# list_1 = []

# for i in range(len(my_list)):
#     list_1.append(my_list[i - 1])
 
# list_2 = []

# for i in range(len(password)):
#     list_2.append(list_1[i - 1])

# password_1 = ["dachi","lasha", "andro", "natia"]

# list_3 = []

# for i in range(len(password)):
#      list_3.append(password_1[i - 1])

# print(password)
# print(my_list)
# print(list_1)
# print(list_2)
# print()
# print(password_1)
# print(list_3)



# from itertools import permutations

# password = ["lasha", "dachi", "andro", "natia"]

# p_list = list(permutations(password))


# for perm in p_list:
#     print(list(perm))
