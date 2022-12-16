## A = Rock, B = Paper, C = Scissors
## X = Rock, Y = Paper, Z = Scissors
## Rock = 1, Paper = 2, Scissors = 3
## Lost = 0, Draw = 3, Win = 6

my_scores = {"X":1 ,"Y": 2, "Z": 3}

#opponent_plays = {"A":"Rock" ,"B": "Paper", "C": "Scissors"}
#my_plays = {"X":"Rock" ,"Y": "Paper", "Z": "Scissors"}
#winners = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
winners = {"A":"Y","B":"Z","C":"X"}
draws = {"A":"X","B":"Y","C":"Z"}
losers = {"A":"Z","B":"X","C":"Y"}


def count(filename):
    file = open(filename,"r")
    total = 0
    for row in file:
        r = row.split()
        my_score = my_scores[r[1]]
        my_score += getwinner(r[1], r[0])
        total += my_score
    print(total)

def getwinner(mine, opponent):
    my_score = 0
    if mine == draws[opponent]:
        my_score += 3
    elif mine == winners[opponent]:
        my_score += 6
    return my_score


count("input2.txt")

## part 2: X = lose, Y = draw, Z = win
my_outcomes = {"X":0 ,"Y": 3, "Z": 6}

def recount(filename):
    file = open(filename,"r")
    total = 0
    for row in file:
        r = row.split()
        my_score = my_outcomes[r[1]]
        my_score += scorePlay(r[0],r[1])
        total += my_score
    print(total)

def scorePlay(opponent,outcome):
    if outcome == "Z":
        #if i'm supposed to win
        my_play = winners[opponent]
    elif outcome == "Y":
        #if it's a draw
        my_play = draws[opponent]
    else:
        #if i lose
        my_play = losers[opponent]
    my_score = my_scores[my_play]
    return my_score

recount("input2.txt")

