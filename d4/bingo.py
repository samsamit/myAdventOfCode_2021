bingoNumbersArr = [
    23,
    30,
    70,
    61,
    79,
    49,
    19,
    37,
    64,
    48,
    72,
    34,
    69,
    53,
    15,
    74,
    89,
    38,
    46,
    36,
    28,
    32,
    45,
    2,
    39,
    58,
    11,
    62,
    97,
    40,
    14,
    87,
    96,
    94,
    91,
    92,
    80,
    99,
    6,
    31,
    57,
    98,
    65,
    10,
    33,
    63,
    42,
    17,
    47,
    66,
    26,
    22,
    73,
    27,
    7,
    0,
    55,
    8,
    56,
    29,
    86,
    25,
    4,
    12,
    51,
    60,
    35,
    50,
    5,
    75,
    95,
    44,
    16,
    93,
    21,
    3,
    24,
    52,
    77,
    76,
    43,
    41,
    9,
    84,
    67,
    71,
    83,
    88,
    59,
    68,
    85,
    82,
    1,
    18,
    13,
    78,
    20,
    90,
    81,
    54,
]


class BingoCard:
    def __init__(self, card) -> None:
        self.card = card
        self.winCount = 0
        pass

    def inputNumber(self, inputNumber):
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if self.card[i][j] == inputNumber:
                    self.card[i][j] = -1
        return self.checkWin()

    def printCard(self):
        print("Card:")
        for row in self.card:
            print(row)

    def checkWin(self):
        # rows
        for row in self.card:
            if self._checkRow(row):
                return True
        for i in range(len(self.card)):
            col = []
            for j in range(len(self.card[i])):
                col.append(self.card[j][i])
            if self._checkRow(col):
                return True
        return False

    def calculateWin(self):
        total = 0
        for row in self.card:
            for number in row:
                if number > 0:
                    total += number
        return total

    def _checkRow(self, row):
        if row.count(-1) == len(row):
            return True
        return False


# Get card
file1 = open("bingoData.txt", "r")
Lines = file1.readlines()

allCards: list[BingoCard] = []
card: list[list] = []
rowCount = 0
for d in Lines:
    cardStringRow = d.split()
    cardRow = []
    for x in cardStringRow:
        cardRow.append(int(x))
    if len(cardRow) > 0:
        card.append(cardRow)
    else:
        allCards.append(BingoCard(card))
        card = []


# Test
# bingoNumbersArr = [14, 83, 84, 74, 37]
# testCard = [
#     [50, 98, 65, 14, 47],
#     [0, 22,  3, 83, 46],
#     [87, 93, 81, 84, 58],
#     [40, 35, 28, 74, 48],
#     [45, 99, 59, 37, 64]
# ]
# tastBingoCard = BingoCard(testCard)
# testCards = [tastBingoCard]
# for number in TestNumbers:
#     for card in testCards:
#         card.inputNumber(number)
#         if card.checkWin():
#             print(f'Winner with calculated winNumber {card.calculateWin() * number}')


# Part 1
# winner = False
# for number in bingoNumbersArr:
#     if winner: continue
#     for i in range(len(allCards)):
#         if allCards[i].inputNumber(number):
#             allCards[i].printCard()
#             print(
#                 f"Winner with calculated winNumber {allCards[i].calculateWin() * number}"
#             )
#             winner = True

# Part 2
winner = False
for number in bingoNumbersArr:
    if winner: continue
    for i in range(len(allCards)):
        if len(allCards) <= i: continue
        if allCards[i].inputNumber(number):
            if len(allCards) == 1:
                allCards[i].printCard()
                print(
                    f"Last card {allCards[i].calculateWin() * number}"
                )
                winner = True
            else:
                del allCards[i]
                