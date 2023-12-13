class ChessCell:
    figure: str
    player: int

class SubAction:
    figure: str
    oldD: int
    oldL: int
    newD: int
    newL: int
    destroyedFigure: str

class Action:
    player: int
    steps: list[SubAction]
    type = 'default'

figureNames = {
    'p': 'Пешка',
    'r': 'Ладья',
    'n': 'Конь',
    'b': 'Слон',
    'q': 'Ферзь',
    'k': 'Король',
    '': 'Пусто'
}

lettersToNumbers = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

numbersToLetters = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h'
}

class ChessGame:
    board: list[list[ChessCell]]
    history: list[Action]
    currentMoveNumber = 1
    kingMovedForPlayers = []
    leftRMovedForPlayers = []
    rightRMovedForPlayers = []
    kingsInDanger = []

    def _initBoard(self):
        self.board = []
        for i in range(8):
            a = []
            for j in range(8):
                c = ChessCell()
                c.figure = ''
                c.player = 0
                a.append(c)
            self.board.append(a)

    def _initFigures(self):
        for i in range(8):
            self.board[1][i].figure = 'p'  # пешка
            self.board[6][i].figure = 'P'

            self.board[0][i].player = 2
            self.board[1][i].player = 2
            self.board[6][i].player = 1
            self.board[7][i].player = 1
        self.board[0][0].figure = 'r'  # ладья
        self.board[0][7].figure = 'r'
        self.board[7][0].figure = 'R'
        self.board[7][7].figure = 'R'
        self.board[0][1].figure = 'n'  # конь
        self.board[0][6].figure = 'n'
        self.board[7][1].figure = 'N'
        self.board[7][6].figure = 'N'
        self.board[0][2].figure = 'b'  # слон
        self.board[0][5].figure = 'b'
        self.board[7][2].figure = 'B'
        self.board[7][5].figure = 'B'
        self.board[0][3].figure = 'q'  # ферзь
        self.board[7][3].figure = 'Q'
        self.board[0][4].figure = 'k'  # король
        self.board[7][4].figure = 'K'

    def init(self):
        self._initBoard()
        self._initFigures()
        self.history = []
        self.kingMovedForPlayers = []
        self.leftRMovedForPlayers = []
        self.rightRMovedForPlayers = []
        self.currentMoveNumber = 1

    def _fieldToStr(self, num):
        if num < 10:
            return ' ' + str(num)
        else:
            return str(num)

    def _cellNameDeco(self, value):
        if value != '':
            return value
        return '.'

    def drawBoard(self, options:list[tuple[int, int]]=None, player=1):
        print('     ', end='')
        for q in range(2 if options else 1):
            for i in range(len(self.board[0])):
                print(numbersToLetters[i + 1], '', end='')
            print('           ', end='')
        print()
        for q in range(2 if options else 1):
            print('     ', (len(self.board[0])) * '— ' + '      ', sep='', end='')
        print()
        for i in range(len(self.board)):
            print(self._fieldToStr(i + 1), ' | ', sep='', end='')
            for j in range(len(self.board[i])):
                opt = False
                if options:
                    opt = (i, j) in options
                if self.board[i][j].figure == '':
                    if opt:
                        print('o ', end='')
                    else:
                        print('. ', end='')
                else:
                    if opt:
                        print('X ', end='')
                    else:
                        print(self._cellNameDeco(str(self.board[i][j].figure)) + ' ', end='')
            if options:
                print('      ', end='')
                print(self._fieldToStr(i + 1), ' | ', sep='', end='')
                for j in range(len(self.board[i])):
                    opt = False
                    if options:
                        opt = (i, j) in options
                    if opt:
                        if self.board[i][j].figure == '':
                            print('* ', end='')
                        elif self.board[i][j].player != player:
                            print(self._cellNameDeco(str(self.board[i][j].figure)) + ' ', end='')
                    else:
                        print('- ', end='')
            print()
        print()

    def getPossibleMovements(self, board, figure, player, d, l):
        """
        d: digit
        l: letter
        """
        movements = []
        match figure.lower():
            case 'p':
                movements.append((d + (-1 if player == 1 else 1), l))
                if player == 1 and d == 6:
                    movements.append((d - 2, l))
                elif player == 2 and d == 1:
                    movements.append((d + 2, l))
                if 0 < l < 7:
                    if player == 1:
                        if d > 0:
                            if board[d-1][l-1].figure != '' and board[d-1][l-1].player != player:
                                movements.append((d - 1, l - 1))
                            if board[d-1][l+1].figure != '' and board[d-1][l+1].player != player:
                                movements.append((d - 1, l + 1))
                    elif player == 2:
                        if d < 7:
                            if board[d+1][l-1].figure != '' and board[d+1][l-1].player != player:
                                movements.append((d + 1, l - 1))
                            if board[d+1][l+1].figure != '' and board[d+1][l+1].player != player:
                                movements.append((d + 1, l + 1))
            case 'r':
                self.addRMovements(movements, player, d, l)
            case 'b':
                self.addBMovements(movements, player, d, l)
            case 'q':
                self.addRMovements(movements, player, d, l)
                self.addBMovements(movements, player, d, l)
            case 'n':
                movements.append((d + 2, l - 1))
                movements.append((d + 2, l + 1))
                movements.append((d - 2, l - 1))
                movements.append((d - 2, l + 1))
                movements.append((d + 1, l + 2))
                movements.append((d - 1, l + 2))
                movements.append((d + 1, l - 2))
                movements.append((d - 1, l - 2))
            case 'k':
                movements.append((d + 1, l - 1))
                movements.append((d + 1, l))
                movements.append((d + 1, l + 1))
                movements.append((d, l - 1))
                movements.append((d, l + 1))
                movements.append((d - 1, l - 1))
                movements.append((d - 1, l))
                movements.append((d - 1, l + 1))

        filtered = []

        for mov in movements:
            if not (mov[0] < 0 or mov[0] > 7 or mov[1] < 0 or mov[1] > 7 or board[mov[0]][mov[1]].player == player):
                filtered.append(mov)

        return filtered

    def appendAndDoBreakOrNot(self, movements:list[tuple[int, int]], option:tuple[int, int], player):
        if option[0] < 0 or option[0] > 7 or option[1] < 0 or option[1] > 7:
            return True
        c = self.board[option[0]][option[1]]
        if c.player == player:
            return True
        if c.player != player and c.player != 0:
            movements.append(option)
            return True
        movements.append(option)
        return False

    def addRMovements(self, movements:list[tuple[int, int]], player, d, l):
        for i in range(1, 8):
            option = (d + i, l)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d - i, l)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d, l + i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d, l - i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break

    def addBMovements(self, movements:list[tuple[int, int]], player, d, l):
        for i in range(1, 8):
            option = (d + i, l + i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d - i, l - i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d - i, l + i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break
        for i in range(1, 8):
            option = (d + i, l - i)
            if self.appendAndDoBreakOrNot(movements, option, player):
                break

    def checkCoordsValid(self, player, dFr, lFr, endPoint=False):
        # if not dFr in lettersToNumbers.values():
        #     return 1, "Первая координата должно быть числом в диапазоне 1-8!"
        # if not lFr in lettersToNumbers.keys():
        #     return 1, "Вторая координата должна быть буквой в диапазоне a-h!"
        if dFr < 0 or dFr > 7 or lFr < 0 or lFr > 7:
            return 1, 'Позиция вне игрового поля!'
        if not endPoint and self.board[dFr][lFr].figure == '':
            return 1, 'На данной позиции пусто!'
        if self.board[dFr][lFr].player != player and not endPoint:
            return 1, 'На данной позиции находится чужая фигура!'
        if self.board[dFr][lFr].player == player and endPoint:
            return 1, 'На конечной позиции уже находится ваша фигура!'
        return 0, ''

    def performMovement(self, player, dFr, lFr, dTo, lTo):
        errCode, message = self.checkCoordsValid(player, dFr, lFr)
        if errCode == 1:
            return 1, 'Исходная точка: ' + message
        errCode, message = self.checkCoordsValid(player, dTo, lTo, endPoint=True)
        if errCode == 1:
            return 1, 'Конечная точка: ' + message
        possibleMovements = self.getPossibleMovements(self.board, self.board[dFr][lFr].figure, player, dFr, lFr)
        if (dTo, lTo) not in possibleMovements:
            return 1, 'Некорректный шаг!'

        a = Action()
        a.player = player
        a.steps = []

        sa = self._subActionFromData(dFr, lFr, dTo, lTo)
        a.steps.append(sa)

        self.performAction(a)

        self.checkKings()

        return 0, str(sa.oldD + 1) + numbersToLetters[sa.oldL + 1] + ' -> ' + str(sa.newD + 1) + numbersToLetters[sa.newL + 1]

    def coordsToNumberFormat(self, s: str):
        parts = s.split()
        if len(parts) != 2:
            return 1, "Ввод должен состоять из цифры и буквы!"
        try:
            d = int(parts[0])
        except ValueError:
            return 1, "Первая координата должна быть цифрой!"
        if d < 1 or d > 8:
            return 1, "Первая координата должна быть цифрой в диапазоне 1-8!"
        try:
            l = lettersToNumbers[parts[1]]
        except KeyError:
            return 1, "Вторая координата должна быть буквой в диапазоне 1-8!"
        return 0, (d - 1, l - 1)

    def revertSteps(self, amount):
        for i in range(amount):
            if len(self.history) == 0:
                return i
            lastAction = self.history[len(self.history) - 1]
            for stepIndex in reversed(range(len(lastAction.steps))):
                step = lastAction.steps[stepIndex]

                if step.destroyedFigure != '':
                    self.board[step.newD][step.newL].figure = step.destroyedFigure
                    self.board[step.newD][step.newL].player = self.getDifferentPlayer(lastAction.player)
                else:
                    self.board[step.newD][step.newL].figure = ''
                    self.board[step.newD][step.newL].player = 0

                self.board[step.oldD][step.oldL].figure = step.figure
                self.board[step.oldD][step.oldL].player = lastAction.player

            self.history.remove(lastAction)
            self.currentMoveNumber -= 1

            self.checkKings()

            return amount

    def getDifferentPlayer(self, player):
        if player == 1:
            return 2
        elif player == 2:
            return 1

    def doCastle(self, player, left):
        if player in self.kingMovedForPlayers or (left and player in self.leftRMovedForPlayers) or (not left and player in self.rightRMovedForPlayers):
            return 1, 'Король и/или ладья уже двигались с начала раунда, нельзя произвести рокировку!'

        theD = 7 if player == 1 else 0
        if left and (self.board[theD][1].figure != '' or self.board[theD][2].figure != '' or self.board[theD][3].figure != '') or \
                not left and (self.board[theD][4].figure != '' or self.board[theD][5].figure != ''):
            return 1, 'Пространство между королём и ладьёй не пусто!'

        a = Action()
        a.player = player

        dFr1 = 7
        dFr2 = 7
        dTo1 = 7
        dTo2 = 7

        lFr1 = 4
        if left:
            lTo1 = 2
            lFr2 = 0
            lTo2 = 3
        else:
            lTo1 = 6
            lFr2 = 7
            lTo2 = 5

        a.steps = []
        if left:
            a.type = 'O-O-O'
        else:
            a.type = 'O-O'

        sa1 = self._subActionFromData(dFr1, lFr1, dTo1, lTo1)
        sa2 = self._subActionFromData(dFr2, lFr2, dTo2, lTo2)
        a.steps.append(sa1)
        a.steps.append(sa2)

        # print(sa1.oldD+1, numbersToLetters[sa1.oldL+1], ' ', sa1.newD+1, numbersToLetters[sa1.newL+1])
        # print(sa2.oldD+1, numbersToLetters[sa2.oldL+1], ' ', sa2.newD+1, numbersToLetters[sa2.newL+1])

        self.performAction(a)

        self.checkKings()

        if left:
            return 0, 'O-O-O'
        else:
            return 0, 'O-O'

    def _subActionFromData(self, dFr, lFr, dTo, lTo):
        sa = SubAction()
        sa.figure = self.board[dFr][lFr].figure
        sa.destroyedFigure = self.board[dTo][lTo].figure
        sa.oldD = dFr
        sa.oldL = lFr
        sa.newD = dTo
        sa.newL = lTo

        return sa

    def performAction(self, a: Action):
        self.history.append(a)
        self.currentMoveNumber += 1

        for stepIndex in range(len(a.steps)):
            step = a.steps[stepIndex]
            self.board[step.newD][step.newL].figure = self.board[step.oldD][step.oldL].figure
            self.board[step.newD][step.newL].player = a.player
            self.board[step.oldD][step.oldL].figure = ''
            self.board[step.oldD][step.oldL].player = 0

    def saveHistoryToFile(self, fileName):
        with open(fileName, 'w') as f:
            for a in self.history:
                f.write(self._serializeAction(a) + '\n')

    def _serializeAction(self, a: Action):
        if a.type == 'default':
            return str(a.steps[0].oldD + 1) + str(numbersToLetters[a.steps[0].oldL + 1]) + " " + str(a.steps[0].newD + 1) + str(numbersToLetters[a.steps[0].newL + 1])
        elif a.type == 'O-O-O' or a.type == 'O-O':
            return a.type
        return ''

    def _checkSomeoneCanHitThat(self, board, player, d, l):
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c.player != 0 and c.player != player:
                    moves = self.getPossibleMovements(board, c.figure, player, i, j)
                    if (d, l) in moves:
                        return True
        return False

    def findAllCellsInDanger(self, board, player):
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c.player == player:
                    if self._checkSomeoneCanHitThat(board, player, i, j):
                        result.append((i, j))
        return result

    def isKingInDanger(self, board, player):
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c.player == player and c.figure.lower() == 'k':
                    return self._checkSomeoneCanHitThat(board, player, i, j)
        return False

    def checkKings(self):
        k1 = self.isKingInDanger(self.board, 1)
        k2 = self.isKingInDanger(self.board, 2)
        self.kingsInDanger = []
        if k1:
            self.kingsInDanger.append(1)
        if k2:
            self.kingsInDanger.append(2)
