def rps(p1, p2):
    """Let's play! You have to return which player won!
    In case of a draw return Draw!.
    rps('scissors','paper') // Player 1 won!
    """
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'scissors' and p2 == 'paper') or (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 =='rock'):
        return "Player 1 won!"
    else:
        return "Player 2 won!"