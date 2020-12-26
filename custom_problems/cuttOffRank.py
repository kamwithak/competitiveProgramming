"""
A group of work friends at Amazon is playing a competitive video game together. 
During the game, each player receives a certain amount of points based on their performance.
At the end of a round, players who achieve at least a cutoff rank get to "level up" their character, gaining increased abilities for them.
Given the scores of the players at the end of the round, how many players will be able to level up their character?

Note that players with equal scores will have equal ranks, but the player with the next lowest score will be ranked based on the position within the list of all players' scores.
For example, if there are four players, and three players tie for first place, their ranks would be 1,1,1, and 4.
Also, no player with a score of O can level up, no matter what their rank.

Write an algorithm that returns the count of players able to level up their character.

Input:
i) cutOffRank, an integer representing the cutoff rank for levelin up the player's character;
ii) num, an integer representing the total number of scores;
iii) scores, a list of integers representing the scores of the players.

Output:
Return an integer representing the number of players who will be able to level up their characters at the end of the round.
"""

from typing import List

def numPlayers(cuttOffRank: int, num: int, scores: List[int]):
    ranks = [sorted(scores).index(x)+1 for x in scores[::-1]]
    print(ranks)
    ctr = 0
    for i in range(num):
        if (scores[i] != 0 and ranks[i] <= cuttOffRank):
            ctr += 1
    return ctr

scores = [2,4,6,1,2,3,4]
print(numPlayers(4, len(scores), scores))