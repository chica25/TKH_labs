# TODO: take in fellow first name
fname = input("Please give me your first name")

# TODO: take in fellow track name
track = input("What is your track?")

# TODO: take in the names of fellows that they know
name = input("Please give me the names of the fellows that you already know")
familiars = []
while name != "exit":
    familiars.append(name)
    name = input("please give me the names of the fellows that you know already.\
            Type in exit to quit.\n")

# TODO: print out all information
print(fname)
print(track)
print(familiars)

