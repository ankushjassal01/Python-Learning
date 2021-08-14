import shelve

with shelve.open('locgame') as game:
    loc = 1
    while True:
        availableExits = ", ".join(game['location'][loc]["exits"].keys())

        print(game['location'][loc]["desc"])

        if loc == 0:
            break
        else:
            allExits = game['location'][loc]["exits"].copy()
            allExits.update(game['location'][loc]["namedExits"])

        direction = input("Available exits are " + availableExits).upper()
        print()

        # Parse the user input, using our vocabulary dictionary if necessary
        if len(direction) > 1:  # more than 1 letter, so check vocab
            words = direction.split()
            for word in words:
                if word in game['vocabulary']:   # does it contain a word we know?
                    direction = game['vocabulary'][word]
                    break

        if direction in allExits:
            loc = allExits[direction]
        else:
            print("You cannot go in that direction")
