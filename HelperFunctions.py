from CharacterClasses import *
def return_class(n):
    chr_list = [Human(),Orc(),Elf(),MosqMan(),MrClean(),TPFeeders()]
    return chr_list[n-1]

def return_equipment(n, equipment_list):
    target = equipment_list
    return target[n-1]

def get_inx(inpt, obj_list):
    try:
        if "?" in inpt:
            answer_q(obj_list )
    except:
        return return_equipment(inpt, obj_list)

def answer_q(obj_list):
    print("Which choice would you like to know more about?\n")
    print("\t (1) %s\n\t (2) %s\n\t (3) %s\n"%(obj_list[0].label,obj_list[1].label,obj_list[2].label))
    inx = int(input())
    return obj_list[inx].description

def choose_x(x, x_list, usr_object):
    import time
    time.sleep(1)
    print("Based on your class you can choose: \n\t (1) %s\n\t (2) %s\n\t (3) %s" % (
    x_list[0].label, x_list[1].label, x_list[2].label))
    print("What'll it be?\n")
    #inx_answer = get_inx(int(input()),x_list)
    x = return_equipment(int(input()), x_list)
    print("You have chosen a(n): %s !\n" % x.label)
    time.sleep(1.2)

def get_name(usr_object):
    inpt_name = input()
    try:
        float(inpt_name)
        print("Incorrect input format. Must only contain letters.")
        get_name()
    except:
        if chk_name(inpt_name):
            usr_object.name = inpt_name.upper()

def chk_name(inpt_name):
    print("%s ... are you sure about that? (Y/n)\n" % inpt_name.upper())
    answer = str(input()) #TODO: Check that input is not a number or other character
    yes_list = ["YES","yes","Y","y","YEs","Yes","yEs","yeS","yES","y","Y"]
    no_list = ["NO","no","nO","No","N","n"]
    if answer in yes_list:
        print("Perfect! Great name, %s\n"%inpt_name.upper())
        return True
    elif answer in no_list:
        print("Okay, then what name do you want?\n")
        new_name = input()
        chk_name(new_name)
    else:
        print("Incorrect answer format. Try 'yes' or 'no'")
        chk_name(inpt_name)

def slow_type(string):
    import time
    import sys
    for i in string:
        print(i, end='')
        time.sleep(.1)
        sys.stdout.flush()


# def chk_format(format_type=str):
#     """
#     Returns Boolean once the inputted format matches the `format_type`
#     :param format_type:
#     :return:
#     """
#     try:
#


slow_type("Welcome to my game.")
print(" ")

