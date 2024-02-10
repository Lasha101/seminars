
# import string



# without_uppercase = user_input.replace("A", "").replace("B", "").replace("C", "").replace("D", "").replace("E", "")\
#                               .replace("F", "").replace("G", "").replace("H", "").replace("I", "").replace("J", "")\
#                               .replace("K", "").replace("L", "").replace("M", "").replace("N", "").replace("O", "")\
#                               .replace("P", "").replace("Q", "").replace("R", "").replace("S", "").replace("T", "")\
#                               .replace("U", "").replace("V", "").replace("W", "").replace("X", "").replace("Y", "")\
#                               .replace("Z", "")


# without_uppercase = user_input.translate({65: None, 66: None, 67: None, 68: None, 69: None, 
#                                           70: None, 71: None, 72: None, 73: None, 74: None, 
#                                           75: None, 76: None, 77: None, 78: None, 79: None, 
#                                           80: None, 81: None, 82: None, 83: None, 84: None, 
#                                           85: None, 86: None, 87: None, 88: None, 89: None, 
#                                           90: None})

# translation_table = str.maketrans('', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# translation_table = str.maketrans('', '', string.ascii_uppercase)

# without_uppercase = user_input.translate(translation_table)

# count = len(user_input) - len(without_uppercase)



# for i in user_input:
#     if i.isupper():
#         count += 1




user_input = input("Enter your string: ").title()

my_str = ""
count = 0
ind = 0

for i in range(len(user_input) - 1):
    if user_input[i].isupper():
        my_str += user_input[i]
        count += 1
        while ind + 1 < len(user_input) and user_input[ind + 1].isalpha():
            my_str += user_input[ind + 1]
            ind += 1
        else:
            my_str += " "
    ind += 1

my_list = my_str.split()

print(my_list[3])

print(count, my_list)





# იარაღის მაღაზიის ანკეტა

# a = input("Minor? ").strip().lower()
# crm = input("Conviction? ").strip().lower()
# p = input("Psycho? ").strip().lower()
# csh = input("Citizenship? ").strip().lower()
# h = input("Habitant? ").strip().lower()

# if (a == "no" and crm == "no" and p == "no") and (csh == "yes" or h == "yes"):
#     print("YES! You can buy the gun!")
# else:
#     print("NO! You CAN NOT buy the gun!")
        



# def question_func(v):
#     a = input(v)
#     if a != "yes" and a != "no":
#         return question_func(v)
#     return a

# print(question_func(var))

def question_func(v):
    a = ""
    while a != "yes" and a != "no":
        a = input(v)
    return a


def loop_func():
    quests_list = ["Minor? ", "Conviction? ","Psycho? ", "Citizenship? ", "Habitant? "]
    answers_list = []
    for i in quests_list:
        answer = question_func(i)
        answers_list.append(answer)
    return answers_list


def checker_func(l):
    ans = l()
    if ans[0] == "no":
        if ans[1] == "no":
            if ans[2] == "no":
                if ans[3] == "yes" or ans[4] == "yes":
                    return "YES! You can buy the gun!"
    return "NO! You CAN NOT buy the gun!"

print(checker_func(loop_func))