import re

user_string_1 = "Disable-LocalUser  Ogurchuk"
user_string_2 = "Enable-LocalUser  Ogurchuk"

user_string_3 = "<h1>   Enable-LocalUser      User_1 </h1>"

p = re.compile(r'(?:Disable|Enable)-LocalUser\s+([A-Za-z0-9_-]*)\s*')
M1 = p.search(user_string_1)
print("Group 0: Value:  {0}, Length: {1}, Type:   {2}".format(M1.group(0), len(M1.group(0)), type(M1.group(0))))
print("Group 1: Value:  {0}, Length: {1}, Type:   {2}".format(M1.group(1), len(M1.group(1)), type(M1.group(1))))
# print("Group 2: ", M1.group(2))

disable_string = "Disable"
enable_string = "Enable"
pattern_user_activation = re.compile(r'(' +
                                     disable_string +
                                     r'|' +
                                     enable_string +
                                     r')' +
                                     r'-LocalUser\s+([A-Za-z0-9_-]*)\s*')
match_user_activation = pattern_user_activation.search(user_string_3)
if match_user_activation.group(2):
    if match_user_activation.group(1) == disable_string:
        print(disable_string)
    elif match_user_activation.group(1) == enable_string:
        print(enable_string)
    else:
        print("Error, matching.")
    print(match_user_activation.group(2))
    print(match_user_activation.group(0))
