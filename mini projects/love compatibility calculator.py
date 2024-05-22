# COMPLETION OF JESS'S HOMEWORK

#  the length of name1 divided by the length of name2, then add the number of 'l' and 'o' in name1, then minus the number of 'v' and 'e' in name2, then add 1 return the result.

def name_compatibility(name1, name2):
    l_o = user_name.count("l") + user_name.count("o")
    v_e = crush_name.count("v") + crush_name.count("e")
    name1div2 = len(name1)/len(name2)
    love = l_o - v_e
    namecompatibility = name1div2 + love + 1
    return namecompatibility

# calculate absolute value of the difference between birthday1 and birthday2, then divide the result by 52, lastly return the remainder of that division. birthday is entered as MMDDYYYY


def birthday_compatibility(birthday1, birthday2):
    v1 = abs(birthday1 - birthday2)
    v2 = v1%52
    return v2 


user_name = input("Enter your name: ")
user_birthday = int(input("Enter your birthday (MMDDYYYY): "))
crush_name = input("Enter your crush's name: ")
crush_birthday = int(input("Enter your crush's birthday (MMDDYYYY): "))

# modify the compatibility variable, it should be the SUM of the user & crush's name compatibility and birthday compatibility. CALL the 2 functions you defined earlier with proper arguments.

Name_Compatibility = name_compatibility(user_name, crush_name)
Birthday_Compatibility = birthday_compatibility(user_birthday, crush_birthday)
compatibility = Name_Compatibility + Birthday_Compatibility

# Finish the code with a conditional statement:
# If the compatibility is greater than 1, you will be together. if it's less than 1, you won't be together. if it's 1, you are soulmates!
# You can change the condition (change 1 to another number) if you want to.

if compatibility > 2:
    print("you will be together :D")
elif compatibility < 2:
    print ("you won't be together.")
else:
    print("you're soulmates!!")
print(compatibility)

