impoer random

def playGame():
    user = input("'r' for rock, 'p' for paper, 's' for sissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if winsGame(user, computer):
        return 'You won!'
    
def winsGame(player, opponent):
    # return true if player wins based on rule above #
    return 'You lost!'

    if (player == 'r' and opponent == 's', or player == 's' and opponant 'p', or player == 'p' and opponant is 'r')
        return True