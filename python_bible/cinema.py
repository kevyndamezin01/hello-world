films = {
         "Finding Dory": [3,5],
         "Bourne": [18,5],
         "Tarzan": [15,5],
         "Ghost Busters": [12,5]
        }

while True:
    choice = input("What film would you like to go see?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                 print("Enjoy the film")
                 films[choice][1] = films[choice][1] - 1
        else:
            print("Sorry! You are to young to see the film")
    else:
        print("We do not show that film....")
