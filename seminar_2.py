import time

login_db = [
    {"user_name":"tako_99", "password" :"Green$1999", "foreign_key": "0"},
    {"user_name":"guga_11", "password" :"Yellow$2011", "foreign_key": "1"},
    {"user_name":"nani_77", "password" :"Black$1977", "foreign_key": "2"},
    {"user_name":"luka_13", "password" :"Orange$2013", "foreign_key": "3"},
]

tasks_db = {
    "0":[{"saturday":[{"morning":"walk the dog"}, {"noon": "restaurant"}, {"evening":"cinema"}]},
         {"sunday":[{"morning":"walk the dog"}, {"noon": "planning week-end"}, {"evening":"nothong to do"}]}],

    "1":[{"saturday":[{"morning":"by the fruits"}, {"noon": "nothing to do"}, {"evening":"with family"}]},
         {"sunday":[{"morning": "math, physics"}, {"noon": "walk in the park"}, {"evening":"english, chemistry"}]}],

    "2":[{"saturday":[{"morning":"sleeping good"}, {"noon": "jogging, yoga"}, {"evening":"wash the car"}]},
         {"sunday":[{"morning":"go to church"}, {"noon": "reading the book"}, {"evening":"nothing to do"}]}],

    "3":[{"saturday":[{"morning":"go to pool"}, {"noon": "call to James"}, {"evening":"nothing to do"}]},
         {"sunday":[{"morning":"go to pool"}, {"noon": "programming"}, {"evening":"nothing to do"}]}],
}

def view_all_tasks(x):
    print("{:<15}| {:<20}| {:<20}| {:<20}".format("Day", "Morning", "Noon", "Evening"))
    print("--" * 41)
    for day_tasks in tasks_db[x]:
        for day, tasks in day_tasks.items():
            print("{:<15}|".format(day.capitalize()), end="")
            for time_slot in ["morning", "noon", "evening"]:
                task_found = next((task[time_slot] for task in tasks if time_slot in task), "")
                print(" {:<20}|".format(task_found), end="")
            print()
            
def view_day_tasks(x, y):
    print("{:<15}| {:<20}| {:<20}| {:<20}".format("Day", "Morning", "Noon", "Evening"))
    print("--" * 41)
    if y == "saturday":
        ind = 0
    else:
        ind = 1
    for day, tasks in tasks_db[x][ind].items():
        print("{:<15}|".format(day.capitalize()), end="")
        for time_slot in ["morning", "noon", "evening"]:
            task_found = next((task[time_slot] for task in tasks if time_slot in task), "")
            print(" {:<20}|".format(task_found), end="")
        print()
    
def view_specific_task(x, y, z):
    if y == "saturday":
        ind = 0
    else:
        ind = 1
    if z == "morning":
        in_1 = 0
    elif z == "noon":
        in_1 = 1
    else:
        in_1 = 2
    print(tasks_db[x][ind][y][in_1][z])

def dispatcher(v): 
    f_key_value = next((user_info["foreign_key"] for user_info in login_db \
                          if user_info["user_name"] == v),\
                          None)
    route_input = input("Enter rout: ").strip().lower()
    var = route_input.count("/")
    msg = "Invalid input!"

    if route_input == "":
        view_all_tasks(f_key_value)
    elif var == 1 and route_input.endswith("/"):
        day = route_input.replace("/", "")
        if day == "saturday" or day == "sunday":
            view_day_tasks(f_key_value, day)
        else:
            raise ValueError(msg)
    elif var == 2 and route_input.endswith("/"):
        day, time, foo = route_input.split("/")
        if day == "saturday" or day == "sunday":
            if time in ["morning", "noon", "evening"]:
                view_specific_task(f_key_value, day, time)
    else:
        raise ValueError(msg)

def main():
    max_attempts = 0
    wait_time = 5  
    while True:
        user_name = input("Enter the username: ").strip().lower()
        password = input("Enter the password: ").strip()
        for user in login_db:
            if user["user_name"] == user_name and user["password"] == password:
                print("Username and password are correct.")
                dispatcher(user_name)
                exit()
        print("Incorrect username or password.")
        max_attempts += 1
        if max_attempts == 3:
            for remaining_time in range(wait_time, 0, -1):
                print(f"Too many unsuccessful attempts. Waiting for {remaining_time} seconds...")
                time.sleep(1)
            max_attempts = 0

main()


# კაფელის მაღაზია


# import math
# import sys

# k_dict ={
#     "grey": 0.2,
#     "blue": 0.3,
#     "white" : 0.4
# }


# print("""
                 
#                  For the normal room enter width and length!
                
#                  For the round room enter only radius!
                 
#                  For the L-shaped room ATTENTION!!! Your L-shaped room's each corner must make 90 degrees!!!
#                  Your room has two L-shaped paralel walls and on the ends they are connected with two sides! 
#                  The bigger L-shaped wall is outer and smaller is inner!
#                  Each L-shaped wall is composed by two sides and they make a corner!
      
#                  Enter the values only in this order: 
      
#                  the length of the outer L-shaped wall's side!
#                  the length of the inner L-shaped wall's side in front of the previous side!
#                  the length of the side connecting two previous sides! In front of this side there is a corner!
#                  NOW, enter the length of the outer L-shaped wall's other side!
#                  the length of the inner L-shaped wall's side in front of the previous side!
#                  the length of the side connecting two previous sides! In front of this side there is a corner!
#               """)

# if len(sys.argv) == 3:
#     radius = float(sys.argv[1])
#     k = k_dict.get(sys.argv[2])
#     cyrc_area = math.pi * pow(radius, 2) * 1.27
#     num = (radius * 2) / k
#     num = math.ceil(num)
#     print(num)
# elif len(sys.argv) == 4:
#     k = k_dict.get(sys.argv[3])
#     if sys.argv[1] == sys.argv[2]:
#         side = float(sys.argv[1])
#         num_1 = math.ceil(side / k)
#         num = num_1 * 2
#         print(num)
#     else:
#         length = float(sys.argv[1])
#         width = float(sys.argv[2])
#         num_1 = math.ceil(length / k)
#         num_2 = math.ceil(width / k)
#         num = num_1 * num_2
#         print(num)
# elif len(sys.argv) == 8:
#     k = k_dict.get(sys.argv[7])
#     outer_1 = float(sys.argv[1])
#     inner_1 = float(sys.argv[2])
#     side_1 = float(sys.argv[3])
#     outer_2 = float(sys.argv[4])
#     inner_2 = float(sys.argv[5])
#     side_2 = float(sys.argv[6])
#     if (inner_1 + side_2) == outer_1 and (inner_2 + side_1) == outer_2:
#         num_1 = outer_1 / k
#         num_2 = side_1 / k
#         number_1 = num_1 + num_2
#         number_1 = math.ceil(number_1)
#         num_3 = outer_2 / k
#         num_4 = side_2 / k
#         number_2 = num_3 + num_4
#         number_2 = math.ceil(number_2)
#         final_number = number_1 * number_2
#         print(final_number)
# else:
#     print("invalid input")

































