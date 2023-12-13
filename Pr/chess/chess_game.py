import chess

c = chess.ChessGame()
c.init()

player = 0
noDraw = False
samePlayer = False

def checkCommand(s: str, pl):
    s = s.lower()
    if s == 'o-o':
        errCode, message = c.doCastle(pl, False)
        if errCode == 0:
            print('Успешно произведена левая рокировка')
            c.drawBoard()
        return True, errCode, message
    elif s == 'o-o-o':
        errCode, message = c.doCastle(pl, True)
        if errCode == 0:
            print('Успешно произведена левая рокировка')
            c.drawBoard()
        return True, errCode, message
    elif s.startswith('save '):
        fileName = s[4:].strip()
        if len(fileName) > 0:
            c.saveHistoryToFile(fileName)
            print('Сохранено ' + str(c.currentMoveNumber - 1) + ' действий!')
        else:
            print('Укажите название файла!')
        return True, 0, None
    elif s == 'p':
        revertedSteps = c.revertSteps(1)
        print('Отменено ' + str(revertedSteps) + ' действий')
        global player
        player += 1
        if player >= 3:
            player = 1
        if revertedSteps != 0:
            c.drawBoard()
        return True, 0, None
    return False, 0, None

if __name__ == '__main__':
    while True:
        if not samePlayer:
            player += 1
        if player >= 3:
            player = 1
        samePlayer = False

        if not noDraw:
            c.drawBoard()
            dangered = c.findAllCellsInDanger(c.board, player)
            # print(dangered)
            if len(dangered) != 0:
                print('Фигуры под ударом:')
                for d in dangered:
                    print(str(d[0]) + " " + str(d[1]) + " (" + c.board[d[0]][d[1]].figure + ")")
        noDraw = False

        firstInput = input('Ход №' + str(c.currentMoveNumber) + ', игрок ' + str(player) + ':\nИсходная точка: ')
        foundCommand, errCode, checkCommandMessage = checkCommand(firstInput, player)
        # print(foundCommand, errCode, checkCommandMessage)
        if foundCommand or errCode == 1:
            if errCode == 1:
                print(checkCommandMessage)
            samePlayer = True
            noDraw = True
            continue

        errCode, messageOrFrCoords = c.coordsToNumberFormat(firstInput)
        if errCode == 1:
            print("Ошибка:", messageOrFrCoords)
            samePlayer = True
            noDraw = True
            continue

        errCode, message = c.checkCoordsValid(player, messageOrFrCoords[0], messageOrFrCoords[1])
        if errCode == 1:
            print("Ошибка:", message)
            samePlayer = True
            noDraw = True
            continue

        figure = c.board[messageOrFrCoords[0]][messageOrFrCoords[1]].figure
        possibleMovements = c.getPossibleMovements(c.board, figure, player, messageOrFrCoords[0], messageOrFrCoords[1])

        if len(possibleMovements) == 0:
            print('Нет ходов!')
            samePlayer = True
            noDraw = True
            continue

        print('Возможные ходы (' + chess.figureNames[figure.lower()] + '):')
        c.drawBoard(options=possibleMovements, player=player)

        while True:
            errCode, messageOrToCoords = c.coordsToNumberFormat(input('Конечная точка: '))
            if errCode == 1:
                print("Ошибка:", messageOrToCoords)
                continue

            errCode, movementMessage = c.performMovement(player=player, dFr=messageOrFrCoords[0], lFr=messageOrFrCoords[1], dTo=messageOrToCoords[0], lTo=messageOrToCoords[1])
            if errCode == 1:
                print("Ошибка:", movementMessage)
                continue
            elif errCode == 0:
                print()
                print('Ход игрока ' + str(player) + ": " + movementMessage)
                print()

            break
