# GUI-based version of RPSLS


import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "Error on name. Please re-enter the correct name."


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "Error on number. Please re-enter a number between 0 and 4."
         

def rpsls(player_choice): 
    print ''
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    difference = (comp_number - player_number) % 5
    if difference == 3:
        print 'Player wins!'
    elif difference == 4:
        print 'Player wins!'
    elif difference == 1:
        print 'Computer wins!'
    elif difference == 2:
        print 'Computer wins!'
    else:
        print 'Player and computer tie!'
     
    
# Handler for input field
def get_guess(guess):
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

#get_guess("Spock")
#get_guess("dynamite")
#get_guess("paper")
#get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
