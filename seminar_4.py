# import time

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

# def view_all_tasks(x):
#     print("{:<15}| {:<20}| {:<20}| {:<20}".format("Day", "Morning", "Noon", "Evening"))
#     print("--" * 41)
#     for day_tasks in tasks_db[x]:
#         for day, tasks in day_tasks.items():
#             print("{:<15}|".format(day.capitalize()), end="")
#             for time_slot in ["morning", "noon", "evening"]:
#                 task_found = next((task[time_slot] for task in tasks if time_slot in task), "")
#                 print(" {:<20}|".format(task_found), end="")
#             print()
            
# def view_day_tasks(x, y):
#     print("{:<15}| {:<20}| {:<20}| {:<20}".format("Day", "Morning", "Noon", "Evening"))
#     print("--" * 41)
#     if y == "saturday":
#         ind = 0
#     else:
#         ind = 1
#     for day, tasks in tasks_db[x][ind].items():
#         print("{:<15}|".format(day.capitalize()), end="")
#         for time_slot in ["morning", "noon", "evening"]:
#             task_found = next((task[time_slot] for task in tasks if time_slot in task), "")
#             print(" {:<20}|".format(task_found), end="")
#         print()
    
# def view_specific_task(x, y, z):
#     if y == "saturday":
#         ind = 0
#     else:
#         ind = 1
#     if z == "morning":
#         in_1 = 0
#     elif z == "noon":
#         in_1 = 1
#     else:
#         in_1 = 2
#     print(tasks_db[x][ind][y][in_1][z])

# def dispatcher(v): 
#     f_key_value = next((user_info["foreign_key"] for user_info in login_db \
#                           if user_info["user_name"] == v),\
#                           None)
#     route_input = input("Enter rout: ").strip().lower()
#     var = route_input.count("/")
#     msg = "Invalid input!"

#     if route_input == "":
#         view_all_tasks(f_key_value)
#     elif var == 1 and route_input.endswith("/"):
#         day = route_input.replace("/", "")
#         if day == "saturday" or day == "sunday":
#             view_day_tasks(f_key_value, day)
#         else:
#             raise ValueError(msg)
#     elif var == 2 and route_input.endswith("/"):
#         day, time, foo = route_input.split("/")
#         if day == "saturday" or day == "sunday":
#             if time in ["morning", "noon", "evening"]:
#                 view_specific_task(f_key_value, day, time)
#     else:
#         raise ValueError(msg)

# def main():
#     max_attempts = 0
#     wait_time = 5  
#     while True:
#         user_name = input("Enter the username: ").strip().lower()
#         password = input("Enter the password: ").strip()
#         for user in login_db:
#             if user["user_name"] == user_name and user["password"] == password:
#                 print("Username and password are correct.")
#                 dispatcher(user_name)
#                 exit()
#         print("Incorrect username or password.")
#         max_attempts += 1
#         if max_attempts == 3:
#             for remaining_time in range(wait_time, 0, -1):
#                 print(f"Too many unsuccessful attempts. Waiting for {remaining_time} seconds...")
#                 time.sleep(1)
#             max_attempts = 0

# main()




# out of RAM: Registration, login, Create and Read from CRUD

import os
import csv
from tabulate import tabulate

def create_register_file():
    header = ["user_name", "password", "foreign_key"]
    with open("register.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

def create_user_task_file(foreign_key):
    task_file_name = f"tasks_{foreign_key}.csv"
    header = ["task", "date"]
    with open(task_file_name, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

def get_next_foreign_key():
    if not os.path.isfile("register.csv"):
        return "0"
    with open("register.csv", "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return str(len(list(csv_reader)))


def check_user(username):
    with open("register.csv", "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["user_name"] == username:
                return row["password"], row["foreign_key"]
    return None, None


def register_user(username, new_password, foreign_key):
    with open("register.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([username, new_password, foreign_key])
    print("Regidtration successful!")
    create_user_task_file(foreign_key)
    print(f"Task file is created for {username}.")



def add_task(username):
    _, foreign_key = check_user(username)
    task_file_name = f"tasks_{foreign_key}.csv"

    task = input("Task description: ")
    date = input("Entrer execution date: (dd/mm/yyyy) ")

    with open(task_file_name, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([task, date])
    print("Task added!")


def display_tasks(username):
    _, foreign_key = check_user(username)
    task_file_name = f"tasks_{foreign_key}.csv"
    with open(task_file_name, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        sorted_tasks = sorted(csv_reader, key=lambda x: x['date'])

        if sorted_tasks:
            headers = ["Task", "Date"]
            task_table = [[task["task"], task["date"]] for task in sorted_tasks]
            print(tabulate(task_table, headers=headers, tablefmt="grid"))
        else:
            print("No tasks to display.")

def main():
    if not os.path.isfile("register.csv"):
        create_register_file()

    username = input("Enter user_name: ")
    password_in_file, foreign_key = check_user(username)

    if password_in_file:
        entered_password = input("Enter password: ")
        if password_in_file == entered_password:
            print("Access granted")

            task_option = input("Add task? (yes/no) ")
            if task_option.lower() == "yes":
                add_task(username) 

            display_option = input("Display tasks? (yes/no) ")
            if display_option.lower() == "yes":
                display_tasks(username)

        else:
            print("Wrong password!")
    else:
        next_foreign_key = get_next_foreign_key()
        register_option = input("Do you want to register? (yes/no) ")
        if register_option.lower() == "yes":
            new_password = input("Enter your password for registation: ")
            register_user(username, new_password, next_foreign_key)
            add_task(username)
        else:
            print("Access denied. User not registered.")

if __name__ == "__main__":
    main()
