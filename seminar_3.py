import string
import math

def count_func(user_input):
    translation_table = str.maketrans('', '', string.ascii_uppercase)
    without_uppercase = user_input.translate(translation_table)
    count = len(user_input) - len(without_uppercase)
    return count


def count_func_1(user_input):
    count = 0
    for i in user_input:
        if i.isupper():
            count += 1
    return count

def count_func_2(user_input):
    my_str = ""

    for char in user_input:
        if char.isalpha():
            my_str += char
        elif my_str and my_str[-1] != " ":
            my_str += " "

    my_list = my_str.split()
    return my_list



def checker_func(a, b, c, d, e):
    if a == "no":
        if b == "no":
            if c == "no":
                if d == "yes" or e == "yes":
                    return True
    return False






def dispatcher(route_input): 
    
    var = route_input.count("/")
    msg = "Invalid input!"

    if route_input == "":
        return "view_all_tasks"
    elif var == 1 and route_input.endswith("/"):
        day = route_input.replace("/", "")
        if day == "saturday" or day == "sunday":
            return "view_day_tasks"
        else:
            raise ValueError(msg)
    elif var == 2 and route_input.endswith("/"):
        day, time, foo = route_input.split("/")
        if day == "saturday" or day == "sunday":
            if time in ["morning", "noon", "evening"]:
                return "view_specific_task"
    else:
        raise ValueError(msg)
    

def cyrc_area(r):
    r = int(r)
    cyrc_area = math.pi * pow(r, 2)
    num = round(cyrc_area, 2)
    return num


def sqr_area(side):
    side = int(side)
    s = pow(side, 2)
    return round(s)

def l_func(outer_1, inner_1, side_1, outer_2, inner_2, side_2):
    if (inner_1 + side_2) == outer_1 and (inner_2 + side_1) == outer_2:
        s = (outer_1 * outer_2) - (inner_1 * inner_2)
        return s
    raise ValueError

def main():
    # x = input("Etnter: ")
    # print(count_func(x))
    # print(count_func_1(x))

    # print(count_func_2(user_input))
    a = input("Enter: ")
    b = input("Enter: ")
    c = input("Enter: ")
    d = input("Enter: ")
    e = input("Enter: ")
    f = input("Enter: ")
    # print(checker_func(a, b, c, d, e))

    # route_input = input("Enter rout: ").strip().lower()
    # dispatcher(route_input)
    # side = input("Enter: ")
    # cyrc_area(r)
    # sqr_area(side)
    l_func(a, b, c, d, e, f)
if __name__ == "__main__":
    main()
