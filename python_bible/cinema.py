# Here we have created a dictionary with that films there is to be views,
# and then used a list to show the age limit and how many tickets there are,
# for the film.
films = {
         "Finding Dory": [3,5],
         "Bourne": [18,5],
         "Tarzan": [15,5],
         "Ghost Busters": [12,5]
        }

# Here we have created a while loop to make the booking operator continue without,
# ending.
while True:
    # Here we have created an input statment to ask the user which film they,
    # would like to see.
    choice = input("What film would you like to go see?: ").strip().title()
    # Here we are using an if statment to check if the film that the user has,
    # entered is infact in the list of fims available.
    if choice in films:
        # Here we are asking the user for there age so we can check it against,
        # the age limit for the film and continue to ask the user's age, otherwise,
        # it will let the user know that the film is not being shown
        age = int(input("How old are you?: ").strip())
        # By using an if statment and saying if the age of the user is greater to,
        # or equal to. By using the if statment this then allows us to check how,
        # many seats are available
        if age >= films[choice][0]:
            # Here we are creating a variable to store how many seats there are,
            # for the film.
            num_seats = films[choice][1]
            # Here we are checking to see that there is a greater number than 0,
            # of seats left for the film, if the statment is true then it will,
            # allow the user to continue to watch the film and then take 1 ticket,
            # away from the ticket allocation there is for the film. Otherwise,
            # if there is not tickets then it will not allow the user to watch the,
            # film.
            if num_seats > 0:
                 print("Enjoy the film")
                 # In order to take 1 away from the ticket allocation we must,
                 # set he variable and then assign it to the -1 ticket for it,
                 # to be continued to be called on.
                 films[choice][1] = films[choice][1] - 1
        else:
            print("Sorry! You are to young to see the film")
    else:
        print("We do not show that film....")
