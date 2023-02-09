def swg():
    import time
    import random
    print("\t \t \t Snake Water Gun\n")
    time.sleep(1)
    print("Rules: "
          "\n1. You need to choose one from Snake Water or Gun. "
          "\n2. Computer also picks a random choice in every chance."
          "\n3. You are given 10 chances."
          "\n4. When Snake is matched with Water. Snake wins the point. "
          "\n5. When Snake is matched with Gun. Gun wins the point."
          "\n6. When Water is matched with Gun. Water wins the point."      
          "\n7. Whoever has more point wins.")
    time.sleep(2)
    print("\nChoose one from Snake, Water or Gun")
    time.sleep(1)
    print("S for Snake\nW for Water\nG for Gun\n")
    list1 = ["S", "W", "G"]
    chance = 10
    _yourchances = 0
    _comppoints = 0
    _urpoints = 0
    time.sleep(1)

    while chance > _yourchances:
        _input = input("Make your choice:")
        _random = random.choice(list1)
        _yourchances = _yourchances + 1
        attemptsleft = chance - _yourchances
        time.sleep(1)

        if _input == _random:
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nTie. Both awarded 0 points.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "S" and _random == "W":
            _urpoints = _urpoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}."
                  f"\nYou won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "S" and _random == "G":
            _comppoints = _comppoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nComputer won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "W" and _random == "S":
            _comppoints = _comppoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nComputer won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "W" and _random == "G":
            _urpoints = _urpoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nYou won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "G" and _random == "S":
            _urpoints = _urpoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nYou won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        elif _input == "G" and _random == "W":
            _comppoints = _comppoints + 1
            print(f"Your choice: {_input} Computer choice: {_random}. "
                  f"\nComputer won the point.")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

        else:
            print("Your choice is invalid. Enter valid choices")
            time.sleep(0.5)
            print(f"Total attempts: {chance} Your Attempts: {_yourchances} ")
            print(f"Attempts left : {attemptsleft}")
            time.sleep(0.5)
            print(f"Your score: {_urpoints} and Computer score: {_comppoints}\n")

    if _urpoints > _comppoints:
        time.sleep(1)
        print(f"\nYour score: {_urpoints} and Computer score: {_comppoints}")
        print("Congratulations. You won!\n")
    elif _comppoints > _urpoints:
        time.sleep(1)
        print(f"\nYour score: {_urpoints} and Computer score: {_comppoints}")
        print("Bad luck. Computer won!\n")
    else:
        time.sleep(1)
        print(f"\nYour score: {_urpoints} and Computer score: {_comppoints}")
        print("Game Tied. Close game!\n")


while True:
    option1 = "Y"
    option2 = "N"
    _prompt = input("Press Y to run the game\nPress N to stop the game\n")
    if _prompt == "Y":
        swg()
    elif _prompt == "N":
        print("You chose to exit the game. Goodbye!")
        break
    else:
        print("Invalid selection")
        print("Closing the program")
        break


