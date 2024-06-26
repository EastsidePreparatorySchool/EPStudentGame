import json

class GameState():
    def __init__(self, month, year):
        self.month = month
        self.year = year

def load_game():
    # If they have preloaded gamestate, load that here
    load = input("Would you like to load a previous game? (Y/N) ")
    if (load.lower() == "y"):
        filepath = input("Enter the file path of the save file: ")
        with open(filepath, "r") as infile:
            data = json.load(infile)
            # TODO: keep loading attrs in GameState
            return GameState(data["month"], data["year"])
    else:
        return GameState(0, "Freshman")

def save_game(g):
    filepath = input("Enter the location where you would like to save: ")
    filecontent = json.dumps(g.__dict__)
    with open(filepath, "w") as outfile:
        outfile.write(filecontent)

def choose_archetype():
    pass

def buy_supplies():
    pass

def check_quit():
    quit = input("Would you like to save and quit? (Y/N) ")
    return quit.lower() == "y"

def game_loop(g):
    if (check_quit()):
        save_game(g)
        return
    
    print("Month: " + str(g.month), "\nYear: " + g.year)
    if(g.month == 0 and g.year == "Freshman"):
        choose_archetype()
    
    # month passes
    g.month += 1
    if (g.month == 12):
        g.month = 0  
        if (g.year == "Freshman"):
            g.year = "Sophomore"
        elif (g.year == "Sophomore"):
            g.year = "Junior"
        elif (g.year == "Junior"):
            g.year = "senior"
    
    # action phase - recursive
    
    # Randomly pre-scheduled event
    
    game_loop(g)

def finish():
    pass    

# save player state in variables here
g = load_game()
game_loop(g)