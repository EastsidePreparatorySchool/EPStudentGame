def load_game():
    # If they have preloaded gamestate, load that here
    pass

def save_game():
    pass

def choose_archetype():
    pass

def buy_supplies():
    pass

# save player state in variables here
month = 0
year = "Freshman"

def check_quit():
    quit = input("Would you like to save and quit? (Y/N)")
    if (quit.lower() == "Y"):
        save_game()
        return True
    else:
        return False
def game_loop():
    if (check_quit() is not True):
        print("Month: " + month, "Year " + year)
    # month passes
    # action
    # Randomly pre-scheduled event
    pass

def finish():
    pass