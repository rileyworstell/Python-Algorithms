"""
Tournament where inputs are competitions and results.
competitions array has elements in the form of [homeTeam, awayTeam], where 
each team is a string representing the name of th team. Results array contains information about the winner of each corresponding competition in the competitions array. 
results[i] denotes the winner of competitions[i].
a 1 means the home team won and a 0 means the away team won.
"""


# O(n) time | O(k) space where k is number of teams
def tournamentWinner(competitions, results):
    teamPoints = {}
    highestPoints = 0
    currentWinner = None
    for i in range(len(results)):
        if competitions[i][0] not in teamPoints:
            teamPoints[competitions[i][0]] = 0
        if competitions[i][1] not in teamPoints:
            teamPoints[competitions[i][1]] = 0
        if results[i] == 0:
            teamPoints[competitions[i][1]] += 3
            if teamPoints[competitions[i][1]] > highestPoints:
                highestPoints = teamPoints[competitions[i][1]]
                currentWinner = competitions[i][1]
        elif results[i] == 1:
            teamPoints[competitions[i][0]] += 3
            if teamPoints[competitions[i][0]] > highestPoints:
                highestPoints = teamPoints[competitions[i][0]]
                currentWinner = competitions[i][0]
    return currentWinner


competitions = [['HTML', 'C'], ['C', 'Python'], ['Python', 'HTML']]
results = [0, 0, 1]  # 1 for home team with [home, away]
print(tournamentWinner(competitions, results))
