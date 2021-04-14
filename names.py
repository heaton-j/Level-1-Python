names = ["Evi", "Madeleine", "Dan", "Kelsey","Cayden", "Hayley", "Darian"]
names.sort()
print(names)
name_check = input("Please enter a name and check if your name is on the list...")
if name_check in names:
    print("Your name was on the list!")
else:
    print("your name was not on the list")
name_change = input("Would you like to replace a name on the list with your name?")
if name_change == "yes":
    name_replace = input("What name would you like to replace?")
else:
    print("Okay")
new = input("Enter a name to replace {}".format(name_replace))
new_list = names, new

print(new_list)


