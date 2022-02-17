# 5 stars for every point
# 3 stars subtracted for every foul
# number of points scored is always greater than fouls
# how many players on a team have a star rating greater than 40
# if all players have a star rating greater than 40 they are a gold team
###
# input:
# number of players
# for each player:
# number of points
# number of fouls

paxPlayers = int(input())
counter = 0
stars = 0
goldTeam = True
fourteePlayers = 0

while paxPlayers != counter:
    counter += 1
    stars = 0
    points = int(input())
    fouls = int(input())
    stars += points * 5
    stars -= fouls * 3
    if stars > 40:
        fourteePlayers += 1
    else:
        goldTeam = False

fourteePlayers = str(fourteePlayers)
if goldTeam == True: 
    print(fourteePlayers + "+")
else:
    print(fourteePlayers)

