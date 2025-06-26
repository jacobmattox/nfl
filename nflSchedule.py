from nflTeamEnum import NflTeams


def main():
    listOfTeamsWithSchedule = []
    with open('nflschedule.csv', encoding="utf-8") as f:
        read_data = f.readlines()

    for line in read_data:
        splitLine = line.split(",")
        teamAndSchedule = processLine(splitLine)
        listOfTeamsWithSchedule.append(teamAndSchedule)

    scheduleByWeekString = scheduleByWeek(listOfTeamsWithSchedule)

    w = open('nflweeklymatchups.txt', 'w', encoding="utf-8")
    w.write(scheduleWithoutDuplicates(scheduleByWeekString))
    w.close()


def processLine(line):
    teamName = line[0]
    line[-1] = line[-1].replace('\n', '')
    team = TeamAndSchedule(teamName, line[1:])
    return (team)


def scheduleByWeek(listOfTeamsWithSchedule):
    printtableSchedulebyWeek = ""
    for i, week in enumerate(listOfTeamsWithSchedule[0].games):
        for j, team in enumerate(listOfTeamsWithSchedule):
            printtableSchedulebyWeek += f"{i + 1}, {team.teamName}, {team.games[i]} \n"
        printtableSchedulebyWeek += '\n'
    return (printtableSchedulebyWeek)


def scheduleWithoutDuplicates(scheduleByWeekString):
    returnString = ""
    splitString = scheduleByWeekString.split('\n')
    for line in splitString:
        if not "@" in line:
            continue
        returnString += (f'{line} \n')
    return (returnString)


class TeamAndSchedule:
    def __init__(self, teamName, games):
        self.teamName = teamName
        self.teamId = NflTeams[teamName].value
        self.games = games

    def __str__(self):
        return (f'team: {self.teamName} id: {self.teamId} #games: {len(self.games)}')

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    main()
