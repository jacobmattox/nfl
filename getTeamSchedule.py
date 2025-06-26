def main():
    userInput = "start"
    retryCount = 0

    while userInput != "EXIT":
        userInput = input(
            "What team/week do you want the schedule for? (options for list of options):  ").upper()
        match userInput:
            case "OPTIONS":
                retryCount = 0
                print(printOptions())
            case "SF" | "CHI" | "CIN" | "BUF" | "DEN" | "CLE" | "TB" | "ARI" | "LAC" | "KC" | "IND" | "WAS" | "DAL" | "MIA" | "PHI" | "ATL" | "NYG" | "JAC" | "NYJ" | "DET" | "GB" | "CAR" | "NE" | "LV" | "LAR" | "BAL" | "NO" | "SEA" | "PIT" | "HOU" | "TEN" | "MIN":
                retryCount = 0
                print(scheduleByTeamOrWeek(userInput))
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" | "13" | "14" | "15" | "16" | "17" | "18":
                retryCount = 0
                print(f"{scheduleByTeamOrWeek(userInput)}")
            case "COUNT":
                print(f"Number of games per week: {countGamesPerWeek()}")
            case _:
                if retryCount == 4:
                    print("think about what you want donkey")
                    break
                else:
                    retryCount += 1
                continue


def printOptions():
    return ("You can type the team initials to get their schedule for the season. You can also type the week number to get all games from that week.\
             Count will give you the number of games each week. Typing exit will exit the program.")


def scheduleByTeamOrWeek(userInput):
    with open('nflweeklymatchups.txt', encoding="utf-8") as f:
        read_data = f.readlines()
    returnData = []
    for line in read_data:
        splitLine = line.replace('  \n', '').replace(
            ' ', '').replace('@', '').split(',')
        if userInput in splitLine:
            returnData.append(line)
    returnString = "".join(returnData)
    return (returnString)


def countGamesPerWeek():
    gamesPerWeek = dict()
    with open('nflweeklymatchups.txt', encoding="utf-8") as f:
        read_data = f.readlines()
    for i, line in enumerate(read_data):
        splitLine = line.split(',')
        if splitLine[0] not in gamesPerWeek:
            gamesPerWeek[splitLine[0]] = 1
        else:
            gamesPerWeek[splitLine[0]] = gamesPerWeek[splitLine[0]] + 1
    return (gamesPerWeek)


# def printWeekSchedule(userInput):
#     with open('nflweeklymatchups.txt', encoding="utf-8") as f:
#         read_data = f.readlines()
#     returnData = []
#     for line in read_data:
#         splitLine = line.replace('  \n', '').replace(
#             ' ', '').replace('@', '').split(',')
#         if userInput in splitLine:
#             returnData.append(line)
#     returnString = "".join(returnData)
#     return (returnString)
if __name__ == "__main__":
    main()
