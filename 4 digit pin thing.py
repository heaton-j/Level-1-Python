#enter your pin
pin = int(input("Please set your secret pin"))
i = 0
while i < pin:
    print(str(i).zfill(4))
    i += 1
pin = str(i).zfill(4)
print("Your secret pin is {}".format(pin))



