def tournamentWinner(competitions, results):
    commands = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            if competitions[i][1] in commands:
                commands[competitions[i][1]] += 3
            else:
                commands[competitions[i][1]] = 3
        else:
            if competitions[i][0] in commands:
                commands[competitions[i][0]] += 3
            else:
                commands[competitions[i][0]] = 3
    commands_winner = sorted(commands.items(), key=lambda x: x[1], reverse=True)
    return commands_winner[0][0]

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]]

results = [0, 0, 1]
print(tournamentWinner(competitions, results))